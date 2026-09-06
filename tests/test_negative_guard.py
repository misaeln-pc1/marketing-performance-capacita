"""Comprehensive unit and offline regression tests for Negative Keyword Guard (DoD Validation).

Covers:
1. Normalization of scope, match type, and Unicode diacritics (fórmulas, tablas dinámicas, etc.).
2. B2B precedence over routing ('clases para empresas' -> B2B_SENCE).
3. Campaign mapping fail-closed (primary campaign_id_hash, secondary name check, unregistered ID, multiple matches).
4. REMOVED and UNKNOWN status criteria & removed shared set filtering (never treated as active).
5. Automatic shared-set attachment loading directly from snapshot contract.
6. Product and modality contract enforcement (Excel vs Power BI, online/mixta modality).
7. Match-aware and scope-aware protected terms validation (presencial, gratis, empleo, empresas).
8. Explicit routing matrix A/B/C and 'paso a paso' canonical rules.
9. Cross-process persistent idempotency via RecommendationLedger.
10. Snapshot serialization, round-trip verification, and state_hash tamper detection.
11. Live read adapter with official GAQL query templates, type filtering, and account-level shared set flow.
12. Sanitized identifier HMAC pseudonymization and sentinel preservation.
13. Secret and PII scanning in fixtures and models.
14. Ledger corruption fail-closed (LEDGER_CORRUPT=HOLD).
15. Two real CLI subprocesses persistent idempotency (Run 1 > 0, Run 2 == 0).
16. Inter-process ledger concurrency locking.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path

from core.negative_guard.adapter import (
    GAQL_AD_GROUP_NEGATIVES,
    GAQL_CAMPAIGN_NEGATIVES,
    GAQL_CAMPAIGN_SHARED_SETS,
    GAQL_CUSTOMER_NEGATIVES,
    GAQL_SHARED_CRITERIA,
    GAQL_SHARED_SETS,
    GoogleAdsNegativeReadAdapter,
)
from core.negative_guard.campaign_contract import (
    CampaignContract,
    CampaignRegistry,
    Modality,
    ProductType,
    validate_ad_group_routing,
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

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_PATH = Path(__file__).parent / "fixtures" / "negative_snapshot_fixtures.json"


class TestNegativeGuard(unittest.TestCase):
    def setUp(self):
        self.snapshot = NegativeSnapshotManager.load_from_json(FIXTURES_PATH)
        self.guard = NegativeGuard(self.snapshot)

    def test_01_normalization_and_unicode_diacritics(self):
        """Test 1: Normalization strips diacritics, brackets, quotes and handles accents."""
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
        """Test 3: Primary campaign_id_hash mapping and strict fail-closed validation."""
        # 1. Unknown / unregistered campaign ID hash -> HOLD_REVIEW
        res_unregistered = self.guard.evaluate_candidate(
            raw_keyword="tutoriales avanzados",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_unregistered_999",
        )
        self.assertFalse(res_unregistered.is_valid_recommendation)
        self.assertEqual(res_unregistered.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("UNKNOWN_CAMPAIGN", res_unregistered.rationale)

        # 2. Incompatible campaign name -> HOLD_REVIEW
        res_incompatible_name = self.guard.evaluate_candidate(
            raw_keyword="tutoriales avanzados",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="CAMPAÑA_INVENTADA_COMPLETAMENTE_DISTINTA",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_incompatible_name.is_valid_recommendation)
        self.assertEqual(res_incompatible_name.policy_decision, PolicyDecision.HOLD_REVIEW)

        # 3. Ambiguous mapping (multiple matches) -> fail closed
        c1 = CampaignContract(
            campaign_id_hash="hash_dup_123",
            campaign_name_pattern="DUP-CAMP-1",
            audience=CampaignType.B2C,
            product=ProductType.EXCEL,
            modality=Modality.PRESENCIAL,
            campaign_family="DUP",
            landing_variant="A",
        )
        c2 = CampaignContract(
            campaign_id_hash="hash_dup_123",
            campaign_name_pattern="DUP-CAMP-2",
            audience=CampaignType.B2C,
            product=ProductType.EXCEL,
            modality=Modality.PRESENCIAL,
            campaign_family="DUP",
            landing_variant="B",
        )
        reg_dup = CampaignRegistry(contracts=[c1, c2])
        self.assertIsNone(reg_dup.resolve("hash_dup_123", "DUP-CAMP-1"), "Multiple matches must fail closed")

        # 4. Unknown keyword intent -> HOLD_REVIEW
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

        # 5. Unknown scope -> ERROR
        res_scope = self.guard.evaluate_candidate(
            raw_keyword="tutoriales",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.UNKNOWN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_scope.is_valid_recommendation)
        self.assertEqual(res_scope.policy_decision, PolicyDecision.ERROR)

        # 6. Unknown match type -> ERROR
        res_match = self.guard.evaluate_candidate(
            raw_keyword="tutoriales",
            match_type=MatchType.UNKNOWN,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_match.is_valid_recommendation)
        self.assertEqual(res_match.policy_decision, PolicyDecision.ERROR)

    def test_04_removed_and_unknown_status_not_active(self):
        """Test 4: REMOVED criteria are not indexed as active live negatives."""
        active_items = self.snapshot.active_items()
        active_texts = [i.keyword_text for i in active_items]
        self.assertNotIn("macro vba antigua", active_texts)

        res = self.guard.evaluate_candidate(
            raw_keyword="macro vba antigua",
            match_type=MatchType.BROAD,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertTrue(res.is_valid_recommendation)
        self.assertEqual(res.policy_decision, PolicyDecision.CANDIDATE)

    def test_05_shared_set_attachments_loaded_from_snapshot(self):
        """Test 5: Shared set attachments are automatically loaded directly from the snapshot contract."""
        self.assertIn("hash_c11111111111", self.guard.campaign_shared_sets)
        self.assertIn("NEG_EXCEL__SOLUCION_PUNTUAL__V1", self.guard.campaign_shared_sets["hash_c11111111111"])

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
        """Test 6: Product and modality contract rules (Power BI, online/mixta, unknown product)."""
        # 1. Modality rule: online cannot be negated in ONLINE campaign
        custom_reg = CampaignRegistry()
        online_contract = CampaignContract(
            campaign_id_hash="hash_online_001",
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
        custom_reg.register_contract(online_contract)
        online_guard = NegativeGuard(self.snapshot, registry=custom_reg)

        res_online = online_guard.evaluate_candidate(
            raw_keyword="curso excel en linea",
            match_type=MatchType.BROAD,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-ONLINE",
            target_campaign_id_hash="hash_online_001",
        )
        self.assertFalse(res_online.is_valid_recommendation)
        self.assertEqual(res_online.policy_decision, PolicyDecision.CONFLICT)

        # 2. Product rule: Power BI cannot be FUERA_ALCANCE in a Power BI campaign
        pbi_contract = CampaignContract(
            campaign_id_hash="hash_pbi_001",
            campaign_name_pattern="SCL-POWERBI-B2C-PRESENCIAL",
            audience=CampaignType.B2C,
            product=ProductType.POWER_BI,
            modality=Modality.PRESENCIAL,
            campaign_family="POWERBI_PRESENCIAL_B2C",
            landing_variant="A",
            allowed_negative_intents={IntentClass.SOLUCION_PUNTUAL, IntentClass.EMPLEO},
            protected_intents=set(),
            protected_terms={"power bi", "powerbi"},
        )
        custom_reg.register_contract(pbi_contract)
        pbi_guard = NegativeGuard(self.snapshot, registry=custom_reg)

        res_pbi_core = pbi_guard.evaluate_candidate(
            raw_keyword="curso power bi",
            match_type=MatchType.BROAD,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-POWERBI-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_pbi_001",
        )
        self.assertFalse(res_pbi_core.is_valid_recommendation)
        self.assertEqual(res_pbi_core.policy_decision, PolicyDecision.CONFLICT)

        # 3. Product rule: Excel taxonomy cannot be auto-applied to Power BI
        res_pbi_excel = pbi_guard.evaluate_candidate(
            raw_keyword="buscarv avanzado",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-POWERBI-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_pbi_001",
        )
        self.assertFalse(res_pbi_excel.is_valid_recommendation)
        self.assertEqual(res_pbi_excel.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("PRODUCT_MISMATCH", res_pbi_excel.rationale)

        # 4. Unknown product fails closed -> HOLD_REVIEW
        unk_prod_contract = CampaignContract(
            campaign_id_hash="hash_unk_prod",
            campaign_name_pattern="SCL-UNKNOWN-PROD",
            audience=CampaignType.B2C,
            product=ProductType.UNKNOWN,
            modality=Modality.PRESENCIAL,
            campaign_family="UNKNOWN",
            landing_variant="N/A",
        )
        custom_reg.register_contract(unk_prod_contract)
        unk_guard = NegativeGuard(self.snapshot, registry=custom_reg)
        res_unk_prod = unk_guard.evaluate_candidate(
            raw_keyword="tutoriales",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-UNKNOWN-PROD",
            target_campaign_id_hash="hash_unk_prod",
        )
        self.assertFalse(res_unk_prod.is_valid_recommendation)
        self.assertEqual(res_unk_prod.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("UNKNOWN_PRODUCT", res_unk_prod.rationale)

    def test_07_cross_campaign_conflicts_and_protected_terms(self):
        """Test 7: Match-aware & scope-aware protected terms, and B2C vs B2B policies."""
        # 1. Isolated protected term -> CONFLICT
        res_iso = self.guard.evaluate_candidate(
            raw_keyword="presencial",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_iso.is_valid_recommendation)
        self.assertEqual(res_iso.policy_decision, PolicyDecision.CONFLICT)

        # 2. Pure value proposition phrase -> CONFLICT
        res_core = self.guard.evaluate_candidate(
            raw_keyword="curso excel presencial",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_core.is_valid_recommendation)
        self.assertEqual(res_core.policy_decision, PolicyDecision.CONFLICT)

        # 3. Compound phrase with excludable modifier 'gratis' -> CANDIDATE (not blocked by substring!)
        res_gratis = self.guard.evaluate_candidate(
            raw_keyword="curso excel presencial gratis",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertTrue(res_gratis.is_valid_recommendation)
        self.assertEqual(res_gratis.policy_decision, PolicyDecision.CANDIDATE)

        # 4. Compound phrase with excludable modifier 'empleo' -> CANDIDATE
        res_empleo = self.guard.evaluate_candidate(
            raw_keyword="curso excel presencial empleo",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertTrue(res_empleo.is_valid_recommendation)
        self.assertEqual(res_empleo.policy_decision, PolicyDecision.CANDIDATE)

        # 5. 'curso excel para empresas' -> CANDIDATE in B2C (B2B_SENCE excludable in B2C)
        res_b2c_b2b = self.guard.evaluate_candidate(
            raw_keyword="curso excel para empresas",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertTrue(res_b2c_b2b.is_valid_recommendation)
        self.assertEqual(res_b2c_b2b.policy_decision, PolicyDecision.CANDIDATE)

        # 6. 'curso excel para empresas' in B2B campaign -> CONFLICT
        res_b2b_self = self.guard.evaluate_candidate(
            raw_keyword="curso excel para empresas",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-EMPRESA-B2B",
            target_campaign_id_hash="hash_c22222222222",
        )
        self.assertFalse(res_b2b_self.is_valid_recommendation)
        self.assertEqual(res_b2b_self.policy_decision, PolicyDecision.CONFLICT)

    def test_08_routing_a_b_c_explicit_matrix(self):
        """Test 8: Explicit routing matrix positive and negative assertions across A/B/C."""
        # 1. 'paso a paso' at campaign level must be CONFLICT
        res_pap_camp = self.guard.evaluate_candidate(
            raw_keyword="curso excel paso a paso",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_pap_camp.is_valid_recommendation)
        self.assertEqual(res_pap_camp.policy_decision, PolicyDecision.CONFLICT)

        # 2. 'desde cero' at campaign level must be redirected to ROUTE
        res_dc_camp = self.guard.evaluate_candidate(
            raw_keyword="desde cero",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_dc_camp.is_valid_recommendation)
        self.assertEqual(res_dc_camp.policy_decision, PolicyDecision.ROUTE)

        # 3. Group A cedes 'principiantes' to B -> CANDIDATE
        res_a_to_b = self.guard.evaluate_candidate(
            raw_keyword="principiantes",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_A_GENERAL",
            target_ad_group_id_hash="hash_g_adg_a",
        )
        self.assertTrue(res_a_to_b.is_valid_recommendation)
        self.assertEqual(res_a_to_b.policy_decision, PolicyDecision.CANDIDATE)

        # 4. Group C cedes 'desde cero' to B -> CANDIDATE
        res_c_to_b = self.guard.evaluate_candidate(
            raw_keyword="desde cero",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_C_CLASES",
            target_ad_group_id_hash="hash_g_adg_c",
        )
        self.assertTrue(res_c_to_b.is_valid_recommendation)
        self.assertEqual(res_c_to_b.policy_decision, PolicyDecision.CANDIDATE)

        # 5. Group B CANNOT negate 'desde cero' within group B -> CONFLICT
        res_b_neg_b = self.guard.evaluate_candidate(
            raw_keyword="desde cero",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_B_DESDE_CERO",
            target_ad_group_id_hash="hash_g_adg_b",
        )
        self.assertFalse(res_b_neg_b.is_valid_recommendation)
        self.assertEqual(res_b_neg_b.policy_decision, PolicyDecision.CONFLICT)
        self.assertIn("ROUTING_CONFLICT_SELF", res_b_neg_b.rationale)

        # 6. Group A cedes 'profesor' to Group C -> CANDIDATE
        res_a_to_c = self.guard.evaluate_candidate(
            raw_keyword="profesor excel",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_A_GENERAL",
            target_ad_group_id_hash="hash_g_adg_a",
        )
        self.assertTrue(res_a_to_c.is_valid_recommendation)
        self.assertEqual(res_a_to_c.policy_decision, PolicyDecision.CANDIDATE)

        # 7. Group C CANNOT negate 'profesor' within group C -> CONFLICT
        res_c_neg_c = self.guard.evaluate_candidate(
            raw_keyword="profesor excel",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_C_CLASES",
            target_ad_group_id_hash="hash_g_adg_c",
        )
        self.assertFalse(res_c_neg_c.is_valid_recommendation)
        self.assertEqual(res_c_neg_c.policy_decision, PolicyDecision.CONFLICT)

        # 8. Unregistered ad group with ROUTING_A_B_C -> fail closed HOLD_REVIEW
        res_unk_adg = self.guard.evaluate_candidate(
            raw_keyword="desde cero",
            match_type=MatchType.EXACT,
            target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_UNKNOWN_RANDOM",
            target_ad_group_id_hash="hash_g_unknown",
        )
        self.assertFalse(res_unk_adg.is_valid_recommendation)
        self.assertEqual(res_unk_adg.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("ROUTING_UNDEFINED_GROUP", res_unk_adg.rationale)

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

            guard_process_1 = NegativeGuard(self.snapshot, ledger=ledger_p1)
            recs_p1 = guard_process_1.evaluate_batch(candidates)
            self.assertEqual(len(recs_p1), 2, "Process 1 must emit 2 recommendations")

            # Process 2: completely new instance and ledger handle pointing to same persistent path
            ledger_p2 = RecommendationLedger(ledger_path)
            guard_process_2 = NegativeGuard(self.snapshot, ledger=ledger_p2)
            recs_p2 = guard_process_2.evaluate_batch(candidates)
            self.assertEqual(len(recs_p2), 0, "Process 2 MUST emit 0 recommendations (PROCESS_2_RECOMMENDATIONS=0)")

    def test_10_snapshot_roundtrip_and_tamper_detection(self):
        """Test 10: Snapshot serialization, hash recalculation, and state_hash tamper detection."""
        # 1. Clean roundtrip
        self.assertTrue(NegativeSnapshotManager.verify_roundtrip(self.snapshot))

        # 2. Tamper detection
        snap_dict = self.snapshot.to_dict()
        # Tamper with keyword text while keeping old state_hash
        snap_dict["items"][0]["keyword_text"] = "manipulated_keyword"
        snap_dict["items"][0]["state_hash"] = "fake_state_hash"

        loaded_tampered = NegativeSnapshot.from_dict(snap_dict)
        self.assertEqual(loaded_tampered.status, "HOLD_REVIEW", "Tampered item must set snapshot to HOLD_REVIEW")
        self.assertIn("STATE_HASH_TAMPER_DETECTED", loaded_tampered.hold_reason)

    def test_11_live_read_adapter_official_model_and_type_filters(self):
        """Test 11: Official GAQL templates, account-level flow, and non-keyword type filters."""
        # Validate query templates: customer query must NOT select invalid fields
        self.assertNotIn("criterion_id", GAQL_CUSTOMER_NEGATIVES)
        self.assertNotIn("keyword.text", GAQL_CUSTOMER_NEGATIVES)
        self.assertNotIn("status", GAQL_CUSTOMER_NEGATIVES)
        self.assertIn("customer_negative_criterion.type", GAQL_CUSTOMER_NEGATIVES)
        self.assertIn("customer_negative_criterion.negative_keyword_list.shared_set", GAQL_CUSTOMER_NEGATIVES)

        # Validate type filter in other GAQL queries
        self.assertIn("shared_criterion.type = 'KEYWORD'", GAQL_SHARED_CRITERIA)
        self.assertIn("campaign_criterion.type = 'KEYWORD'", GAQL_CAMPAIGN_NEGATIVES)
        self.assertIn("ad_group_criterion.type = 'KEYWORD'", GAQL_AD_GROUP_NEGATIVES)

        # Mock GAQL responses representing full official account-level and entity flow
        def mock_gaql(customer_id: str, query: str):
            if "customer_negative_criterion" in query:
                return [
                    {
                        "type": "NEGATIVE_KEYWORD_LIST",
                        "shared_set": "customers/123/sharedSets/501",
                    }
                ]
            elif "FROM shared_criterion" in query:
                return [
                    # Valid keyword in account-level shared set 501
                    {"shared_set": "501", "type": "KEYWORD", "keyword_text": "gratis", "match_type": "EXACT"},
                    # Valid keyword in campaign shared set 502
                    {"shared_set": "502", "type": "KEYWORD", "keyword_text": "buscarv", "match_type": "PHRASE"},
                    # Non-keyword criterion: LOCATION -> must be discarded
                    {"shared_set": "501", "type": "LOCATION", "keyword_text": "santiago", "match_type": "EXACT"},
                    # Non-keyword criterion: AUDIENCE -> must be discarded
                    {"shared_set": "501", "type": "USER_LIST", "keyword_text": "audience_1", "match_type": "BROAD"},
                    # Keyword in REMOVED shared set 503 -> must be discarded
                    {"shared_set": "503", "type": "KEYWORD", "keyword_text": "removed_term", "match_type": "BROAD"},
                    # Keyword with UNKNOWN match type -> must be discarded
                    {"shared_set": "501", "type": "KEYWORD", "keyword_text": "valid_text", "match_type": "UNKNOWN"},
                    # Keyword without text -> must be discarded
                    {"shared_set": "501", "type": "KEYWORD", "keyword_text": "", "match_type": "BROAD"},
                    # Keyword without parent -> must be discarded
                    {"shared_set": "999", "type": "KEYWORD", "keyword_text": "orphan_term", "match_type": "BROAD"},
                ]
            elif "FROM shared_set" in query:
                return [
                    {"id": "501", "name": "GLOBAL_ACC_NEGATIVES", "type": "ACCOUNT_LEVEL_NEGATIVE_KEYWORDS", "status": "ENABLED"},
                    {"id": "502", "name": "SET_CAMP_SOLUCIONES", "type": "NEGATIVE_KEYWORDS", "status": "ENABLED"},
                    {"id": "503", "name": "SET_REMOVED", "type": "NEGATIVE_KEYWORDS", "status": "REMOVED"},
                ]
            elif "campaign_shared_set" in query:
                return [
                    {"campaign": "1001", "shared_set": "502", "status": "ENABLED"},
                    {"campaign": "1001", "shared_set": "503", "status": "ENABLED"},  # 503 is removed set -> discarded
                ]
            elif "campaign_criterion" in query:
                return [
                    {"campaign_id": "1001", "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL", "type": "KEYWORD", "keyword_text": "clases particulares", "match_type": "PHRASE", "status": "ENABLED"},
                    {"campaign_id": "1001", "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL", "type": "PLACEMENT", "keyword_text": "youtube.com", "match_type": "EXACT", "status": "ENABLED"},  # non-keyword discarded
                ]
            elif "ad_group_criterion" in query:
                return [
                    {"campaign_id": "1001", "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL", "ad_group_id": "2001", "ad_group_name": "ADG_A_GENERAL", "type": "KEYWORD", "keyword_text": "desde cero", "match_type": "EXACT", "status": "ENABLED"},
                ]
            return []

        adapter = GoogleAdsNegativeReadAdapter(gaql_executor=mock_gaql)
        snap = adapter.build_snapshot(customer_id="123456789", evidence_source="SIMULATED_API")

        self.assertEqual(snap.status, "READY")
        # Exactly 4 valid keyword items:
        # 1. 'gratis' (CUSTOMER / Account-level via 501)
        # 2. 'buscarv' (SHARED_SET via 502)
        # 3. 'clases particulares' (CAMPAIGN)
        # 4. 'desde cero' (AD_GROUP)
        self.assertEqual(len(snap.items), 4)

        # Check account-level modeling as global customer coverage
        acc_item = [i for i in snap.items if i.keyword_text == "gratis"][0]
        self.assertEqual(acc_item.source_scope, SourceScope.CUSTOMER)
        self.assertEqual(acc_item.campaign_name, "GLOBAL")

        # Check removed shared set was discarded from campaign attachments
        c_hash = hash_identifier("1001")
        self.assertEqual(snap.campaign_shared_sets.get(c_hash), ["SET_CAMP_SOLUCIONES"])

        # Unconfigured / Auth failure returns HOLD_DATA_GAP
        adapter_unconfigured = GoogleAdsNegativeReadAdapter(gaql_executor=None)
        hold_snap = adapter_unconfigured.build_snapshot(customer_id="123456789")
        self.assertEqual(hold_snap.status, "HOLD_DATA_GAP")
        self.assertIn("ACCESS_TOKEN_SCOPE_INSUFFICIENT", hold_snap.hold_reason)

    def test_12_sanitized_ids_and_sentinels(self):
        """Test 12: Deterministic identifier hashing masks IDs and preserves sentinels."""
        # Sentinels must not be hashed
        self.assertEqual(hash_identifier("none"), "none")
        self.assertEqual(hash_identifier("unknown"), "unknown")
        self.assertEqual(hash_identifier("global"), "global")
        self.assertEqual(hash_identifier(""), "none")

        # Numeric IDs are deterministically hashed
        h1 = hash_identifier("1234567890")
        self.assertTrue(h1.startswith("hash_"))
        self.assertEqual(len(h1), 17)
        self.assertNotIn("1234567890", h1)

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

        email_matches = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", fixtures_text)
        self.assertEqual(len(email_matches), 0, f"Email PII found: {email_matches}")

        phone_matches = re.findall(r"\+56\s*9\s*\d{8}", fixtures_text)
        self.assertEqual(len(phone_matches), 0, f"Phone PII found: {phone_matches}")

    def test_14_ledger_corruption_fail_closed(self):
        """Test 14: Corrupted ledger fails closed with LEDGER_CORRUPT=HOLD."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ledger_dir = Path(tmp_dir)
            corrupt_file = ledger_dir / "negative_guard_recommendations_ledger.json"
            # Write invalid JSON
            corrupt_file.write_text("{corrupt_json: true,", encoding="utf-8")

            ledger = RecommendationLedger(ledger_dir)
            self.assertTrue(ledger.is_corrupt)

            guard = NegativeGuard(self.snapshot, ledger=ledger)
            res = guard.evaluate_candidate(
                raw_keyword="ejercicios excel avanzados",
                match_type=MatchType.PHRASE,
                target_scope=SourceScope.CAMPAIGN,
                target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
                target_campaign_id_hash="hash_c11111111111",
            )
            self.assertFalse(res.is_valid_recommendation)
            self.assertEqual(res.policy_decision, PolicyDecision.HOLD_REVIEW)
            self.assertIn("LEDGER_CORRUPT=HOLD", res.rationale)

            # Record must raise RuntimeError on corrupt ledger
            with self.assertRaises(RuntimeError):
                ledger.record("manifest_1", "rec_1")

    def test_15_two_real_cli_subprocesses_idempotency(self):
        """Test 15: Two independent real CLI subprocesses verify zero duplicate recommendations."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            cmd = [
                sys.executable,
                str(REPO_ROOT / "scripts" / "google_ads_readonly" / "run_negative_guard.py"),
                "--snapshot-path",
                str(FIXTURES_PATH),
                "--demo",
                "--ledger-dir",
                tmp_dir,
            ]

            # Subprocess 1
            proc1 = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_ROOT))
            self.assertEqual(proc1.returncode, 0, f"Process 1 failed: {proc1.stderr}")
            self.assertIn("RUN_1_VALID_DELTA_RECOMMENDATIONS: 2", proc1.stdout)

            # Subprocess 2
            proc2 = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_ROOT))
            self.assertEqual(proc2.returncode, 0, f"Process 2 failed: {proc2.stderr}")
            self.assertIn("RUN_1_VALID_DELTA_RECOMMENDATIONS: 0", proc2.stdout)

    def test_16_ledger_concurrency_locking(self):
        """Test 16: Inter-process ledger concurrency locking protects simultaneous writes."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ledger_dir = Path(tmp_dir)

            def worker(worker_id: int):
                ledger = RecommendationLedger(ledger_dir)
                for i in range(5):
                    ledger.record("manifest_test", f"rec_worker_{worker_id}_{i}")

            threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()

            final_ledger = RecommendationLedger(ledger_dir)
            self.assertEqual(final_ledger.count(), 20, "All 20 records must be persisted without corruption")


if __name__ == "__main__":
    unittest.main()
