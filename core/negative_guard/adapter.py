"""Live read adapter for Google Ads negative keyword criteria across all scopes."""

from __future__ import annotations

import logging
from typing import Any, Callable, Dict, List, Optional

from .models import (
    CriterionStatus,
    IntentClass,
    MatchType,
    NegativeKeywordItem,
    NegativeSnapshot,
    PolicyDecision,
    SourceScope,
    hash_identifier,
    normalize_criterion_status,
    normalize_keyword_text,
    normalize_match_type,
)
from .snapshot import NegativeSnapshotManager

logger = logging.getLogger(__name__)


# Official GAQL query templates for Google Ads Negative Keyword Retrieval
GAQL_CUSTOMER_NEGATIVES = """
SELECT
    customer_negative_criterion.criterion_id,
    customer_negative_criterion.keyword.text,
    customer_negative_criterion.keyword.match_type,
    customer_negative_criterion.status
FROM customer_negative_criterion
"""

GAQL_SHARED_SETS = """
SELECT
    shared_set.id,
    shared_set.name,
    shared_set.type,
    shared_set.status
FROM shared_set
WHERE shared_set.type = 'NEGATIVE_KEYWORDS'
"""

GAQL_SHARED_CRITERIA = """
SELECT
    shared_criterion.criterion_id,
    shared_criterion.shared_set,
    shared_criterion.keyword.text,
    shared_criterion.keyword.match_type
FROM shared_criterion
"""

GAQL_CAMPAIGN_SHARED_SETS = """
SELECT
    campaign_shared_set.campaign,
    campaign_shared_set.shared_set,
    campaign_shared_set.status
FROM campaign_shared_set
"""

GAQL_CAMPAIGN_NEGATIVES = """
SELECT
    campaign.id,
    campaign.name,
    campaign_criterion.criterion_id,
    campaign_criterion.keyword.text,
    campaign_criterion.keyword.match_type,
    campaign_criterion.negative,
    campaign_criterion.status
FROM campaign_criterion
WHERE campaign_criterion.negative = TRUE
"""

GAQL_AD_GROUP_NEGATIVES = """
SELECT
    campaign.id,
    campaign.name,
    ad_group.id,
    ad_group.name,
    ad_group_criterion.criterion_id,
    ad_group_criterion.keyword.text,
    ad_group_criterion.keyword.match_type,
    ad_group_criterion.negative,
    ad_group_criterion.status
FROM ad_group_criterion
WHERE ad_group_criterion.negative = TRUE
"""


