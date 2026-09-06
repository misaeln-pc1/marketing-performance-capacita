"""Data models, enums, and normalization utilities for Negative Keyword Guard."""

from __future__ import annotations

import enum
import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


class SourceScope(str, enum.Enum):
    CUSTOMER = "CUSTOMER"
    SHARED_SET = "SHARED_SET"
    CAMPAIGN = "CAMPAIGN"
    AD_GROUP = "AD_GROUP"


class MatchType(str, enum.Enum):
    EXACT = "EXACT"
    PHRASE = "PHRASE"
    BROAD = "BROAD"


class CampaignType(str, enum.Enum):
    B2C = "B2C"
    B2B_EMPRESA = "B2B_EMPRESA"
    UNKNOWN = "UNKNOWN"


class IntentClass(str, enum.Enum):
    SOLUCION_PUNTUAL = "SOLUCION_PUNTUAL"
    EMPLEO = "EMPLEO"
    MODALIDAD = "MODALIDAD"
    B2B_SENCE = "B2B_SENCE"
    CLASES_PARTICULARES = "CLASES_PARTICULARES"
    FUERA_ALCANCE = "FUERA_ALCANCE"
    ROUTING_A_B_C = "ROUTING_A_B_C"
    DESCONOCIDO = "DESCONOCIDO"


class PolicyDecision(str, enum.Enum):
    PRESERVE = "PRESERVE"
    REVIEW = "REVIEW"
    ROUTE = "ROUTE"
    CONFLICT = "CONFLICT"
    CANDIDATE = "CANDIDATE"
    EXCLUDE = "EXCLUDE"
    HOLD_DATA_GAP = "HOLD_DATA_GAP"


def hash_identifier(raw_id: Optional[str], salt: str = "capacita_safe") -> str:
    """Returns a deterministic, sanitized 12-char SHA-256 hex hash.

    Never prints or stores the original raw identifier.
    """
    if not raw_id:
        return "none"
    # If already a hash or masked, preserve sanitization
    if str(raw_id).startswith("hash_") or "***" in str(raw_id):
        return str(raw_id)
    raw_str = str(raw_id).strip()
    h = hashlib.sha256(f"{salt}:{raw_str}".encode("utf-8")).hexdigest()[:12]
    return f"hash_{h}"


def normalize_keyword_text(raw_text: str) -> tuple[str, Optional[MatchType]]:
    """Normalizes keyword text, strips punctuation/brackets/quotes, collapses whitespace.

    Returns (cleaned_text, inferred_match_type_or_none).
    """
    if not raw_text:
        return "", None

    cleaned = raw_text.strip()
    inferred_match: Optional[MatchType] = None

    # Exact match in bracket notation: [keyword]
    if cleaned.startswith("[") and cleaned.endswith("]"):
        cleaned = cleaned[1:-1].strip()
        inferred_match = MatchType.EXACT
    # Phrase match in quote notation: "keyword"
    elif cleaned.startswith('"') and cleaned.endswith('"'):
        cleaned = cleaned[1:-1].strip()
        inferred_match = MatchType.PHRASE

    # Lowercase, normalize spaces
    cleaned = re.sub(r"\s+", " ", cleaned).lower().strip()
    return cleaned, inferred_match


def normalize_match_type(raw_match_type: Any, inferred: Optional[MatchType] = None) -> MatchType:
    """Normalizes match type into standard EXACT, PHRASE, BROAD."""
    if inferred:
        return inferred
    if not raw_match_type:
        return MatchType.BROAD

    val = str(raw_match_type).strip().upper()
    if "EXACT" in val:
        return MatchType.EXACT
    if "PHRASE" in val:
        return MatchType.PHRASE
    if "BROAD" in val:
        return MatchType.BROAD
    return MatchType.BROAD


def normalize_scope(raw_scope: Any) -> SourceScope:
    """Normalizes scope into CUSTOMER, SHARED_SET, CAMPAIGN, AD_GROUP."""
    val = str(raw_scope).strip().upper()
    if "SHARED" in val or "SET" in val or "LIST" in val:
        return SourceScope.SHARED_SET
    if "AD_GROUP" in val or "ADGROUP" in val or "GRUPO" in val:
        return SourceScope.AD_GROUP
    if "CAMPAIGN" in val or "CAMPANA" in val:
        return SourceScope.CAMPAIGN
    if "CUSTOMER" in val or "ACCOUNT" in val or "CUENTA" in val:
        return SourceScope.CUSTOMER
    return SourceScope.CAMPAIGN


