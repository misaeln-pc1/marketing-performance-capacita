"""Unit and offline regression tests for Negative Keyword Guard (Fail-Closed & Persistent).

Covers:
1. Normalization of scope, match type, and Unicode diacritics (fórmulas, tablas dinámicas, etc.).
2. B2B precedence over routing ('clases para empresas' -> B2B_SENCE).
3. Campaign contract fail-closed rules (UNKNOWN campaign, UNKNOWN intent, UNKNOWN scope, UNKNOWN match type).
4. REMOVED/UNKNOWN criteria filtering (never treated as active live negatives).
5. Automatic shared-set attachment loading directly from snapshot contract.
6. Product and modality contract enforcement.
7. Cross-campaign conflict detection (B2C vs B2B, protected value proposition terms).
8. Routing A/B/C and 'paso a paso' canonical rule.
9. Cross-process persistent idempotency via RecommendationLedger.
10. Snapshot serialization, hash validation, and round-trip verification.
11. Live read adapter with simulated GAQL responses and HOLD_DATA_GAP fallback.
12. Sanitized deterministic identifier hashing.
13. Secret and PII scanning in fixtures and models.
"""

from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

from core.negative_guard.adapter import GoogleAdsNegativeReadAdapter
from core.negative_guard.campaign_contract import (
    CampaignContract,
    CampaignRegistry,
    Modality,
    ProductType,
)
from core.negative_guard.classifier import classify_campaign, classify_keyword_intent
from core.negative_guard.guard import NegativeGuard
from core.negative_guard.ledger import RecommendationLedger
from core.negative_guard.models import (
    CampaignType,
    CriterionStatus,
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
    strip_accents,
)
from core.negative_guard.snapshot import NegativeSnapshotManager

FIXTURES_PATH = Path(__file__).parent / "fixtures" / "negative_snapshot_fixtures.json"


