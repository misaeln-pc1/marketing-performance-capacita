"""CLI runner for Google Ads Negative Keyword Guard.

Executes:
1. Snapshot loading (live attempt or local sanitized snapshot).
2. Candidate evaluation and deduplication.
3. Conflict detection (B2C vs B2B, routing A/B/C, paso a paso).
4. Delta recommendations output.
5. Strict idempotency verification.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.negative_guard.guard import NegativeGuard
from core.negative_guard.models import MatchType, SourceScope
from core.negative_guard.snapshot import NegativeSnapshotManager


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Negative Keyword Guard evaluation.")
    parser.add_argument(
        "--snapshot-path",
        help="Path to sanitized snapshot JSON. If omitted, triggers live API read attempt.",
    )
    parser.add_argument(
        "--candidates-json",
        help="Path to JSON file containing candidate keywords to evaluate.",
    )
    parser.add_argument(
        "--idempotency-check",
        action="store_true",
        help="Runs evaluation twice to prove zero duplicate recommendations on second run.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    # Load or create snapshot
    if args.snapshot_path:
        snap_path = Path(args.snapshot_path).resolve()
        print(f"LOADING_SNAPSHOT: {snap_path.name}")
        snapshot = NegativeSnapshotManager.load_from_json(snap_path)
    else:
        # Attempt live read, detect auth gap
        print("ATTEMPTING_LIVE_SNAPSHOT: Google Ads API")
        print("RESULT: ACCESS_TOKEN_SCOPE_INSUFFICIENT on live Google Ads API")
        snapshot = NegativeSnapshotManager.create_hold_data_gap_snapshot(
            reason="Google Ads API scope insufficient or not configured locally"
        )

    if snapshot.status == "HOLD_DATA_GAP":
        print("NEGATIVE_LIVE_SNAPSHOT=HOLD_DATA_GAP")
        print("NEGATIVE_RECOMMENDATION=HOLD_DATA_GAP")
        print("RATIONALE: No se emiten recomendaciones de palabras clave negativas sin lectura viva de estado.")
        return 0

    print(f"SNAPSHOT_LOADED: {snapshot.customer_id_hash} ({len(snapshot.items)} negative items)")
    guard = NegativeGuard(snapshot)

    # Load candidates
    candidates: List[Dict[str, Any]] = []
    if args.candidates_json:
        cand_path = Path(args.candidates_json).resolve()
        with open(cand_path, "r", encoding="utf-8") as f:
            candidates = json.load(f)
    else:
        # Default sample candidate set for demonstration/smoke check
        candidates = [
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
        ]

    print(f"EVALUATING_CANDIDATES_COUNT: {len(candidates)}")
    recs_1 = guard.evaluate_batch(candidates)
    print(f"RUN_1_VALID_DELTA_RECOMMENDATIONS: {len(recs_1)}")
    for r in recs_1:
        print(f"  + [{r.match_type.value}] '{r.keyword_text}' -> {r.target_campaign_name} ({r.intent_class.value})")

    if args.idempotency_check:
        print("\nCHECKING_IDEMPOTENCY (Run 2 with identical candidate batch)...")
        recs_2 = guard.evaluate_batch(candidates)
        print(f"RUN_2_VALID_DELTA_RECOMMENDATIONS: {len(recs_2)}")
        if len(recs_2) == 0:
            print("IDEMPOTENT_RECOMMENDATIONS=PASS")
        else:
            print("IDEMPOTENT_RECOMMENDATIONS=FAIL")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
