from __future__ import annotations

"""Select a GA4 property accessible to the authenticated user.

Menus go to stderr so stdout contains only the selected numeric property ID,
which lets PowerShell capture it safely during setup.
"""

import sys

import google.auth
from google.analytics.admin import AnalyticsAdminServiceClient

ANALYTICS_SCOPE = "https://www.googleapis.com/auth/analytics.readonly"


def main() -> int:
    credentials, _ = google.auth.default(scopes=[ANALYTICS_SCOPE])
    client = AnalyticsAdminServiceClient(credentials=credentials)
    summaries = list(client.list_account_summaries())

    properties: list[tuple[str, str, str]] = []
    for account in summaries:
        account_name = getattr(account, "display_name", "") or getattr(account, "account", "")
        for prop in account.property_summaries:
            raw_id = str(prop.property).split("/", 1)[-1]
            properties.append((raw_id, str(prop.display_name), str(account_name)))

    if not properties:
        print("GA4_PROPERTIES=0", file=sys.stderr)
        return 2

    if len(properties) == 1:
        print(properties[0][0])
        return 0

    print("Select the GA4 property for Capacita:", file=sys.stderr)
    for index, (_, display_name, account_name) in enumerate(properties, start=1):
        print(f"  {index}. {display_name} ({account_name})", file=sys.stderr)

    while True:
        print("Enter option number: ", end="", file=sys.stderr, flush=True)
        choice = input().strip()
        if choice.isdigit() and 1 <= int(choice) <= len(properties):
            print(properties[int(choice) - 1][0])
            return 0
        print("Invalid option.", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