class GoogleAdsNegativeReadAdapter:
    """Standardized READ-only adapter for extracting and sanitizing negative keyword criteria."""

    def __init__(
        self,
        gaql_executor: Optional[Callable[[str, str], List[Dict[str, Any]]]] = None,
        auth_provider: Optional[Callable[[], bool]] = None,
    ):
        """
        gaql_executor: Callable accepting (customer_id: str, query: str) -> List[Dict[str, Any]].
                       Can be a live Google Ads SearchStream caller or simulated mock.
        auth_provider: Optional check returning True if credentials with necessary scope are valid.
        """
        self.gaql_executor = gaql_executor
        self.auth_provider = auth_provider

    def is_live_execution_ready(self) -> bool:
        if self.gaql_executor is None:
            return False
        if self.auth_provider is not None:
            return self.auth_provider()
        return True

    def build_snapshot(
        self,
        customer_id: str,
        evidence_source: str = "LIVE_API_READ",
    ) -> NegativeSnapshot:
        """Builds a full NegativeSnapshot across all 6 Google Ads negative criteria entities.

        If live execution is unavailable or raises an auth/connection error, fails closed
        by returning a HOLD_DATA_GAP snapshot with an explicit hold reason.
        """
        if not self.is_live_execution_ready():
            return NegativeSnapshotManager.create_hold_data_gap_snapshot(
                reason="ACCESS_TOKEN_SCOPE_INSUFFICIENT: Live Google Ads read adapter requires OAuth adwords scope."
            )

        sanitized_cust = hash_identifier(customer_id)
        all_items: List[NegativeKeywordItem] = []
        campaign_shared_sets: Dict[str, List[str]] = {}

        try:
            # 1. Customer Negative Criteria
            cust_rows = self.gaql_executor(customer_id, GAQL_CUSTOMER_NEGATIVES)
            for row in cust_rows:
                status = normalize_criterion_status(row.get("status", "ENABLED"))
                if status in (CriterionStatus.REMOVED, CriterionStatus.UNKNOWN):
                    continue
                kw_text = row.get("keyword_text") or (row.get("keyword") or {}).get("text", "")
                match_type = row.get("match_type") or (row.get("keyword") or {}).get("match_type", "BROAD")
                item = NegativeKeywordItem(
                    keyword_text=kw_text,
                    match_type=normalize_match_type(match_type),
                    source_scope=SourceScope.CUSTOMER,
                    campaign_name="GLOBAL",
                    campaign_id_hash="none",
                    ad_group_name="NONE",
                    ad_group_id_hash="none",
                    shared_set_name="NONE",
                    customer_id_hash=sanitized_cust,
                    status=status,
                    evidence_source=evidence_source,
                )
                all_items.append(item)

            # 2. Shared Sets (Negative Keyword Lists)
            shared_set_rows = self.gaql_executor(customer_id, GAQL_SHARED_SETS)
            shared_set_id_to_name: Dict[str, str] = {}
            for row in shared_set_rows:
                s_id = str(row.get("id") or (row.get("shared_set") or {}).get("id", ""))
                s_name = str(row.get("name") or (row.get("shared_set") or {}).get("name", "UNKNOWN_SET"))
                s_status = normalize_criterion_status(row.get("status") or (row.get("shared_set") or {}).get("status", "ENABLED"))
                if s_status in (CriterionStatus.REMOVED, CriterionStatus.UNKNOWN):
                    continue
                if s_id:
                    shared_set_id_to_name[s_id] = s_name

            # 3. Shared Criteria (Criteria inside Shared Sets)
            shared_crit_rows = self.gaql_executor(customer_id, GAQL_SHARED_CRITERIA)
            for row in shared_crit_rows:
                s_ref = str(row.get("shared_set") or (row.get("shared_criterion") or {}).get("shared_set", ""))
                # Handle resource name like 'customers/123/sharedSets/456' or raw ID '456'
                s_id = s_ref.split("/")[-1] if "/" in s_ref else s_ref
                set_name = shared_set_id_to_name.get(s_id, f"SET_{hash_identifier(s_id)}")

                kw_text = row.get("keyword_text") or (row.get("keyword") or {}).get("text", "")
                match_type = row.get("match_type") or (row.get("keyword") or {}).get("match_type", "BROAD")
                item = NegativeKeywordItem(
                    keyword_text=kw_text,
                    match_type=normalize_match_type(match_type),
                    source_scope=SourceScope.SHARED_SET,
                    campaign_name="GLOBAL",
                    campaign_id_hash="none",
                    ad_group_name="NONE",
                    ad_group_id_hash="none",
                    shared_set_name=set_name,
                    customer_id_hash=sanitized_cust,
                    status=CriterionStatus.ENABLED,
                    evidence_source=evidence_source,
                )
                all_items.append(item)

            # 4. Campaign Shared Sets (Attachments)
            camp_shared_rows = self.gaql_executor(customer_id, GAQL_CAMPAIGN_SHARED_SETS)
            for row in camp_shared_rows:
                c_ref = str(row.get("campaign") or (row.get("campaign_shared_set") or {}).get("campaign", ""))
                c_id = c_ref.split("/")[-1] if "/" in c_ref else c_ref
                c_hash = hash_identifier(c_id)

                s_ref = str(row.get("shared_set") or (row.get("campaign_shared_set") or {}).get("shared_set", ""))
                s_id = s_ref.split("/")[-1] if "/" in s_ref else s_ref
                set_name = shared_set_id_to_name.get(s_id, f"SET_{hash_identifier(s_id)}")

                att_status = normalize_criterion_status(row.get("status") or (row.get("campaign_shared_set") or {}).get("status", "ENABLED"))
                if att_status in (CriterionStatus.REMOVED, CriterionStatus.UNKNOWN):
                    continue

                if c_hash not in campaign_shared_sets:
                    campaign_shared_sets[c_hash] = []
                if set_name not in campaign_shared_sets[c_hash]:
                    campaign_shared_sets[c_hash].append(set_name)

            # 5. Campaign Criteria (Direct Campaign Negatives)
            camp_crit_rows = self.gaql_executor(customer_id, GAQL_CAMPAIGN_NEGATIVES)
            for row in camp_crit_rows:
                c_id = str(row.get("campaign_id") or (row.get("campaign") or {}).get("id", ""))
                c_name = str(row.get("campaign_name") or (row.get("campaign") or {}).get("name", "GLOBAL"))
                kw_text = row.get("keyword_text") or (row.get("keyword") or {}).get("text", "")
                match_type = row.get("match_type") or (row.get("keyword") or {}).get("match_type", "BROAD")
                status = normalize_criterion_status(row.get("status", "ENABLED"))
                if status in (CriterionStatus.REMOVED, CriterionStatus.UNKNOWN):
                    continue

                item = NegativeKeywordItem(
                    keyword_text=kw_text,
                    match_type=normalize_match_type(match_type),
                    source_scope=SourceScope.CAMPAIGN,
                    campaign_name=c_name,
                    campaign_id_hash=hash_identifier(c_id),
                    ad_group_name="NONE",
                    ad_group_id_hash="none",
                    shared_set_name="NONE",
                    customer_id_hash=sanitized_cust,
                    status=status,
                    evidence_source=evidence_source,
                )
                all_items.append(item)

            # 6. Ad Group Criteria (Direct Ad Group Negatives)
            adg_crit_rows = self.gaql_executor(customer_id, GAQL_AD_GROUP_NEGATIVES)
            for row in adg_crit_rows:
                c_id = str(row.get("campaign_id") or (row.get("campaign") or {}).get("id", ""))
                c_name = str(row.get("campaign_name") or (row.get("campaign") or {}).get("name", "GLOBAL"))
                g_id = str(row.get("ad_group_id") or (row.get("ad_group") or {}).get("id", ""))
                g_name = str(row.get("ad_group_name") or (row.get("ad_group") or {}).get("name", "NONE"))
                kw_text = row.get("keyword_text") or (row.get("keyword") or {}).get("text", "")
                match_type = row.get("match_type") or (row.get("keyword") or {}).get("match_type", "BROAD")
                status = normalize_criterion_status(row.get("status", "ENABLED"))
                if status in (CriterionStatus.REMOVED, CriterionStatus.UNKNOWN):
                    continue

                item = NegativeKeywordItem(
                    keyword_text=kw_text,
                    match_type=normalize_match_type(match_type),
                    source_scope=SourceScope.AD_GROUP,
                    campaign_name=c_name,
                    campaign_id_hash=hash_identifier(c_id),
                    ad_group_name=g_name,
                    ad_group_id_hash=hash_identifier(g_id),
                    shared_set_name="NONE",
                    customer_id_hash=sanitized_cust,
                    status=status,
                    evidence_source=evidence_source,
                )
                all_items.append(item)

            return NegativeSnapshot(
                customer_id_hash=sanitized_cust,
                items=all_items,
                campaign_shared_sets=campaign_shared_sets,
                evidence_source=evidence_source,
                status="READY",
            )

        except Exception as e:
            logger.error("Error executing live negative criteria query: %s", str(e))
            return NegativeSnapshotManager.create_hold_data_gap_snapshot(
                reason=f"LIVE_QUERY_EXCEPTION: {type(e).__name__}"
            )