@dataclass
class NegativeKeywordItem:
    """Standardized representation of a single negative keyword criterion."""
    keyword_text: str
    match_type: MatchType
    source_scope: SourceScope
    campaign_name: str = "GLOBAL"
    campaign_id_hash: str = "none"
    ad_group_name: str = "NONE"
    ad_group_id_hash: str = "none"
    shared_set_name: str = "NONE"
    customer_id_hash: str = "none"
    status: str = "ENABLED"
    intent_class: IntentClass = IntentClass.DESCONOCIDO
    policy_decision: PolicyDecision = PolicyDecision.PRESERVE
    evidence_source: str = "FIXTURE"
    state_hash: str = ""

    def __post_init__(self):
        cleaned, inferred_match = normalize_keyword_text(self.keyword_text)
        self.keyword_text = cleaned
        self.match_type = normalize_match_type(self.match_type, inferred_match)
        self.source_scope = normalize_scope(self.source_scope)
        if not self.state_hash:
            self.state_hash = self.compute_state_hash()

    def compute_state_hash(self) -> str:
        payload = (
            f"{self.customer_id_hash}|{self.campaign_id_hash}|{self.ad_group_id_hash}|"
            f"{self.source_scope.value}|{self.shared_set_name}|{self.keyword_text}|"
            f"{self.match_type.value}|{self.status}"
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["source_scope"] = self.source_scope.value
        d["match_type"] = self.match_type.value
        d["intent_class"] = self.intent_class.value
        d["policy_decision"] = self.policy_decision.value
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> NegativeKeywordItem:
        return cls(
            keyword_text=data.get("keyword_text", ""),
            match_type=normalize_match_type(data.get("match_type")),
            source_scope=normalize_scope(data.get("source_scope", "CAMPAIGN")),
            campaign_name=data.get("campaign_name", "GLOBAL"),
            campaign_id_hash=hash_identifier(data.get("campaign_id_hash") or data.get("campaign_id")),
            ad_group_name=data.get("ad_group_name", "NONE"),
            ad_group_id_hash=hash_identifier(data.get("ad_group_id_hash") or data.get("ad_group_id")),
            shared_set_name=data.get("shared_set_name", "NONE"),
            customer_id_hash=hash_identifier(data.get("customer_id_hash") or data.get("customer_id")),
            status=data.get("status", "ENABLED"),
            intent_class=IntentClass(data.get("intent_class", IntentClass.DESCONOCIDO.value)),
            policy_decision=PolicyDecision(data.get("policy_decision", PolicyDecision.PRESERVE.value)),
            evidence_source=data.get("evidence_source", "FIXTURE"),
            state_hash=data.get("state_hash", ""),
        )


@dataclass
class RecommendationItem:
    """A recommended negative keyword action or delta."""
    keyword_text: str
    match_type: MatchType
    recommended_scope: SourceScope
    target_campaign_name: str
    target_campaign_id_hash: str
    target_ad_group_name: str
    target_ad_group_id_hash: str
    intent_class: IntentClass
    policy_decision: PolicyDecision
    rationale: str
    recommendation_hash: str = ""

    def __post_init__(self):
        cleaned, inferred = normalize_keyword_text(self.keyword_text)
        self.keyword_text = cleaned
        self.match_type = normalize_match_type(self.match_type, inferred)
        if not self.recommendation_hash:
            self.recommendation_hash = self.compute_hash()

    def compute_hash(self) -> str:
        payload = (
            f"{self.keyword_text}|{self.match_type.value}|{self.recommended_scope.value}|"
            f"{self.target_campaign_id_hash}|{self.target_ad_group_id_hash}|"
            f"{self.intent_class.value}|{self.policy_decision.value}"
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["match_type"] = self.match_type.value
        d["recommended_scope"] = self.recommended_scope.value
        d["intent_class"] = self.intent_class.value
        d["policy_decision"] = self.policy_decision.value
        return d


@dataclass
class NegativeSnapshot:
    """Complete snapshot of negative keywords for an account or audit run."""
    snapshot_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    customer_id_hash: str = "none"
    items: List[NegativeKeywordItem] = field(default_factory=list)
    evidence_source: str = "FIXTURE"
    status: str = "READY"
    manifest_hash: str = ""

    def __post_init__(self):
        if not self.manifest_hash:
            self.manifest_hash = self.compute_manifest_hash()

    def compute_manifest_hash(self) -> str:
        items_payload = ",".join(sorted(i.state_hash for i in self.items))
        return hashlib.sha256(f"{self.customer_id_hash}:{items_payload}".encode("utf-8")).hexdigest()[:16]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "snapshot_at": self.snapshot_at,
            "customer_id_hash": self.customer_id_hash,
            "evidence_source": self.evidence_source,
            "status": self.status,
            "manifest_hash": self.manifest_hash,
            "items_count": len(self.items),
            "items": [i.to_dict() for i in self.items],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> NegativeSnapshot:
        items = [NegativeKeywordItem.from_dict(d) for d in data.get("items", [])]
        return cls(
            snapshot_at=data.get("snapshot_at", datetime.now(timezone.utc).isoformat()),
            customer_id_hash=data.get("customer_id_hash", "none"),
            items=items,
            evidence_source=data.get("evidence_source", "FIXTURE"),
            status=data.get("status", "READY"),
            manifest_hash=data.get("manifest_hash", ""),
        )
