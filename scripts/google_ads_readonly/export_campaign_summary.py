"""Export a multi-file Google Ads historical diagnosis in read-only mode.

The exporter performs GAQL SELECT queries only. It never mutates campaigns,
budgets, bids, ads, keywords, conversions, or account settings.

Raw outputs are required to live outside the repository.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
ALLOWED_ENV_VARS = (
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
    "GOOGLE_ADS_LOGIN_CUSTOMER_ID",
    "GOOGLE_ADS_USE_PROTO_PLUS",
)
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
LONG_NUMBER_PATTERN = re.compile(r"(?<!\d)\d{7,}(?!\d)")


ReportFormatter = Callable[[Any, str], Dict[str, Any]]
ReportSpec = Tuple[str, str, Sequence[str], ReportFormatter]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export a read-only Google Ads historical diagnosis bundle."
    )
    parser.add_argument(
        "--config-path",
        required=True,
        help="Absolute path to google-ads.yaml outside the repository.",
    )
    parser.add_argument(
        "--customer-id",
        required=True,
        help="Google Ads client customer ID. Use only in local execution.",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=90,
        help="Inclusive historical window ending today. Default: 90.",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Absolute output directory outside the repository.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually execute read-only Google Ads API queries.",
    )
    return parser.parse_args()


def ensure_external_file(path_value: str) -> Path:
    resolved = Path(path_value).expanduser().resolve()
    if REPO_ROOT in resolved.parents or resolved == REPO_ROOT:
        raise ValueError("Config path must be outside the repository.")
    if not resolved.is_file():
        raise FileNotFoundError(f"Config file not found: {resolved}")
    return resolved


def ensure_external_output_dir(path_value: str) -> Path:
    resolved = Path(path_value).expanduser().resolve()
    if REPO_ROOT in resolved.parents or resolved == REPO_ROOT:
        raise ValueError("Output directory must be outside the repository.")
    return resolved


def validate_days(days: int) -> None:
    if days < 1 or days > 730:
        raise ValueError("--days must be between 1 and 730.")


def load_env_config() -> Dict[str, str]:
    return {key: value for key in ALLOWED_ENV_VARS if (value := os.getenv(key))}


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


def join_values(values: Iterable[Any]) -> str:
    return " | ".join(sanitize_text(value) for value in values)


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


def quality_score(value: Any) -> Any:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return ""
    return parsed if parsed > 0 else ""


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
        for row in batch.results:
            yield row


def fetch_account_context(client: Any, customer_id: str) -> Tuple[str, str]:
    query = """
        SELECT
          customer.currency_code,
          customer.time_zone
        FROM customer
        LIMIT 1
    """
    row = next(iter(search_rows(client, customer_id, query)), None)
    if row is None:
        return "", ""
    return str(row.customer.currency_code), str(row.customer.time_zone)


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


def format_campaign_config(row: Any, currency_code: str) -> Dict[str, Any]:
    settings = row.campaign.network_settings
    return {
        "campaign_name": str(row.campaign.name),
        "campaign_status": enum_name(row.campaign.status),
        "channel_type": enum_name(row.campaign.advertising_channel_type),
        "bidding_strategy_type": enum_name(row.campaign.bidding_strategy_type),
        "daily_budget_currency": money_from_micros(row.campaign_budget.amount_micros),
        "currency_code": currency_code,
        "target_google_search": bool(settings.target_google_search),
        "target_search_network": bool(settings.target_search_network),
        "target_partner_search_network": bool(settings.target_partner_search_network),
        "target_content_network": bool(settings.target_content_network),
    }


def format_campaign_daily(row: Any, currency_code: str) -> Dict[str, Any]:
    result = {
        "date": str(row.segments.date),
        "campaign_name": str(row.campaign.name),
        "campaign_status": enum_name(row.campaign.status),
        "channel_type": enum_name(row.campaign.advertising_channel_type),
        "bidding_strategy_type": enum_name(row.campaign.bidding_strategy_type),
        "currency_code": currency_code,
        "search_impression_share_pct": percentage(row.metrics.search_impression_share),
        "search_budget_lost_impression_share_pct": percentage(
            row.metrics.search_budget_lost_impression_share
        ),
        "search_rank_lost_impression_share_pct": percentage(
            row.metrics.search_rank_lost_impression_share
        ),
        "top_impression_percentage_pct": percentage(row.metrics.top_impression_percentage),
        "absolute_top_impression_percentage_pct": percentage(
            row.metrics.absolute_top_impression_percentage
        ),
    }
    result.update(base_metrics(row))
    return result


def format_device_network(row: Any, currency_code: str) -> Dict[str, Any]:
    result = {
        "date": str(row.segments.date),
        "campaign_name": str(row.campaign.name),
        "device": enum_name(row.segments.device),
        "ad_network_type": enum_name(row.segments.ad_network_type),
        "currency_code": currency_code,
    }
    result.update(base_metrics(row))
    return result


def format_search_term(row: Any, currency_code: str) -> Dict[str, Any]:
    result = {
        "date": str(row.segments.date),
        "campaign_name": str(row.campaign.name),
        "ad_group_name": str(row.ad_group.name),
        "keyword_text": sanitize_text(row.segments.keyword.info.text),
        "keyword_match_type": enum_name(row.segments.keyword.info.match_type),
        "search_term": sanitize_text(row.search_term_view.search_term),
        "search_term_match_type": enum_name(row.segments.search_term_match_type),
        "search_term_targeting_status": enum_name(row.segments.search_term_targeting_status),
        "device": enum_name(row.segments.device),
        "ad_network_type": enum_name(row.segments.ad_network_type),
        "currency_code": currency_code,
    }
    result.update(base_metrics(row))
    return result


def format_keyword(row: Any, currency_code: str) -> Dict[str, Any]:
    quality = row.ad_group_criterion.quality_info
    result = {
        "date": str(row.segments.date),
        "campaign_name": str(row.campaign.name),
        "ad_group_name": str(row.ad_group.name),
        "keyword_text": sanitize_text(row.ad_group_criterion.keyword.text),
        "keyword_match_type": enum_name(row.ad_group_criterion.keyword.match_type),
        "keyword_status": enum_name(row.ad_group_criterion.status),
        "quality_score_current": quality_score(quality.quality_score),
        "ad_relevance_current": enum_name(quality.creative_quality_score),
        "landing_page_experience_current": enum_name(quality.post_click_quality_score),
        "expected_ctr_current": enum_name(quality.search_predicted_ctr),
        "currency_code": currency_code,
        "search_impression_share_pct": percentage(row.metrics.search_impression_share),
        "search_rank_lost_impression_share_pct": percentage(
            row.metrics.search_rank_lost_impression_share
        ),
        "search_exact_match_impression_share_pct": percentage(
            row.metrics.search_exact_match_impression_share
        ),
    }
    result.update(base_metrics(row))
    return result


def format_landing_page(row: Any, currency_code: str) -> Dict[str, Any]:
    result = {
        "date": str(row.segments.date),
        "campaign_name": str(row.campaign.name),
        "ad_group_name": str(row.ad_group.name),
        "expanded_final_url": sanitize_text(
            row.expanded_landing_page_view.expanded_final_url
        ),
        "device": enum_name(row.segments.device),
        "currency_code": currency_code,
    }
    result.update(base_metrics(row))
    return result


def format_conversion_action(row: Any, currency_code: str) -> Dict[str, Any]:
    return {
        "date": str(row.segments.date),
        "campaign_name": str(row.campaign.name),
        "conversion_action_name": sanitize_text(row.segments.conversion_action_name),
        "conversion_action_category": enum_name(row.segments.conversion_action_category),
        "conversions": round(float(row.metrics.conversions), 6),
        "all_conversions": round(float(row.metrics.all_conversions), 6),
        "conversions_value": round(float(row.metrics.conversions_value), 6),
        "all_conversions_value": round(float(row.metrics.all_conversions_value), 6),
        "currency_code": currency_code,
    }


def format_ad(row: Any, currency_code: str) -> Dict[str, Any]:
    result = {
        "date": str(row.segments.date),
        "campaign_name": str(row.campaign.name),
        "ad_group_name": str(row.ad_group.name),
        "ad_status": enum_name(row.ad_group_ad.status),
        "ad_type": enum_name(row.ad_group_ad.ad.type),
        "ad_strength": enum_name(row.ad_group_ad.ad_strength),
        "final_urls": join_values(row.ad_group_ad.ad.final_urls),
        "currency_code": currency_code,
    }
    result.update(base_metrics(row))
    return result


def build_report_specs(start_date: date, end_date: date) -> List[ReportSpec]:
    start = start_date.isoformat()
    end = end_date.isoformat()
    date_filter = f"segments.date BETWEEN '{start}' AND '{end}'"
    search_filter = "campaign.advertising_channel_type = 'SEARCH'"

    common_metric_fields = """
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
            "02_campaign_config.csv",
            """
                SELECT
                  campaign.name,
                  campaign.status,
                  campaign.advertising_channel_type,
                  campaign.bidding_strategy_type,
                  campaign.network_settings.target_google_search,
                  campaign.network_settings.target_search_network,
                  campaign.network_settings.target_partner_search_network,
                  campaign.network_settings.target_content_network,
                  campaign_budget.amount_micros
                FROM campaign
                WHERE campaign.advertising_channel_type = 'SEARCH'
                ORDER BY campaign.name
            """,
            (
                "campaign_name",
                "campaign_status",
                "channel_type",
                "bidding_strategy_type",
                "daily_budget_currency",
                "currency_code",
                "target_google_search",
                "target_search_network",
                "target_partner_search_network",
                "target_content_network",
            ),
            format_campaign_config,
        ),
        (
            "03_campaign_daily.csv",
            f"""
                SELECT
                  segments.date,
                  campaign.name,
                  campaign.status,
                  campaign.advertising_channel_type,
                  campaign.bidding_strategy_type,
                  {common_metric_fields},
                  metrics.search_impression_share,
                  metrics.search_budget_lost_impression_share,
                  metrics.search_rank_lost_impression_share,
                  metrics.top_impression_percentage,
                  metrics.absolute_top_impression_percentage
                FROM campaign
                WHERE {date_filter}
                  AND {search_filter}
                ORDER BY segments.date DESC, metrics.cost_micros DESC
            """,
            (
                "date",
                "campaign_name",
                "campaign_status",
                "channel_type",
                "bidding_strategy_type",
                "currency_code",
                "impressions",
                "clicks",
                "ctr_pct",
                "cost_currency",
                "average_cpc_currency",
                "conversions",
                "all_conversions",
                "conversion_rate_pct",
                "cost_per_conversion_currency",
                "search_impression_share_pct",
                "search_budget_lost_impression_share_pct",
                "search_rank_lost_impression_share_pct",
                "top_impression_percentage_pct",
                "absolute_top_impression_percentage_pct",
            ),
            format_campaign_daily,
        ),
        (
            "04_device_network_daily.csv",
            f"""
                SELECT
                  segments.date,
                  segments.device,
                  segments.ad_network_type,
                  campaign.name,
                  {common_metric_fields}
                FROM campaign
                WHERE {date_filter}
                  AND {search_filter}
                ORDER BY segments.date DESC, metrics.cost_micros DESC
            """,
            (
                "date",
                "campaign_name",
                "device",
                "ad_network_type",
                "currency_code",
                "impressions",
                "clicks",
                "ctr_pct",
                "cost_currency",
                "average_cpc_currency",
                "conversions",
                "all_conversions",
                "conversion_rate_pct",
                "cost_per_conversion_currency",
            ),
            format_device_network,
        ),
        (
            "05_search_terms_daily.csv",
            f"""
                SELECT
                  segments.date,
                  campaign.name,
                  ad_group.name,
                  segments.keyword.info.text,
                  segments.keyword.info.match_type,
                  search_term_view.search_term,
                  segments.search_term_match_type,
                  segments.search_term_targeting_status,
                  segments.device,
                  segments.ad_network_type,
                  {common_metric_fields}
                FROM search_term_view
                WHERE {date_filter}
                  AND {search_filter}
                ORDER BY metrics.cost_micros DESC
            """,
            (
                "date",
                "campaign_name",
                "ad_group_name",
                "keyword_text",
                "keyword_match_type",
                "search_term",
                "search_term_match_type",
                "search_term_targeting_status",
                "device",
                "ad_network_type",
                "currency_code",
                "impressions",
                "clicks",
                "ctr_pct",
                "cost_currency",
                "average_cpc_currency",
                "conversions",
                "all_conversions",
                "conversion_rate_pct",
                "cost_per_conversion_currency",
            ),
            format_search_term,
        ),
        (
            "06_keywords_quality_daily.csv",
            f"""
                SELECT
                  segments.date,
                  campaign.name,
                  ad_group.name,
                  ad_group_criterion.keyword.text,
                  ad_group_criterion.keyword.match_type,
                  ad_group_criterion.status,
                  ad_group_criterion.quality_info.quality_score,
                  ad_group_criterion.quality_info.creative_quality_score,
                  ad_group_criterion.quality_info.post_click_quality_score,
                  ad_group_criterion.quality_info.search_predicted_ctr,
                  {common_metric_fields},
                  metrics.search_impression_share,
                  metrics.search_rank_lost_impression_share,
                  metrics.search_exact_match_impression_share
                FROM keyword_view
                WHERE {date_filter}
                  AND {search_filter}
                ORDER BY metrics.cost_micros DESC
            """,
            (
                "date",
                "campaign_name",
                "ad_group_name",
                "keyword_text",
                "keyword_match_type",
                "keyword_status",
                "quality_score_current",
                "ad_relevance_current",
                "landing_page_experience_current",
                "expected_ctr_current",
                "currency_code",
                "impressions",
                "clicks",
                "ctr_pct",
                "cost_currency",
                "average_cpc_currency",
                "conversions",
                "all_conversions",
                "conversion_rate_pct",
                "cost_per_conversion_currency",
                "search_impression_share_pct",
                "search_rank_lost_impression_share_pct",
                "search_exact_match_impression_share_pct",
            ),
            format_keyword,
        ),
        (
            "07_landing_pages_daily.csv",
            f"""
                SELECT
                  segments.date,
                  campaign.name,
                  ad_group.name,
                  expanded_landing_page_view.expanded_final_url,
                  segments.device,
                  {common_metric_fields}
                FROM expanded_landing_page_view
                WHERE {date_filter}
                  AND {search_filter}
                ORDER BY metrics.cost_micros DESC
            """,
            (
                "date",
                "campaign_name",
                "ad_group_name",
                "expanded_final_url",
                "device",
                "currency_code",
                "impressions",
                "clicks",
                "ctr_pct",
                "cost_currency",
                "average_cpc_currency",
                "conversions",
                "all_conversions",
                "conversion_rate_pct",
                "cost_per_conversion_currency",
            ),
            format_landing_page,
        ),
        (
            "08_conversion_actions_daily.csv",
            f"""
                SELECT
                  segments.date,
                  campaign.name,
                  segments.conversion_action_name,
                  segments.conversion_action_category,
                  metrics.conversions,
                  metrics.all_conversions,
                  metrics.conversions_value,
                  metrics.all_conversions_value
                FROM campaign
                WHERE {date_filter}
                  AND {search_filter}
                ORDER BY segments.date DESC, metrics.conversions DESC
            """,
            (
                "date",
                "campaign_name",
                "conversion_action_name",
                "conversion_action_category",
                "conversions",
                "all_conversions",
                "conversions_value",
                "all_conversions_value",
                "currency_code",
            ),
            format_conversion_action,
        ),
        (
            "09_ads_daily.csv",
            f"""
                SELECT
                  segments.date,
                  campaign.name,
                  ad_group.name,
                  ad_group_ad.status,
                  ad_group_ad.ad.type,
                  ad_group_ad.ad_strength,
                  ad_group_ad.ad.final_urls,
                  {common_metric_fields}
                FROM ad_group_ad
                WHERE {date_filter}
                  AND {search_filter}
                ORDER BY metrics.cost_micros DESC
            """,
            (
                "date",
                "campaign_name",
                "ad_group_name",
                "ad_status",
                "ad_type",
                "ad_strength",
                "final_urls",
                "currency_code",
                "impressions",
                "clicks",
                "ctr_pct",
                "cost_currency",
                "average_cpc_currency",
                "conversions",
                "all_conversions",
                "conversion_rate_pct",
                "cost_per_conversion_currency",
            ),
            format_ad,
        ),
    ]


