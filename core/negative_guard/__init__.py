"""Core Negative Keyword Guard package for Capacita Marketing Performance.

Implements the negative keyword intent policy, live snapshot contract,
campaign contracts, conflict detection (B2C vs B2B, routing A/B/C, paso a paso exception),
deduplication, delta calculation, persistent cross-process idempotency, and live read adapter.
"""

from .adapter import GoogleAdsNegativeReadAdapter
from .campaign_contract import CampaignContract, CampaignRegistry, Modality, ProductType
from .classifier import classify_campaign, classify_keyword_intent
from .guard import EvaluationResult, NegativeGuard
from .ledger import ClaimResult, RecommendationLedger
from .live_executor import GoogleAdsLiveExecutor
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
    normalize_criterion_status,
    normalize_keyword_text,
    normalize_match_type,
    normalize_scope,
    strip_accents,
)
from .snapshot import NegativeSnapshotManager

__all__ = [
    "GoogleAdsNegativeReadAdapter",
    "CampaignContract",
    "CampaignRegistry",
    "Modality",
    "ProductType",
    "CampaignType",
    "CriterionStatus",
    "IntentClass",
    "MatchType",
    "NegativeKeywordItem",
    "NegativeSnapshot",
    "PolicyDecision",
    "RecommendationItem",
    "SourceScope",
    "hash_identifier",
    "normalize_criterion_status",
    "normalize_keyword_text",
    "normalize_match_type",
    "normalize_scope",
    "strip_accents",
    "classify_campaign",
    "classify_keyword_intent",
    "EvaluationResult",
    "NegativeGuard",
    "ClaimResult",
    "RecommendationLedger",
    "GoogleAdsLiveExecutor",
    "NegativeSnapshotManager",
]
