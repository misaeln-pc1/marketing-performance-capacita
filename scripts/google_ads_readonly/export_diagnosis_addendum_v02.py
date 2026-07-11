"""Export missing Google Ads diagnosis layers in strict read-only mode.

This addendum complements export_campaign_summary.py with:
- search terms and triggering keywords;
- effective landing pages;
- hour/day/device/network performance;
- customer-level search term insight categories when available.

All Google Ads requests are GAQL SELECT queries. Raw outputs must remain outside
this public repository.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Sequence, Tuple

EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
LONG_NUMBER_PATTERN = re.compile(r"(?<!\d)\d{7,}(?!\d)")
ReportFormatter = Callable[[Any, str], Dict[str, Any]]
ReportSpec = Tuple[str, str, Sequence[str], ReportFormatter]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export Google Ads diagnosis addendum V02 in read-only mode."
    )
    parser.add_argument("--config-path", required=True)
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--execute", action="store_true")
    return parser.parse_args()


def detect_repo_root(script_path: Path) -> Path | None:
    for candidate in (script_path.parent, *script_path.parents):
        if (candidate / ".git").exists() or (
            (candidate / "PROJECT_CONTEXT.md").exists()
            and (candidate / "README.md").exists()
        ):
            return candidate.resolve()
    return None


def resolve_external_file(path_value: str, repo_root: Path | None) -> Path:
    path = Path(path_value).expanduser().resolve()
    if repo_root and (path == repo_root or repo_root in path.parents):
        raise ValueError("Config path must be outside the repository.")
    if not path.is_file():
        raise FileNotFoundError(f"Config file not found: {path}")
    return path


def resolve_external_dir(path_value: str, repo_root: Path | None) -> Path:
    path = Path(path_value).expanduser().resolve()
    if repo_root and (path == repo_root or repo_root in path.parents):
        raise ValueError("Output directory must be outside the repository.")
    return path


def validate_days(days: int) -> None:
    if days < 1 or days > 730:
        raise ValueError("--days must be between 1 and 730.")


def build_client(config_path: Path):
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:
        raise RuntimeError("Missing dependency: pip install google-ads") from exc
    return GoogleAdsClient.load_from_storage(path=str(config_path))


def enum_name(value: Any) -> str:
    if value is None:
        return ""
    if hasattr(value, "name"):
        return str(value.name)
    return str(value)


def sanitize_text(value: Any) -> str:
    text = "" if value is None else str(value)
    text = EMAIL_PATTERN.sub("[REDACTED_EMAIL]", text)
    text = LONG_NUMBER_PATTERN.sub("[REDACTED_NUMBER]", text)
    return text


def money_from_micros(value: Any) -> float:
    try:
        return round(float(value) / 1_000_000, 6)
    except (TypeError, ValueError):
        return 0.0


def percentage(value: Any) -> float:
    try:
        return round(float(value) * 100, 6)
    except (TypeError, ValueError):
        return 0.0


def write_csv(path: Path, fieldnames: Sequence[str], rows: Sequence[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def search_rows(client: Any, customer_id: str, query: str) -> Iterable[Any]:
    service = client.get_service("GoogleAdsService")
    stream = service.search_stream(customer_id=customer_id, query=query)
    for batch in stream:
        yield from batch.results


def fetch_currency(client: Any, customer_id: str) -> str:
    query = "SELECT customer.currency_code FROM customer LIMIT 1"
    row = next(iter(search_rows(client, customer_id, query)), None)
    return str(row.customer.currency_code) if row is not None else ""


def base_metrics(row: Any) -> Dict[str, Any]:
    metrics = row.metrics
    return {
        "impressions": int(metrics.impressions),
        "clicks": int(metrics.clicks),
        "ctr_pct": percentage(metrics.ctr),
        "cost_currency": money_from_micros(metrics.cost_micros),
        "average_cpc_currency": money_from_micros(metrics.average_cpc),
        "conversions": round(float(metrics.conversions), 6),
        "all_conversions": round(float(metrics.all_conversions), 6),
        "conversion_rate_pct": percentage(metrics.conversions_from_interactions_rate),
        "cost_per_conversion_currency": money_from_micros(metrics.cost_per_conversion),
    }


def format_search_term(row: Any, currency_code: str) -> Dict[str, Any]:
    result = {
        "date": str(row.segments.date),
        "campaign_name": str(row.campaign.name),
        "ad_group_name": str(row.ad_group.name),
        "channel_type": enum_name(row.campaign.advertising_channel_type),
        "keyword_text": sanitize_text(row.segments.keyword.info.text),
        "keyword_match_type": enum_name(row.segments.keyword.info.match_type),
        "search_term": sanitize_text(row.search_term_view.search_term),
        "search_term_match_type": enum_name(row.segments.search_term_match_type),
        "device": enum_name(row.segments.device),
        "ad_network_type": enum_name(row.segments.ad_network_type),
        "currency_code": currency_code,
    }
    result.update(base_metrics(row))
    return result


def format_landing(row: Any, currency_code: str) -> Dict[str, Any]:
    result = {
        "date": str(row.segments.date),
        "campaign_name": str(row.campaign.name),
        "ad_group_name": str(row.ad_group.name),
        "channel_type": enum_name(row.campaign.advertising_channel_type),
        "expanded_final_url": sanitize_text(
            row.expanded_landing_page_view.expanded_final_url
        ),
        "device": enum_name(row.segments.device),
        "currency_code": currency_code,
    }
    result.update(base_metrics(row))
    return result


def format_hour_day(row: Any, currency_code: str) -> Dict[str, Any]:
    result = {
        "date": str(row.segments.date),
        "day_of_week": enum_name(row.segments.day_of_week),
        "hour": int(row.segments.hour),
        "campaign_name": str(row.campaign.name),
        "device": enum_name(row.segments.device),
        "ad_network_type": enum_name(row.segments.ad_network_type),
        "currency_code": currency_code,
    }
    result.update(base_metrics(row))
    return result


def format_search_insight(row: Any, currency_code: str) -> Dict[str, Any]:
    return {
        "date": str(row.segments.date),
        "category_label": sanitize_text(
            row.customer_search_term_insight.category_label
        ),
        "search_subcategory": sanitize_text(row.segments.search_subcategory),
        "search_term": sanitize_text(row.segments.search_term),
        "currency_code": currency_code,
        "impressions": int(row.metrics.impressions),
        "clicks": int(row.metrics.clicks),
        "ctr_pct": percentage(row.metrics.ctr),
        "conversions": round(float(row.metrics.conversions), 6),
        "conversion_rate_pct": percentage(
            row.metrics.conversions_from_interactions_rate
        ),
    }


def build_reports(start_date: date, end_date: date) -> List[ReportSpec]:
    date_filter = (
        f"segments.date BETWEEN '{start_date.isoformat()}' "
        f"AND '{end_date.isoformat()}'"
    )
    common = """
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
    return [
        (
            "11_search_terms_daily_v02.csv",
            f"""
                SELECT
                  segments.date,
                  campaign.name,
                  campaign.advertising_channel_type,
                  ad_group.name,
                  segments.keyword.info.text,
                  segments.keyword.info.match_type,
                  search_term_view.search_term,
                  segments.search_term_match_type,
                  segments.device,
                  segments.ad_network_type,
                  {common}
                FROM search_term_view
                WHERE {date_filter}
                  AND campaign.advertising_channel_type = 'SEARCH'
                ORDER BY metrics.cost_micros DESC
            """,
            (
                "date", "campaign_name", "ad_group_name", "channel_type",
                "keyword_text", "keyword_match_type", "search_term",
                "search_term_match_type", "device", "ad_network_type",
                "currency_code", "impressions", "clicks", "ctr_pct",
                "cost_currency", "average_cpc_currency", "conversions",
                "all_conversions", "conversion_rate_pct",
                "cost_per_conversion_currency",
            ),
            format_search_term,
        ),
        (
            "12_landing_pages_daily_v02.csv",
            f"""
                SELECT
                  segments.date,
                  campaign.name,
                  campaign.advertising_channel_type,
                  ad_group.name,
                  expanded_landing_page_view.expanded_final_url,
                  segments.device,
                  {common}
                FROM expanded_landing_page_view
                WHERE {date_filter}
                  AND campaign.advertising_channel_type = 'SEARCH'
                ORDER BY metrics.cost_micros DESC
            """,
            (
                "date", "campaign_name", "ad_group_name", "channel_type",
                "expanded_final_url", "device", "currency_code",
                "impressions", "clicks", "ctr_pct", "cost_currency",
                "average_cpc_currency", "conversions", "all_conversions",
                "conversion_rate_pct", "cost_per_conversion_currency",
            ),
            format_landing,
        ),
        (
            "13_hour_day_device_daily.csv",
            f"""
                SELECT
                  segments.date,
                  segments.day_of_week,
                  segments.hour,
                  segments.device,
                  segments.ad_network_type,
                  campaign.name,
                  campaign.advertising_channel_type,
                  {common}
                FROM campaign
                WHERE {date_filter}
                  AND campaign.advertising_channel_type = 'SEARCH'
                ORDER BY segments.date DESC, metrics.cost_micros DESC
            """,
            (
                "date", "day_of_week", "hour", "campaign_name", "device",
                "ad_network_type", "currency_code", "impressions", "clicks",
                "ctr_pct", "cost_currency", "average_cpc_currency",
                "conversions", "all_conversions", "conversion_rate_pct",
                "cost_per_conversion_currency",
            ),
            format_hour_day,
        ),
        (
            "14_customer_search_term_insights.csv",
            f"""
                SELECT
                  segments.date,
                  customer_search_term_insight.category_label,
                  segments.search_subcategory,
                  segments.search_term,
                  metrics.impressions,
                  metrics.clicks,
                  metrics.ctr,
                  metrics.conversions,
                  metrics.conversions_from_interactions_rate
                FROM customer_search_term_insight
                WHERE {date_filter}
                ORDER BY metrics.clicks DESC
            """,
            (
                "date", "category_label", "search_subcategory", "search_term",
                "currency_code", "impressions", "clicks", "ctr_pct",
                "conversions", "conversion_rate_pct",
            ),
            format_search_insight,
        ),
    ]


