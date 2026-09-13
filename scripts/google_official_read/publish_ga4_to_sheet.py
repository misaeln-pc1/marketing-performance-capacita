from __future__ import annotations

"""Publish a rolling GA4 paid-Google snapshot to the existing Marketing Sheet.

Official APIs only:
- Google Analytics Data API (READ)
- Google Sheets API (writes only to the reporting sink selected by env var)

No Ads mutations, no GA4 configuration writes, no query strings, no PII.
The script is idempotent by Key_Unica and refreshes a small rolling window so
late-arriving GA4 data can be corrected without duplicate rows.
"""

import os
import sys
from datetime import datetime
from typing import Iterable, Sequence
from zoneinfo import ZoneInfo

import google.auth
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
from googleapiclient.discovery import build

ANALYTICS_SCOPE = "https://www.googleapis.com/auth/analytics.readonly"
SHEETS_SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SANTIAGO = ZoneInfo("America/Santiago")

CAMPAIGN_SHEET = "Log_Diario_GA4_Campaigns"
LANDING_SHEET = "Log_Diario_GA4_Landing_Pages"

CAMPAIGN_HEADERS = [
    "Fecha",
    "Campaña",
    "Fuente",
    "Medio",
    "Sesiones",
    "Sesiones_Con_Interaccion",
    "Tasa_Interaccion",
    "Usuarios",
    "Usuarios_Nuevos",
    "Eventos_Clave",
    "Key_Unica",
    "Fecha_Carga",
]
LANDING_HEADERS = [
    "Fecha",
    "Landing_Page",
    "Campaña",
    "Fuente",
    "Medio",
    "Sesiones",
    "Sesiones_Con_Interaccion",
    "Tasa_Interaccion",
    "Usuarios",
    "Usuarios_Nuevos",
    "Eventos_Clave",
    "Key_Unica",
    "Fecha_Carga",
]


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"MISSING_ENV:{name}")
    return value


def normalize_property_id(raw: str) -> str:
    value = raw.strip()
    if value.startswith("properties/"):
        value = value.split("/", 1)[1]
    if not value.isdigit():
        raise RuntimeError("INVALID_GA4_PROPERTY_ID")
    return value


def metric(row, index: int) -> float:
    raw = row.metric_values[index].value or "0"
    try:
        return float(raw)
    except ValueError:
        return 0.0


def date_iso(raw: str) -> str:
    if len(raw) == 8 and raw.isdigit():
        return f"{raw[0:4]}-{raw[4:6]}-{raw[6:8]}"
    return raw


def campaign_name(google_ads_name: str, generic_name: str) -> str:
    google_ads_name = (google_ads_name or "").strip()
    if google_ads_name and google_ads_name != "(not set)":
        return google_ads_name
    return (generic_name or "").strip()


def is_paid_google(google_ads_name: str, source: str, medium: str) -> bool:
    if (google_ads_name or "").strip() not in {"", "(not set)"}:
        return True
    return (source or "").strip().lower() == "google" and (medium or "").strip().lower() == "cpc"


def run_report(client: BetaAnalyticsDataClient, property_id: str, dimensions: Sequence[str], lookback_days: int):
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name=name) for name in dimensions],
        metrics=[
            Metric(name="sessions"),
            Metric(name="engagedSessions"),
            Metric(name="engagementRate"),
            Metric(name="totalUsers"),
            Metric(name="newUsers"),
            Metric(name="keyEvents"),
        ],
        date_ranges=[DateRange(start_date=f"{lookback_days}daysAgo", end_date="yesterday")],
        limit=100000,
    )
    return client.run_report(request)


def build_campaign_rows(response, loaded_at: str) -> list[list[object]]:
    output: list[list[object]] = []
    for row in response.rows:
        date = date_iso(row.dimension_values[0].value)
        ads_campaign = row.dimension_values[1].value
        generic_campaign = row.dimension_values[2].value
        source = row.dimension_values[3].value
        medium = row.dimension_values[4].value
        if not is_paid_google(ads_campaign, source, medium):
            continue
        campaign = campaign_name(ads_campaign, generic_campaign)
        key = f"{date}||{campaign}||{source}||{medium}"
        output.append([
            date,
            campaign,
            source,
            medium,
            int(metric(row, 0)),
            int(metric(row, 1)),
            metric(row, 2),
            int(metric(row, 3)),
            int(metric(row, 4)),
            metric(row, 5),
            key,
            loaded_at,
        ])
    return output


