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

# Conditional imports — google-ads-python and protobuf libraries
try:
    from google.ads.googleads.client import GoogleAdsClient  # type: ignore
    _GOOGLE_ADS_AVAILABLE = True
except ImportError:
    _GOOGLE_ADS_AVAILABLE = False

try:
    from google.ads.googleads.util import convert_proto_plus_to_protobuf  # type: ignore
except ImportError:
    convert_proto_plus_to_protobuf = None

try:
    import proto  # type: ignore
except ImportError:
    proto = None

try:
    from google.protobuf.message import Message as ProtobufMessage  # type: ignore
except ImportError:
    ProtobufMessage = None

try:
    from google.protobuf.json_format import MessageToDict  # type: ignore
except ImportError:
    MessageToDict = None


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

    @classmethod
    def _row_to_protobuf_message(cls, row: Any) -> Any:
        """Converts any supported row format into a native protobuf Message.

        Supported formats:
        1. Native protobuf message (google.protobuf.message.Message)
        2. Proto-plus message (proto.Message)

        Uses official google-ads-python utility when available, or equivalent
        supported mechanism (e.g. type(row).pb(row) / row._pb).

        Fails closed (TypeError) for any unsupported or unknown row type.
        """
        if row is None:
            raise TypeError("ROW_CONVERSION_FAILED: Row is None. Fail-closed.")

        # 1. Official google-ads-python utility (handles proto.Message and native protobuf)
        if convert_proto_plus_to_protobuf is not None:
            try:
                return convert_proto_plus_to_protobuf(row)
            except TypeError:
                pass  # Fall through to explicit checks or duck-typing

        # 2. Proto-plus message instance
        if proto is not None and isinstance(row, proto.Message):
            if hasattr(type(row), "pb") and callable(getattr(type(row), "pb")):
                return type(row).pb(row)
            if hasattr(row, "_pb"):
                return row._pb

        # 3. Duck-typed proto-plus (e.g. mock objects exposing ._pb or type.pb)
        if hasattr(row, "_pb") and hasattr(row._pb, "DESCRIPTOR"):
            return row._pb
        if hasattr(type(row), "pb") and callable(getattr(type(row), "pb")):
            try:
                candidate = type(row).pb(row)
                if hasattr(candidate, "DESCRIPTOR"):
                    return candidate
            except Exception:
                pass

        # 4. Native protobuf Message instance
        if ProtobufMessage is not None and isinstance(row, ProtobufMessage):
            return row

        # 5. Duck-typed native protobuf message
        if hasattr(row, "DESCRIPTOR") and (hasattr(row, "ListFields") or hasattr(row.DESCRIPTOR, "fields")):
            return row

        # Fail-closed: unsupported row type. Never fallback to str(row) or invent structure.
        raise TypeError(
            f"ROW_CONVERSION_FAILED: Unsupported row type '{type(row).__name__}'. "
            "Row must be a native protobuf or proto-plus message. Fail-closed."
        )

    @classmethod
    def _protobuf_row_to_dict(cls, row: Any) -> Dict[str, Any]:
        """Converts a GoogleAdsRow (protobuf or proto-plus) to a plain dict.

        Explicitly supports both formats officially used by google-ads-python:
        1. Native protobuf (google.protobuf.message.Message)
        2. Proto-plus (proto.Message)

        Preserves the nested structure expected by GoogleAdsNegativeReadAdapter:
        campaign, ad_group, shared_set, customer_negative_criterion,
        shared_criterion, campaign_criterion, ad_group_criterion, keyword.

        Fails closed (TypeError/ValueError) if the row cannot be converted.
        Never uses str(row) as an operational fallback.
        """
        pb_msg = cls._row_to_protobuf_message(row)

        if MessageToDict is not None:
            try:
                result = MessageToDict(
                    pb_msg,
                    preserving_proto_field_name=True,
                )
            except Exception:
                result = cls._extract_proto_value(pb_msg)
        else:
            result = cls._extract_proto_value(pb_msg)

        if not isinstance(result, dict):
            raise ValueError(
                f"ROW_CONVERSION_FAILED: Expected dict from protobuf conversion, got {type(result).__name__}."
            )

        # Normalize field names and promote nested keyword structure
        cls._normalize_nested_row_structure(result)

        return result

    @staticmethod
    def _normalize_nested_row_structure(result: Dict[str, Any]) -> None:
        """Normalizes nested fields to match GoogleAdsNegativeReadAdapter expectations.

        1. Recursively maps 'type_' to 'type' if 'type' is not present (due to Python keyword collision).
        2. Promotes 'keyword' from nested criteria (campaign_criterion, shared_criterion,
           ad_group_criterion) to top-level if not already present, ensuring both nested
           and top-level access succeed.
        """
        def _norm_type_keys(obj: Any) -> None:
            if isinstance(obj, dict):
                if "type_" in obj and "type" not in obj:
                    obj["type"] = obj["type_"]
                for v in obj.values():
                    _norm_type_keys(v)
            elif isinstance(obj, list):
                for item in obj:
                    _norm_type_keys(item)

        _norm_type_keys(result)

        for crit_key in ("campaign_criterion", "shared_criterion", "ad_group_criterion"):
            crit = result.get(crit_key)
            if isinstance(crit, dict) and "keyword" in crit:
                if "keyword" not in result:
                    result["keyword"] = crit["keyword"]
                break

    @classmethod
    def _extract_proto_value(cls, value: Any) -> Any:
        """Recursively extracts value from protobuf message or field."""
        if hasattr(value, "ListFields"):
            nested: Dict[str, Any] = {}
            for fd, f_val in value.ListFields():
                nested[fd.name] = cls._extract_proto_value(f_val)
            return nested
        if hasattr(value, "DESCRIPTOR"):
            nested = {}
            for fd in value.DESCRIPTOR.fields:
                val = getattr(value, fd.name, None)
                if val is not None:
                    nested[fd.name] = cls._extract_proto_value(val)
            return nested
        if isinstance(value, (list, tuple)):
            return [cls._extract_proto_value(v) for v in value]
        return value
