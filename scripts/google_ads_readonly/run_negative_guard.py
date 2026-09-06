"""CLI runner for Google Ads Negative Keyword Guard (Fail-Closed Architecture).

Executes:
1. Snapshot loading (live attempt via adapter or local sanitized snapshot).
2. Candidate evaluation and deduplication.
3. Conflict detection (B2C vs B2B, routing A/B/C, paso a paso).
4. Delta recommendations output.
5. Cross-process persistent idempotency verification.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.negative_guard.adapter import GoogleAdsNegativeReadAdapter
from core.negative_guard.campaign_contract import (
    CampaignRegistry,
    DEMO_CAMPAIGN_CONTRACTS,
)
from core.negative_guard.guard import NegativeGuard
from core.negative_guard.ledger import RecommendationLedger
from core.negative_guard.live_executor import GoogleAdsLiveExecutor
from core.negative_guard.models import MatchType, SourceScope
from core.negative_guard.snapshot import NegativeSnapshotManager


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Negative Keyword Guard evaluation fail-closed.")
    parser.add_argument(
        "--snapshot-path",
        help="Path to sanitized snapshot JSON. If omitted, triggers live API read attempt.",
    )
    parser.add_argument(
        "--candidates-json",
        help="Path to JSON file containing candidate keywords to evaluate. Required unless --demo is used.",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Explicitly allows running with built-in demonstration candidate keywords. Fails closed if omitted without --candidates-json.",
    )
    parser.add_argument(
        "--ledger-dir",
        help="Optional custom directory for persistent idempotency ledger. Defaults to user's local capacita cache.",
    )
    parser.add_argument(
        "--idempotency-check",
        action="store_true",
        help="Runs evaluation across two independent guard instances using the persistent ledger to verify zero duplicate recommendations.",
    )
    parser.add_argument(
        "--runtime-config-path",
        help="Path to external private runtime config JSON for live Google Ads API execution. Not stored in repo.",
    )
    return parser.parse_args()


DEMO_CANDIDATES = [
    {
        "keyword_text": "gratis",
        "match_type": "EXACT",
        "target_scope": "CAMPAIGN",
        "target_campaign_name": "SCL-EXCEL-B2C-PRESENCIAL",
        "target_campaign_id_hash": "hash_c11111111111",
    },
    {
        "keyword_text": "curso excel paso a paso",
        "match_type": "PHRASE",
        "target_scope": "CAMPAIGN",
        "target_campaign_name": "SCL-EXCEL-B2C-PRESENCIAL",
        "target_campaign_id_hash": "hash_c11111111111",
    },
    {
        "keyword_text": "factura empresa sence",
        "match_type": "PHRASE",
        "target_scope": "CAMPAIGN",
        "target_campaign_name": "SCL-EXCEL-EMPRESA-B2B",
        "target_campaign_id_hash": "hash_c22222222222",
    },
    {
        "keyword_text": "ejercicios excel avanzados",
        "match_type": "PHRASE",
        "target_scope": "CAMPAIGN",
        "target_campaign_name": "SCL-EXCEL-B2C-PRESENCIAL",
        "target_campaign_id_hash": "hash_c11111111111",
    },
    {
        "keyword_text": "curso excel online",
        "match_type": "BROAD",
        "target_scope": "CAMPAIGN",
        "target_campaign_name": "SCL-EXCEL-B2C-PRESENCIAL",
        "target_campaign_id_hash": "hash_c11111111111",
    },
]


def main() -> int:
    args = parse_args()

    # Fail-closed candidate check: refuse implicit demo candidates
    candidates: List[Dict[str, Any]] = []
    if args.candidates_json:
        cand_path = Path(args.candidates_json).resolve()
        if not cand_path.is_file():
            print(f"[FAIL-CLOSED ERROR] Candidates file not found: {cand_path}", file=sys.stderr)
            return 1
        with open(cand_path, "r", encoding="utf-8") as f:
            candidates = json.load(f)
    elif args.demo:
        print("[NOTICE] Running with explicit --demo candidate keyword set.")
        candidates = list(DEMO_CANDIDATES)
    else:
        print(
            "[FAIL-CLOSED ERROR] Missing candidate keywords. Provide --candidates-json <path> or explicitly specify --demo for smoke tests.",
            file=sys.stderr,
        )
        return 1

    # Resolve live executor if runtime config is provided
    live_exec: Optional[GoogleAdsLiveExecutor] = None
    if args.runtime_config_path:
        try:
            live_exec = GoogleAdsLiveExecutor(Path(args.runtime_config_path).resolve())
        except Exception as e:
            print(f"[FAIL-CLOSED ERROR] Runtime config error: {type(e).__name__}", file=sys.stderr)
            return 1

    # Load or create snapshot
    if args.snapshot_path:
        snap_path = Path(args.snapshot_path).resolve()
        print(f"LOADING_SNAPSHOT: {snap_path.name}")
        snapshot = NegativeSnapshotManager.load_from_json(snap_path)
    elif live_exec is not None:
        print("ATTEMPTING_LIVE_SNAPSHOT: GoogleAdsNegativeReadAdapter with GoogleAdsLiveExecutor")
        try:
            adapter = GoogleAdsNegativeReadAdapter(gaql_executor=live_exec.create_gaql_executor())
            snapshot = adapter.build_snapshot(customer_id=live_exec.customer_id)
        except Exception as e:
            snapshot = NegativeSnapshot(
                status="HOLD_DATA_GAP",
                hold_reason=f"LIVE_EXECUTOR_HOLD: {type(e).__name__}",
                evidence_source="FAIL_CLOSED",
            )
    else:
        print("ATTEMPTING_LIVE_SNAPSHOT: GoogleAdsNegativeReadAdapter")
        adapter = GoogleAdsNegativeReadAdapter()
        snapshot = adapter.build_snapshot(customer_id="unconfigured")

    # Machine-readable output on HOLD_DATA_GAP
    if snapshot.status == "HOLD_DATA_GAP":
        payload = {
            "status": "HOLD_DATA_GAP",
            "hold_reason": snapshot.hold_reason or "Missing live state read access",
            "recommendations_count": 0,
            "machine_readable_code": "NEGATIVE_SNAPSHOT_HOLD_DATA_GAP",
        }
        print(json.dumps(payload, indent=2))
        print("NEGATIVE_LIVE_SNAPSHOT=HOLD_DATA_GAP")
        print("NEGATIVE_RECOMMENDATION=HOLD_DATA_GAP")
        print("RATIONALE: No se emiten recomendaciones de palabras clave negativas sin lectura viva de estado.")
        # Exit code 2 explicitly signifies HOLD_DATA_GAP to automated schedulers (distinct from 0=success and 1=error)
        return 2

    print(f"SNAPSHOT_LOADED: {snapshot.customer_id_hash} ({len(snapshot.active_items())} active negative items)")
    ledger_path = Path(args.ledger_dir).resolve() if args.ledger_dir else None
    ledger = RecommendationLedger(ledger_path)
    if ledger.is_corrupt:
        print("[FAIL-CLOSED ERROR] Persistent ledger is corrupt: LEDGER_CORRUPT=HOLD", file=sys.stderr)
        return 1

    # Use demo registry for --demo, or load private mapping for live execution
    if live_exec is not None:
        if live_exec.campaign_contract_path:
            registry = CampaignRegistry.load_contracts_from_json(
                Path(live_exec.campaign_contract_path)
            )
        else:
            print("[FAIL-CLOSED ERROR] No campaign_contract_path in runtime config.", file=sys.stderr)
            return 1
    else:
        # Demo mode: use demo contracts explicitly
        registry = CampaignRegistry(contracts=DEMO_CAMPAIGN_CONTRACTS)

    guard_1 = NegativeGuard(snapshot, registry=registry, ledger=ledger)

    print(f"EVALUATING_CANDIDATES_COUNT: {len(candidates)}")
    recs_1 = guard_1.evaluate_batch(candidates)
    print(f"RUN_1_VALID_DELTA_RECOMMENDATIONS: {len(recs_1)}")
    for r in recs_1:
        print(f"  + [{r.match_type.value}] '{r.keyword_text}' -> {r.target_campaign_name} ({r.intent_class.value})")

    if args.idempotency_check:
        print("\nCHECKING_CROSS_PROCESS_IDEMPOTENCY (Run 2 with fresh guard instance over same persistent ledger)...")
        fresh_ledger = RecommendationLedger(ledger_path)
        guard_2 = NegativeGuard(snapshot, registry=registry, ledger=fresh_ledger)
        recs_2 = guard_2.evaluate_batch(candidates)
        print(f"RUN_2_VALID_DELTA_RECOMMENDATIONS: {len(recs_2)}")
        if len(recs_1) > 0 and len(recs_2) == 0:
            print("IDEMPOTENT_RECOMMENDATIONS=PASS")
        else:
            print(f"IDEMPOTENT_RECOMMENDATIONS=FAIL (Run 1: {len(recs_1)}, Run 2: {len(recs_2)})")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
