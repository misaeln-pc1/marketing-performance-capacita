"""Core Negative Keyword Guard package for Capacita Marketing Performance.

Implements the negative keyword intent policy, live snapshot contract,
conflict detection (B2C vs B2B, routing A/B/C, paso a paso exception),
deduplication, delta calculation, and idempotent recommendation engine.
"""

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
from .classifier import classify_campaign, classify_keyword_intent
from .guard import NegativeGuard
from .snapshot import NegativeSnapshotManager

__all__ = [
    "CampaignType",
    "IntentClass",
    "MatchType",
    "NegativeKeywordItem",
    "NegativeSnapshot",
    "PolicyDecision",
    "RecommendationItem",
    "SourceScope",
    "hash_identifier",
    "normalize_keyword_text",
    "normalize_match_type",
    "normalize_scope",
    "classify_campaign",
    "classify_keyword_intent",
    "NegativeGuard",
    "NegativeSnapshotManager",
]