def build_landing_rows(response, loaded_at: str) -> list[list[object]]:
    output: list[list[object]] = []
    for row in response.rows:
        date = date_iso(row.dimension_values[0].value)
        landing = row.dimension_values[1].value  # `landingPage`: deliberately excludes query string.
        ads_campaign = row.dimension_values[2].value
        generic_campaign = row.dimension_values[3].value
        source = row.dimension_values[4].value
        medium = row.dimension_values[5].value
        if not is_paid_google(ads_campaign, source, medium):
            continue
        campaign = campaign_name(ads_campaign, generic_campaign)
        key = f"{date}||{landing}||{campaign}||{source}||{medium}"
        output.append([
            date,
            landing,
            campaign,
            source,
            medium,
            int(metric(row, 0)),
            int(metric(row, 1)),
            metric(row, 2),
            int(metric(row, 3)),
            int(metric(row, 4)),
            metric(row, 5),
            key,
            loaded_at,
        ])
    return output


def chunks(items: Sequence[dict], size: int = 400) -> Iterable[Sequence[dict]]:
    for start in range(0, len(items), size):
        yield items[start : start + size]


def assert_headers(service, spreadsheet_id: str, sheet: str, expected: Sequence[str]) -> None:
    end_col = chr(ord("A") + len(expected) - 1)
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"'{sheet}'!A1:{end_col}1",
    ).execute()
    actual = (result.get("values") or [[]])[0]
    if actual != list(expected):
        raise RuntimeError(f"HEADER_MISMATCH:{sheet}")


def upsert_rows(service, spreadsheet_id: str, sheet: str, rows: Sequence[Sequence[object]], key_index: int) -> tuple[int, int]:
    if not rows:
        return 0, 0

    existing = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"'{sheet}'!A2:Z",
    ).execute().get("values", [])

    key_to_row: dict[str, int] = {}
    for offset, row in enumerate(existing, start=2):
        if len(row) > key_index and str(row[key_index]).strip():
            key_to_row[str(row[key_index]).strip()] = offset

    updates: list[dict] = []
    new_rows: list[list[object]] = []
    end_col = chr(ord("A") + len(rows[0]) - 1)
    for row in rows:
        key = str(row[key_index])
        target_row = key_to_row.get(key)
        if target_row:
            updates.append({"range": f"'{sheet}'!A{target_row}:{end_col}{target_row}", "values": [list(row)]})
        else:
            new_rows.append(list(row))

    for batch in chunks(updates):
        service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={"valueInputOption": "RAW", "data": list(batch)},
        ).execute()

    if new_rows:
        service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=f"'{sheet}'!A:{end_col}",
            valueInputOption="RAW",
            insertDataOption="INSERT_ROWS",
            body={"values": new_rows},
        ).execute()

    return len(updates), len(new_rows)


def main() -> int:
    try:
        property_id = normalize_property_id(required_env("GA4_PROPERTY_ID"))
        spreadsheet_id = required_env("GOOGLE_MARKETING_SPREADSHEET_ID")
        lookback_days = int(os.getenv("GA4_REFRESH_LOOKBACK_DAYS", "3"))
        if lookback_days < 1 or lookback_days > 30:
            raise RuntimeError("GA4_REFRESH_LOOKBACK_DAYS_OUT_OF_RANGE")

        credentials, _ = google.auth.default(scopes=[ANALYTICS_SCOPE, SHEETS_SCOPE])
        analytics = BetaAnalyticsDataClient(credentials=credentials)
        sheets = build("sheets", "v4", credentials=credentials, cache_discovery=False)
        loaded_at = datetime.now(SANTIAGO).strftime("%Y-%m-%d %H:%M:%S")

        assert_headers(sheets, spreadsheet_id, CAMPAIGN_SHEET, CAMPAIGN_HEADERS)
        assert_headers(sheets, spreadsheet_id, LANDING_SHEET, LANDING_HEADERS)

        campaign_response = run_report(
            analytics,
            property_id,
            ["date", "sessionGoogleAdsCampaignName", "sessionCampaignName", "sessionSource", "sessionMedium"],
            lookback_days,
        )
        landing_response = run_report(
            analytics,
            property_id,
            ["date", "landingPage", "sessionGoogleAdsCampaignName", "sessionCampaignName", "sessionSource", "sessionMedium"],
            lookback_days,
        )

        campaign_rows = build_campaign_rows(campaign_response, loaded_at)
        landing_rows = build_landing_rows(landing_response, loaded_at)

        campaign_updated, campaign_added = upsert_rows(
            sheets, spreadsheet_id, CAMPAIGN_SHEET, campaign_rows, key_index=10
        )
        landing_updated, landing_added = upsert_rows(
            sheets, spreadsheet_id, LANDING_SHEET, landing_rows, key_index=11
        )

        print("GA4_TO_SHEET=PASS")
        print(f"GA4_CAMPAIGN_ROWS={len(campaign_rows)} UPDATED={campaign_updated} ADDED={campaign_added}")
        print(f"GA4_LANDING_ROWS={len(landing_rows)} UPDATED={landing_updated} ADDED={landing_added}")
        print("PII_QUERY_STRING_CAPTURED=0")
        return 0
    except Exception as exc:
        print("GA4_TO_SHEET=HOLD", file=sys.stderr)
        print(f"{type(exc).__name__}: {str(exc)[:300]}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