def format_api_error(exc: Exception) -> Dict[str, Any]:
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


def build_window_summary(
    campaign_rows: Sequence[Dict[str, Any]],
    end_date: date,
    requested_days: int,
    currency_code: str,
) -> List[Dict[str, Any]]:
    windows = sorted({7, 30, requested_days})
    summary: List[Dict[str, Any]] = []
    for window in windows:
        start_date = end_date - timedelta(days=window - 1)
        selected = [
            row
            for row in campaign_rows
            if start_date <= date.fromisoformat(str(row["date"])) <= end_date
        ]
        impressions = sum(int(row["impressions"]) for row in selected)
        clicks = sum(int(row["clicks"]) for row in selected)
        cost = sum(float(row["cost_currency"]) for row in selected)
        conversions = sum(float(row["conversions"]) for row in selected)
        all_conversions = sum(float(row["all_conversions"]) for row in selected)
        summary.append(
            {
                "window_days": window,
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
                "currency_code": currency_code,
                "impressions": impressions,
                "clicks": clicks,
                "ctr_pct": round((clicks / impressions * 100) if impressions else 0.0, 6),
                "cost_currency": round(cost, 6),
                "average_cpc_currency": round((cost / clicks) if clicks else 0.0, 6),
                "conversions": round(conversions, 6),
                "all_conversions": round(all_conversions, 6),
                "conversion_rate_pct": round((conversions / clicks * 100) if clicks else 0.0, 6),
                "cost_per_conversion_currency": round(
                    (cost / conversions) if conversions else 0.0, 6
                ),
            }
        )
    return summary


