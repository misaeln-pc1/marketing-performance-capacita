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
17. HMAC external key required (fail-closed, no public fallback).
18. Public fallback key removed (source scan).
19. Invalid prehashed ID rejected.
20. Sentinels preserved.
21. Atomic ledger claim with concurrent subprocesses.
22. PAUSED items not active (differentiated signal).
23. Live executor wired (hold auth).
24. Private campaign mapping required (empty registry fail-closed).
25. Manifest hash tamper detection.
26. GoogleAdsRow-like native protobuf conversion to dict with nested structure.
27. GoogleAdsRow-like proto-plus conversion to dict with nested structure.
28. Converted rows consumed end-to-end by GoogleAdsNegativeReadAdapter.
29. Unknown/unsupported row types fail closed (TypeError, no _raw/invented structure).
"""

from __future__ import annotations

import copy
import json
import os
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
    DEMO_CAMPAIGN_CONTRACTS,
    Modality,
    ProductType,
    validate_ad_group_routing,
)
from core.negative_guard.classifier import classify_campaign, classify_keyword_intent
from core.negative_guard.guard import NegativeGuard
from core.negative_guard.ledger import ClaimResult, RecommendationLedger
from core.negative_guard.live_executor import GoogleAdsLiveExecutor
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

try:
    from google.ads.googleads.v24.services.types.google_ads_service import GoogleAdsRow as V24GoogleAdsRow
    from google.ads.googleads.v24.resources.types.campaign import Campaign as V24Campaign
    from google.ads.googleads.v24.resources.types.ad_group import AdGroup as V24AdGroup
    from google.ads.googleads.v24.resources.types.shared_set import SharedSet as V24SharedSet
    from google.ads.googleads.v24.resources.types.customer_negative_criterion import CustomerNegativeCriterion as V24CustomerNegativeCriterion
    from google.ads.googleads.v24.resources.types.shared_criterion import SharedCriterion as V24SharedCriterion
    from google.ads.googleads.v24.resources.types.campaign_criterion import CampaignCriterion as V24CampaignCriterion
    from google.ads.googleads.v24.resources.types.ad_group_criterion import AdGroupCriterion as V24AdGroupCriterion
    from google.ads.googleads.v24.resources.types.campaign_shared_set import CampaignSharedSet as V24CampaignSharedSet
    from google.ads.googleads.v24.common.types.criteria import KeywordInfo as V24KeywordInfo, NegativeKeywordListInfo as V24NegativeKeywordListInfo
    from google.ads.googleads.v24.enums.types.keyword_match_type import KeywordMatchTypeEnum as V24KeywordMatchTypeEnum
    from google.ads.googleads.v24.enums.types.shared_set_type import SharedSetTypeEnum as V24SharedSetTypeEnum
    from google.ads.googleads.v24.enums.types.shared_set_status import SharedSetStatusEnum as V24SharedSetStatusEnum
    from google.ads.googleads.v24.enums.types.criterion_type import CriterionTypeEnum as V24CriterionTypeEnum
    from google.ads.googleads.v24.enums.types.campaign_shared_set_status import CampaignSharedSetStatusEnum as V24CampaignSharedSetStatusEnum
    from google.ads.googleads.util import convert_proto_plus_to_protobuf
    _V24_AVAILABLE = True
except ImportError:
    _V24_AVAILABLE = False
    convert_proto_plus_to_protobuf = None

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURES_PATH = Path(__file__).parent / "fixtures" / "negative_snapshot_fixtures.json"

# Test HMAC key — used for all tests, never committed to production
TEST_HMAC_KEY = "test_key_for_ci_only_not_production"


class TestNegativeGuard(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures with explicit HMAC key in environment."""
        os.environ["CAPACITA_HMAC_KEY"] = TEST_HMAC_KEY
        self.snapshot = NegativeSnapshotManager.load_from_json(FIXTURES_PATH)
        self.registry = CampaignRegistry(contracts=DEMO_CAMPAIGN_CONTRACTS)
        self.guard = NegativeGuard(self.snapshot, registry=self.registry)

    def tearDown(self):
        """Clean up HMAC key from environment."""
        os.environ.pop("CAPACITA_HMAC_KEY", None)

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
            target_campaign_id_hash="hash_000000000099",
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
            campaign_id_hash="hash_d000123abcde",
            campaign_name_pattern="DUP-CAMP-1",
            audience=CampaignType.B2C,
            product=ProductType.EXCEL,
            modality=Modality.PRESENCIAL,
            campaign_family="DUP",
            landing_variant="A",
        )
        c2 = CampaignContract(
            campaign_id_hash="hash_d000123abcde",
            campaign_name_pattern="DUP-CAMP-2",
            audience=CampaignType.B2C,
            product=ProductType.EXCEL,
            modality=Modality.PRESENCIAL,
            campaign_family="DUP",
            landing_variant="B",
        )
        reg_dup = CampaignRegistry(contracts=[c1, c2])
        self.assertIsNone(reg_dup.resolve("hash_d000123abcde", "DUP-CAMP-1"), "Multiple matches must fail closed")

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
        custom_reg = CampaignRegistry(contracts=list(DEMO_CAMPAIGN_CONTRACTS))
        online_contract = CampaignContract(
            campaign_id_hash="hash_0000000000e1",
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
            target_campaign_id_hash="hash_0000000000e1",
        )
        self.assertFalse(res_online.is_valid_recommendation)
        self.assertEqual(res_online.policy_decision, PolicyDecision.CONFLICT)

        # 2. Product rule: Power BI cannot be FUERA_ALCANCE in a Power BI campaign
        pbi_contract = CampaignContract(
            campaign_id_hash="hash_0000000000b1",
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
            target_campaign_id_hash="hash_0000000000b1",
        )
        self.assertFalse(res_pbi_core.is_valid_recommendation)
        self.assertEqual(res_pbi_core.policy_decision, PolicyDecision.CONFLICT)

        # 3. Product rule: Excel taxonomy cannot be auto-applied to Power BI
        res_pbi_excel = pbi_guard.evaluate_candidate(
            raw_keyword="buscarv avanzado",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-POWERBI-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_0000000000b1",
        )
        self.assertFalse(res_pbi_excel.is_valid_recommendation)
        self.assertEqual(res_pbi_excel.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("PRODUCT_MISMATCH", res_pbi_excel.rationale)

        # 4. Unknown product fails closed -> HOLD_REVIEW
        unk_prod_contract = CampaignContract(
            campaign_id_hash="hash_000000000003",
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
            target_campaign_id_hash="hash_000000000003",
        )
        self.assertFalse(res_unk_prod.is_valid_recommendation)
        self.assertEqual(res_unk_prod.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("UNKNOWN_PRODUCT", res_unk_prod.rationale)

    def test_07_cross_campaign_conflicts_and_protected_terms(self):
        """Test 7: Match-aware & scope-aware protected terms, and B2C vs B2B policies."""
        res_iso = self.guard.evaluate_candidate(
            raw_keyword="presencial", match_type=MatchType.EXACT, target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_iso.is_valid_recommendation)
        self.assertEqual(res_iso.policy_decision, PolicyDecision.CONFLICT)

        res_core = self.guard.evaluate_candidate(
            raw_keyword="curso excel presencial", match_type=MatchType.PHRASE, target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_core.is_valid_recommendation)
        self.assertEqual(res_core.policy_decision, PolicyDecision.CONFLICT)

        res_gratis = self.guard.evaluate_candidate(
            raw_keyword="curso excel presencial gratis", match_type=MatchType.PHRASE, target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
        )
        self.assertTrue(res_gratis.is_valid_recommendation)
        self.assertEqual(res_gratis.policy_decision, PolicyDecision.CANDIDATE)

        res_empleo = self.guard.evaluate_candidate(
            raw_keyword="curso excel presencial empleo", match_type=MatchType.PHRASE, target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
        )
        self.assertTrue(res_empleo.is_valid_recommendation)
        self.assertEqual(res_empleo.policy_decision, PolicyDecision.CANDIDATE)

        res_b2c_b2b = self.guard.evaluate_candidate(
            raw_keyword="curso excel para empresas", match_type=MatchType.PHRASE, target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
        )
        self.assertTrue(res_b2c_b2b.is_valid_recommendation)
        self.assertEqual(res_b2c_b2b.policy_decision, PolicyDecision.CANDIDATE)

        res_b2b_self = self.guard.evaluate_candidate(
            raw_keyword="curso excel para empresas", match_type=MatchType.PHRASE, target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-EMPRESA-B2B", target_campaign_id_hash="hash_c22222222222",
        )
        self.assertFalse(res_b2b_self.is_valid_recommendation)
        self.assertEqual(res_b2b_self.policy_decision, PolicyDecision.CONFLICT)

    def test_08_routing_a_b_c_explicit_matrix(self):
        """Test 8: Explicit routing matrix positive and negative assertions across A/B/C."""
        res_pap_camp = self.guard.evaluate_candidate(
            raw_keyword="curso excel paso a paso", match_type=MatchType.PHRASE, target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_pap_camp.is_valid_recommendation)
        self.assertEqual(res_pap_camp.policy_decision, PolicyDecision.CONFLICT)

        res_dc_camp = self.guard.evaluate_candidate(
            raw_keyword="desde cero", match_type=MatchType.EXACT, target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res_dc_camp.is_valid_recommendation)
        self.assertEqual(res_dc_camp.policy_decision, PolicyDecision.ROUTE)

        res_a_to_b = self.guard.evaluate_candidate(
            raw_keyword="principiantes", match_type=MatchType.PHRASE, target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_A_GENERAL", target_ad_group_id_hash="hash_00000000000a",
        )
        self.assertTrue(res_a_to_b.is_valid_recommendation)
        self.assertEqual(res_a_to_b.policy_decision, PolicyDecision.CANDIDATE)

        res_c_to_b = self.guard.evaluate_candidate(
            raw_keyword="desde cero", match_type=MatchType.EXACT, target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_C_CLASES", target_ad_group_id_hash="hash_00000000000c",
        )
        self.assertTrue(res_c_to_b.is_valid_recommendation)
        self.assertEqual(res_c_to_b.policy_decision, PolicyDecision.CANDIDATE)

        res_b_neg_b = self.guard.evaluate_candidate(
            raw_keyword="desde cero", match_type=MatchType.EXACT, target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_B_DESDE_CERO", target_ad_group_id_hash="hash_00000000000b",
        )
        self.assertFalse(res_b_neg_b.is_valid_recommendation)
        self.assertEqual(res_b_neg_b.policy_decision, PolicyDecision.CONFLICT)
        self.assertIn("ROUTING_CONFLICT_SELF", res_b_neg_b.rationale)

        res_a_to_c = self.guard.evaluate_candidate(
            raw_keyword="profesor excel", match_type=MatchType.PHRASE, target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_A_GENERAL", target_ad_group_id_hash="hash_00000000000a",
        )
        self.assertTrue(res_a_to_c.is_valid_recommendation)
        self.assertEqual(res_a_to_c.policy_decision, PolicyDecision.CANDIDATE)

        res_c_neg_c = self.guard.evaluate_candidate(
            raw_keyword="profesor excel", match_type=MatchType.PHRASE, target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_C_CLASES", target_ad_group_id_hash="hash_00000000000c",
        )
        self.assertFalse(res_c_neg_c.is_valid_recommendation)
        self.assertEqual(res_c_neg_c.policy_decision, PolicyDecision.CONFLICT)

        res_unk_adg = self.guard.evaluate_candidate(
            raw_keyword="desde cero", match_type=MatchType.EXACT, target_scope=SourceScope.AD_GROUP,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL", target_campaign_id_hash="hash_c11111111111",
            target_ad_group_name="ADG_UNKNOWN_RANDOM", target_ad_group_id_hash="hash_00000000000e",
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

            guard_process_1 = NegativeGuard(self.snapshot, registry=self.registry, ledger=ledger_p1)
            recs_p1 = guard_process_1.evaluate_batch(candidates)
            self.assertEqual(len(recs_p1), 2, "Process 1 must emit 2 recommendations")

            # Process 2: completely new instance and ledger handle pointing to same persistent path
            ledger_p2 = RecommendationLedger(ledger_path)
            guard_process_2 = NegativeGuard(self.snapshot, registry=self.registry, ledger=ledger_p2)
            recs_p2 = guard_process_2.evaluate_batch(candidates)
            self.assertEqual(len(recs_p2), 0, "Process 2 MUST emit 0 recommendations (PROCESS_2_RECOMMENDATIONS=0)")

    def test_10_snapshot_roundtrip_and_tamper_detection(self):
        """Test 10: Snapshot serialization, hash recalculation, and state_hash tamper detection."""
        self.assertTrue(NegativeSnapshotManager.verify_roundtrip(self.snapshot))

        snap_dict = self.snapshot.to_dict()
        snap_dict["items"][0]["keyword_text"] = "manipulated_keyword"
        snap_dict["items"][0]["state_hash"] = "fake_state_hash"

        loaded_tampered = NegativeSnapshot.from_dict(snap_dict)
        self.assertEqual(loaded_tampered.status, "HOLD_REVIEW", "Tampered item must set snapshot to HOLD_REVIEW")
        self.assertIn("STATE_HASH_TAMPER_DETECTED", loaded_tampered.hold_reason)

    def test_11_live_read_adapter_official_model_and_type_filters(self):
        """Test 11: Official GAQL templates, account-level flow, and non-keyword type filters."""
        self.assertNotIn("criterion_id", GAQL_CUSTOMER_NEGATIVES)
        self.assertNotIn("keyword.text", GAQL_CUSTOMER_NEGATIVES)
        self.assertNotIn("status", GAQL_CUSTOMER_NEGATIVES)
        self.assertIn("customer_negative_criterion.type", GAQL_CUSTOMER_NEGATIVES)
        self.assertIn("customer_negative_criterion.negative_keyword_list.shared_set", GAQL_CUSTOMER_NEGATIVES)
        self.assertIn("shared_criterion.type = 'KEYWORD'", GAQL_SHARED_CRITERIA)
        self.assertIn("campaign_criterion.type = 'KEYWORD'", GAQL_CAMPAIGN_NEGATIVES)
        self.assertIn("ad_group_criterion.type = 'KEYWORD'", GAQL_AD_GROUP_NEGATIVES)

        def mock_gaql(customer_id: str, query: str):
            if "customer_negative_criterion" in query:
                return [{"type": "NEGATIVE_KEYWORD_LIST", "shared_set": "customers/123/sharedSets/501"}]
            elif "FROM shared_criterion" in query:
                return [
                    {"shared_set": "501", "type": "KEYWORD", "keyword_text": "gratis", "match_type": "EXACT"},
                    {"shared_set": "502", "type": "KEYWORD", "keyword_text": "buscarv", "match_type": "PHRASE"},
                    {"shared_set": "501", "type": "LOCATION", "keyword_text": "santiago", "match_type": "EXACT"},
                    {"shared_set": "501", "type": "USER_LIST", "keyword_text": "audience_1", "match_type": "BROAD"},
                    {"shared_set": "503", "type": "KEYWORD", "keyword_text": "removed_term", "match_type": "BROAD"},
                    {"shared_set": "501", "type": "KEYWORD", "keyword_text": "valid_text", "match_type": "UNKNOWN"},
                    {"shared_set": "501", "type": "KEYWORD", "keyword_text": "", "match_type": "BROAD"},
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
                    {"campaign": "1001", "shared_set": "503", "status": "ENABLED"},
                ]
            elif "campaign_criterion" in query:
                return [
                    {"campaign_id": "1001", "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL", "type": "KEYWORD", "keyword_text": "clases particulares", "match_type": "PHRASE", "status": "ENABLED"},
                    {"campaign_id": "1001", "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL", "type": "PLACEMENT", "keyword_text": "youtube.com", "match_type": "EXACT", "status": "ENABLED"},
                ]
            elif "ad_group_criterion" in query:
                return [
                    {"campaign_id": "1001", "campaign_name": "SCL-EXCEL-B2C-PRESENCIAL", "ad_group_id": "2001", "ad_group_name": "ADG_A_GENERAL", "type": "KEYWORD", "keyword_text": "desde cero", "match_type": "EXACT", "status": "ENABLED"},
                ]
            return []

        adapter = GoogleAdsNegativeReadAdapter(gaql_executor=mock_gaql)
        snap = adapter.build_snapshot(customer_id="123456789", evidence_source="SIMULATED_API")

        self.assertEqual(snap.status, "READY")
        self.assertEqual(len(snap.items), 4)

        acc_item = [i for i in snap.items if i.keyword_text == "gratis"][0]
        self.assertEqual(acc_item.source_scope, SourceScope.CUSTOMER)
        self.assertEqual(acc_item.campaign_name, "GLOBAL")

        c_hash = hash_identifier("1001")
        self.assertEqual(snap.campaign_shared_sets.get(c_hash), ["SET_CAMP_SOLUCIONES"])

        adapter_unconfigured = GoogleAdsNegativeReadAdapter(gaql_executor=None)
        hold_snap = adapter_unconfigured.build_snapshot(customer_id="123456789")
        self.assertEqual(hold_snap.status, "HOLD_DATA_GAP")
        self.assertIn("ACCESS_TOKEN_SCOPE_INSUFFICIENT", hold_snap.hold_reason)

    def test_12_sanitized_ids_and_sentinels(self):
        """Test 12: Deterministic identifier hashing masks IDs and preserves sentinels."""
        self.assertEqual(hash_identifier("none"), "none")
        self.assertEqual(hash_identifier("unknown"), "unknown")
        self.assertEqual(hash_identifier("global"), "global")
        self.assertEqual(hash_identifier(""), "none")

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
            corrupt_file.write_text("{corrupt_json: true,", encoding="utf-8")

            ledger = RecommendationLedger(ledger_dir)
            self.assertTrue(ledger.is_corrupt)

            guard = NegativeGuard(self.snapshot, registry=self.registry, ledger=ledger)
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

            # claim_once must return HOLD_CORRUPT on corrupt ledger
            result = ledger.claim_once("manifest_1", "rec_1")
            self.assertEqual(result, ClaimResult.HOLD_CORRUPT)

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
            env = os.environ.copy()
            env["CAPACITA_HMAC_KEY"] = TEST_HMAC_KEY

            proc1 = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_ROOT), env=env)
            self.assertEqual(proc1.returncode, 0, f"Process 1 failed: {proc1.stderr}")
            self.assertIn("RUN_1_VALID_DELTA_RECOMMENDATIONS: 2", proc1.stdout)

            proc2 = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_ROOT), env=env)
            self.assertEqual(proc2.returncode, 0, f"Process 2 failed: {proc2.stderr}")
            self.assertIn("RUN_1_VALID_DELTA_RECOMMENDATIONS: 0", proc2.stdout)

    def test_16_ledger_concurrency_locking(self):
        """Test 16: Inter-process ledger concurrency locking protects simultaneous writes."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ledger_dir = Path(tmp_dir)

            def worker(worker_id: int):
                ledger = RecommendationLedger(ledger_dir)
                for i in range(5):
                    ledger.claim_once("manifest_test", f"rec_worker_{worker_id}_{i}")

            threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()

            final_ledger = RecommendationLedger(ledger_dir)
            self.assertEqual(final_ledger.count(), 20, "All 20 records must be persisted without corruption")

    def test_17_hmac_external_key_required(self):
        """Test 17: HMAC_EXTERNAL_KEY_REQUIRED — fail-closed without key."""
        os.environ.pop("CAPACITA_HMAC_KEY", None)
        with self.assertRaises(ValueError) as ctx:
            hash_identifier("12345")
        self.assertIn("HMAC_KEY_MISSING", str(ctx.exception))

    def test_18_public_fallback_key_removed(self):
        """Test 18: PUBLIC_FALLBACK_KEY_REMOVED — ephemeral key string must not exist in source."""
        models_path = REPO_ROOT / "core" / "negative_guard" / "models.py"
        source_code = models_path.read_text(encoding="utf-8")
        self.assertNotIn("capacita_runtime_hmac_ephemeral", source_code,
                         "Public fallback HMAC key must be completely removed from source")

    def test_19_invalid_prehashed_id_rejected(self):
        """Test 19: INVALID_PREHASHED_ID_REJECTED — strict format validation."""
        # Invalid: hash_ prefix but not 12 hex chars
        with self.assertRaises(ValueError) as ctx:
            hash_identifier("hash_ZZZZ")
        self.assertIn("INVALID_PREHASHED_ID", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            hash_identifier("hash_toolong1234567")
        self.assertIn("INVALID_PREHASHED_ID", str(ctx.exception))

        # Invalid: alias_ prefix rejected
        with self.assertRaises(ValueError) as ctx:
            hash_identifier("alias_abc")
        self.assertIn("INVALID_IDENTIFIER_FORMAT", str(ctx.exception))

        # Invalid: *** pattern rejected
        with self.assertRaises(ValueError) as ctx:
            hash_identifier("***MASKED***")
        self.assertIn("INVALID_IDENTIFIER_FORMAT", str(ctx.exception))

        # Valid: proper hash_ format passes through
        self.assertEqual(hash_identifier("hash_abcdef012345"), "hash_abcdef012345")

    def test_20_sentinels_preserved(self):
        """Test 20: SENTINELS_PRESERVED — explicit sentinels pass through without hashing."""
        self.assertEqual(hash_identifier("none"), "none")
        self.assertEqual(hash_identifier("unknown"), "unknown")
        self.assertEqual(hash_identifier("global"), "global")
        self.assertEqual(hash_identifier("n/a"), "n/a")
        self.assertEqual(hash_identifier(""), "none")
        self.assertEqual(hash_identifier(None), "none")
        self.assertEqual(hash_identifier("  NONE  "), "none")
        self.assertEqual(hash_identifier("UNKNOWN"), "unknown")
        self.assertEqual(hash_identifier("  Global  "), "global")

    def test_21_atomic_ledger_claim_concurrent_subprocesses(self):
        """Test 21: ATOMIC_LEDGER_CLAIM — two subprocesses, same recommendation, exactly one CLAIMED."""
        with tempfile.TemporaryDirectory() as tmp_dir:
            ledger_dir = Path(tmp_dir)
            # Write a small script that claims a specific key
            claim_script = Path(tmp_dir) / "claim_worker.py"
            claim_script.write_text(f"""
