"""Explicit contract and registry for Google Ads campaigns (fail-closed architecture)."""

from __future__ import annotations

import enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set

from .models import CampaignType, IntentClass, hash_identifier


class Modality(str, enum.Enum):
    PRESENCIAL = "PRESENCIAL"
    ONLINE = "ONLINE"
    MIXTA = "MIXTA"
    UNKNOWN = "UNKNOWN"


class ProductType(str, enum.Enum):
    EXCEL = "EXCEL"
    POWER_BI = "POWER_BI"
    IA_TRABAJO = "IA_TRABAJO"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class CampaignContract:
    """Canonical contract defining operational attributes and negative keyword policy for a campaign."""
    campaign_name_pattern: str
    audience: CampaignType
    product: ProductType
    modality: Modality
    campaign_family: str
    landing_variant: str  # "A", "B", "C", "N/A"
    allowed_negative_intents: Set[IntentClass] = field(default_factory=set)
    protected_intents: Set[IntentClass] = field(default_factory=set)
    protected_terms: Set[str] = field(default_factory=set)


# Known canonical campaign registry for Capacita
DEFAULT_CAMPAIGN_CONTRACTS: List[CampaignContract] = [
    CampaignContract(
        campaign_name_pattern="SCL-EXCEL-B2C-PRESENCIAL",
        audience=CampaignType.B2C,
        product=ProductType.EXCEL,
        modality=Modality.PRESENCIAL,
        campaign_family="EXCEL_PRESENCIAL_B2C",
        landing_variant="A",
        allowed_negative_intents={
            IntentClass.SOLUCION_PUNTUAL,
            IntentClass.EMPLEO,
            IntentClass.MODALIDAD,
            IntentClass.CLASES_PARTICULARES,
            IntentClass.FUERA_ALCANCE,
            IntentClass.ROUTING_A_B_C,  # Allowed at ad group level
        },
        protected_intents=set(),
        protected_terms={
            "presencial", "santiago", "capacita", "curso presencial",
            "curso presencial santiago", "curso excel presencial",
        },
    ),
    CampaignContract(
        campaign_name_pattern="SCL-EXCEL-EMPRESA-B2B",
        audience=CampaignType.B2B_EMPRESA,
        product=ProductType.EXCEL,
        modality=Modality.PRESENCIAL,
        campaign_family="EXCEL_EMPRESA_B2B",
        landing_variant="N/A",
        allowed_negative_intents={
            IntentClass.SOLUCION_PUNTUAL,
            IntentClass.EMPLEO,
            IntentClass.CLASES_PARTICULARES,
            IntentClass.FUERA_ALCANCE,
        },
        protected_intents={
            IntentClass.B2B_SENCE,  # B2B terms MUST NOT be negated in B2B campaigns
        },
        protected_terms={
            "empresa", "empresas", "sence", "otic", "factura", "cotizacion",
            "capacitacion empresas", "curso excel empresas",
        },
    ),
    CampaignContract(
        campaign_name_pattern="META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3",
        audience=CampaignType.B2C,
        product=ProductType.EXCEL,
        modality=Modality.PRESENCIAL,
        campaign_family="EXCEL_PRESENCIAL_B2C",
        landing_variant="N/A",
        allowed_negative_intents={
            IntentClass.SOLUCION_PUNTUAL,
            IntentClass.EMPLEO,
            IntentClass.MODALIDAD,
            IntentClass.FUERA_ALCANCE,
            IntentClass.ROUTING_A_B_C,
        },
        protected_intents=set(),
        protected_terms={"presencial", "santiago", "curso excel presencial"},
    ),
]


class CampaignRegistry:
    """Injectable registry that resolves campaigns to contracts fail-closed."""

    def __init__(self, contracts: Optional[List[CampaignContract]] = None):
        self._contracts: List[CampaignContract] = list(contracts or DEFAULT_CAMPAIGN_CONTRACTS)
        self._custom_mappings: Dict[str, CampaignContract] = {}

    def register_campaign(self, campaign_name: str, contract: CampaignContract) -> None:
        """Explicitly registers a campaign name mapping."""
        self._custom_mappings[campaign_name.strip().upper()] = contract

    def resolve(self, campaign_name: str) -> Optional[CampaignContract]:
        """Resolves campaign contract. Returns None if unknown (fail-closed)."""
        if not campaign_name or campaign_name.strip().upper() in ("UNKNOWN", "NONE", "GLOBAL"):
            return None

        name_upper = campaign_name.strip().upper()

        if name_upper in self._custom_mappings:
            return self._custom_mappings[name_upper]

        for contract in self._contracts:
            if contract.campaign_name_pattern.upper() in name_upper:
                return contract

        return None
