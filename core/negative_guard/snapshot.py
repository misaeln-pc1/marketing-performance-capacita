"""Snapshot manager for reading, serializing, and sanitizing negative keyword state."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import (
    NegativeKeywordItem,
    NegativeSnapshot,
    hash_identifier,
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
            evidence_source="LIVE_API_HOLD",
            status="HOLD_DATA_GAP",
        )

    @staticmethod
    def create_sanitized_snapshot_from_items(
        items: List[Dict[str, Any]],
        customer_id_raw: Optional[str] = None,
        evidence_source: str = "HISTORICAL_EXPORT",
    ) -> NegativeSnapshot:
        """Builds a fully sanitized NegativeSnapshot from a list of raw or semi-raw dictionary items."""
        cust_hash = hash_identifier(customer_id_raw)
        keyword_items: List[NegativeKeywordItem] = []

        for row in items:
            item = NegativeKeywordItem(
                keyword_text=row.get("keyword_text", ""),
                match_type=row.get("match_type", "BROAD"),
                source_scope=row.get("source_scope", "CAMPAIGN"),
                campaign_name=row.get("campaign_name", "GLOBAL"),
                campaign_id_hash=hash_identifier(row.get("campaign_id_hash") or row.get("campaign_id")),
                ad_group_name=row.get("ad_group_name", "NONE"),
                ad_group_id_hash=hash_identifier(row.get("ad_group_id_hash") or row.get("ad_group_id")),
                shared_set_name=row.get("shared_set_name", "NONE"),
                customer_id_hash=cust_hash,
                status=row.get("status", "ENABLED"),
                intent_class=row.get("intent_class", "DESCONOCIDO"),
                policy_decision=row.get("policy_decision", "PRESERVE"),
                evidence_source=evidence_source,
            )
            keyword_items.append(item)

        return NegativeSnapshot(
            customer_id_hash=cust_hash,
            items=keyword_items,
            evidence_source=evidence_source,
            status="READY",
        )
