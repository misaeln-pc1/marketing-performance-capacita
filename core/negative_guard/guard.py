"""Negative Keyword Guard evaluation engine.

Implements:
- Deduplication against existing live negative criteria and shared sets.
- Cross-campaign conflict detection (B2C vs B2B).
- Scope enforcement (Routing A/B/C vs Global Exclusions).
- "paso a paso" global exclusion prohibition.
- Strict idempotency (second run yields zero duplicate recommendations).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

from .classifier import classify_campaign, classify_keyword_intent
from .models import (
    CampaignType,
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
    """Evaluates candidate negative keywords against live state and canonical policies."""

    def __init__(self, snapshot: Optional[NegativeSnapshot] = None):
        self.snapshot = snapshot
        self.existing_lookup: Set[Tuple[str, MatchType, SourceScope, str]] = set()
        self.campaign_shared_sets: Dict[str, Set[str]] = {}
        self.shared_set_negatives: Dict[str, Set[Tuple[str, MatchType]]] = {}
        self.previously_recommended_hashes: Set[str] = set()

        if self.snapshot and self.snapshot.status != "HOLD_DATA_GAP":
            self._index_snapshot(self.snapshot)

    def _index_snapshot(self, snapshot: NegativeSnapshot) -> None:
        """Indexes live snapshot criteria for fast and exact duplicate/conflict lookup."""
        for item in snapshot.items:
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

            # Track shared set associations
            if item.source_scope == SourceScope.SHARED_SET and item.shared_set_name != "NONE":
                if item.shared_set_name not in self.shared_set_negatives:
                    self.shared_set_negatives[item.shared_set_name] = set()
                self.shared_set_negatives[item.shared_set_name].add((item.keyword_text, item.match_type))

    def associate_campaign_with_shared_set(self, campaign_id_hash: str, shared_set_name: str) -> None:
        """Records that a campaign is associated with a specific shared negative set."""
        if campaign_id_hash not in self.campaign_shared_sets:
            self.campaign_shared_sets[campaign_id_hash] = set()
        self.campaign_shared_sets[campaign_id_hash].add(shared_set_name)

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
        """Evaluates a single candidate negative keyword and returns an EvaluationResult."""
        # Gate 0: Snapshot data gap
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
        camp_type = classify_campaign(target_campaign_name)
        intent_class = classify_keyword_intent(text)

        target_campaign_id_hash = hash_identifier(target_campaign_id_hash)
        target_ad_group_id_hash = hash_identifier(target_ad_group_id_hash)

        # Gate 1: Deduplication against live state (if already present, preserve it and do not recommend duplicate)
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

        # Gate 3: Routing A/B/C cannot be global exclusions
        if intent_class == IntentClass.ROUTING_A_B_C:
            if norm_scope in (SourceScope.CUSTOMER, SourceScope.SHARED_SET, SourceScope.CAMPAIGN):
                return EvaluationResult(
                    is_valid_recommendation=False,
                    policy_decision=PolicyDecision.ROUTE,
                    rationale=f"Término '{text}' tiene intención de ROUTING_A_B_C. No debe ser negativa global; debe enrutarse a nivel de grupo de anuncios.",
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
        elif camp_type == CampaignType.B2C:
            # If a candidate keyword attempts to negate the core presencial or santiago offering
            core_protected_terms = {"presencial", "santiago", "curso", "capacita", "curso presencial", "curso presencial santiago"}
            if text in core_protected_terms:
                return EvaluationResult(
                    is_valid_recommendation=False,
                    policy_decision=PolicyDecision.CONFLICT,
                    rationale=f"CONFLICTO B2C: Término '{text}' bloquea la propuesta de valor o producto central de la campaña B2C.",
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

        # Gate 6: Idempotency check against previously emitted recommendations
        if rec.recommendation_hash in self.previously_recommended_hashes:
            return EvaluationResult(
                is_valid_recommendation=False,
                policy_decision=PolicyDecision.PRESERVE,
                rationale=f"IDEMPOTENCIA: Recomendación para '{text}' ya fue emitida previamente en esta sesión/snapshot.",
                intent_class=intent_class,
            )

        self.previously_recommended_hashes.add(rec.recommendation_hash)

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
