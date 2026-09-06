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
    UNKNOWN = "UNKNOWN"


class MatchType(str, enum.Enum):
    EXACT = "EXACT"
    PHRASE = "PHRASE"
    BROAD = "BROAD"
    UNKNOWN = "UNKNOWN"


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
    HOLD_REVIEW = "HOLD_REVIEW"
    ERROR = "ERROR"


class CriterionStatus(str, enum.Enum):
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
    REMOVED = "REMOVED"
    UNKNOWN = "UNKNOWN"


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


def strip_accents(text: str) -> str:
    """Removes diacritical marks (accents) from text."""
    import unicodedata
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def normalize_keyword_text(raw_text: str) -> tuple[str, Optional[MatchType]]:
    """Normalizes keyword text: strips punctuation/brackets/quotes, removes diacritics, collapses whitespace.

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

    # Strip accents and lower
    cleaned = strip_accents(cleaned)
    # Lowercase, normalize spaces
    cleaned = re.sub(r"\s+", " ", cleaned).lower().strip()
    return cleaned, inferred_match


def normalize_match_type(raw_match_type: Any, inferred: Optional[MatchType] = None) -> MatchType:
    """Normalizes match type into standard EXACT, PHRASE, BROAD, or UNKNOWN."""
    if inferred and inferred != MatchType.UNKNOWN:
        return inferred
    if not raw_match_type:
        return MatchType.UNKNOWN

    val = str(raw_match_type).strip().upper()
    if "EXACT" in val:
        return MatchType.EXACT
    if "PHRASE" in val:
        return MatchType.PHRASE
    if "BROAD" in val:
        return MatchType.BROAD
    return MatchType.UNKNOWN


def normalize_scope(raw_scope: Any) -> SourceScope:
    """Normalizes scope into CUSTOMER, SHARED_SET, CAMPAIGN, AD_GROUP, or UNKNOWN."""
    if not raw_scope:
        return SourceScope.UNKNOWN
    val = str(raw_scope).strip().upper()
    if "SHARED" in val or "SET" in val or "LIST" in val:
        return SourceScope.SHARED_SET
    if "AD_GROUP" in val or "ADGROUP" in val or "GRUPO" in val:
        return SourceScope.AD_GROUP
    if "CAMPAIGN" in val or "CAMPANA" in val:
        return SourceScope.CAMPAIGN
    if "CUSTOMER" in val or "ACCOUNT" in val or "CUENTA" in val:
        return SourceScope.CUSTOMER
    return SourceScope.UNKNOWN


def normalize_criterion_status(raw_status: Any) -> CriterionStatus:
    """Normalizes criterion status into ENABLED, PAUSED, REMOVED, UNKNOWN."""
    if not raw_status:
        return CriterionStatus.UNKNOWN
    val = str(raw_status).strip().upper()
    if "ENABLED" in val or "ACTIVE" in val:
        return CriterionStatus.ENABLED
    if "PAUSED" in val:
        return CriterionStatus.PAUSED
    if "REMOVED" in val or "DELETED" in val:
        return CriterionStatus.REMOVED
    return CriterionStatus.UNKNOWN


ALLOWED_EVIDENCE_SOURCES = {
    "FIXTURE",
    "HISTORICAL_EXPORT",
    "LIVE_API_HOLD",
    "LIVE_API_READ",
    "SIMULATED_API",
    "MOCK_OFFICIAL_RESPONSE",
}


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
    status: CriterionStatus = CriterionStatus.ENABLED
    intent_class: IntentClass = IntentClass.DESCONOCIDO
    policy_decision: PolicyDecision = PolicyDecision.PRESERVE
    evidence_source: str = "FIXTURE"
    state_hash: str = ""

    def __post_init__(self):
        cleaned, inferred_match = normalize_keyword_text(self.keyword_text)
        self.keyword_text = cleaned
        self.match_type = normalize_match_type(self.match_type, inferred_match)
        self.source_scope = normalize_scope(self.source_scope)
        if isinstance(self.status, str):
            self.status = normalize_criterion_status(self.status)
        if isinstance(self.intent_class, str):
            try:
                self.intent_class = IntentClass(self.intent_class)
            except ValueError:
                self.intent_class = IntentClass.DESCONOCIDO
        if isinstance(self.policy_decision, str):
            try:
                self.policy_decision = PolicyDecision(self.policy_decision)
            except ValueError:
                self.policy_decision = PolicyDecision.PRESERVE
        self.campaign_id_hash = hash_identifier(self.campaign_id_hash)
        self.ad_group_id_hash = hash_identifier(self.ad_group_id_hash)
        self.customer_id_hash = hash_identifier(self.customer_id_hash)
        if not self.state_hash:
            self.state_hash = self.compute_state_hash()

    def compute_state_hash(self) -> str:
        payload = (
            f"{self.customer_id_hash}|{self.campaign_id_hash}|{self.ad_group_id_hash}|"
            f"{self.source_scope.value}|{self.shared_set_name}|{self.keyword_text}|"
            f"{self.match_type.value}|{self.status.value}"
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["source_scope"] = self.source_scope.value
        d["match_type"] = self.match_type.value
        d["intent_class"] = self.intent_class.value
        d["policy_decision"] = self.policy_decision.value
        d["status"] = self.status.value
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
            status=normalize_criterion_status(data.get("status", "ENABLED")),
            intent_class=IntentClass(data.get("intent_class", IntentClass.DESCONOCIDO.value)) if data.get("intent_class") in IntentClass._value2member_map_ else IntentClass.DESCONOCIDO,
            policy_decision=PolicyDecision(data.get("policy_decision", PolicyDecision.PRESERVE.value)) if data.get("policy_decision") in PolicyDecision._value2member_map_ else PolicyDecision.PRESERVE,
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
        if isinstance(self.intent_class, str):
            self.intent_class = IntentClass(self.intent_class)
        if isinstance(self.policy_decision, str):
            self.policy_decision = PolicyDecision(self.policy_decision)
        if isinstance(self.recommended_scope, str):
            self.recommended_scope = normalize_scope(self.recommended_scope)
        self.target_campaign_id_hash = hash_identifier(self.target_campaign_id_hash)
        self.target_ad_group_id_hash = hash_identifier(self.target_ad_group_id_hash)
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
    schema_version: str = "1.1.0"
    snapshot_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    customer_id_hash: str = "none"
    items: List[NegativeKeywordItem] = field(default_factory=list)
    campaign_shared_sets: Dict[str, List[str]] = field(default_factory=dict)
    evidence_source: str = "FIXTURE"
    status: str = "READY"
    hold_reason: Optional[str] = None
    manifest_hash: str = ""

    def __post_init__(self):
        self.customer_id_hash = hash_identifier(self.customer_id_hash)
        if self.evidence_source not in ALLOWED_EVIDENCE_SOURCES:
            self.evidence_source = "FIXTURE"
        # Always recompute manifest_hash deterministically
        self.manifest_hash = self.compute_manifest_hash()

    def active_items(self) -> List[NegativeKeywordItem]:
        """Returns only active negative criteria, excluding REMOVED or UNKNOWN status."""
        return [
            item for item in self.items
            if item.status not in (CriterionStatus.REMOVED, CriterionStatus.UNKNOWN)
        ]

    def compute_manifest_hash(self) -> str:
        items_payload = ",".join(sorted(i.state_hash for i in self.items))
        # Deterministic sorting of campaign shared sets
        attachments_list = []
        for camp_id, ssets in sorted(self.campaign_shared_sets.items()):
            sanitized_camp = hash_identifier(camp_id)
            sorted_sets = ",".join(sorted(ssets))
            attachments_list.append(f"{sanitized_camp}=[{sorted_sets}]")
        attachments_payload = ";".join(attachments_list)
        raw_manifest = (
            f"{self.schema_version}:{self.customer_id_hash}:{items_payload}:"
            f"{attachments_payload}:{self.status}:{self.hold_reason or ''}"
        )
        return hashlib.sha256(raw_manifest.encode("utf-8")).hexdigest()[:16]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "snapshot_at": self.snapshot_at,
            "customer_id_hash": self.customer_id_hash,
            "evidence_source": self.evidence_source,
            "status": self.status,
            "hold_reason": self.hold_reason,
            "manifest_hash": self.manifest_hash,
            "campaign_shared_sets": {
                hash_identifier(k): sorted(v) for k, v in self.campaign_shared_sets.items()
            },
            "items_count": len(self.items),
            "active_items_count": len(self.active_items()),
            "items": [i.to_dict() for i in self.items],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> NegativeSnapshot:
        items = [NegativeKeywordItem.from_dict(d) for d in data.get("items", [])]
        raw_attachments = data.get("campaign_shared_sets", {})
        attachments: Dict[str, List[str]] = {}
        for k, v in raw_attachments.items():
            attachments[hash_identifier(k)] = list(v) if isinstance(v, list) else [str(v)]

        ev_source = data.get("evidence_source", "FIXTURE")
        if ev_source not in ALLOWED_EVIDENCE_SOURCES:
            ev_source = "FIXTURE"

        snap = cls(
            schema_version=data.get("schema_version", "1.1.0"),
            snapshot_at=data.get("snapshot_at", datetime.now(timezone.utc).isoformat()),
            customer_id_hash=hash_identifier(data.get("customer_id_hash", "none")),
            items=items,
            campaign_shared_sets=attachments,
            evidence_source=ev_source,
            status=data.get("status", "READY"),
            hold_reason=data.get("hold_reason"),
        )
        return snap
