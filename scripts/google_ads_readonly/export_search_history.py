"""Export Google Ads read-only historical diagnostics to local CSV files.

This script performs GAQL read-only queries only. It writes raw Google Ads outputs
locally under automation/google-ads-readonly/output/ by default. Do not commit the
resulting CSV files because they may contain account, campaign, ad group, search
term, URL, or commercially sensitive data.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = REPO_ROOT / "automation" / "google-ads-readonly" / "output" / "google_ads_history"
ALLOWED_ENV_VARS = (
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID",
    "GOOGLE_ADS_USE_PROTO_PLUS",
)


@dataclass(frozen=True)
class ReportSpec:
    name: str
    filename: str
    query: str
    fields: List[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export Google Ads historical diagnostics in read-only mode.")
    parser.add_argument("--config-path", help="Absolute path to a local google-ads config file outside the repo.")
    parser.add_argument("--customer-id", required=True, help="Google Ads customer ID without dashes.")
    parser.add_argument("--start-date", help="Start date YYYY-MM-DD. Defaults to 30 days ago.")
    parser.add_argument("--end-date", help="End date YYYY-MM-DD. Defaults to today.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Local output directory for CSV files.")
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


def ensure_safe_output_dir(output_dir: str) -> Path:
    resolved = Path(output_dir).expanduser().resolve()
    # Default output is inside the repo output/ folder, which is intentionally gitignored.
    # If a custom path is used inside the repo, require it to stay under the approved output directory.
    approved_output_root = (REPO_ROOT / "automation" / "google-ads-readonly" / "output").resolve()
    if REPO_ROOT in resolved.parents and not (approved_output_root == resolved or approved_output_root in resolved.parents):
        raise ValueError("Output inside repo is only allowed under automation/google-ads-readonly/output/.")
    resolved.mkdir(parents=True, exist_ok=True)
    return resolved


def load_env_config() -> Dict[str, str]:
    return {key: value for key in ALLOWED_ENV_VARS if (value := os.getenv(key))}


def build_client(config_path: Optional[Path], env_config: Dict[str, str]):
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:
        raise RuntimeError("Missing dependency: pip install google-ads") from exc

    if config_path:
        return GoogleAdsClient.load_from_storage(path=str(config_path))

    required = [
        "GOOGLE_ADS_DEVELOPER_TOKEN",
        "GOOGLE_ADS_CLIENT_ID",
        "GOOGLE_ADS_CLIENT_SECRET",
        "GOOGLE_ADS_REFRESH_TOKEN",
    ]
    missing = [key for key in required if key not in env_config]
    if missing:
        raise ValueError(f"Missing env config keys: {', '.join(missing)}")

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


def resolve_date_range(start_date: Optional[str], end_date: Optional[str]) -> tuple[str, str]:
    end = date.fromisoformat(end_date) if end_date else date.today()
    start = date.fromisoformat(start_date) if start_date else end - timedelta(days=30)
    if start > end:
        raise ValueError("start-date cannot be after end-date.")
    return start.isoformat(), end.isoformat()


def metrics_common(prefix: str = "") -> List[str]:
    return [
        f"{prefix}metrics.impressions",
        f"{prefix}metrics.clicks",
        f"{prefix}metrics.ctr",
        f"{prefix}metrics.average_cpc",
        f"{prefix}metrics.cost_micros",
        f"{prefix}metrics.conversions",
        f"{prefix}metrics.conversions_from_interactions_rate",
    ]


def report_specs(start: str, end: str) -> List[ReportSpec]:
    return [
        ReportSpec(
            name="search_terms",
            filename="search_terms.csv",
            fields=[
                "date",
                "campaign_name",
                "ad_group_name",
                "search_term",
                "search_term_status",
                "impressions",
                "clicks",
                "ctr",
                "average_cpc_micros",
                "cost_micros",
                "conversions",
                "conversion_rate",
            ],
            query=f"""
                SELECT
                  segments.date,
                  campaign.name,
                  ad_group.name,
                  search_term_view.search_term,
                  search_term_view.status,
                  metrics.impressions,
                  metrics.clicks,
                  metrics.ctr,
                  metrics.average_cpc,
                  metrics.cost_micros,
                  metrics.conversions,
                  metrics.conversions_from_interactions_rate
                FROM search_term_view
                WHERE segments.date BETWEEN '{start}' AND '{end}'
                ORDER BY metrics.cost_micros DESC
            """,
        ),
        ReportSpec(
            name="keywords",
            filename="keywords.csv",
            fields=[
                "date",
                "campaign_name",
                "ad_group_name",
                "keyword_text",
                "keyword_match_type",
                "criterion_status",
                "impressions",
                "clicks",
                "ctr",
                "average_cpc_micros",
                "cost_micros",
                "conversions",
                "conversion_rate",
            ],
            query=f"""
                SELECT
                  segments.date,
                  campaign.name,
                  ad_group.name,
                  ad_group_criterion.keyword.text,
                  ad_group_criterion.keyword.match_type,
                  ad_group_criterion.status,
                  metrics.impressions,
                  metrics.clicks,
                  metrics.ctr,
                  metrics.average_cpc,
                  metrics.cost_micros,
                  metrics.conversions,
                  metrics.conversions_from_interactions_rate
                FROM keyword_view
                WHERE segments.date BETWEEN '{start}' AND '{end}'
                ORDER BY metrics.cost_micros DESC
            """,
        ),
        ReportSpec(
            name="landing_pages",
            filename="landing_pages.csv",
            fields=[
                "date",
                "expanded_final_url",
                "impressions",
                "clicks",
                "ctr",
                "average_cpc_micros",
                "cost_micros",
                "conversions",
                "conversion_rate",
            ],
            query=f"""
                SELECT
                  segments.date,
                  expanded_landing_page_view.expanded_final_url,
                  metrics.impressions,
                  metrics.clicks,
                  metrics.ctr,
                  metrics.average_cpc,
                  metrics.cost_micros,
                  metrics.conversions,
                  metrics.conversions_from_interactions_rate
                FROM expanded_landing_page_view
                WHERE segments.date BETWEEN '{start}' AND '{end}'
                ORDER BY metrics.cost_micros DESC
            """,
        ),
        ReportSpec(
            name="campaign_daily",
            filename="campaign_daily.csv",
            fields=[
                "date",
                "campaign_name",
                "campaign_channel_type",
                "impressions",
                "clicks",
                "ctr",
                "average_cpc_micros",
                "cost_micros",
                "conversions",
                "conversion_rate",
            ],
            query=f"""
                SELECT
                  segments.date,
                  campaign.name,
                  campaign.advertising_channel_type,
                  metrics.impressions,
                  metrics.clicks,
                  metrics.ctr,
                  metrics.average_cpc,
                  metrics.cost_micros,
                  metrics.conversions,
                  metrics.conversions_from_interactions_rate
                FROM campaign
                WHERE segments.date BETWEEN '{start}' AND '{end}'
                  AND campaign.status != 'REMOVED'
                ORDER BY segments.date DESC, metrics.cost_micros DESC
            """,
        ),
    ]


def enum_name(value) -> str:
    if hasattr(value, "name"):
        return value.name
    return str(value)


def row_to_dict(report_name: str, row) -> Dict[str, object]:
    metrics = row.metrics
    base = {
        "date": getattr(row.segments, "date", ""),
        "impressions": getattr(metrics, "impressions", 0),
        "clicks": getattr(metrics, "clicks", 0),
        "ctr": getattr(metrics, "ctr", 0),
        "average_cpc_micros": getattr(metrics, "average_cpc", 0),
        "cost_micros": getattr(metrics, "cost_micros", 0),
        "conversions": getattr(metrics, "conversions", 0),
        "conversion_rate": getattr(metrics, "conversions_from_interactions_rate", 0),
    }

    if report_name == "search_terms":
        base.update(
            {
                "campaign_name": row.campaign.name,
                "ad_group_name": row.ad_group.name,
                "search_term": row.search_term_view.search_term,
                "search_term_status": enum_name(row.search_term_view.status),
            }
        )
    elif report_name == "keywords":
        base.update(
            {
                "campaign_name": row.campaign.name,
                "ad_group_name": row.ad_group.name,
                "keyword_text": row.ad_group_criterion.keyword.text,
                "keyword_match_type": enum_name(row.ad_group_criterion.keyword.match_type),
                "criterion_status": enum_name(row.ad_group_criterion.status),
            }
        )
    elif report_name == "landing_pages":
        base.update({"expanded_final_url": row.expanded_landing_page_view.expanded_final_url})
    elif report_name == "campaign_daily":
        base.update(
            {
                "campaign_name": row.campaign.name,
                "campaign_channel_type": enum_name(row.campaign.advertising_channel_type),
            }
        )
    else:
        raise ValueError(f"Unsupported report: {report_name}")
    return base


def run_report(client, customer_id: str, spec: ReportSpec, output_dir: Path) -> int:
    service = client.get_service("GoogleAdsService")
    output_path = output_dir / spec.filename
    count = 0
    with output_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=spec.fields)
        writer.writeheader()
        stream = service.search_stream(customer_id=customer_id, query=spec.query)
        for batch in stream:
            for row in batch.results:
                writer.writerow(row_to_dict(spec.name, row))
                count += 1
    print(f"REPORT_READY: {spec.name} rows={count} file={output_path}")
    return count


def main() -> int:
    args = parse_args()
    try:
        config_path = ensure_external_config(args.config_path)
        output_dir = ensure_safe_output_dir(args.output_dir)
        env_config = load_env_config()
        start, end = resolve_date_range(args.start_date, args.end_date)
        specs = report_specs(start, end)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    if not args.execute:
        print("DRY_RUN: export_search_history ready")
        print(f"DATE_RANGE: {start} to {end}")
        print(f"OUTPUT_DIR: {output_dir}")
        for spec in specs:
            print(f"REPORT_PLANNED: {spec.name} -> {spec.filename}")
        print("NEXT_STEP: rerun with --execute in a local environment with external credentials")
        return 0

    try:
        client = build_client(config_path, env_config)
        for spec in specs:
            run_report(client, args.customer_id, spec, output_dir)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
