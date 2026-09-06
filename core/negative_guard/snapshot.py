"""Snapshot manager for reading, serializing, and sanitizing negative keyword state."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import (
    CriterionStatus,
    IntentClass,
    NegativeKeywordItem,
    NegativeSnapshot,
    PolicyDecision,
    hash_identifier,
    normalize_criterion_status,
    normalize_match_type,
    normalize_scope,
)


class NegativeSnapshotManager:
    """Manages negative keyword snapshots with full sanitization and manifest tracking."""

    @staticmethod
    def load_from_json(file_path: Path) -> NegativeSnapshot:
        """Loads a snapshot from a sanitized JSON file."""
        if not file_path.is_file():
            raise FileNotFoundError(f"Snapshot file not found: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return NegativeSnapshot.from_dict(data)

    @staticmethod
    def save_to_json(snapshot: NegativeSnapshot, file_path: Path) -> Path:
        """Saves a snapshot to a sanitized JSON file."""
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(snapshot.to_dict(), f, indent=2, ensure_ascii=False)
        return file_path

    @staticmethod
    def create_hold_data_gap_snapshot(
        reason: str = "Auth scope insufficient or live API access not available",
    ) -> NegativeSnapshot:
        """Creates an explicit HOLD_DATA_GAP snapshot when live state cannot be queried."""
        return NegativeSnapshot(
            customer_id_hash="none",
            items=[],
            campaign_shared_sets={},
            evidence_source="LIVE_API_HOLD",
            status="HOLD_DATA_GAP",
            hold_reason=reason,
        )

    @staticmethod
    def create_sanitized_snapshot_from_items(
        items: List[Dict[str, Any]],
        customer_id_raw: Optional[str] = None,
        campaign_shared_sets: Optional[Dict[str, List[str]]] = None,
        evidence_source: str = "HISTORICAL_EXPORT",
    ) -> NegativeSnapshot:
        """Builds a fully sanitized NegativeSnapshot from a list of raw or semi-raw dictionary items."""
        cust_hash = hash_identifier(customer_id_raw)
        keyword_items: List[NegativeKeywordItem] = []

        for row in items:
            raw_intent = row.get("intent_class", IntentClass.DESCONOCIDO)
            if isinstance(raw_intent, str):
                try:
                    intent_enum = IntentClass(raw_intent)
                except ValueError:
                    intent_enum = IntentClass.DESCONOCIDO
            else:
                intent_enum = raw_intent

            raw_policy = row.get("policy_decision", PolicyDecision.PRESERVE)
            if isinstance(raw_policy, str):
                try:
                    policy_enum = PolicyDecision(raw_policy)
                except ValueError:
                    policy_enum = PolicyDecision.PRESERVE
            else:
                policy_enum = raw_policy

            item = NegativeKeywordItem(
                keyword_text=row.get("keyword_text", ""),
                match_type=normalize_match_type(row.get("match_type", "BROAD")),
                source_scope=normalize_scope(row.get("source_scope", "CAMPAIGN")),
                campaign_name=row.get("campaign_name", "GLOBAL"),
                campaign_id_hash=hash_identifier(row.get("campaign_id_hash") or row.get("campaign_id")),
                ad_group_name=row.get("ad_group_name", "NONE"),
                ad_group_id_hash=hash_identifier(row.get("ad_group_id_hash") or row.get("ad_group_id")),
                shared_set_name=row.get("shared_set_name", "NONE"),
                customer_id_hash=cust_hash,
                status=normalize_criterion_status(row.get("status", "ENABLED")),
                intent_class=intent_enum,
                policy_decision=policy_enum,
                evidence_source=evidence_source,
            )
            keyword_items.append(item)

        attachments = {}
        if campaign_shared_sets:
            for k, v in campaign_shared_sets.items():
                attachments[hash_identifier(k)] = list(v) if isinstance(v, list) else [str(v)]

        return NegativeSnapshot(
            customer_id_hash=cust_hash,
            items=keyword_items,
            campaign_shared_sets=attachments,
            evidence_source=evidence_source,
            status="READY",
        )

    @staticmethod
    def verify_roundtrip(snapshot: NegativeSnapshot) -> bool:
        """Verifies full roundtrip serialization without data loss or hash divergence."""
        data_dict = snapshot.to_dict()
        json_str = json.dumps(data_dict, ensure_ascii=False)
        reconstructed = NegativeSnapshot.from_dict(json.loads(json_str))

        if reconstructed.manifest_hash != snapshot.manifest_hash:
            return False
        if len(reconstructed.items) != len(snapshot.items):
            return False
        if len(reconstructed.active_items()) != len(snapshot.active_items()):
            return False
        if reconstructed.customer_id_hash != snapshot.customer_id_hash:
            return False
        if reconstructed.status != snapshot.status:
            return False
        if reconstructed.schema_version != snapshot.schema_version:
            return False
        return True
