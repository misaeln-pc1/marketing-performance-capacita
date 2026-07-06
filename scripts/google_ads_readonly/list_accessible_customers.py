"""Read-only scaffold to list accessible Google Ads customers.

This script is intentionally conservative:
- secrets must come from env vars or an external local config path;
- config paths inside the repository are rejected;
- output is masked;
- no mutation methods are exposed.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, Iterable, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]
ALLOWED_ENV_VARS = (
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID",
    "GOOGLE_ADS_USE_PROTO_PLUS",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List accessible Google Ads customers in read-only mode.")
    parser.add_argument("--config-path", help="Absolute path to a local google-ads config file outside the repo.")
    parser.add_argument("--execute", action="store_true", help="Actually call the Google Ads API.")
    return parser.parse_args()


def ensure_external_config(config_path: Optional[str]) -> Optional[Path]:
    if not config_path:
        return None
    resolved = Path(config_path).expanduser().resolve()
    if REPO_ROOT in resolved.parents or resolved == REPO_ROOT:
        raise ValueError("Config path must be outside the repository.")
    if not resolved.is_file():
        raise FileNotFoundError(f"Config file not found: {resolved}")
    return resolved


def load_env_config() -> Dict[str, str]:
    return {key: value for key in ALLOWED_ENV_VARS if (value := os.getenv(key))}


def validate_read_only_inputs(config_path: Optional[Path], env_config: Dict[str, str]) -> None:
    if config_path is None and not env_config:
        raise ValueError("Missing local Google Ads configuration. Use env vars or --config-path outside the repo.")


def mask_customer_id(raw_customer_id: str) -> str:
    digits = "".join(ch for ch in raw_customer_id if ch.isdigit())
    if len(digits) < 7:
        return "***masked***"
    return f"{digits[:3]}-***-{digits[-4:]}"


def preview_configuration_source(config_path: Optional[Path], env_config: Dict[str, str]) -> str:
    if config_path:
        return f"external-config:{config_path.name}"
    return "env-vars:" + ",".join(sorted(env_config.keys()))


def list_accessible_customers(config_path: Optional[Path], env_config: Dict[str, str]) -> Iterable[str]:
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:
        raise RuntimeError("Missing dependency: pip install google-ads") from exc

    if config_path:
        client = GoogleAdsClient.load_from_storage(path=str(config_path))
    else:
        client = GoogleAdsClient.load_from_dict(
            {
                "developer_token": env_config["GOOGLE_ADS_DEVELOPER_TOKEN"],
                "client_id": env_config["GOOGLE_ADS_CLIENT_ID"],
                "client_secret": env_config["GOOGLE_ADS_CLIENT_SECRET"],
                "refresh_token": env_config["GOOGLE_ADS_REFRESH_TOKEN"],
                "login_customer_id": env_config.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID"),
                "use_proto_plus": env_config.get("GOOGLE_ADS_USE_PROTO_PLUS", "true").lower() == "true",
            }
        )

    service = client.get_service("CustomerService")
    response = service.list_accessible_customers()
    for resource_name in response.resource_names:
        yield resource_name.rsplit("/", 1)[-1]


def main() -> int:
    args = parse_args()
    try:
        config_path = ensure_external_config(args.config_path)
        env_config = load_env_config()
        validate_read_only_inputs(config_path, env_config)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    if not args.execute:
        source = preview_configuration_source(config_path, env_config)
        print("DRY_RUN: list_accessible_customers scaffold ready")
        print(f"CONFIG_SOURCE: {source}")
        print("NEXT_STEP: rerun with --execute in a local environment with external credentials")
        return 0

    try:
        customers = list(list_accessible_customers(config_path, env_config))
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    print(f"ACCESSIBLE_CUSTOMERS_COUNT: {len(customers)}")
    for customer_id in customers:
        print(mask_customer_id(customer_id))
    return 0


if __name__ == "__main__":
    sys.exit(main())
