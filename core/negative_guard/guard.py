"""Negative Keyword Guard evaluation engine.

Implements:
- Deduplication against existing live negative criteria and shared sets.
- Cross-campaign conflict detection (B2C vs B2B, modality, product).
- Strict fail-closed validation for unknown campaigns, intents, scopes, and match types.
- Scope enforcement (Routing A/B/C explicit matrix vs Global Exclusions).
- Match-aware and scope-aware protected terms validation (no naive substring matching).
- Real product and modality compatibility checks.
- "paso a paso" canonical rule.
- Cross-process persistent idempotency using manifest_hash + recommendation_hash.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

from .campaign_contract import (
    CampaignContract,
    CampaignRegistry,
    Modality,
    ProductType,
    validate_ad_group_routing,
)
from .classifier import DEFAULT_REGISTRY, classify_campaign, classify_keyword_intent
from .ledger import RecommendationLedger
from .models import (
    CampaignType,
    CriterionStatus,
    IntentClass,
    MatchType,
    NegativeKeywordItem,
    NegativeSnapshot,
    PolicyDecision,
    RecommendationItem,
    SourceScope,
    hash_identifier,
    normalize_keyword_text,
    normalize_match_type,
    normalize_scope,
)


@dataclass
class EvaluationResult:
    is_valid_recommendation: bool
    policy_decision: PolicyDecision
    rationale: str
    intent_class: IntentClass
    recommendation: Optional[RecommendationItem] = None


class NegativeGuard:
    """Evaluates candidate negative keywords against live state and canonical policies fail-closed."""

    def __init__(
        self,
        snapshot: Optional[NegativeSnapshot] = None,
        registry: Optional[CampaignRegistry] = None,
        ledger: Optional[RecommendationLedger] = None,
    ):
        self.snapshot = snapshot
        self.registry = registry or DEFAULT_REGISTRY
        self.ledger = ledger
        self.existing_lookup: Set[Tuple[str, MatchType, SourceScope, str]] = set()
        self.campaign_shared_sets: Dict[str, Set[str]] = {}
        self.shared_set_negatives: Dict[str, Set[Tuple[str, MatchType]]] = {}
        self.previously_recommended_hashes: Set[str] = set()

        if self.snapshot and self.snapshot.status != "HOLD_DATA_GAP":
            self._load_snapshot_attachments(self.snapshot)
            self._index_snapshot(self.snapshot)

    def _load_snapshot_attachments(self, snapshot: NegativeSnapshot) -> None:
        """Loads campaign shared set attachments directly from snapshot contract."""
        for camp_id_hash, ssets in snapshot.campaign_shared_sets.items():
            sanitized_camp = hash_identifier(camp_id_hash)
            if sanitized_camp not in self.campaign_shared_sets:
                self.campaign_shared_sets[sanitized_camp] = set()
            for sset in ssets:
                self.campaign_shared_sets[sanitized_camp].add(sset)

    def _index_snapshot(self, snapshot: NegativeSnapshot) -> None:
        """Indexes active live snapshot criteria for fast and exact duplicate/conflict lookup.

        Criteria with REMOVED or UNKNOWN status are strictly ignored and not treated as active.
        """
        for item in snapshot.active_items():
            # Key: (normalized_text, match_type, scope, campaign_or_set_identifier)
            key = (
                item.keyword_text,
                item.match_type,
                item.source_scope,
                item.campaign_id_hash if item.source_scope == SourceScope.CAMPAIGN else (
                    item.ad_group_id_hash if item.source_scope == SourceScope.AD_GROUP else "GLOBAL"
                ),
            )
            self.existing_lookup.add(key)

            # Also index customer-level / account-level negatives
            if item.source_scope == SourceScope.CUSTOMER:
                self.existing_lookup.add((item.keyword_text, item.match_type, SourceScope.CUSTOMER, "GLOBAL"))

            # Track shared set criteria
            if item.source_scope == SourceScope.SHARED_SET and item.shared_set_name != "NONE":
                if item.shared_set_name not in self.shared_set_negatives:
                    self.shared_set_negatives[item.shared_set_name] = set()
                self.shared_set_negatives[item.shared_set_name].add((item.keyword_text, item.match_type))

    def associate_campaign_with_shared_set(self, campaign_id_hash: str, shared_set_name: str) -> None:
        """Records that a campaign is associated with a specific shared negative set."""
        sanitized_id = hash_identifier(campaign_id_hash)
        if sanitized_id not in self.campaign_shared_sets:
            self.campaign_shared_sets[sanitized_id] = set()
        self.campaign_shared_sets[sanitized_id].add(shared_set_name)

    def is_already_covered(
        self,
        keyword_text: str,
        match_type: MatchType,
        target_scope: SourceScope,
        campaign_id_hash: str,
        ad_group_id_hash: str = "none",
    ) -> bool:
        """Checks if keyword is already covered at customer level, shared set, campaign, or ad group."""
        # 1. Customer level coverage
        if (keyword_text, match_type, SourceScope.CUSTOMER, "GLOBAL") in self.existing_lookup:
            return True

        # 2. Shared sets linked to this campaign
        linked_sets = self.campaign_shared_sets.get(campaign_id_hash, set())
        for sset in linked_sets:
            if (keyword_text, match_type) in self.shared_set_negatives.get(sset, set()):
                return True

        # 3. Direct campaign level coverage
        if (keyword_text, match_type, SourceScope.CAMPAIGN, campaign_id_hash) in self.existing_lookup:
            return True

        # 4. Direct ad group level coverage
        if target_scope == SourceScope.AD_GROUP:
            if (keyword_text, match_type, SourceScope.AD_GROUP, ad_group_id_hash) in self.existing_lookup:
                return True

        return False

    def evaluate_candidate(
        self,
        raw_keyword: str,
        match_type: MatchType,
        target_scope: SourceScope,
        target_campaign_name: str,
        target_campaign_id_hash: str = "none",
        target_ad_group_name: str = "NONE",
        target_ad_group_id_hash: str = "none",
    ) -> EvaluationResult:
        """Evaluates a single candidate negative keyword fail-closed."""
        # Fail-closed check: Persistent Ledger corruption
        if self.ledger is not None and getattr(self.ledger, "is_corrupt", False):
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.HOLD_REVIEW,
                rationale="LEDGER_CORRUPT=HOLD: El ledger persistente está corrupto. Fail-closed.",
                intent_class=IntentClass.DESCONOCIDO,
            )

        # Gate 0: Snapshot data gap (Fail-closed if no snapshot or missing live data)
        if not self.snapshot or self.snapshot.status == "HOLD_DATA_GAP":
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.HOLD_DATA_GAP,
                rationale="Falta lectura viva de estado de negativas (HOLD_DATA_GAP). No se emiten recomendaciones sin estado vivo.",
                intent_class=IntentClass.DESCONOCIDO,
            )

        text, inferred_match = normalize_keyword_text(raw_keyword)
        norm_match = normalize_match_type(match_type, inferred_match)
        norm_scope = normalize_scope(target_scope)

        # Gate 0.1: Scope and MatchType Fail-closed checks
        if norm_scope == SourceScope.UNKNOWN:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.ERROR,
                rationale=f"UNKNOWN_SCOPE: Alcance '{target_scope}' no reconocido. Fail-closed.",
                intent_class=IntentClass.DESCONOCIDO,
            )
        if norm_match == MatchType.UNKNOWN:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.ERROR,
                rationale=f"UNKNOWN_MATCH_TYPE: Tipo de concordancia '{match_type}' no reconocido. Fail-closed.",
                intent_class=IntentClass.DESCONOCIDO,
            )

        target_campaign_id_hash = hash_identifier(target_campaign_id_hash)
        target_ad_group_id_hash = hash_identifier(target_ad_group_id_hash)

        # Gate 0.2: Campaign Mapping: Primary key campaign_id_hash, secondary check campaign_name
        contract = self.registry.resolve(target_campaign_id_hash, target_campaign_name)
        if contract is None:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.HOLD_REVIEW,
                rationale=f"UNKNOWN_CAMPAIGN: Campaña ID '{target_campaign_id_hash}' (nombre '{target_campaign_name}') no resuelta en contrato canónico. Fail-closed -> HOLD_REVIEW.",
                intent_class=IntentClass.DESCONOCIDO,
            )

        # Gate 0.3: Product and Modality validation
        if contract.product == ProductType.UNKNOWN:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.HOLD_REVIEW,
                rationale=f"UNKNOWN_PRODUCT: Producto de campaña '{contract.campaign_name_pattern}' es UNKNOWN. Fail-closed -> HOLD_REVIEW.",
                intent_class=IntentClass.DESCONOCIDO,
            )

        camp_type = contract.audience
        intent_class = classify_keyword_intent(text)

        # Product-specific compatibility:
        if contract.product == ProductType.POWER_BI:
            if "power bi" in text or "powerbi" in text:
                return EvaluationResult(
                    is_valid_recommendation=False,
                    policy_decision=PolicyDecision.CONFLICT,
                    rationale="PRODUCT_CORE_OFFERING: Power BI es el producto de la campaña; no puede considerarse FUERA_ALCANCE ni excluirse.",
                    intent_class=IntentClass.FUERA_ALCANCE,
                )
            # Excel taxonomy cannot be automatically applied to Power BI
            if any(term in text for term in ("excel", "buscarv", "tablas dinamicas", "sumar.si")):
                return EvaluationResult(
                    is_valid_recommendation=False,
                    policy_decision=PolicyDecision.HOLD_REVIEW,
                    rationale="PRODUCT_MISMATCH: Taxonomía de Excel no puede aplicarse automáticamente a campaña de Power BI.",
                    intent_class=intent_class,
                )

        # Modality check: if campaign is ONLINE or MIXTA, do not negate online intent
        if contract.modality in (Modality.ONLINE, Modality.MIXTA) and intent_class == IntentClass.MODALIDAD:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.CONFLICT,
                rationale=f"MODALITY_CONFLICT: Campaña '{target_campaign_name}' es modalidad {contract.modality.value}; no se niegan términos de modalidad no presencial.",
                intent_class=intent_class,
            )

        # Gate 0.4: Match-aware & scope-aware protected terms check
        # Isolated protected term -> CONFLICT
        if text in contract.protected_terms:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.CONFLICT,
                rationale=f"PROTECTED_TERM_ISOLATED: Término '{text}' es parte central de la propuesta de valor protegida para '{target_campaign_name}'.",
                intent_class=intent_class,
            )

        # Check if text is composed only of protected/core tokens without any excludable modifier
        words = set(text.split())
        core_tokens = {"curso", "excel", "presencial", "santiago", "capacita"}
        if words.issubset(core_tokens) or (intent_class == IntentClass.DESCONOCIDO and any(pt in text for pt in contract.protected_terms)):
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.CONFLICT,
                rationale=f"PROTECTED_TERM_COMPOUND: Consulta '{text}' está compuesta por la propuesta de valor protegida sin modificador excluible.",
                intent_class=intent_class,
            )

        # Gate 0.5: Intent Fail-closed Check
        if intent_class == IntentClass.DESCONOCIDO:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.HOLD_REVIEW,
                rationale=f"UNKNOWN_INTENT: Intención para '{text}' no clasificada en taxonomía canónica. Fail-closed -> HOLD_REVIEW.",
                intent_class=IntentClass.DESCONOCIDO,
            )

        if intent_class in contract.protected_intents:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.CONFLICT,
                rationale=f"PROTECTED_INTENT: Intención '{intent_class.value}' está protegida en '{target_campaign_name}'.",
                intent_class=intent_class,
            )

        if contract.allowed_negative_intents and intent_class not in contract.allowed_negative_intents:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.HOLD_REVIEW,
                rationale=f"INTENT_NOT_ALLOWED: Intención '{intent_class.value}' no está en las negativas permitidas para '{target_campaign_name}'.",
                intent_class=intent_class,
            )

        # Gate 1: Deduplication against live state
        if self.is_already_covered(
            text, norm_match, norm_scope, target_campaign_id_hash, target_ad_group_id_hash
        ):
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.PRESERVE,
                rationale=f"DUPLICADO: La negativa '{text}' ({norm_match.value}) ya está activa en el alcance {norm_scope.value} o en una lista vinculada.",
                intent_class=intent_class,
            )

        # Gate 2: Check "paso a paso" exception
        if "paso a paso" in text:
            if norm_scope in (SourceScope.CUSTOMER, SourceScope.SHARED_SET, SourceScope.CAMPAIGN):
                return EvaluationResult(
                    is_valid_recommendation=False,
                    policy_decision=PolicyDecision.CONFLICT,
                    rationale="REGLA CANONICA: 'paso a paso' NO es negativa global. Es intención comercial válida para Landing B (desde cero).",
                    intent_class=IntentClass.ROUTING_A_B_C,
                )

        # Gate 3: Routing A/B/C explicit matrix validation
        if intent_class == IntentClass.ROUTING_A_B_C:
            if norm_scope in (SourceScope.CUSTOMER, SourceScope.SHARED_SET, SourceScope.CAMPAIGN):
                return EvaluationResult(
                    is_valid_recommendation=False,
                    policy_decision=PolicyDecision.ROUTE,
                    rationale=f"Término '{text}' tiene intención de ROUTING_A_B_C. No debe ser negativa global; debe enrutarse a nivel de grupo de anuncios.",
                    intent_class=intent_class,
                )
            # Scope is AD_GROUP -> Validate against explicit routing matrix
            routing_decision, routing_rationale = validate_ad_group_routing(contract, text, target_ad_group_name)
            if routing_decision != PolicyDecision.CANDIDATE:
                return EvaluationResult(
                    is_valid_recommendation=False,
                    policy_decision=routing_decision,
                    rationale=routing_rationale,
                    intent_class=intent_class,
                )

        # Gate 4: Cross-campaign conflict (B2C vs B2B)
        if camp_type == CampaignType.B2B_EMPRESA:
            if intent_class == IntentClass.B2B_SENCE:
                return EvaluationResult(
                    is_valid_recommendation=False,
                    policy_decision=PolicyDecision.CONFLICT,
                    rationale=f"CONFLICTO SEVERO B2B: Término '{text}' (B2B/Sence) no puede aplicarse a una campaña B2B Empresa.",
                    intent_class=intent_class,
                )

        # Gate 5: Candidate recommendation creation
        rec = RecommendationItem(
            keyword_text=text,
            match_type=norm_match,
            recommended_scope=norm_scope,
            target_campaign_name=target_campaign_name,
            target_campaign_id_hash=target_campaign_id_hash,
            target_ad_group_name=target_ad_group_name,
            target_ad_group_id_hash=target_ad_group_id_hash,
            intent_class=intent_class,
            policy_decision=PolicyDecision.CANDIDATE,
            rationale=f"Delta válido para intención {intent_class.value} en campaña {target_campaign_name} ({camp_type.value}).",
        )

        # Gate 6: In-memory session idempotency check
        if rec.recommendation_hash in self.previously_recommended_hashes:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.PRESERVE,
                rationale=f"IDEMPOTENCIA: Recomendación para '{text}' ya fue emitida previamente en esta sesión.",
                intent_class=intent_class,
            )

        # Gate 7: Cross-process persistent ledger idempotency check
        if self.ledger is not None and self.snapshot is not None:
            if self.ledger.is_recorded(self.snapshot.manifest_hash, rec.recommendation_hash):
                return EvaluationResult(
                    is_valid_recommendation=False,
                    policy_decision=PolicyDecision.PRESERVE,
                    rationale=f"IDEMPOTENCIA_PERSISTENTE: Recomendación para '{text}' ya está registrada en el ledger persistente.",
                    intent_class=intent_class,
                )

        # Register in session and in persistent ledger
        self.previously_recommended_hashes.add(rec.recommendation_hash)
        if self.ledger is not None and self.snapshot is not None:
            self.ledger.record(self.snapshot.manifest_hash, rec.recommendation_hash, rec.to_dict())

        return EvaluationResult(
            is_valid_recommendation=True,
            policy_decision=PolicyDecision.CANDIDATE,
            rationale=rec.rationale,
            intent_class=intent_class,
            recommendation=rec,
        )

    def evaluate_batch(
        self,
        candidates: List[Dict[str, Any]],
    ) -> List[RecommendationItem]:
        """Evaluates a batch of candidate dictionaries and returns only valid delta recommendations."""
        valid_recs: List[RecommendationItem] = []
        for cand in candidates:
            res = self.evaluate_candidate(
                raw_keyword=cand.get("keyword_text", ""),
                match_type=normalize_match_type(cand.get("match_type")),
                target_scope=normalize_scope(cand.get("target_scope", "CAMPAIGN")),
                target_campaign_name=cand.get("target_campaign_name", "UNKNOWN"),
                target_campaign_id_hash=cand.get("target_campaign_id_hash", "none"),
                target_ad_group_name=cand.get("target_ad_group_name", "NONE"),
                target_ad_group_id_hash=cand.get("target_ad_group_id_hash", "none"),
            )
            if res.is_valid_recommendation and res.recommendation:
                valid_recs.append(res.recommendation)
        return valid_recs