def format_api_error(exc: Exception) -> Dict[str, str]:
    messages: List[str] = []
    failure = getattr(exc, "failure", None)
    for error in getattr(failure, "errors", []) if failure is not None else []:
        message = getattr(error, "message", None)
        if message:
            messages.append(str(message))
    return {
        "type": type(exc).__name__,
        "request_id": str(getattr(exc, "request_id", "")),
        "message": " | ".join(messages) if messages else str(exc),
    }


def main() -> int:
    args = parse_args()
    repo_root = detect_repo_root(Path(__file__).resolve())
    try:
        validate_days(args.days)
        config_path = resolve_external_file(args.config_path, repo_root)
        output_dir = resolve_external_dir(args.output_dir, repo_root)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    end_date = date.today()
    start_date = end_date - timedelta(days=args.days - 1)
    reports = build_reports(start_date, end_date)

    if not args.execute:
        print("DRY_RUN: diagnosis addendum V02 ready")
        print(f"DATE_RANGE: {start_date.isoformat()} to {end_date.isoformat()}")
        print(f"REPORT_COUNT: {len(reports)}")
        print("OUTPUT_POLICY: external directory only")
        return 0

    try:
        client = build_client(config_path)
        currency_code = fetch_currency(client, args.customer_id)
    except Exception as exc:
        print(f"ERROR: {format_api_error(exc)}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest: Dict[str, Any] = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "date_range_start": start_date.isoformat(),
        "date_range_end": end_date.isoformat(),
        "window_days": args.days,
        "currency_code": currency_code,
        "read_only": True,
        "customer_id_included_in_outputs": False,
        "reports": [],
        "errors": [],
    }

    for filename, query, fieldnames, formatter in reports:
        try:
            rows = [
                formatter(row, currency_code)
                for row in search_rows(client, args.customer_id, query)
            ]
            write_csv(output_dir / filename, fieldnames, rows)
            manifest["reports"].append(
                {"file": filename, "rows": len(rows), "status": "ok"}
            )
            print(f"REPORT_READY: {filename} rows={len(rows)}")
        except Exception as exc:
            error = format_api_error(exc)
            error["file"] = filename
            manifest["errors"].append(error)
            manifest["reports"].append(
                {"file": filename, "rows": 0, "status": "error"}
            )
            print(f"REPORT_ERROR: {filename}: {error['message']}")

    with (output_dir / "manifest_addendum_v02.json").open(
        "w", encoding="utf-8"
    ) as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)

    print(f"ADDENDUM_READY: {output_dir}")
    print(
        "REPORTS_OK:",
        sum(1 for report in manifest["reports"] if report["status"] == "ok"),
    )
    print("REPORTS_ERROR:", len(manifest["errors"]))
    return 2 if manifest["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
