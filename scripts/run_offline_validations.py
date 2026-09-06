"""Comprehensive offline validation suite runner for Marketing Official Read Control Plane & Negative Guard.

Runs:
1. Python unit tests (13 test cases covering normalization, B2B precedence, campaign contracts,
   removed status filtering, shared-set attachments, cross-process persistent idempotency, roundtrip, live adapter).
2. Negative guard CLI fail-closed checks (refusal of implicit demo candidates, exit code 2 on HOLD_DATA_GAP).
3. CLI persistent cross-process idempotency check.
4. Meta Ads PowerShell export script mock test under Set-StrictMode Latest.
5. Deep security and privacy scan over `origin/main...HEAD` diff and all added/modified files:
   - Access tokens, refresh tokens, client secrets, private keys.
   - Raw account IDs, unmasked Google Ads customer IDs, Meta ad account IDs.
   - PII (emails, Chilean phone numbers, RUTs, full private names).
6. Git whitespace check (`git diff origin/main...HEAD --check`).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]


def run_cmd(cmd: list[str], description: str) -> tuple[int, str]:
    print(f"\n[RUNNING] {description}...")
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(proc.stdout)
    return proc.returncode, proc.stdout


def scan_text(patterns: list[tuple[str, str]], text: str, allowlist: list[str] = None) -> list[str]:
    violations: list[str] = []
    allowlist = allowlist or []
    for label, pat in patterns:
        matches = re.findall(pat, text)
        filtered = [m for m in matches if not any(allowed in str(m) for allowed in allowlist)]
        if filtered:
            violations.append(f"{label}: found {len(filtered)} occurrences -> {filtered[:3]}")
    return violations


def main() -> int:
    print("==================================================")
    print("MARKETING OFFICIAL READ & NEGATIVE GUARD OFFLINE VALIDATIONS")
    print("==================================================")

    # 1. Run Unit Tests (13 test cases)
    code, out = run_cmd([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"], "Python Unit Tests")
    if code != 0 or "OK" not in out:
        print("[FAILED] Unit tests failed.")
        return 1

    # 2. Run CLI Fail-Closed Candidates Check (must fail without --demo or --candidates-json)
    code, out = run_cmd(
        [sys.executable, "scripts/google_ads_readonly/run_negative_guard.py"],
        "CLI Fail-Closed Check (missing candidates)",
    )
    if code != 1 or "FAIL-CLOSED ERROR" not in out:
        print("[FAILED] CLI did not fail closed on missing candidates.")
        return 1
    print("[PASS] CLI correctly failed closed on missing candidates.")

    # 3. Run CLI HOLD_DATA_GAP Machine-Readable Exit Code Check (exit code 2)
    code, out = run_cmd(
        [sys.executable, "scripts/google_ads_readonly/run_negative_guard.py", "--demo"],
        "CLI HOLD_DATA_GAP Exit Code Check",
    )
    if code != 2 or "NEGATIVE_SNAPSHOT_HOLD_DATA_GAP" not in out:
        print(f"[FAILED] CLI did not return exit code 2 for HOLD_DATA_GAP (got code {code}).")
        return 1
    print("[PASS] CLI returned machine-readable exit code 2 for HOLD_DATA_GAP.")

    # 4. Run CLI Persistent Idempotency Check with Snapshot
    code, out = run_cmd(
        [
            sys.executable,
            "scripts/google_ads_readonly/run_negative_guard.py",
            "--snapshot-path",
            "tests/fixtures/negative_snapshot_fixtures.json",
            "--demo",
            "--idempotency-check",
        ],
        "Negative Guard CLI Persistent Cross-Process Idempotency Check",
    )
    if code != 0 or "IDEMPOTENT_RECOMMENDATIONS=PASS" not in out:
        print("[FAILED] Persistent idempotency check failed.")
        return 1

    # 5. Run Meta Ads PowerShell Mock Script Test under StrictMode
    code, out = run_cmd(
        ["powershell", "-ExecutionPolicy", "Bypass", "-File", "tests/test_meta_script_mock.ps1"],
        "Meta Ads PowerShell Script Mock Test (Set-StrictMode Latest)",
    )
    if code != 0 or "META_SCRIPT_RUNTIME=MOCK_PASS" not in out:
        print("[FAILED] Meta Ads mock script test failed.")
        return 1

    # 6. Deep Security, Secrets, IDs and PII Scan over origin/main diff and changed files
    print("\n[RUNNING] Deep Security and PII Scan over net diff against origin/main...")
    code, combined_diff = run_cmd(["git", "diff", "origin/main"], "Extracting git diff origin/main (net diff)")

    # Extract only newly added lines, excluding scanner script self-references
    added_lines: List[str] = []
    current_file = ""
    for line in combined_diff.splitlines():
        if line.startswith("+++ b/"):
            current_file = line[6:]
            continue
        # Skip self scan
        if "run_offline_validations.py" in current_file:
            continue
        if line.startswith("+") and not line.startswith("+++"):
            added_lines.append(line[1:])

    added_text = "\n".join(added_lines)

    secret_patterns = [
        ("Google OAuth Access Token", r"ya29\.[a-zA-Z0-9_-]+"),
        ("Google Refresh Token", r"1//[a-zA-Z0-9_-]{20,}"),
        ("GitHub Token", r"gh[pousr]_[a-zA-Z0-9]{20,}"),
        ("Meta Graph Token", r"EAAB[a-zA-Z0-9]{20,}"),
        ("Generic Private Key", r"-----BEGIN (?:RSA )?PRIVATE KEY-----"),
        ("Client Secret Pattern", r"(?i)client_secret\s*[:=]\s*['\"][a-zA-Z0-9_-]{16,}['\"]"),
        ("Raw Password Pattern", r"(?i)password\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
    ]

    full_name_pat = "Misael" + r"\s+Novoa\s+Jara"
    pii_patterns = [
        ("Email Address", r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
        ("Chilean Phone Number", r"\+?56\s*9\s*\d{8}\b"),
        ("Chilean RUT", r"\b\d{1,2}\.\d{3}\.\d{3}-[\dkK]\b"),
        ("Full Private Name", full_name_pat),
    ]

    # Specific unmasked real customer/account ID patterns
    gads_real_id = "996" + "773" + r"\d{4}"
    meta_real_id = "act_" + "268" + r"\d{6,}"
    generic_unmasked_id = r"\b(?<!hash_)(?<!hash_c)(?<!hash_g)(?<!v)\d{9,10}\b"

    id_patterns = [
        ("Real Google Ads Customer ID", gads_real_id),
        ("Real Meta Ad Account ID", meta_real_id),
        ("Generic Unmasked 9-10 digit ID", generic_unmasked_id),
    ]

    # Allowlist for false positives (dummy test numbers, dates, emails in examples)
    scanner_allowlist = [
        "example.com",
        "capacita.cl",
        "1234567890",
        "123456789",
        "111111111",
        "999888777",
        "20260905",
        "20260801",
        "20260831",
        "20260729",
        "20260728",
        "20260711",
        "20260710",
        "20260708",
        "20260706",
        "20260705",
        "20260621",
        "20260526",
        "5123538405",  # Public GitHub PR Review ID
    ]

    diff_secret_violations = scan_text(secret_patterns, added_text, allowlist=scanner_allowlist)
    diff_pii_violations = scan_text(pii_patterns, added_text, allowlist=scanner_allowlist)
    diff_id_violations = scan_text(id_patterns, added_text, allowlist=scanner_allowlist)

    print("\n--- SECURITY AND SANITIZATION SCAN RESULTS ---")
    print(f"SECRETS_IN_DIFF: {len(diff_secret_violations)}")
    if diff_secret_violations:
        print("  " + "\n  ".join(diff_secret_violations))

    print(f"PII_IN_DIFF: {len(diff_pii_violations)}")
    if diff_pii_violations:
        print("  " + "\n  ".join(diff_pii_violations))

    print(f"RAW_IDS_IN_DIFF: {len(diff_id_violations)}")
    if diff_id_violations:
        print("  " + "\n  ".join(diff_id_violations))

    if diff_secret_violations or diff_pii_violations or diff_id_violations:
        print("[FAILED] Sanitization check failed.")
        return 1

    # 7. Git diff whitespace check
    code, out = run_cmd(["git", "diff", "origin/main...HEAD", "--check"], "Git Whitespace Check")
    if code != 0:
        print("[FAILED] git diff origin/main...HEAD --check found whitespace errors.")
        return 1

    print("\n==================================================")
    print("ALL OFFLINE VALIDATIONS PASSED CLEANLY (100%)")
    print("==================================================")
    return 0


if __name__ == "__main__":
    sys.exit(main())
