"""Google Ads Live Executor — Minimal read-only GAQL executor for Negative Guard.

Implements:
- Runtime configuration from external private file (not in repo).
- GoogleAdsClient.load_from_storage + GoogleAdsService.search_stream integration.
- Only GAQL SELECT queries. No mutate/create/update/delete.
- Converts GoogleAdsRow/protobuf to dict for GoogleAdsNegativeReadAdapter.
- Never prints customer IDs, tokens, or config values.
- Fail-closed if config is missing or google-ads library is unavailable.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# Conditional import — google-ads-python is runtime-only, not a repo dependency
try:
    from google.ads.googleads.client import GoogleAdsClient  # type: ignore
    _GOOGLE_ADS_AVAILABLE = True
except ImportError:
    _GOOGLE_ADS_AVAILABLE = False


class GoogleAdsLiveExecutor:
    """Minimal live executor for read-only GAQL SELECT queries against Google Ads API.

    Receives all configuration from an external private file (--runtime-config-path).
    Never stores or prints customer IDs, tokens, or config values in logs or output.
    """

    def __init__(self, runtime_config_path: Path):
        """Initialize from a runtime config JSON file.

        Expected schema:
        {
            "google_ads_config_path": "/path/to/google-ads.yaml",
            "customer_id": "1234567890",
            "campaign_contract_path": "/path/to/campaign_contracts.json",
            "ledger_path": "/path/to/ledger_dir"
        }
        """
        if not runtime_config_path.is_file():
            raise FileNotFoundError(
                f"RUNTIME_CONFIG_MISSING: Config file not found: {runtime_config_path}. "
                "Fail-closed: live execution requires explicit runtime configuration."
            )

        with open(runtime_config_path, "r", encoding="utf-8") as f:
            self._config: Dict[str, Any] = json.load(f)

        self._google_ads_config_path = self._config.get("google_ads_config_path", "")
        self._customer_id = self._config.get("customer_id", "")
        self._campaign_contract_path = self._config.get("campaign_contract_path", "")
        self._ledger_path = self._config.get("ledger_path", "")

        if not self._google_ads_config_path:
            raise ValueError("RUNTIME_CONFIG_INCOMPLETE: 'google_ads_config_path' is required.")
        if not self._customer_id:
            raise ValueError("RUNTIME_CONFIG_INCOMPLETE: 'customer_id' is required.")

        self._client = None

    @property
    def customer_id(self) -> str:
        """Returns customer ID. Not for printing — use only for API calls."""
        return self._customer_id

    @property
    def campaign_contract_path(self) -> Optional[str]:
        return self._campaign_contract_path or None

    @property
    def ledger_path(self) -> Optional[str]:
        return self._ledger_path or None

    def is_available(self) -> bool:
        """Checks if the google-ads library is installed."""
        return _GOOGLE_ADS_AVAILABLE

    def _get_client(self):
        """Lazily initializes the GoogleAdsClient from the config YAML."""
        if not _GOOGLE_ADS_AVAILABLE:
            raise RuntimeError(
                "GOOGLE_ADS_LIBRARY_MISSING: google-ads Python library is not installed. "
                "Install with: pip install google-ads"
            )
        if self._client is None:
            config_path = Path(self._google_ads_config_path)
            if not config_path.is_file():
                raise FileNotFoundError(
                    f"GOOGLE_ADS_CONFIG_MISSING: {config_path}. "
                    "Fail-closed: live API requires valid google-ads.yaml."
                )
            self._client = GoogleAdsClient.load_from_storage(str(config_path))
        return self._client

    def execute_gaql_select(self, query: str) -> List[Dict[str, Any]]:
        """Executes a GAQL SELECT query and returns results as list of dicts.

        Only SELECT queries are allowed. Fail-closed for any mutation attempt.
        """
        # Safety check: only allow SELECT queries
        query_upper = query.strip().upper()
        if not query_upper.startswith("SELECT"):
            raise ValueError(
                f"GAQL_MUTATION_BLOCKED: Only SELECT queries are allowed. "
                f"Received query starting with: {query_upper[:20]}..."
            )

        client = self._get_client()
        ga_service = client.get_service("GoogleAdsService")

        rows: List[Dict[str, Any]] = []
        try:
            stream = ga_service.search_stream(
                customer_id=self._customer_id,
                query=query,
            )
            for batch in stream:
                for row in batch.results:
                    rows.append(self._protobuf_row_to_dict(row))
        except Exception as e:
            # Never log the customer ID or credentials
            logger.error("GAQL query execution failed: %s", type(e).__name__)
            raise

        return rows

    def create_gaql_executor(self):
        """Returns a callable (customer_id, query) -> List[Dict] for use with GoogleAdsNegativeReadAdapter."""
        def executor(customer_id: str, query: str) -> List[Dict[str, Any]]:
            # Ignore the customer_id parameter — we use the one from config
            return self.execute_gaql_select(query)
        return executor

    @staticmethod
    def _protobuf_row_to_dict(row) -> Dict[str, Any]:
        """Converts a GoogleAdsRow protobuf message to a plain dict.

        Handles nested protobuf messages by recursively extracting fields.
        """
        result: Dict[str, Any] = {}

        try:
            # Use protobuf message descriptor to iterate fields
            for field_descriptor in row.DESCRIPTOR.fields:
                field_name = field_descriptor.name
                value = getattr(row, field_name, None)
                if value is not None:
                    result[field_name] = GoogleAdsLiveExecutor._extract_proto_value(value)
        except AttributeError:
            # Fallback: try to convert via __dict__ or str
            try:
                from google.protobuf.json_format import MessageToDict  # type: ignore
                result = MessageToDict(row, preserving_proto_field_name=True)
            except Exception:
                result = {"_raw": str(row)}

        return result

    @staticmethod
    def _extract_proto_value(value) -> Any:
        """Recursively extracts value from protobuf field."""
        if hasattr(value, "DESCRIPTOR"):
            # Nested message
            nested = {}
            for fd in value.DESCRIPTOR.fields:
                nested[fd.name] = GoogleAdsLiveExecutor._extract_proto_value(
                    getattr(value, fd.name, None)
                )
            return nested
        if isinstance(value, (list, tuple)):
            return [GoogleAdsLiveExecutor._extract_proto_value(v) for v in value]
        return value
