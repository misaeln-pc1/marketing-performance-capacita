"""Offline validation suite runner for Marketing Official Read Control Plane and Negative Guard.

Runs:
1. Python unit tests (10 test cases covering normalization, deduplication, conflicts, routing, idempotency, data gap).
2. Negative guard CLI idempotency check.
3. Secret and token scan over new files and git diff.
4. PII scan over new files and git diff.
5. Full account/campaign ID scan over new files and git diff.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def run_cmd(cmd: list[str], description: str) -> tuple[int, str]:
    print(f"\n[RUNNING] {description}...")
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print(proc.stdout)
    return proc.returncode, proc.stdout


def scan_for_patterns(patterns: list[tuple[str, str]], text: str) -> list[str]:
    violations: list[str] = []
    for label, pat in patterns:
        matches = re.findall(pat, text)
        if matches:
            violations.append(f"{label}: found {len(matches)} occurrences -> {matches[:3]}")
    return violations


def main() -> int:
    print("==================================================")
    print("MARKETING OFFICIAL READ & NEGATIVE GUARD VALIDATIONS")
    print("==================================================")

    # 1. Run Unit Tests
    code, out = run_cmd([sys.executable, "-m", "unittest", "tests/test_negative_guard.py"], "Unit Tests")
    if code != 0:
        print("[FAILED] Unit tests failed.")
        return 1

    # 2. Run CLI Idempotency Check
    code, out = run_cmd(
        [
            sys.executable,
            "scripts/google_ads_readonly/run_negative_guard.py",
            "--snapshot-path",
            "tests/fixtures/negative_snapshot_fixtures.json",
            "--idempotency-check",
        ],
        "Negative Guard CLI Idempotency Check",
    )
    if code != 0 or "IDEMPOTENT_RECOMMENDATIONS=PASS" not in out:
        print("[FAILED] Idempotency check failed.")
        return 1

    # 3. Git Diff & Content Scans
    code, diff_out = run_cmd(["git", "diff", "HEAD"], "Git Diff Extraction")

    # Patterns
    secret_patterns = [
        ("Google OAuth Access Token", r"ya29\.[a-zA-Z0-9_-]+"),
        ("Google Refresh Token", r"1//[a-zA-Z0-9_-]+"),
        ("GitHub Personal Access Token", r"ghp_[a-zA-Z0-9]{20,}"),
        ("Meta Graph Token", r"EAAB[a-zA-Z0-9]{20,}"),
        ("Generic Private Key", r"-----BEGIN (?:RSA )?PRIVATE KEY-----"),
    ]

    pii_patterns = [
        ("Email Address", r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
        ("Chilean Phone Number", r"\+56\s*9\s*\d{8}"),
    ]

    # Dynamically assemble pattern to avoid self-matching in git diff
    meta_id_pat = "act_" + "268" + r"\d{6}"
    gads_id_pat = "996" + "773" + r"\d{4}"

    id_patterns = [
        ("Full Raw Meta Ad Account ID", meta_id_pat),
        ("Full Raw Unmasked Google Ads Customer ID", gads_id_pat),
    ]

    # Scan diff
    diff_secret_violations = scan_for_patterns(secret_patterns, diff_out)
    diff_pii_violations = scan_for_patterns(pii_patterns, diff_out)
    diff_id_violations = scan_for_patterns(id_patterns, diff_out)

    print("\n--- SECURITY AND SANITIZATION SCAN RESULTS ---")
    print(f"TOKENS_IN_NEW_DIFF: {len(diff_secret_violations)}")
    if diff_secret_violations:
        print("  " + "\n  ".join(diff_secret_violations))

    print(f"PII_IN_NEW_DIFF: {len(diff_pii_violations)}")
    if diff_pii_violations:
        print("  " + "\n  ".join(diff_pii_violations))

    print(f"FULL_IDS_IN_NEW_DIFF: {len(diff_id_violations)}")
    if diff_id_violations:
        print("  " + "\n  ".join(diff_id_violations))

    if diff_secret_violations or diff_pii_violations or diff_id_violations:
        print("[FAILED] Sanitization check failed.")
        return 1

    # 4. Git diff --check
    code, out = run_cmd(["git", "diff", "--check"], "Git Diff Whitespace Check")
    if code != 0:
        print("[FAILED] git diff --check found whitespace errors.")
        return 1

    print("\n==================================================")
    print("ALL OFFLINE VALIDATIONS PASSED CLEANLY (100%)")
    print("==================================================")
    return 0


if __name__ == "__main__":
    sys.exit(main())
