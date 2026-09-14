from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

MODULE_DIR = Path(__file__).resolve().parents[1] / "scripts" / "google_official_read"
sys.path.insert(0, str(MODULE_DIR))

import publish_ga4_to_sheet as bridge  # noqa: E402


class FakeRow:
    def __init__(self, dimensions, metrics):
        self.dimension_values = [SimpleNamespace(value=str(value)) for value in dimensions]
        self.metric_values = [SimpleNamespace(value=str(value)) for value in metrics]


class FakeResponse:
    def __init__(self, rows):
        self.rows = rows


class GoogleOfficialReadTests(unittest.TestCase):
    def test_date_iso(self):
        self.assertEqual(bridge.date_iso("20260913"), "2026-09-13")

    def test_paid_google_filter(self):
        self.assertTrue(bridge.is_paid_google("google", "cpc"))
        self.assertTrue(bridge.is_paid_google("GOOGLE", "CPC"))
        self.assertFalse(bridge.is_paid_google("google", "organic"))
        self.assertFalse(bridge.is_paid_google("bing", "cpc"))

    def test_campaign_rows_exclude_non_paid(self):
        response = FakeResponse([
            FakeRow(["20260912", "EXCEL-PRE-STGO", "google", "cpc"], [10, 7, 0.7, 8, 3, 1]),
            FakeRow(["20260912", "(organic)", "google", "organic"], [20, 15, 0.75, 18, 4, 0]),
        ])
        rows = bridge.build_campaign_rows(response, "2026-09-13 05:30:00")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], "2026-09-12")
        self.assertEqual(rows[0][1], "EXCEL-PRE-STGO")
        self.assertEqual(rows[0][10], "2026-09-12||EXCEL-PRE-STGO||google||cpc")

    def test_landing_rows_use_path_only(self):
        response = FakeResponse([
            FakeRow(
                ["20260912", "/curso-excel-presencial", "EXCEL-PRE-STGO", "google", "cpc"],
                [9, 6, 0.6667, 7, 2, 1],
            )
        ])
        rows = bridge.build_landing_rows(response, "2026-09-13 05:30:00")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "/curso-excel-presencial")
        self.assertNotIn("?", rows[0][1])
        self.assertEqual(
            rows[0][11],
            "2026-09-12||/curso-excel-presencial||EXCEL-PRE-STGO||google||cpc",
        )

    def test_schema_key_positions_match_sheet_contract(self):
        self.assertEqual(bridge.CAMPAIGN_HEADERS[10], "Key_Unica")
        self.assertEqual(bridge.LANDING_HEADERS[11], "Key_Unica")
        self.assertEqual(len(bridge.CAMPAIGN_HEADERS), 12)
        self.assertEqual(len(bridge.LANDING_HEADERS), 13)


if __name__ == "__main__":
    unittest.main()
