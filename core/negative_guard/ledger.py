"""Persistent ledger for recommendation idempotency across processes and sessions (Fail-Closed & Concurrency-Safe)."""

from __future__ import annotations

import enum
import json
import os
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Generator, Optional

DEFAULT_LEDGER_DIR = Path.home() / ".capacita" / "negative_guard_ledger"


class ClaimResult(str, enum.Enum):
    """Result of an atomic ledger claim operation."""
    CLAIMED = "CLAIMED"
    ALREADY_EXISTS = "ALREADY_EXISTS"
    HOLD_CORRUPT = "HOLD_CORRUPT"
    HOLD_LOCKED = "HOLD_LOCKED"


class RecommendationLedger:
    """Manages persistent deduplication keys keyed by manifest_hash + recommendation_hash.

    Implements:
    - Fail-closed on corruption (is_corrupt=True, no silent empty dict fallback).
    - Cross-process atomic locking to ensure concurrency safety.
    - Atomic claim_once() that combines reload + corruption check + existence + write.
    """

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
        self.lock_file = self.ledger_dir / "negative_guard_recommendations_ledger.lock"
        self._entries: Dict[str, Dict[str, Any]] = {}
        self.is_corrupt: bool = False
        self.corrupt_error: Optional[str] = None
        self._load()

    @contextmanager
    def _lock(self, timeout: float = 5.0) -> Generator[None, None, None]:
        """Atomic inter-process lock with fail-closed timeout."""
        self.ledger_dir.mkdir(parents=True, exist_ok=True)
        start = time.time()
        fd = None
        acquired = False
        while time.time() - start < timeout:
            try:
                fd = os.open(str(self.lock_file), os.O_CREAT | os.O_EXCL | os.O_RDWR)
                acquired = True
                break
            except FileExistsError:
                # Check stale lock (> 30 seconds)
                try:
                    mtime = self.lock_file.stat().st_mtime
                    if time.time() - mtime > 30.0:
                        self.lock_file.unlink(missing_ok=True)
                except Exception:
                    pass
                time.sleep(0.05)

        if not acquired:
            raise TimeoutError("CONCURRENCY_LOCKED: No se pudo adquirir el lock del ledger dentro del timeout.")

        try:
            yield
        finally:
            if acquired:
                try:
                    if fd is not None:
                        os.close(fd)
                    self.lock_file.unlink(missing_ok=True)
                except Exception:
                    pass

    def _load(self) -> None:
        """Loads entries from persistent file if it exists. Sets is_corrupt if JSON is corrupted."""
        if self.ledger_file.is_file():
            try:
                with open(self.ledger_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if not isinstance(data, dict):
                    self.is_corrupt = True
                    self.corrupt_error = "LEDGER_FORMAT_ERROR: Root is not a JSON object"
                    return
                self._entries = data
                self.is_corrupt = False
                self.corrupt_error = None
            except Exception as e:
                # Fail-closed: record corruption instead of overwriting with empty dict
                self.is_corrupt = True
                self.corrupt_error = str(e)

    def _save(self) -> None:
        """Atomically saves entries to persistent file."""
        if self.is_corrupt:
            raise RuntimeError(f"LEDGER_CORRUPT: Cannot save corrupt ledger ({self.corrupt_error})")
        self.ledger_dir.mkdir(parents=True, exist_ok=True)
        tmp_file = self.ledger_file.with_suffix(".tmp")
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(self._entries, f, indent=2, ensure_ascii=False)
        tmp_file.replace(self.ledger_file)

    @staticmethod
    def make_key(manifest_hash: str, recommendation_hash: str) -> str:
        return f"{manifest_hash}:{recommendation_hash}"

    def claim_once(
        self,
        manifest_hash: str,
        recommendation_hash: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> ClaimResult:
        """Atomic claim: reload + corruption check + existence + write if new.

        Within a single lock:
        1. Reload latest ledger state from disk.
        2. Check for corruption -> HOLD_CORRUPT.
        3. Check if key already exists -> ALREADY_EXISTS.
        4. Write new entry atomically -> CLAIMED.

        Returns ClaimResult indicating the outcome.
        """
        try:
            with self._lock():
                self._load()
                if self.is_corrupt:
                    return ClaimResult.HOLD_CORRUPT
                key = self.make_key(manifest_hash, recommendation_hash)
                if key in self._entries:
                    return ClaimResult.ALREADY_EXISTS
                self._entries[key] = metadata or {"recorded": True}
                self._save()
                return ClaimResult.CLAIMED
        except TimeoutError:
            return ClaimResult.HOLD_LOCKED

    def count(self) -> int:
        with self._lock():
            self._load()
            return len(self._entries)

    def clear(self) -> None:
        with self._lock():
            self._entries.clear()
            self.is_corrupt = False
            self.corrupt_error = None
            if self.ledger_file.is_file():
                try:
                    self.ledger_file.unlink()
                except Exception:
                    pass
