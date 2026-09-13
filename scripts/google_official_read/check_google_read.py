from __future__ import annotations

"""Unified READ-only health check for Google Ads + GA4.

No credentials, account IDs, property IDs, or secrets belong in this file.
Runtime values are supplied through environment variables and Application Default Credentials.
"""

import json
import os
import sys
from dataclasses import asdict, dataclass


ADWORDS_SCOPE = "https://www.googleapis.com/auth/adwords"
ANALYTICS_SCOPE = "https://www.googleapis.com/auth/analytics.readonly"


@dataclass
class CheckResult:
    component: str
    status: str
    detail: str


def check_google_ads() -> CheckResult:
    try:
        import google.auth
        from google.ads.googleads.client import GoogleAdsClient

        credentials, _ = google.auth.default(scopes=[ADWORDS_SCOPE])
        # Refresh is deferred to the client call. The config must remain outside the repo.
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
        from google.analytics.admin import AnalyticsAdminServiceClient

        credentials, _ = google.auth.default(scopes=[ANALYTICS_SCOPE])
        client = AnalyticsAdminServiceClient(credentials=credentials)
        summaries = list(client.list_account_summaries())
        properties = sum(len(list(summary.property_summaries)) for summary in summaries)
        return CheckResult("ga4", "PASS", f"accounts={len(summaries)};properties={properties}")
    except Exception as exc:
        return CheckResult("ga4", "HOLD", f"{type(exc).__name__}: {str(exc)[:240]}")


def main() -> int:
    results = [check_google_ads(), check_ga4()]
    print(json.dumps([asdict(r) for r in results], ensure_ascii=False, indent=2))
    return 0 if all(r.status == "PASS" for r in results) else 2


if __name__ == "__main__":
    sys.exit(main())
