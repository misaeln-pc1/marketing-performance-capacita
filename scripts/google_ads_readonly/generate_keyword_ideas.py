"""Read-only scaffold to generate keyword ideas from local seed terms."""

from __future__ import annotations

import argparse
import csv
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SEEDS_FILE = REPO_ROOT / "automation" / "google-ads-readonly" / "keyword_seeds_presencial_santiago.csv"
ALLOWED_ENV_VARS = (
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID",
    "GOOGLE_ADS_USE_PROTO_PLUS",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate keyword ideas in read-only mode.")
    parser.add_argument("--config-path", help="Absolute path to a local google-ads config file outside the repo.")
    parser.add_argument("--customer-id", help="Google Ads customer ID. Use only in local execution.")
    parser.add_argument("--seeds-file", default=str(DEFAULT_SEEDS_FILE), help="CSV with local seed keywords.")
    parser.add_argument("--language-id", help="Google Ads language constant ID, for example 1000.")
    parser.add_argument("--geo-target-constant", action="append", default=[], help="Geo target constant ID.")
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


def load_seed_keywords(seeds_file: str) -> List[str]:
    path = Path(seeds_file).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Seeds file not found: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        seeds = [row["keyword_seed"].strip() for row in reader if row.get("keyword_seed")]
    if not seeds:
        raise ValueError("Seeds file is empty.")
    return seeds


def validate_inputs(
    *,
    config_path: Optional[Path],
    env_config: Dict[str, str],
    customer_id: Optional[str],
    language_id: Optional[str],
    geo_target_constants: List[str],
) -> None:
    if config_path is None and not env_config:
        raise ValueError("Missing local Google Ads configuration. Use env vars or --config-path outside the repo.")
    if not customer_id:
        raise ValueError("Missing --customer-id.")
    if not language_id:
        raise ValueError("Missing --language-id.")
    if not geo_target_constants:
        raise ValueError("At least one --geo-target-constant is required.")


def build_client(config_path: Optional[Path], env_config: Dict[str, str]):
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:
        raise RuntimeError("Missing dependency: pip install google-ads") from exc

    if config_path:
        return GoogleAdsClient.load_from_storage(path=str(config_path))
    return GoogleAdsClient.load_from_dict(
        {
            "developer_token": env_config["GOOGLE_ADS_DEVELOPER_TOKEN"],
            "client_id": env_config["GOOGLE_ADS_CLIENT_ID"],
            "client_secret": env_config["GOOGLE_ADS_CLIENT_SECRET"],
            "refresh_token": env_config["GOOGLE_ADS_REFRESH_TOKEN"],
            "login_customer_id": env_config.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID"),
            "use_proto_plus": env_config.get("GOOGLE_ADS_USE_PROTO_PLUS", "true").lower() == "true",
        }
    )


def generate_keyword_ideas(
    *,
    config_path: Optional[Path],
    env_config: Dict[str, str],
    customer_id: str,
    language_id: str,
    geo_target_constants: List[str],
    seed_keywords: List[str],
):
    client = build_client(config_path, env_config)
    googleads_service = client.get_service("GoogleAdsService")
    keyword_plan_idea_service = client.get_service("KeywordPlanIdeaService")
    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.language = googleads_service.language_constant_path(language_id)
    request.geo_target_constants.extend(
        googleads_service.geo_target_constant_path(geo_id) for geo_id in geo_target_constants
    )
    request.keyword_seed.keywords.extend(seed_keywords)
    request.include_adult_keywords = False
    return keyword_plan_idea_service.generate_keyword_ideas(request=request)


def format_competition(metrics) -> str:
    competition = getattr(metrics, "competition", "")
    if hasattr(competition, "name"):
        return str(competition.name)
    return str(competition)


def format_keyword_idea_row(idea) -> str:
    metrics = getattr(idea, "keyword_idea_metrics", None)
    avg_monthly_searches = ""
    competition = ""
    low_top_of_page_bid_micros = ""
    high_top_of_page_bid_micros = ""

    if metrics is not None:
        avg_monthly_searches = getattr(metrics, "avg_monthly_searches", "")
        competition = format_competition(metrics)
        low_top_of_page_bid_micros = getattr(metrics, "low_top_of_page_bid_micros", "")
        high_top_of_page_bid_micros = getattr(metrics, "high_top_of_page_bid_micros", "")

    return "\t".join(
        [
            getattr(idea, "text", "").strip(),
            str(avg_monthly_searches),
            competition,
            str(low_top_of_page_bid_micros),
            str(high_top_of_page_bid_micros),
        ]
    )


def main() -> int:
    args = parse_args()
    try:
        config_path = ensure_external_config(args.config_path)
        env_config = load_env_config()
        seed_keywords = load_seed_keywords(args.seeds_file)
        validate_inputs(
            config_path=config_path,
            env_config=env_config,
            customer_id=args.customer_id,
            language_id=args.language_id,
            geo_target_constants=args.geo_target_constant,
        )
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    if not args.execute:
        print("DRY_RUN: generate_keyword_ideas scaffold ready")
        print(f"SEED_KEYWORDS_COUNT: {len(seed_keywords)}")
        print(f"GEO_TARGET_CONSTANTS_COUNT: {len(args.geo_target_constant)}")
        print("NEXT_STEP: rerun with --execute in a local environment with external credentials")
        return 0

    try:
        response = generate_keyword_ideas(
            config_path=config_path,
            env_config=env_config,
            customer_id=args.customer_id,
            language_id=args.language_id,
            geo_target_constants=args.geo_target_constant,
            seed_keywords=seed_keywords,
        )
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    print("KEYWORD_IDEAS_READY")
    print(
        "keyword_idea_text\tavg_monthly_searches\tcompetition\tlow_top_of_page_bid_micros\thigh_top_of_page_bid_micros"
    )
    for idea in response.results:
        text = getattr(idea, "text", "").strip()
        if text:
            print(format_keyword_idea_row(idea))
    return 0


if __name__ == "__main__":
    sys.exit(main())
