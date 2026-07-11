"""Generate keyword market history for Google Search in read-only mode.

The script calls KeywordPlanIdeaService.GenerateKeywordHistoricalMetrics and
writes only local CSV/JSON outputs. It does not mutate campaigns or account
settings.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
LONG_NUMBER_PATTERN = re.compile(r"(?<!\d)\d{7,}(?!\d)")

DEFAULT_KEYWORDS = (
    "curso excel básico e intermedio",
    "curso excel básico",
    "curso de excel básico",
    "excel básico",
    "excel desde cero",
    "curso excel intermedio",
    "curso de excel intermedio",
    "excel intermedio",
    "curso excel presencial",
    "curso de excel presencial",
    "curso excel presencial santiago",
    "curso excel santiago centro",
    "clases de excel",
    "clases particulares de excel",
    "clases de excel a domicilio",
    "profesor de excel",
    "profesor de excel a domicilio",
    "curso excel online",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Google Search keyword historical market metrics."
    )
    parser.add_argument("--config-path", required=True)
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--language-id", default="1003")
    parser.add_argument("--geo-target-constant", action="append", default=["1023191"])
    parser.add_argument(
        "--keywords-file",
        help="Optional UTF-8 CSV/TXT outside the repo. CSV column: keyword.",
    )
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
        raise ValueError("Input/config path must be outside the repository.")
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    return path


def resolve_external_dir(path_value: str, repo_root: Path | None) -> Path:
    path = Path(path_value).expanduser().resolve()
    if repo_root and (path == repo_root or repo_root in path.parents):
        raise ValueError("Output directory must be outside the repository.")
    return path


def sanitize_text(value: Any) -> str:
    text = "" if value is None else str(value)
    text = EMAIL_PATTERN.sub("[REDACTED_EMAIL]", text)
    text = LONG_NUMBER_PATTERN.sub("[REDACTED_NUMBER]", text)
    return text


def enum_name(value: Any) -> str:
    if value is None:
        return ""
    if hasattr(value, "name"):
        return str(value.name)
    return str(value)


def money_from_micros(value: Any) -> float | str:
    if value in (None, ""):
        return ""
    try:
        return round(float(value) / 1_000_000, 6)
    except (TypeError, ValueError):
        return ""


def write_csv(path: Path, fieldnames: Sequence[str], rows: Sequence[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def load_keywords(path_value: str | None, repo_root: Path | None) -> List[str]:
    if not path_value:
        return list(DEFAULT_KEYWORDS)
    path = resolve_external_file(path_value, repo_root)
    if path.suffix.lower() == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            keywords = [
                str(row.get("keyword", "")).strip()
                for row in reader
                if str(row.get("keyword", "")).strip()
            ]
    else:
        keywords = [
            line.strip()
            for line in path.read_text(encoding="utf-8-sig").splitlines()
            if line.strip()
        ]
    if not keywords:
        raise ValueError("Keywords file is empty.")
    return list(dict.fromkeys(keywords))


def build_client(config_path: Path):
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError as exc:
        raise RuntimeError("Missing dependency: pip install google-ads") from exc
    return GoogleAdsClient.load_from_storage(path=str(config_path))


def search_rows(client: Any, customer_id: str, query: str) -> Iterable[Any]:
    service = client.get_service("GoogleAdsService")
    stream = service.search_stream(customer_id=customer_id, query=query)
    for batch in stream:
        yield from batch.results


def fetch_currency(client: Any, customer_id: str) -> str:
    row = next(
        iter(
            search_rows(
                client,
                customer_id,
                "SELECT customer.currency_code FROM customer LIMIT 1",
            )
        ),
        None,
    )
    return str(row.customer.currency_code) if row is not None else ""


def generate_metrics(
    client: Any,
    customer_id: str,
    language_id: str,
    geo_ids: Sequence[str],
    keywords: Sequence[str],
):
    googleads_service = client.get_service("GoogleAdsService")
    geo_service = client.get_service("GeoTargetConstantService")
    idea_service = client.get_service("KeywordPlanIdeaService")
    request = client.get_type("GenerateKeywordHistoricalMetricsRequest")
    request.customer_id = customer_id
    request.keywords.extend(keywords)
    request.language = googleads_service.language_constant_path(language_id)
    request.geo_target_constants.extend(
        geo_service.geo_target_constant_path(geo_id) for geo_id in geo_ids
    )
    request.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
    return idea_service.generate_keyword_historical_metrics(request=request)


def main() -> int:
    args = parse_args()
    repo_root = detect_repo_root(Path(__file__).resolve())
    try:
        config_path = resolve_external_file(args.config_path, repo_root)
        output_dir = resolve_external_dir(args.output_dir, repo_root)
        keywords = load_keywords(args.keywords_file, repo_root)
        if not args.geo_target_constant:
            raise ValueError("At least one --geo-target-constant is required.")
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    if not args.execute:
        print("DRY_RUN: keyword market history V02 ready")
        print(f"KEYWORD_COUNT: {len(keywords)}")
        print(f"LANGUAGE_ID: {args.language_id}")
        print(f"GEO_TARGET_COUNT: {len(args.geo_target_constant)}")
        print("OUTPUT_POLICY: external directory only")
        return 0

    try:
        client = build_client(config_path)
        currency_code = fetch_currency(client, args.customer_id)
        response = generate_metrics(
            client,
            args.customer_id,
            args.language_id,
            args.geo_target_constant,
            keywords,
        )
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {exc}")
        return 1

    output_dir.mkdir(parents=True, exist_ok=True)
    summary_rows: List[Dict[str, Any]] = []
    monthly_rows: List[Dict[str, Any]] = []

    for result in response.results:
        metrics = result.keyword_metrics
        keyword = sanitize_text(result.text)
        close_variants = " | ".join(sanitize_text(v) for v in result.close_variants)
        summary_rows.append(
            {
                "keyword": keyword,
                "close_variants": close_variants,
                "currency_code": currency_code,
                "avg_monthly_searches": getattr(metrics, "avg_monthly_searches", ""),
                "competition": enum_name(getattr(metrics, "competition", "")),
                "competition_index_0_100": getattr(metrics, "competition_index", ""),
                "low_top_of_page_bid_currency": money_from_micros(
                    getattr(metrics, "low_top_of_page_bid_micros", "")
                ),
                "high_top_of_page_bid_currency": money_from_micros(
                    getattr(metrics, "high_top_of_page_bid_micros", "")
                ),
            }
        )
        for volume in metrics.monthly_search_volumes:
            monthly_rows.append(
                {
                    "keyword": keyword,
                    "year": int(volume.year),
                    "month": enum_name(volume.month),
                    "monthly_searches": int(volume.monthly_searches),
                }
            )

    write_csv(
        output_dir / "15_keyword_market_summary.csv",
        (
            "keyword", "close_variants", "currency_code",
            "avg_monthly_searches", "competition", "competition_index_0_100",
            "low_top_of_page_bid_currency", "high_top_of_page_bid_currency",
        ),
        summary_rows,
    )
    write_csv(
        output_dir / "16_keyword_monthly_volume.csv",
        ("keyword", "year", "month", "monthly_searches"),
        monthly_rows,
    )

    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "read_only": True,
        "customer_id_included_in_outputs": False,
        "currency_code": currency_code,
        "language_id": args.language_id,
        "geo_target_constant_count": len(args.geo_target_constant),
        "keyword_count_requested": len(keywords),
        "keyword_count_returned": len(summary_rows),
        "monthly_rows": len(monthly_rows),
    }
    with (output_dir / "manifest_keyword_market_v02.json").open(
        "w", encoding="utf-8"
    ) as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)

    print(f"MARKET_HISTORY_READY: {output_dir}")
    print(f"KEYWORDS_RETURNED: {len(summary_rows)}")
    print(f"MONTHLY_ROWS: {len(monthly_rows)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
