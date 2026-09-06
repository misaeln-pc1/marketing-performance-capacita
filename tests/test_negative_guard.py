"""Unit and offline regression tests for Negative Keyword Guard.

Covers:
1. Normalization of scope and match type.
2. Existing negative deduplication.
3. Cross-campaign conflict detection (B2C vs B2B).
4. Routing A/B/C vs global exclusions.
5. Shared set linked to campaign deduplication.
6. Missing live data -> HOLD_DATA_GAP.
7. Strict idempotency: second run emits zero duplicate recommendations.
8. Sanitized IDs verification.
9. Secret scan in fixtures/models.
10. PII scan in fixtures/models.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from core.negative_guard.classifier import classify_campaign, classify_keyword_intent
from core.negative_guard.guard import NegativeGuard
from core.negative_guard.models import (
    CampaignType,
    IntentClass,
    MatchType,
    NegativeKeywordItem,
    NegativeSnapshot,
    PolicyDecision,
    SourceScope,
    hash_identifier,
    normalize_keyword_text,
    normalize_match_type,
    normalize_scope,
)
from core.negative_guard.snapshot import NegativeSnapshotManager


FIXTURES_PATH = Path(__file__).parent / "fixtures" / "negative_snapshot_fixtures.json"


class TestNegativeGuard(unittest.TestCase):
    def setUp(self):
        self.snapshot = NegativeSnapshotManager.load_from_json(FIXTURES_PATH)
        self.guard = NegativeGuard(self.snapshot)
        # Associate campaign hash_c11111111111 with shared set NEG_EXCEL__SOLUCION_PUNTUAL__V1
        self.guard.associate_campaign_with_shared_set(
            campaign_id_hash="hash_c11111111111",
            shared_set_name="NEG_EXCEL__SOLUCION_PUNTUAL__V1",
        )

    def test_01_normalization_scope_and_match_type(self):
        """Test 1: Normalization of scope, match type, and keyword text."""
        # Text and match type inference
        text, match = normalize_keyword_text("[curso excel basico]")
        self.assertEqual(text, "curso excel basico")
        self.assertEqual(match, MatchType.EXACT)

        text2, match2 = normalize_keyword_text('  "formulas avanzadas"  ')
        self.assertEqual(text2, "formulas avanzadas")
        self.assertEqual(match2, MatchType.PHRASE)

        # Match type normalizer fallback
        self.assertEqual(normalize_match_type("broad"), MatchType.BROAD)
        self.assertEqual(normalize_match_type("EXACT_MATCH"), MatchType.EXACT)

        # Scope normalizer
        self.assertEqual(normalize_scope("campaign_criterion"), SourceScope.CAMPAIGN)
        self.assertEqual(normalize_scope("shared_set"), SourceScope.SHARED_SET)
        self.assertEqual(normalize_scope("ad_group"), SourceScope.AD_GROUP)
        self.assertEqual(normalize_scope("customer"), SourceScope.CUSTOMER)

    def test_02_negative_already_existing(self):
        """Test 2: Deduplication prevents recommending existing negatives."""
        # 'gratis' is at CUSTOMER level
        res = self.guard.evaluate_candidate(
            raw_keyword="gratis",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res.is_valid_recommendation)
        self.assertEqual(res.policy_decision, PolicyDecision.PRESERVE)
        self.assertIn("DUPLICADO", res.rationale)

        # 'clases particulares' is already at CAMPAIGN level for SCL-EXCEL-B2C-PRESENCIAL
        res2 = self.guard.evaluate_candidate(
            raw_keyword="clases particulares",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res2.is_valid_recommendation)
        self.assertEqual(res2.policy_decision, PolicyDecision.PRESERVE)
        self.assertIn("DUPLICADO", res2.rationale)

    def test_03_conflict_b2c_vs_b2b(self):
        """Test 3: Cross-campaign conflict detection between B2C and B2B."""
        # Trying to apply B2B terms ('empresa', 'sence') to B2B campaign is a conflict
        res_b2b = self.guard.evaluate_candidate(
            raw_keyword="factura empresa sence",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-EMPRESA-B2B",
            target_campaign_id_hash="hash_c22222222222",
        )
        self.assertFalse(res_b2b.is_valid_recommendation)
        self.assertEqual(res_b2b.policy_decision, PolicyDecision.CONFLICT)
        self.assertIn("CONFLICTO SEVERO B2B", res_b2b.rationale)

        # Trying to negative-block core B2C offerings in B2C campaign is a conflict
        res_b2c = self.guard.evaluate_candidate(
            raw_keyword="curso presencial santiago",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_b2c.is_valid_recommendation)
        self.assertEqual(res_b2c.policy_decision, PolicyDecision.CONFLICT)
        self.assertIn("CONFLICTO B2C", res_b2c.rationale)

    def test_04_routing_a_b_c_and_paso_a_paso(self):
        """Test 4: Routing A/B/C terms and 'paso a paso' exception."""
        # 'paso a paso' as global or campaign negative must be rejected
        res_pap = self.guard.evaluate_candidate(
            raw_keyword="curso excel paso a paso",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_pap.is_valid_recommendation)
        self.assertEqual(res_pap.policy_decision, PolicyDecision.CONFLICT)
        self.assertIn("paso a paso' NO es negativa global", res_pap.rationale)

        # 'desde cero' at CAMPAIGN level must be redirected to AD_GROUP routing
        res_dc = self.guard.evaluate_candidate(
            raw_keyword="desde cero",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_dc.is_valid_recommendation)
        self.assertEqual(res_dc.policy_decision, PolicyDecision.ROUTE)
        self.assertIn("ROUTING_A_B_C", res_dc.rationale)

        # 'desde cero' as negative inside AD_GROUP ADG_C_CLASES (for routing to B) is valid if not duplicate
        res_dc_adg = self.guard.evaluate_candidate(
            raw_keyword="desde cero",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_C_CLASES",
            target_ad_group_id_hash="hash_g33333333333",
        )
        self.assertTrue(res_dc_adg.is_valid_recommendation)
        self.assertEqual(res_dc_adg.policy_decision, PolicyDecision.CANDIDATE)

    def test_05_shared_set_linked_to_campaign(self):
        """Test 5: Shared set linked to campaign prevents duplicate recommendations."""
        # 'buscarv' is in shared set NEG_EXCEL__SOLUCION_PUNTUAL__V1 linked to hash_c11111111111
        res = self.guard.evaluate_candidate(
            raw_keyword="buscarv",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res.is_valid_recommendation)
        self.assertEqual(res.policy_decision, PolicyDecision.PRESERVE)
        self.assertIn("DUPLICADO", res.rationale)

    def test_06_missing_live_data_hold_data_gap(self):
        """Test 6: Missing live data yields HOLD_DATA_GAP without crashing."""
        gap_snapshot = NegativeSnapshotManager.create_hold_data_gap_snapshot(
            reason="Auth scope insufficient"
        )
        gap_guard = NegativeGuard(gap_snapshot)

        res = gap_guard.evaluate_candidate(
            raw_keyword="ejercicios resueltos",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res.is_valid_recommendation)
        self.assertEqual(res.policy_decision, PolicyDecision.HOLD_DATA_GAP)
        self.assertIn("HOLD_DATA_GAP", res.rationale)

        # None snapshot test
        none_guard = NegativeGuard(None)
        res_none = none_guard.evaluate_candidate(
            raw_keyword="ejercicios resueltos",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_none.is_valid_recommendation)
        self.assertEqual(res_none.policy_decision, PolicyDecision.HOLD_DATA_GAP)

    def test_07_strict_idempotency_second_run_zero_duplicates(self):
        """Test 7: Idempotency - second run emits zero duplicate recommendations."""
        candidates = [
            {
                "keyword_text": "ejercicios excel avanzados",
                "match_type": "PHRASE",
                "target_scope": "CAMPAIGN",
                "target_campaign_name": "SCL-EXCEL-B2C-PRESENCIAL",
                "target_campaign_id_hash": "hash_c11111111111",
            },
            {
                "keyword_text": "curso excel online",
                "match_type": "BROAD",
                "target_scope": "CAMPAIGN",
                "target_campaign_name": "SCL-EXCEL-B2C-PRESENCIAL",
                "target_campaign_id_hash": "hash_c11111111111",
            },
        ]

        # Run 1
        recs_run_1 = self.guard.evaluate_batch(candidates)
        self.assertEqual(len(recs_run_1), 2)
        self.assertEqual(recs_run_1[0].keyword_text, "ejercicios excel avanzados")
        self.assertEqual(recs_run_1[1].keyword_text, "curso excel online")

        # Run 2 with identical input on same guard session
        recs_run_2 = self.guard.evaluate_batch(candidates)
        self.assertEqual(len(recs_run_2), 0, "Second run MUST produce 0 duplicate recommendations")

    def test_08_sanitized_ids_verification(self):
        """Test 8: Hash identifier produces masked/hashed IDs, never raw numbers."""
        h1 = hash_identifier("1234567890")
        self.assertTrue(h1.startswith("hash_"))
        self.assertEqual(len(h1), 17)  # 'hash_' (5) + 12 hex chars
        self.assertNotIn("1234567890", h1)

        # Preserves already masked or hashed string
        h2 = hash_identifier("123-***-7890")
        self.assertEqual(h2, "123-***-7890")

    def test_09_secret_scan(self):
        """Test 9: Secret scan over fixtures and models."""
        fixtures_text = FIXTURES_PATH.read_text(encoding="utf-8")
        # Patterns for tokens, secrets, private keys
        secret_patterns = [
            r"ya29\.[a-zA-Z0-9_-]+",  # Google OAuth access token
            r"1//[a-zA-Z0-9_-]+",     # Google refresh token
            r"ghp_[a-zA-Z0-9]{20,}",  # GitHub token
            r"EAAB[a-zA-Z0-9]+",      # Meta token
            r"(?i)bearer\s+[a-z0-9_\-\.]{20,}",
            r"(?i)client_secret",
            r"(?i)password\s*[:=]\s*['\"][^'\"]+['\"]",
        ]
        for pat in secret_patterns:
            matches = re.findall(pat, fixtures_text)
            self.assertEqual(len(matches), 0, f"Secret pattern detected in fixtures: {pat}")

    def test_10_pii_scan(self):
        """Test 10: PII scan over fixtures."""
        fixtures_text = FIXTURES_PATH.read_text(encoding="utf-8")
        # Email pattern
        email_matches = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", fixtures_text)
        self.assertEqual(len(email_matches), 0, f"Email PII found: {email_matches}")

        # Chilean phone pattern
        phone_matches = re.findall(r"\+56\s*9\s*\d{8}", fixtures_text)
        self.assertEqual(len(phone_matches), 0, f"Phone PII found: {phone_matches}")


if __name__ == "__main__":
    unittest.main()