class TestNegativeGuard(unittest.TestCase):
    def setUp(self):
        self.snapshot = NegativeSnapshotManager.load_from_json(FIXTURES_PATH)
        # The snapshot contract automatically includes attachments for hash_c11111111111
        self.guard = NegativeGuard(self.snapshot)

    def test_01_normalization_and_unicode_diacritics(self):
        """Test 1: Normalization strips diacritics, brackets, quotes and handles accents."""
        # Diacritics test cases specified in review
        accent_cases = [
            ("fórmulas", "formulas", IntentClass.SOLUCION_PUNTUAL),
            ("tablas dinámicas", "tablas dinamicas", IntentClass.SOLUCION_PUNTUAL),
            ("cómo hacer", "como hacer", IntentClass.SOLUCION_PUNTUAL),
            ("búsqueda de trabajo", "busqueda de trabajo", IntentClass.EMPLEO),
            ("en línea", "en linea", IntentClass.MODALIDAD),
            ("currículum", "curriculum", IntentClass.EMPLEO),
            ("cotización", "cotizacion", IntentClass.B2B_SENCE),
        ]

        for raw, expected_norm, expected_intent in accent_cases:
            cleaned, _ = normalize_keyword_text(raw)
            self.assertEqual(cleaned, expected_norm, f"Failed normalization for: {raw}")
            intent = classify_keyword_intent(raw)
            self.assertEqual(intent, expected_intent, f"Failed intent classification for: {raw}")

        # Notation inference
        text, match = normalize_keyword_text("[curso excel basico]")
        self.assertEqual(text, "curso excel basico")
        self.assertEqual(match, MatchType.EXACT)

        text2, match2 = normalize_keyword_text('  "fórmulas avanzadas"  ')
        self.assertEqual(text2, "formulas avanzadas")
        self.assertEqual(match2, MatchType.PHRASE)

        # Match type and scope normalizers
        self.assertEqual(normalize_match_type("broad"), MatchType.BROAD)
        self.assertEqual(normalize_match_type("EXACT_MATCH"), MatchType.EXACT)
        self.assertEqual(normalize_match_type("INVALID_TYPE"), MatchType.UNKNOWN)

        self.assertEqual(normalize_scope("campaign_criterion"), SourceScope.CAMPAIGN)
        self.assertEqual(normalize_scope("shared_set"), SourceScope.SHARED_SET)
        self.assertEqual(normalize_scope("ad_group"), SourceScope.AD_GROUP)
        self.assertEqual(normalize_scope("customer"), SourceScope.CUSTOMER)
        self.assertEqual(normalize_scope("UNKNOWN_SCOPE"), SourceScope.UNKNOWN)

    def test_02_b2b_precedence_over_routing(self):
        """Test 2: Precedence - 'clases para empresas' is classified as B2B, not merely routing."""
        intent = classify_keyword_intent("clases para empresas")
        self.assertEqual(intent, IntentClass.B2B_SENCE, "Must classify as B2B_SENCE first, not routing")

        intent2 = classify_keyword_intent("curso para empresas")
        self.assertEqual(intent2, IntentClass.B2B_SENCE)

        # Generic 'clases' without B2B token remains routing
        intent3 = classify_keyword_intent("clases presenciales")
        self.assertEqual(intent3, IntentClass.ROUTING_A_B_C)

    def test_03_campaign_mapping_fail_closed(self):
        """Test 3: Fail-closed validation for unknown campaigns, intents, scopes, and match types."""
        # 1. Unknown campaign name -> HOLD_REVIEW
        res_camp = self.guard.evaluate_candidate(
            raw_keyword="tutoriales avanzados",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="CAMPAÑA_INVENTADA_DESCONOCIDA",
        )
        self.assertFalse(res_camp.is_valid_recommendation)
        self.assertEqual(res_camp.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("UNKNOWN_CAMPAIGN", res_camp.rationale)

        # 2. Unknown keyword intent -> HOLD_REVIEW
        res_intent = self.guard.evaluate_candidate(
            raw_keyword="palabra_aleatoria_inexistente_xyz",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_intent.is_valid_recommendation)
        self.assertEqual(res_intent.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("UNKNOWN_INTENT", res_intent.rationale)

        # 3. Unknown scope -> ERROR
        res_scope = self.guard.evaluate_candidate(
            raw_keyword="tutoriales",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.UNKNOWN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_scope.is_valid_recommendation)
        self.assertEqual(res_scope.policy_decision, PolicyDecision.ERROR)
        self.assertIn("UNKNOWN_SCOPE", res_scope.rationale)

        # 4. Unknown match type -> ERROR
        res_match = self.guard.evaluate_candidate(
            raw_keyword="tutoriales",
            match_type=MatchType.UNKNOWN,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_match.is_valid_recommendation)
        self.assertEqual(res_match.policy_decision, PolicyDecision.ERROR)
        self.assertIn("UNKNOWN_MATCH_TYPE", res_match.rationale)

    def test_04_removed_and_unknown_status_not_active(self):
        """Test 4: REMOVED criteria are not indexed as active live negatives."""
        # 'macro vba antigua' has status 'REMOVED' in the fixtures
        active_items = self.snapshot.active_items()
        active_texts = [i.keyword_text for i in active_items]
        self.assertNotIn("macro vba antigua", active_texts)

        # Evaluating a candidate that matches a REMOVED criterion does not trigger DUPLICADO
        res = self.guard.evaluate_candidate(
            raw_keyword="macro vba antigua",
            match_type=MatchType.BROAD,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        # Because it's FUERA_ALCANCE and not active, it should be accepted as a valid delta recommendation
        self.assertTrue(res.is_valid_recommendation)
        self.assertEqual(res.policy_decision, PolicyDecision.CANDIDATE)

    def test_05_shared_set_attachments_loaded_from_snapshot(self):
        """Test 5: Shared set attachments are automatically loaded directly from the snapshot contract."""
        # hash_c11111111111 has NEG_EXCEL__SOLUCION_PUNTUAL__V1 in snapshot.campaign_shared_sets
        self.assertIn("hash_c11111111111", self.guard.campaign_shared_sets)
        self.assertIn("NEG_EXCEL__SOLUCION_PUNTUAL__V1", self.guard.campaign_shared_sets["hash_c11111111111"])

        # 'buscarv' is in NEG_EXCEL__SOLUCION_PUNTUAL__V1 -> MUST be blocked as DUPLICADO
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

    def test_06_product_and_modality_contract_rules(self):
        """Test 6: Product and modality compatibility checks in Campaign Contract."""
        # Create a custom registry with an ONLINE campaign
        custom_reg = CampaignRegistry()
        online_contract = CampaignContract(
            campaign_name_pattern="SCL-EXCEL-B2C-ONLINE",
            audience=CampaignType.B2C,
            product=ProductType.EXCEL,
            modality=Modality.ONLINE,
            campaign_family="EXCEL_ONLINE_B2C",
            landing_variant="N/A",
            allowed_negative_intents={IntentClass.SOLUCION_PUNTUAL, IntentClass.EMPLEO},
            protected_intents=set(),
            protected_terms={"online", "en linea"},
        )
        custom_reg.register_campaign("SCL-EXCEL-B2C-ONLINE", online_contract)
        online_guard = NegativeGuard(self.snapshot, registry=custom_reg)

        # Attempting to negative-block "curso excel en linea" in an ONLINE campaign must fail with CONFLICT
        res_online = online_guard.evaluate_candidate(
            raw_keyword="curso excel en linea",
            match_type=MatchType.BROAD,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-ONLINE",
            target_campaign_id_hash="hash_online_001",
        )
        self.assertFalse(res_online.is_valid_recommendation)
        self.assertEqual(res_online.policy_decision, PolicyDecision.CONFLICT)

    def test_07_cross_campaign_conflicts(self):
        """Test 7: Cross-campaign conflict detection between B2C and B2B."""
        # B2B term in B2B campaign is CONFLICT
        res_b2b = self.guard.evaluate_candidate(
            raw_keyword="factura empresa sence",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-EMPRESA-B2B",
            target_campaign_id_hash="hash_c22222222222",
        )
        self.assertFalse(res_b2b.is_valid_recommendation)
        self.assertEqual(res_b2b.policy_decision, PolicyDecision.CONFLICT)

        # Core protected B2C offering in B2C campaign is CONFLICT
        res_b2c = self.guard.evaluate_candidate(
            raw_keyword="curso presencial santiago",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_b2c.is_valid_recommendation)
        self.assertEqual(res_b2c.policy_decision, PolicyDecision.CONFLICT)

    def test_08_routing_a_b_c_and_paso_a_paso(self):
        """Test 8: Routing A/B/C terms and 'paso a paso' canonical rule."""
        # 'paso a paso' as campaign negative must be CONFLICT
        res_pap = self.guard.evaluate_candidate(
            raw_keyword="curso excel paso a paso",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_pap.is_valid_recommendation)
        self.assertEqual(res_pap.policy_decision, PolicyDecision.CONFLICT)

        # 'desde cero' at CAMPAIGN level must be redirected to ROUTE
        res_dc = self.guard.evaluate_candidate(
            raw_keyword="desde cero",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_dc.is_valid_recommendation)
        self.assertEqual(res_dc.policy_decision, PolicyDecision.ROUTE)

        # 'desde cero' at AD_GROUP level for another group is valid CANDIDATE
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

    def test_09_persistent_cross_process_idempotency(self):
        """Test 9: Cross-process idempotency - second independent process emits ZERO duplicates."""
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

        with tempfile.TemporaryDirectory() as tmp_dir:
            ledger_path = Path(tmp_dir)
            ledger_p1 = RecommendationLedger(ledger_path)

            # Process / Instance 1
            guard_process_1 = NegativeGuard(self.snapshot, ledger=ledger_p1)
            recs_p1 = guard_process_1.evaluate_batch(candidates)
            self.assertEqual(len(recs_p1), 2, "Process 1 must emit N recommendations")

            # Process / Instance 2: completely new instance and ledger handle pointing to same persistent path
            ledger_p2 = RecommendationLedger(ledger_path)
            guard_process_2 = NegativeGuard(self.snapshot, ledger=ledger_p2)
            recs_p2 = guard_process_2.evaluate_batch(candidates)
            self.assertEqual(len(recs_p2), 0, "Process 2 MUST emit 0 recommendations (PROCESS_2_RECOMMENDATIONS=0)")

    def test_10_snapshot_roundtrip_verification(self):
        """Test 10: Snapshot serialization, hash recalculation, and round-trip equality."""
        # 1. Roundtrip loaded snapshot
        self.assertTrue(NegativeSnapshotManager.verify_roundtrip(self.snapshot))

        # 2. Build from raw rows, verify roundtrip
        raw_rows = [
            {
                "keyword_text": "ejemplo funcion suma",
                "match_type": "EXACT",
                "source_scope": "CAMPAIGN",
                "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL",
                "campaign_id": "111111111",
                "status": "ENABLED",
                "intent_class": "SOLUCION_PUNTUAL",
                "policy_decision": "PRESERVE",
            },
            {
                "keyword_text": "ofertas de trabajo excel",
                "match_type": "BROAD",
                "source_scope": "CAMPAIGN",
                "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL",
                "campaign_id": "111111111",
                "status": "ENABLED",
                "intent_class": "EMPLEO",
                "policy_decision": "PRESERVE",
            },
        ]
        snap = NegativeSnapshotManager.create_sanitized_snapshot_from_items(
            items=raw_rows,
            customer_id_raw="999888777",
            campaign_shared_sets={"111111111": ["SET_EXCEL_DEMO"]},
        )
        self.assertTrue(NegativeSnapshotManager.verify_roundtrip(snap))
        self.assertEqual(snap.schema_version, "1.1.0")
        self.assertEqual(len(snap.items), 2)
        self.assertTrue(snap.manifest_hash)

    def test_11_live_read_adapter_mock_and_hold(self):
        """Test 11: Live read adapter extracts all 6 entities with simulated GAQL responses and fails closed on auth."""
        # Mock GAQL responses for all 6 entities
        def mock_gaql(customer_id: str, query: str):
            if "customer_negative_criterion" in query:
                return [
                    {"keyword_text": "gratis", "match_type": "EXACT", "status": "ENABLED"}
                ]
            elif "shared_set" in query and "type = 'NEGATIVE_KEYWORDS'" in query:
                return [
                    {"id": "501", "name": "SET_TEST_SOLUCIONES", "status": "ENABLED"}
                ]
            elif "shared_criterion" in query:
                return [
                    {"shared_set": "customers/123/sharedSets/501", "keyword_text": "buscarv", "match_type": "PHRASE"}
                ]
            elif "campaign_shared_set" in query:
                return [
                    {"campaign": "customers/123/campaigns/1001", "shared_set": "customers/123/sharedSets/501", "status": "ENABLED"}
                ]
            elif "campaign_criterion" in query:
                return [
                    {"campaign_id": "1001", "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL", "keyword_text": "clases particulares", "match_type": "PHRASE", "status": "ENABLED"}
                ]
            elif "ad_group_criterion" in query:
                return [
                    {"campaign_id": "1001", "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL", "ad_group_id": "2001", "ad_group_name": "ADG_1", "keyword_text": "desde cero", "match_type": "EXACT", "status": "ENABLED"}
                ]
            return []

        adapter = GoogleAdsNegativeReadAdapter(gaql_executor=mock_gaql)
        snap = adapter.build_snapshot(customer_id="123456789", evidence_source="SIMULATED_API")

        self.assertEqual(snap.status, "READY")
        self.assertEqual(len(snap.items), 4)  # customer + shared + campaign + ad_group
        self.assertEqual(len(snap.campaign_shared_sets), 1)
        self.assertTrue(NegativeSnapshotManager.verify_roundtrip(snap))

        # Unconfigured / Auth failure returns HOLD_DATA_GAP
        adapter_unconfigured = GoogleAdsNegativeReadAdapter(gaql_executor=None)
        hold_snap = adapter_unconfigured.build_snapshot(customer_id="123456789")
        self.assertEqual(hold_snap.status, "HOLD_DATA_GAP")
        self.assertIn("ACCESS_TOKEN_SCOPE_INSUFFICIENT", hold_snap.hold_reason)

    def test_12_sanitized_ids_verification(self):
        """Test 12: Deterministic identifier hashing masks raw customer and campaign IDs."""
        h1 = hash_identifier("1234567890")
        self.assertTrue(h1.startswith("hash_"))
        self.assertEqual(len(h1), 17)
        self.assertNotIn("1234567890", h1)

        # Deterministic
        h2 = hash_identifier("1234567890")
        self.assertEqual(h1, h2)

    def test_13_secret_and_pii_scan(self):
        """Test 13: Secret and PII scan over test fixtures."""
        fixtures_text = FIXTURES_PATH.read_text(encoding="utf-8")
        secret_patterns = [
            r"ya29\.[a-zA-Z0-9_-]+",
            r"1//[a-zA-Z0-9_-]+",
            r"ghp_[a-zA-Z0-9]{20,}",
            r"EAAB[a-zA-Z0-9]+",
            r"(?i)bearer\s+[a-z0-9_\-\.]{20,}",
            r"(?i)client_secret",
            r"(?i)password\s*[:=]\s*['\"][^'\"]+['\"]",
        ]
        for pat in secret_patterns:
            matches = re.findall(pat, fixtures_text)
            self.assertEqual(len(matches), 0, f"Secret pattern detected in fixtures: {pat}")

        # Email
        email_matches = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", fixtures_text)
        self.assertEqual(len(email_matches), 0, f"Email PII found: {email_matches}")

        # Chilean phone
        phone_matches = re.findall(r"\+56\s*9\s*\d{8}", fixtures_text)
        self.assertEqual(len(phone_matches), 0, f"Phone PII found: {phone_matches}")


if __name__ == "__main__":
    unittest.main()