import sys, os, time
sys.path.insert(0, r"{REPO_ROOT}")
os.environ["CAPACITA_HMAC_KEY"] = "{TEST_HMAC_KEY}"
from pathlib import Path
from core.negative_guard.ledger import RecommendationLedger

ledger = RecommendationLedger(Path(r"{ledger_dir}"))
result = ledger.claim_once("same_manifest", "same_recommendation")
print(result.value)
""", encoding="utf-8")

            env = os.environ.copy()
            env["CAPACITA_HMAC_KEY"] = TEST_HMAC_KEY

            # Launch two subprocesses simultaneously
            p1 = subprocess.Popen([sys.executable, str(claim_script)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
            p2 = subprocess.Popen([sys.executable, str(claim_script)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)

            out1, err1 = p1.communicate(timeout=30)
            out2, err2 = p2.communicate(timeout=30)

            results = [out1.strip(), out2.strip()]
            claimed_count = results.count("CLAIMED")
            already_exists_count = results.count("ALREADY_EXISTS")

            self.assertEqual(claimed_count, 1, f"Exactly one CLAIMED expected, got {claimed_count}. Results: {results}")
            self.assertEqual(already_exists_count, 1, f"Exactly one ALREADY_EXISTS expected. Results: {results}")

            # Verify single ledger entry
            final_ledger = RecommendationLedger(ledger_dir)
            self.assertEqual(final_ledger.count(), 1, "TOTAL_LEDGER_ENTRIES=1")

    def test_22_paused_not_active(self):
        """Test 22: PAUSED_NOT_ACTIVE — PAUSED items excluded from active, differentiated signal."""
        # Verify PAUSED items exist in snapshot but not in active_items
        all_paused = self.snapshot.paused_items()
        self.assertEqual(len(all_paused), 4, "Fixtures should contain 4 PAUSED items")

        active = self.snapshot.active_items()
        active_texts = {i.keyword_text for i in active}
        for paused_item in all_paused:
            self.assertNotIn(paused_item.keyword_text, active_texts,
                             f"PAUSED item '{paused_item.keyword_text}' should NOT be in active_items()")

        # Verify PAUSED scopes coverage
        paused_scopes = {i.source_scope for i in all_paused}
        self.assertIn(SourceScope.CUSTOMER, paused_scopes, "CUSTOMER_PAUSED fixture missing")
        self.assertIn(SourceScope.SHARED_SET, paused_scopes, "SHARED_SET_PAUSED fixture missing")
        self.assertIn(SourceScope.CAMPAIGN, paused_scopes, "CAMPAIGN_PAUSED fixture missing")
        self.assertIn(SourceScope.AD_GROUP, paused_scopes, "AD_GROUP_PAUSED fixture missing")

        # Verify guard produces EXISTS_PAUSED signal for a PAUSED keyword
        res = self.guard.evaluate_candidate(
            raw_keyword="descargar excel gratis",
            match_type=MatchType.BROAD,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res.is_valid_recommendation)
        self.assertEqual(res.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("EXISTS_PAUSED", res.rationale)
        self.assertIn("REVIEW_REACTIVATION", res.rationale)

    def test_23_live_executor_wired_hold_auth(self):
        """Test 23: LIVE_EXECUTOR_WIRED — module exists, fails closed without config."""
        # Module exists and is importable
        self.assertTrue(hasattr(GoogleAdsLiveExecutor, '__init__'))
        self.assertTrue(hasattr(GoogleAdsLiveExecutor, 'execute_gaql_select'))
        self.assertTrue(hasattr(GoogleAdsLiveExecutor, 'create_gaql_executor'))

        # Fail-closed without config file
        with self.assertRaises(FileNotFoundError) as ctx:
            GoogleAdsLiveExecutor(Path("/nonexistent/config.json"))
        self.assertIn("RUNTIME_CONFIG_MISSING", str(ctx.exception))

        # Fail-closed with incomplete config
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump({"google_ads_config_path": "/some/path"}, f)
            incomplete_path = f.name
        try:
            with self.assertRaises(ValueError) as ctx:
                GoogleAdsLiveExecutor(Path(incomplete_path))
            self.assertIn("RUNTIME_CONFIG_INCOMPLETE", str(ctx.exception))
        finally:
            os.unlink(incomplete_path)

    def test_24_private_campaign_mapping_required(self):
        """Test 24: PRIVATE_CAMPAIGN_MAPPING_REQUIRED — empty registry fails closed."""
        # Empty registry resolves nothing
        empty_reg = CampaignRegistry()
        self.assertIsNone(empty_reg.resolve("hash_c11111111111", "SCL-EXCEL-B2C-PRESENCIAL"))

        # Guard with empty registry fails closed on all candidates
        guard_empty = NegativeGuard(self.snapshot, registry=empty_reg)
        res = guard_empty.evaluate_candidate(
            raw_keyword="ejercicios excel avanzados",
            match_type=MatchType.PHRASE,
            target_scope=SourceScope.CAMPAIGN,
            target_campaign_name="SCL-EXCEL-B2C-PRESENCIAL",
            target_campaign_id_hash="hash_c11111111111",
        )
        self.assertFalse(res.is_valid_recommendation)
        self.assertEqual(res.policy_decision, PolicyDecision.HOLD_REVIEW)
        self.assertIn("UNKNOWN_CAMPAIGN", res.rationale)

        # load_contracts_from_json fails closed with missing file
        with self.assertRaises(FileNotFoundError) as ctx:
            CampaignRegistry.load_contracts_from_json(Path("/nonexistent/contracts.json"))
        self.assertIn("CAMPAIGN_MAPPING_MISSING", str(ctx.exception))

    def test_25_manifest_hash_tamper_detection(self):
        """Test 25: MANIFEST_HASH_TAMPER_DETECTION — manipulation of various fields."""
        snap_dict = self.snapshot.to_dict()
        original_manifest = snap_dict["manifest_hash"]

        # 1. Tamper campaign_shared_sets
        tampered_1 = copy.deepcopy(snap_dict)
        tampered_1["campaign_shared_sets"]["hash_c11111111111"].append("INJECTED_SET")
        loaded_1 = NegativeSnapshot.from_dict(tampered_1)
        self.assertEqual(loaded_1.status, "HOLD_REVIEW")
        self.assertIn("MANIFEST_HASH_TAMPER_DETECTED", loaded_1.hold_reason)

        # 2. Tamper status
        tampered_2 = copy.deepcopy(snap_dict)
        tampered_2["status"] = "COMPROMISED"
        loaded_2 = NegativeSnapshot.from_dict(tampered_2)
        self.assertEqual(loaded_2.status, "HOLD_REVIEW")
        self.assertIn("MANIFEST_HASH_TAMPER_DETECTED", loaded_2.hold_reason)

        # 3. Tamper hold_reason
        tampered_3 = copy.deepcopy(snap_dict)
        tampered_3["hold_reason"] = "INJECTED_REASON"
        loaded_3 = NegativeSnapshot.from_dict(tampered_3)
        self.assertEqual(loaded_3.status, "HOLD_REVIEW")
        self.assertIn("MANIFEST_HASH_TAMPER_DETECTED", loaded_3.hold_reason)

        # 4. Item added
        tampered_4 = copy.deepcopy(snap_dict)
        tampered_4["items"] = list(tampered_4["items"]) + [{
            "keyword_text": "injected_keyword",
            "match_type": "BROAD",
            "source_scope": "CAMPAIGN",
            "campaign_name": "INJECTED",
            "campaign_id_hash": "none",
            "status": "ENABLED",
        }]
        loaded_4 = NegativeSnapshot.from_dict(tampered_4)
        self.assertEqual(loaded_4.status, "HOLD_REVIEW")
        self.assertIn("MANIFEST_HASH_TAMPER_DETECTED", loaded_4.hold_reason)

        # 5. Item removed
        tampered_5 = copy.deepcopy(snap_dict)
        tampered_5["items"] = list(tampered_5["items"])[:-1]  # Remove last item
        loaded_5 = NegativeSnapshot.from_dict(tampered_5)
        self.assertEqual(loaded_5.status, "HOLD_REVIEW")
        self.assertIn("MANIFEST_HASH_TAMPER_DETECTED", loaded_5.hold_reason)

        # 6. Clean roundtrip should NOT trigger tamper detection
        clean = NegativeSnapshot.from_dict(snap_dict)
        self.assertNotEqual(clean.status, "HOLD_REVIEW",
                            "Clean roundtrip should not trigger tamper detection")

    def test_26_protobuf_row_conversion(self):
        """Test 26: PROTOBUF_ROW_CONVERSION — GoogleAdsRow-like native protobuf conversion to nested dict."""
        if _V24_AVAILABLE and convert_proto_plus_to_protobuf is not None:
            row_pp = V24GoogleAdsRow(
                campaign=V24Campaign(id=1001, name="SCL-EXCEL-B2C-PRESENCIAL"),
                campaign_criterion=V24CampaignCriterion(
                    criterion_id=801,
                    type_=V24CriterionTypeEnum.CriterionType.KEYWORD,
                    keyword=V24KeywordInfo(text="curso excel gratis", match_type=V24KeywordMatchTypeEnum.KeywordMatchType.EXACT),
                    negative=True,
                    status="ENABLED",
                ),
            )
            row_native = convert_proto_plus_to_protobuf(row_pp)
            res = GoogleAdsLiveExecutor._protobuf_row_to_dict(row_native)
        else:
            class MockFieldDesc:
                def __init__(self, name):
                    self.name = name

            class MockMsgDesc:
                def __init__(self, field_names):
                    self.fields = [MockFieldDesc(n) for n in field_names]

            class MockNativeRow:
                def __init__(self):
                    self.campaign = {"id": "1001", "name": "SCL-EXCEL-B2C-PRESENCIAL"}
                    self.campaign_criterion = {
                        "criterion_id": "801",
                        "type": "KEYWORD",
                        "keyword": {"text": "curso excel gratis", "match_type": "EXACT"},
                        "negative": True,
                        "status": "ENABLED",
                    }
                    self.DESCRIPTOR = MockMsgDesc(["campaign", "campaign_criterion"])

                def ListFields(self):
                    return [
                        (MockFieldDesc("campaign"), self.campaign),
                        (MockFieldDesc("campaign_criterion"), self.campaign_criterion),
                    ]

            res = GoogleAdsLiveExecutor._protobuf_row_to_dict(MockNativeRow())

        self.assertIsInstance(res, dict)
        self.assertNotIn("_raw", res, "Operational fallback '_raw' must never be produced")
        self.assertIn("campaign", res)
        self.assertIn("campaign_criterion", res)
        self.assertIn("keyword", res)

        # Verify real nested structure
        self.assertEqual(str(res["campaign"]["id"]), "1001")
        self.assertEqual(res["campaign"]["name"], "SCL-EXCEL-B2C-PRESENCIAL")
        self.assertEqual(str(res["campaign_criterion"]["criterion_id"]), "801")
        self.assertEqual(res["campaign_criterion"]["type"], "KEYWORD")
        self.assertEqual(res["campaign_criterion"]["keyword"]["text"], "curso excel gratis")
        self.assertEqual(res["campaign_criterion"]["keyword"]["match_type"], "EXACT")
        self.assertEqual(res["keyword"]["text"], "curso excel gratis")
        self.assertEqual(res["keyword"]["match_type"], "EXACT")

    def test_27_proto_plus_row_conversion(self):
        """Test 27: PROTO_PLUS_ROW_CONVERSION — GoogleAdsRow-like proto-plus conversion to nested dict."""
        if _V24_AVAILABLE:
            row_pp = V24GoogleAdsRow(
                campaign=V24Campaign(id=1001, name="SCL-EXCEL-B2C-PRESENCIAL"),
                campaign_criterion=V24CampaignCriterion(
                    criterion_id=801,
                    type_=V24CriterionTypeEnum.CriterionType.KEYWORD,
                    keyword=V24KeywordInfo(text="curso excel gratis", match_type=V24KeywordMatchTypeEnum.KeywordMatchType.EXACT),
                    negative=True,
                    status="ENABLED",
                ),
            )
            res = GoogleAdsLiveExecutor._protobuf_row_to_dict(row_pp)
        else:
            class MockProtoPlusRow:
                def __init__(self):
                    class MockFieldDesc:
                        def __init__(self, name):
                            self.name = name

                    class MockMsgDesc:
                        def __init__(self, field_names):
                            self.fields = [MockFieldDesc(n) for n in field_names]

                    class MockNativeRow:
                        def __init__(self):
                            self.campaign = {"id": "1001", "name": "SCL-EXCEL-B2C-PRESENCIAL"}
                            self.campaign_criterion = {
                                "criterion_id": "801",
                                "type": "KEYWORD",
                                "keyword": {"text": "curso excel gratis", "match_type": "EXACT"},
                                "negative": True,
                                "status": "ENABLED",
                            }
                            self.DESCRIPTOR = MockMsgDesc(["campaign", "campaign_criterion"])

                        def ListFields(self):
                            return [
                                (MockFieldDesc("campaign"), self.campaign),
                                (MockFieldDesc("campaign_criterion"), self.campaign_criterion),
                            ]

                    self._pb = MockNativeRow()

            res = GoogleAdsLiveExecutor._protobuf_row_to_dict(MockProtoPlusRow())

        self.assertIsInstance(res, dict)
        self.assertNotIn("_raw", res, "Operational fallback '_raw' must never be produced")
        self.assertIn("campaign", res)
        self.assertIn("campaign_criterion", res)
        self.assertIn("keyword", res)

        # Real conversion validation
        self.assertEqual(str(res["campaign"]["id"]), "1001")
        self.assertEqual(res["campaign"]["name"], "SCL-EXCEL-B2C-PRESENCIAL")
        self.assertEqual(str(res["campaign_criterion"]["criterion_id"]), "801")
        self.assertEqual(res["campaign_criterion"]["type"], "KEYWORD")
        self.assertEqual(res["campaign_criterion"]["keyword"]["text"], "curso excel gratis")
        self.assertEqual(res["campaign_criterion"]["keyword"]["match_type"], "EXACT")
        self.assertEqual(res["keyword"]["text"], "curso excel gratis")
        self.assertEqual(res["keyword"]["match_type"], "EXACT")

    def test_28_row_conversion_consumed_by_adapter(self):
        """Test 28: ADAPTER_NESTED_STRUCTURE — Converted rows across all scopes consumed by adapter."""
        if not _V24_AVAILABLE:
            self.skipTest("google-ads-python v24 not available in environment")

        r_shared_set = V24GoogleAdsRow(
            shared_set=V24SharedSet(
                id=501,
                name="GLOBAL_ACC_NEGATIVES",
                type_=V24SharedSetTypeEnum.SharedSetType.ACCOUNT_LEVEL_NEGATIVE_KEYWORDS,
                status=V24SharedSetStatusEnum.SharedSetStatus.ENABLED,
            )
        )
        r_cust_crit = V24GoogleAdsRow(
            customer_negative_criterion=V24CustomerNegativeCriterion(
                id=601,
                type_=V24CriterionTypeEnum.CriterionType.NEGATIVE_KEYWORD_LIST,
                negative_keyword_list=V24NegativeKeywordListInfo(
                    shared_set="customers/123/sharedSets/501"
                ),
            )
        )
        r_shared_crit = V24GoogleAdsRow(
            shared_criterion=V24SharedCriterion(
                criterion_id=701,
                shared_set="customers/123/sharedSets/501",
                type_=V24CriterionTypeEnum.CriterionType.KEYWORD,
                keyword=V24KeywordInfo(text="gratis", match_type=V24KeywordMatchTypeEnum.KeywordMatchType.EXACT),
            )
        )
        r_camp_shared = V24GoogleAdsRow(
            campaign_shared_set=V24CampaignSharedSet(
                campaign="customers/123/campaigns/1001",
                shared_set="customers/123/sharedSets/501",
                status=V24CampaignSharedSetStatusEnum.CampaignSharedSetStatus.ENABLED,
            )
        )
        r_camp_crit = V24GoogleAdsRow(
            campaign=V24Campaign(id=1001, name="SCL-EXCEL-B2C-PRESENCIAL"),
            campaign_criterion=V24CampaignCriterion(
                criterion_id=801,
                type_=V24CriterionTypeEnum.CriterionType.KEYWORD,
                keyword=V24KeywordInfo(text="clases particulares", match_type=V24KeywordMatchTypeEnum.KeywordMatchType.PHRASE),
                negative=True,
            )
        )
        r_adg_crit = V24GoogleAdsRow(
            campaign=V24Campaign(id=1001, name="SCL-EXCEL-B2C-PRESENCIAL"),
            ad_group=V24AdGroup(id=2001, name="ADG_A_GENERAL"),
            ad_group_criterion=V24AdGroupCriterion(
                criterion_id=901,
                type_=V24CriterionTypeEnum.CriterionType.KEYWORD,
                keyword=V24KeywordInfo(text="desde cero", match_type=V24KeywordMatchTypeEnum.KeywordMatchType.EXACT),
                negative=True,
            )
        )

        def mock_gaql(cust_id: str, query: str):
            if "FROM shared_set" in query:
                return [GoogleAdsLiveExecutor._protobuf_row_to_dict(r_shared_set)]
            elif "customer_negative_criterion" in query:
                return [GoogleAdsLiveExecutor._protobuf_row_to_dict(r_cust_crit)]
            elif "FROM shared_criterion" in query:
                return [GoogleAdsLiveExecutor._protobuf_row_to_dict(r_shared_crit)]
            elif "campaign_shared_set" in query:
                return [GoogleAdsLiveExecutor._protobuf_row_to_dict(r_camp_shared)]
            elif "campaign_criterion" in query:
                return [GoogleAdsLiveExecutor._protobuf_row_to_dict(r_camp_crit)]
            elif "ad_group_criterion" in query:
                return [GoogleAdsLiveExecutor._protobuf_row_to_dict(r_adg_crit)]
            return []

        adapter = GoogleAdsNegativeReadAdapter(gaql_executor=mock_gaql)
        snap = adapter.build_snapshot(customer_id="1234567890", evidence_source="SIMULATED_PROTOBUF_STREAM")

        self.assertEqual(snap.status, "READY")
        self.assertEqual(len(snap.items), 3)

        # Customer/account-level item
        cust_items = [i for i in snap.items if i.source_scope == SourceScope.CUSTOMER]
        self.assertEqual(len(cust_items), 1)
        self.assertEqual(cust_items[0].keyword_text, "gratis")
        self.assertEqual(cust_items[0].match_type, MatchType.EXACT)
        self.assertEqual(cust_items[0].campaign_name, "GLOBAL")

        # Campaign item
        camp_items = [i for i in snap.items if i.source_scope == SourceScope.CAMPAIGN]
        self.assertEqual(len(camp_items), 1)
        self.assertEqual(camp_items[0].keyword_text, "clases particulares")
        self.assertEqual(camp_items[0].match_type, MatchType.PHRASE)
        self.assertEqual(camp_items[0].campaign_name, "SCL-EXCEL-B2C-PRESENCIAL")

        # Ad group item
        adg_items = [i for i in snap.items if i.source_scope == SourceScope.AD_GROUP]
        self.assertEqual(len(adg_items), 1)
        self.assertEqual(adg_items[0].keyword_text, "desde cero")
        self.assertEqual(adg_items[0].match_type, MatchType.EXACT)
        self.assertEqual(adg_items[0].campaign_name, "SCL-EXCEL-B2C-PRESENCIAL")
        self.assertEqual(adg_items[0].ad_group_name, "ADG_A_GENERAL")

    def test_29_unknown_row_fail_closed(self):
        """Test 29: UNKNOWN_ROW_FAIL_CLOSED — Unsupported row types fail closed with TypeError."""
        bad_inputs = [
            "SELECT * FROM campaign",
            12345,
            {"campaign": {"id": 1001}},
            None,
            [1, 2, 3],
            object(),
        ]
        for bad in bad_inputs:
            with self.subTest(bad_type=type(bad)):
                with self.assertRaises(TypeError) as ctx:
                    GoogleAdsLiveExecutor._protobuf_row_to_dict(bad)
                self.assertIn("ROW_CONVERSION_FAILED", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
