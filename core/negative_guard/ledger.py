"""Persistent ledger for recommendation idempotency across processes and sessions."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Set


DEFAULT_LEDGER_DIR = Path.home() / ".capacita" / "negative_guard_ledger"


class RecommendationLedger:
    """Manages persistent deduplication keys keyed by manifest_hash + recommendation_hash."""

    def __init__(self, ledger_dir: Optional[Path] = None):
        if ledger_dir is not None:
            self.ledger_dir = Path(ledger_dir).resolve()
        else:
            env_path = os.environ.get("NEGATIVE_GUARD_LEDGER_PATH")
            if env_path:
                self.ledger_dir = Path(env_path).resolve()
            else:
                self.ledger_dir = DEFAULT_LEDGER_DIR

        self.ledger_file = self.ledger_dir / "negative_guard_recommendations_ledger.json"
        self._entries: Dict[str, Dict[str, Any]] = {}
        self._load()

    def _load(self) -> None:
        """Loads entries from persistent file if it exists."""
        if self.ledger_file.is_file():
            try:
                with open(self.ledger_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    self._entries = data
            except Exception:
                # If corrupted, start clean to prevent crashing
                self._entries = {}

    def _save(self) -> None:
        """Atomically saves entries to persistent file."""
        self.ledger_dir.mkdir(parents=True, exist_ok=True)
        tmp_file = self.ledger_file.with_suffix(".tmp")
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(self._entries, f, indent=2, ensure_ascii=False)
        tmp_file.replace(self.ledger_file)

    @staticmethod
    def make_key(manifest_hash: str, recommendation_hash: str) -> str:
        return f"{manifest_hash}:{recommendation_hash}"

    def is_recorded(self, manifest_hash: str, recommendation_hash: str) -> bool:
        """Returns True if the recommendation has already been recorded for this snapshot manifest."""
        key = self.make_key(manifest_hash, recommendation_hash)
        return key in self._entries

    def record(
        self,
        manifest_hash: str,
        recommendation_hash: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Records a recommendation hash under the specified snapshot manifest hash."""
        key = self.make_key(manifest_hash, recommendation_hash)
        self._entries[key] = metadata or {"recorded": True}
        self._save()

    def count(self) -> int:
        return len(self._entries)

    def clear(self) -> None:
        self._entries.clear()
        if self.ledger_file.is_file():
            try:
                self.ledger_file.unlink()
            except Exception:
                pass
