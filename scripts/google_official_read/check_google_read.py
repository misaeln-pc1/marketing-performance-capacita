from __future__ import annotations

"""Unified health check for the permanent Google Marketing READ path.

Checks:
- Google Ads API: list accessible customers (READ only)
- GA4 Data API: run a tiny report on the selected property (READ only)
- Google Sheets API: read the control-plane header

No credentials, account IDs, property IDs, or secrets belong in this file.
Runtime values are supplied through environment variables and ADC.
"""

import json
import os
import sys
from dataclasses import asdict, dataclass

ADWORDS_SCOPE = "https://www.googleapis.com/auth/adwords"
ANALYTICS_SCOPE = "https://www.googleapis.com/auth/analytics.readonly"
SHEETS_SCOPE = "https://www.googleapis.com/auth/spreadsheets"


@dataclass
class CheckResult:
    component: str
    status: str
    detail: str


def check_google_ads() -> CheckResult:
    try:
        from google.ads.googleads.client import GoogleAdsClient

        config_path = os.environ.get("GOOGLE_ADS_CONFIGURATION_FILE_PATH")
        if not config_path:
            return CheckResult("google_ads", "HOLD_CONFIG", "GOOGLE_ADS_CONFIGURATION_FILE_PATH is not set")
        client = GoogleAdsClient.load_from_storage(path=config_path)
        customer_service = client.get_service("CustomerService")
        resource_names = customer_service.list_accessible_customers().resource_names
        return CheckResult("google_ads", "PASS", f"accessible_customers={len(resource_names)}")
    except Exception as exc:  # fail closed; never print credentials/tokens
        return CheckResult("google_ads", "HOLD", f"{type(exc).__name__}: {str(exc)[:240]}")


def check_ga4() -> CheckResult:
    try:
        import google.auth
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import DateRange, Metric, RunReportRequest

        raw_property = os.environ.get("GA4_PROPERTY_ID", "").strip()
        if not raw_property:
            return CheckResult("ga4", "HOLD_CONFIG", "GA4_PROPERTY_ID is not set")
        property_id = raw_property.split("/", 1)[1] if raw_property.startswith("properties/") else raw_property
        if not property_id.isdigit():
            return CheckResult("ga4", "HOLD_CONFIG", "GA4_PROPERTY_ID is invalid")

        credentials, _ = google.auth.default(scopes=[ANALYTICS_SCOPE])
        client = BetaAnalyticsDataClient(credentials=credentials)
        response = client.run_report(
            RunReportRequest(
                property=f"properties/{property_id}",
                metrics=[Metric(name="sessions")],
                date_ranges=[DateRange(start_date="yesterday", end_date="yesterday")],
                limit=1,
            )
        )
        return CheckResult("ga4", "PASS", f"property_read=ok;rows={len(response.rows)}")
    except Exception as exc:
        return CheckResult("ga4", "HOLD", f"{type(exc).__name__}: {str(exc)[:240]}")


def check_reporting_sheet() -> CheckResult:
    try:
        import google.auth
        from googleapiclient.discovery import build

        spreadsheet_id = os.environ.get("GOOGLE_MARKETING_SPREADSHEET_ID", "").strip()
        if not spreadsheet_id:
            return CheckResult("reporting_sheet", "HOLD_CONFIG", "GOOGLE_MARKETING_SPREADSHEET_ID is not set")
        credentials, _ = google.auth.default(scopes=[SHEETS_SCOPE])
        service = build("sheets", "v4", credentials=credentials, cache_discovery=False)
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range="'Control_Plane_Status'!A1:E1",
        ).execute()
        values = result.get("values", [])
        if not values or values[0][:2] != ["Fuente", "Estado"]:
            return CheckResult("reporting_sheet", "HOLD_SCHEMA", "Control_Plane_Status header mismatch")
        return CheckResult("reporting_sheet", "PASS", "sheet_read=ok")
    except Exception as exc:
        return CheckResult("reporting_sheet", "HOLD", f"{type(exc).__name__}: {str(exc)[:240]}")


def get_results() -> list[CheckResult]:
    return [check_google_ads(), check_ga4(), check_reporting_sheet()]


def main() -> int:
    results = get_results()
    print(json.dumps([asdict(r) for r in results], ensure_ascii=False, indent=2))
    return 0 if all(r.status == "PASS" for r in results) else 2


if __name__ == "__main__":
    sys.exit(main())
