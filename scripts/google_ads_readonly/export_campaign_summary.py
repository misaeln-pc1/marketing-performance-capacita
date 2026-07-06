"""Read-only scaffold for an aggregated campaign summary export.

This script is intentionally blocked from execution.
Reason: the repo has not yet approved the exact read-only report contract
or whether GAQL is acceptable for this use case.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Dict, Optional


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
    parser = argparse.ArgumentParser(description="Prepare a read-only aggregated campaign summary export.")
    parser.add_argument("--config-path", help="Absolute path to a local google-ads config file outside the repo.")
    parser.add_argument("--customer-id", help="Google Ads customer ID. Use only in local execution.")
    parser.add_argument(
        "--output-path",
        default=str(REPO_ROOT / "automation" / "google-ads-readonly" / "output" / "campaign-summary-placeholder.csv"),
        help="Local output path for a future aggregated summary.",
    )
    parser.add_argument("--execute", action="store_true", help="Reserved for future reviewed implementation.")
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


def validate_inputs(config_path: Optional[Path], env_config: Dict[str, str], customer_id: Optional[str]) -> None:
    if config_path is None and not env_config:
        raise ValueError("Missing local Google Ads configuration. Use env vars or --config-path outside the repo.")
    if not customer_id:
        raise ValueError("Missing --customer-id.")


def main() -> int:
    args = parse_args()
    try:
        config_path = ensure_external_config(args.config_path)
        env_config = load_env_config()
        validate_inputs(config_path, env_config, args.customer_id)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    print("BLOCKED_SCAFFOLD: campaign summary export is intentionally disabled")
    print("REASON: pending approval of a strict read-only report contract")
    print(f"OUTPUT_PLACEHOLDER: {Path(args.output_path).name}")
    if args.execute:
        print("ERROR: --execute is not enabled for this scaffold")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