def main() -> int:
    args = parse_args()
    try:
        validate_days(args.days)
        config_path = ensure_external_file(args.config_path)
        output_dir = ensure_external_output_dir(args.output_dir)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    end_date = date.today()
    start_date = end_date - timedelta(days=args.days - 1)
    report_specs = build_report_specs(start_date, end_date)

    if not args.execute:
        print("DRY_RUN: historical diagnosis exporter ready")
        print(f"DATE_RANGE: {start_date.isoformat()} to {end_date.isoformat()}")
        print(f"REPORT_COUNT: {len(report_specs) + 2}")
        print("OUTPUT_POLICY: external directory only; raw outputs are not versioned")
        print("NEXT_STEP: rerun with --execute after review and authorization")
        return 0

    try:
        client = build_client(config_path)
        currency_code, time_zone = fetch_account_context(client, args.customer_id)
    except Exception as exc:
        print(f"ERROR: {format_api_error(exc)}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    account_rows = [
        {
            "currency_code": currency_code,
            "time_zone": time_zone,
            "date_range_start": start_date.isoformat(),
            "date_range_end": end_date.isoformat(),
            "window_days": args.days,
        }
    ]
    write_csv(
        output_dir / "01_account_context.csv",
        ("currency_code", "time_zone", "date_range_start", "date_range_end", "window_days"),
        account_rows,
    )

    manifest: Dict[str, Any] = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "date_range_start": start_date.isoformat(),
        "date_range_end": end_date.isoformat(),
        "window_days": args.days,
        "currency_code": currency_code,
        "time_zone": time_zone,
        "read_only": True,
        "customer_id_included_in_outputs": False,
        "reports": [],
        "errors": [],
    }
    campaign_daily_rows: List[Dict[str, Any]] = []

    for filename, query, fieldnames, formatter in report_specs:
        try:
            rows = [formatter(row, currency_code) for row in search_rows(client, args.customer_id, query)]
            write_csv(output_dir / filename, fieldnames, rows)
            manifest["reports"].append({"file": filename, "rows": len(rows), "status": "ok"})
            if filename == "03_campaign_daily.csv":
                campaign_daily_rows = rows
            print(f"REPORT_READY: {filename} rows={len(rows)}")
        except Exception as exc:
            error = format_api_error(exc)
            error["file"] = filename
            manifest["errors"].append(error)
            manifest["reports"].append({"file": filename, "rows": 0, "status": "error"})
            print(f"REPORT_ERROR: {filename}: {error['message']}")

    window_summary = build_window_summary(
        campaign_rows=campaign_daily_rows,
        end_date=end_date,
        requested_days=args.days,
        currency_code=currency_code,
    )
    summary_fields = (
        "window_days",
        "start_date",
        "end_date",
        "currency_code",
        "impressions",
        "clicks",
        "ctr_pct",
        "cost_currency",
        "average_cpc_currency",
        "conversions",
        "all_conversions",
        "conversion_rate_pct",
        "cost_per_conversion_currency",
    )
    write_csv(output_dir / "10_window_summary.csv", summary_fields, window_summary)
    manifest["reports"].append(
        {"file": "10_window_summary.csv", "rows": len(window_summary), "status": "ok"}
    )

    with (output_dir / "manifest.json").open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)

    print(f"DIAGNOSIS_READY: {output_dir}")
    print(f"REPORTS_OK: {sum(1 for report in manifest['reports'] if report['status'] == 'ok')}")
    print(f"REPORTS_ERROR: {len(manifest['errors'])}")
    return 2 if manifest["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
