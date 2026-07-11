"""Export the two Google Ads diagnosis reports that failed in v01.

Read-only only: this script performs GAQL SELECT queries and never mutates
campaigns, budgets, bids, ads, keywords, conversions, or account settings.
Raw outputs must remain outside the repository.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
LONG_NUMBER_PATTERN = re.compile(r"(?<!\d)\d{7,}(?!\d)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export corrected search-term and landing-page reports."
    )
    parser.add_argument("--config-path", required=True)
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--end-date",
        help="Optional complete-data end date in YYYY-MM-DD. Default: yesterday.",
    )
    parser.add_argument("--execute", action="store_true")
    return parser.parse_args()


def external_file(value: str) -> Path:
    path = Path(value).expanduser().resolve()
    if path == REPO_ROOT or REPO_ROOT in path.parents:
        raise ValueError("Config path must be outside the repository.")
    if not path.is_file():
        raise FileNotFoundError(f"Config file not found: {path}")
    return path


def external_dir(value: str) -> Path:
    path = Path(value).expanduser().resolve()
    if path == REPO_ROOT or REPO_ROOT in path.parents:
        raise ValueError("Output directory must be outside the repository.")
    return path


def sanitize(value: Any) -> str:
    text = "" if value is None else str(value)
    text = EMAIL_PATTERN.sub("[REDACTED_EMAIL]", text)
    return LONG_NUMBER_PATTERN.sub("[REDACTED_NUMBER]", text)


def enum_name(value: Any) -> str:
    return str(getattr(value, "name", value or ""))


def pct(value: Any) -> float:
    try:
        return round(float(value) * 100, 6)
    except (TypeError, ValueError):
        return 0.0


def money(value: Any) -> float:
    try:
        return round(float(value) / 1_000_000, 6)
    except (TypeError, ValueError):
        return 0.0


def base_metrics(row: Any) -> Dict[str, Any]:
    metrics = row.metrics
    return {
        "impressions": int(metrics.impressions),
        "clicks": int(metrics.clicks),
        "ctr_pct": pct(metrics.ctr),
        "cost_currency": money(metrics.cost_micros),
        "average_cpc_currency": money(metrics.average_cpc),
        "conversions": round(float(metrics.conversions), 6),
        "all_conversions": round(float(metrics.all_conversions), 6),
        "conversion_rate_pct": pct(metrics.conversions_from_interactions_rate),
        "cost_per_conversion_currency": money(metrics.cost_per_conversion),
    }


def write_csv(path: Path, fields: Sequence[str], rows: Sequence[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def search_rows(client: Any, customer_id: str, query: str) -> Iterable[Any]:
    service = client.get_service("GoogleAdsService")
    for batch in service.search_stream(customer_id=customer_id, query=query):
        yield from batch.results


def load_client(config_path: Path):
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:
        raise RuntimeError("Missing dependency: pip install google-ads") from exc
    return GoogleAdsClient.load_from_storage(path=str(config_path))


def api_error(exc: Exception) -> Dict[str, str]:
    messages: List[str] = []
    failure = getattr(exc, "failure", None)
    for error in getattr(failure, "errors", []) if failure is not None else []:
        if getattr(error, "message", None):
            messages.append(str(error.message))
    return {
        "type": type(exc).__name__,
        "request_id": str(getattr(exc, "request_id", "")),
        "message": " | ".join(messages) if messages else str(exc),
    }


def main() -> int:
    args = parse_args()
    if not 1 <= args.days <= 730:
        print("ERROR: --days must be between 1 and 730.")
        return 1

    try:
        config_path = external_file(args.config_path)
        output_dir = external_dir(args.output_dir)
        end_date = (
            date.fromisoformat(args.end_date)
            if args.end_date
            else date.today() - timedelta(days=1)
        )
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    start_date = end_date - timedelta(days=args.days - 1)
    manifest: Dict[str, Any] = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "date_range_start": start_date.isoformat(),
        "date_range_end": end_date.isoformat(),
        "requested_days": args.days,
        "read_only": True,
        "reports": [],
        "errors": [],
    }

    if not args.execute:
        print("DRY_RUN_READY")
        print(f"DATE_RANGE: {start_date} to {end_date}")
        print(f"OUTPUT_DIR: {output_dir}")
        print("REPORTS: 05_search_terms_daily.csv, 07_landing_pages_daily.csv")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    client = load_client(config_path)
    date_filter = f"segments.date BETWEEN '{start_date}' AND '{end_date}'"
    common_metrics = """
      metrics.impressions,
      metrics.clicks,
      metrics.ctr,
      metrics.cost_micros,
      metrics.average_cpc,
      metrics.conversions,
      metrics.all_conversions,
      metrics.conversions_from_interactions_rate,
      metrics.cost_per_conversion
    """

    reports = [
        {
            "file": "05_search_terms_daily.csv",
            "fields": (
                "date", "campaign_name", "ad_group_name", "keyword_text",
                "keyword_match_type", "search_term", "search_term_match_type",
                "search_term_targeting_status", "device", "ad_network_type",
                "impressions", "clicks", "ctr_pct", "cost_currency",
                "average_cpc_currency", "conversions", "all_conversions",
                "conversion_rate_pct", "cost_per_conversion_currency",
            ),
            "query": f"""
              SELECT
                segments.date,
                campaign.name,
                ad_group.name,
                segments.keyword.info.text,
                segments.keyword.info.match_type,
                search_term_view.search_term,
                search_term_view.status,
                segments.search_term_match_type,
                segments.device,
                segments.ad_network_type,
                {common_metrics}
              FROM search_term_view
              WHERE {date_filter}
                AND campaign.advertising_channel_type = 'SEARCH'
              ORDER BY metrics.cost_micros DESC
            """,
            "formatter": lambda row: {
                "date": str(row.segments.date),
                "campaign_name": str(row.campaign.name),
                "ad_group_name": str(row.ad_group.name),
                "keyword_text": sanitize(row.segments.keyword.info.text),
                "keyword_match_type": enum_name(row.segments.keyword.info.match_type),
                "search_term": sanitize(row.search_term_view.search_term),
                "search_term_match_type": enum_name(row.segments.search_term_match_type),
                "search_term_targeting_status": enum_name(row.search_term_view.status),
                "device": enum_name(row.segments.device),
                "ad_network_type": enum_name(row.segments.ad_network_type),
                **base_metrics(row),
            },
        },
        {
            "file": "07_landing_pages_daily.csv",
            "fields": (
                "date", "campaign_name", "ad_group_name", "channel_type",
                "expanded_final_url", "device", "impressions", "clicks",
                "ctr_pct", "cost_currency", "average_cpc_currency",
                "conversions", "all_conversions", "conversion_rate_pct",
                "cost_per_conversion_currency",
            ),
            "query": f"""
              SELECT
                segments.date,
                campaign.name,
                ad_group.name,
                campaign.advertising_channel_type,
                expanded_landing_page_view.expanded_final_url,
                segments.device,
                {common_metrics}
              FROM expanded_landing_page_view
              WHERE {date_filter}
                AND campaign.advertising_channel_type = 'SEARCH'
              ORDER BY metrics.cost_micros DESC
            """,
            "formatter": lambda row: {
                "date": str(row.segments.date),
                "campaign_name": str(row.campaign.name),
                "ad_group_name": str(row.ad_group.name),
                "channel_type": enum_name(row.campaign.advertising_channel_type),
                "expanded_final_url": sanitize(
                    row.expanded_landing_page_view.expanded_final_url
                ),
                "device": enum_name(row.segments.device),
                **base_metrics(row),
            },
        },
    ]

    for report in reports:
        try:
            rows = [report["formatter"](row) for row in search_rows(
                client, args.customer_id, report["query"]
            )]
            write_csv(output_dir / report["file"], report["fields"], rows)
            manifest["reports"].append({
                "file": report["file"], "rows": len(rows), "status": "ok"
            })
        except Exception as exc:
            error = {"file": report["file"], **api_error(exc)}
            manifest["errors"].append(error)
            manifest["reports"].append({
                "file": report["file"], "rows": 0, "status": "error"
            })

    with (output_dir / "manifest_missing_reports.json").open(
        "w", encoding="utf-8"
    ) as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)

    ok_count = sum(item["status"] == "ok" for item in manifest["reports"])
    print(f"MISSING_REPORTS_READY: {ok_count}/2")
    for item in manifest["reports"]:
        print(f"{item['file']}: {item['status']} rows={item['rows']}")
    return 0 if not manifest["errors"] else 2


if __name__ == "__main__":
    sys.exit(main())
