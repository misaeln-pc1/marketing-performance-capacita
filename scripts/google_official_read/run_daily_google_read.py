from __future__ import annotations

"""Daily observable runner for the permanent Google Marketing READ path.

The job never mutates Google Ads or GA4 configuration. It:
1. checks Google Ads, GA4 and the reporting Sheet;
2. refreshes the rolling GA4 paid-Google snapshot when GA4 + Sheet are healthy;
3. writes only health/status rows to `Control_Plane_Status`.
"""

import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import google.auth
from googleapiclient.discovery import build

from check_google_read import SHEETS_SCOPE, get_results
import publish_ga4_to_sheet

SANTIAGO = ZoneInfo("America/Santiago")


def write_status(spreadsheet_id: str, rows: list[list[str]]) -> None:
    credentials, _ = google.auth.default(scopes=[SHEETS_SCOPE])
    service = build("sheets", "v4", credentials=credentials, cache_discovery=False)
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range="'Control_Plane_Status'!A2:E4",
        valueInputOption="RAW",
        body={"values": rows},
    ).execute()


def main() -> int:
    checked_at = datetime.now(SANTIAGO).strftime("%Y-%m-%d %H:%M:%S")
    results = get_results()
    by_component = {result.component: result for result in results}

    ga4_bridge_status = "HOLD"
    ga4_bridge_detail = "not_run"
    if (
        by_component.get("ga4")
        and by_component["ga4"].status == "PASS"
        and by_component.get("reporting_sheet")
        and by_component["reporting_sheet"].status == "PASS"
    ):
        publish_exit = publish_ga4_to_sheet.main()
        ga4_bridge_status = "PASS" if publish_exit == 0 else "HOLD"
        ga4_bridge_detail = "rolling_3d_upsert" if publish_exit == 0 else "publish_failed"

    spreadsheet_id = os.environ.get("GOOGLE_MARKETING_SPREADSHEET_ID", "").strip()
    if spreadsheet_id and by_component.get("reporting_sheet") and by_component["reporting_sheet"].status == "PASS":
        status_rows = [
            [
                "Google Ads API",
                by_component["google_ads"].status,
                checked_at,
                "accessible customers / auth",
                by_component["google_ads"].detail,
            ],
            [
                "GA4 Data API",
                by_component["ga4"].status,
                checked_at,
                "selected property / yesterday",
                by_component["ga4"].detail,
            ],
            [
                "GA4 → Reporting Sheet",
                ga4_bridge_status,
                checked_at,
                "paid Google rolling window",
                ga4_bridge_detail,
            ],
        ]
        write_status(spreadsheet_id, status_rows)

    for result in results:
        print(f"{result.component.upper()}={result.status} {result.detail}")
    print(f"GA4_SHEET_BRIDGE={ga4_bridge_status} {ga4_bridge_detail}")

    return 0 if all(result.status == "PASS" for result in results) and ga4_bridge_status == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
