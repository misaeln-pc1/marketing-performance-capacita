"""Explicit contract and registry for Google Ads campaigns (fail-closed architecture)."""

from __future__ import annotations

import enum
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from .models import CampaignType, IntentClass, PolicyDecision, hash_identifier


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
    campaign_id_hash: str
    campaign_name_pattern: str
    audience: CampaignType
    product: ProductType
    modality: Modality
    campaign_family: str
    landing_variant: str  # "A", "B", "C", "N/A"
    allowed_negative_intents: Set[IntentClass] = field(default_factory=set)
    protected_intents: Set[IntentClass] = field(default_factory=set)
    protected_terms: Set[str] = field(default_factory=set)
    # Ad group routing map: normalized ad group name/pattern -> variant ('A', 'B', 'C')
    ad_group_routing: Dict[str, str] = field(default_factory=dict)
    # Explicit valid destinations for routing signals
    routing_destinations: Dict[str, str] = field(default_factory=dict)


# Demo / fixture campaign contracts — FOR TESTS AND DEMONSTRATIONS ONLY.
# Production live execution requires private mapping loaded via load_contracts_from_json().
DEMO_CAMPAIGN_CONTRACTS: List[CampaignContract] = [
    CampaignContract(
        campaign_id_hash="hash_c11111111111",
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
            IntentClass.ROUTING_A_B_C,
            IntentClass.B2B_SENCE,
        },
        protected_intents=set(),
        protected_terms={
            "presencial", "santiago", "capacita", "curso presencial",
            "curso presencial santiago", "curso excel presencial",
        },
        ad_group_routing={
            "ADG_A_GENERAL": "A",
            "ADG_1": "A",
            "ADG_B_DESDE_CERO": "B",
            "ADG_B_PASO_A_PASO": "B",
            "ADG_C_CLASES": "C",
            "ADG_C_PROFESOR": "C",
        },
        routing_destinations={
            "desde_cero": "B",
            "principiantes": "B",
            "paso_a_paso": "B",
            "profesor": "C",
            "clases": "C",
        },
    ),
    CampaignContract(
        campaign_id_hash="hash_c22222222222",
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
            IntentClass.B2B_SENCE,
        },
        protected_terms={
            "empresa", "empresas", "sence", "otic", "factura", "cotizacion",
            "capacitacion empresas", "curso excel empresas",
        },
        ad_group_routing={},
        routing_destinations={},
    ),
]


class CampaignRegistry:
    """Injectable registry that resolves campaigns to contracts fail-closed.

    Primary key: campaign_id_hash.
    Secondary validation: campaign_name / campaign_family compatibility.

    Default constructor creates an EMPTY registry (fail-closed).
    For tests/demos, pass DEMO_CAMPAIGN_CONTRACTS explicitly.
    For live execution, use load_contracts_from_json() with a private mapping file.
    """

    def __init__(self, contracts: Optional[List[CampaignContract]] = None):
        self._contracts: List[CampaignContract] = []
        self._id_hash_map: Dict[str, List[CampaignContract]] = {}
        for c in (contracts or []):
            self.register_contract(c)

    def register_contract(self, contract: CampaignContract) -> None:
        """Registers a campaign contract indexed primarily by campaign_id_hash."""
        c_hash = hash_identifier(contract.campaign_id_hash)
        self._contracts.append(contract)
        if c_hash not in self._id_hash_map:
            self._id_hash_map[c_hash] = []
        self._id_hash_map[c_hash].append(contract)

    def register_campaign(self, campaign_id_hash: str, contract: CampaignContract) -> None:
        """Registers a campaign mapping."""
        self.register_contract(contract)

    def resolve(
        self,
        campaign_id_hash: str,
        campaign_name: Optional[str] = None,
    ) -> Optional[CampaignContract]:
        """Resolves campaign contract fail-closed.

        Primary check: campaign_id_hash.
        Fail-closed ante:
        - ID no registrado (0 matches -> None)
        - Múltiples coincidencias (> 1 matches -> None)
        - Nombre incompatible con campaign_name_pattern o campaign_family (None)
        """
        if not campaign_id_hash:
            return None
        sanitized_id = hash_identifier(campaign_id_hash)
        if sanitized_id in ("none", "unknown", "global", "n/a"):
            return None

        matching = self._id_hash_map.get(sanitized_id, [])
        if len(matching) == 0:
            return None
        if len(matching) > 1:
            # Ambiguous mapping: multiple contracts share the same campaign_id_hash -> fail-closed
            return None

        contract = matching[0]

        # Secondary check: verify name/family compatibility if provided
        if campaign_name and campaign_name.strip().upper() not in ("UNKNOWN", "NONE", "GLOBAL", ""):
            name_upper = campaign_name.strip().upper()
            pat_upper = contract.campaign_name_pattern.strip().upper()
            fam_upper = contract.campaign_family.strip().upper()
            if pat_upper not in name_upper and fam_upper not in name_upper:
                return None

        return contract

    @classmethod
    def load_contracts_from_json(cls, file_path: Path) -> "CampaignRegistry":
        """Loads campaign contracts from a private JSON mapping file.

        Required for live execution. The file must NOT be in the repo.
        Fails closed if the file is missing or invalid.
        """
        if not file_path.is_file():
            raise FileNotFoundError(
                f"CAMPAIGN_MAPPING_MISSING: Private campaign contract file not found: {file_path}. "
                "Fail-closed: live execution requires an explicit mapping file."
            )
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("CAMPAIGN_MAPPING_FORMAT_ERROR: Expected a JSON array of campaign contracts.")
        contracts = []
        for entry in data:
            c = CampaignContract(
                campaign_id_hash=entry.get("campaign_id_hash", ""),
                campaign_name_pattern=entry.get("campaign_name_pattern", ""),
                audience=CampaignType(entry.get("audience", "UNKNOWN")),
                product=ProductType(entry.get("product", "UNKNOWN")),
                modality=Modality(entry.get("modality", "UNKNOWN")),
                campaign_family=entry.get("campaign_family", ""),
                landing_variant=entry.get("landing_variant", "N/A"),
                allowed_negative_intents={IntentClass(i) for i in entry.get("allowed_negative_intents", [])},
                protected_intents={IntentClass(i) for i in entry.get("protected_intents", [])},
                protected_terms=set(entry.get("protected_terms", [])),
                ad_group_routing=entry.get("ad_group_routing", {}),
                routing_destinations=entry.get("routing_destinations", {}),
            )
            contracts.append(c)
        return cls(contracts=contracts)


def validate_ad_group_routing(
    contract: CampaignContract,
    text: str,
    target_ad_group_name: str,
) -> tuple[PolicyDecision, str]:
    """Validates ROUTING_A_B_C candidate terms against explicit routing matrix.

    Rules:
    - A can cede 'desde cero' to B.
    - C can cede 'desde cero' to B.
    - B CANNOT negate 'desde cero' within group B.
    - 'profesor'/'clases' can only be excluded if destination is expressly defined.
    - Do NOT accept ROUTING_A_B_C in any AD_GROUP by default -> fail-closed HOLD_REVIEW.
    """
    if not target_ad_group_name or target_ad_group_name.strip().upper() in ("NONE", "UNKNOWN", ""):
        return (
            PolicyDecision.HOLD_REVIEW,
            "ROUTING_NO_AD_GROUP: Término de routing A/B/C requiere grupo de anuncios específico.",
        )

    # Lookup ad group variant
    adg_clean = target_ad_group_name.strip().upper()
    variant = contract.ad_group_routing.get(adg_clean)
    if not variant:
        # Check partial pattern
        for pat, var in contract.ad_group_routing.items():
            if pat in adg_clean:
                variant = var
                break

    if not variant:
        return (
            PolicyDecision.HOLD_REVIEW,
            f"ROUTING_UNDEFINED_GROUP: Grupo '{target_ad_group_name}' no registrado en matriz de routing. Fail-closed.",
        )

    # 1. 'desde cero', 'principiantes', 'paso a paso' signals
    is_desde_cero_signal = any(s in text for s in ("desde cero", "principiante", "paso a paso"))
    if is_desde_cero_signal:
        dest = contract.routing_destinations.get("desde_cero", "B")
        if variant == dest:
            return (
                PolicyDecision.CONFLICT,
                f"ROUTING_CONFLICT_SELF: No se puede negativizar 'desde cero/principiantes' dentro del Grupo {variant} (destino propio).",
            )
        if variant in ("A", "C"):
            # A and C can cede to B
            return (
                PolicyDecision.CANDIDATE,
                f"ROUTING_VALID: Grupo {variant} cede 'desde cero' hacia Grupo {dest}.",
            )

    # 2. 'profesor', 'clases' signals
    is_clases_signal = any(s in text for s in ("profesor", "clases"))
    if is_clases_signal:
        dest = contract.routing_destinations.get("profesor", "C")
        if not dest:
            return (
                PolicyDecision.HOLD_REVIEW,
                "ROUTING_NO_DESTINATION: Destino para señal 'profesor/clases' no está expresamente definido.",
            )
        if variant == dest:
            return (
                PolicyDecision.CONFLICT,
                f"ROUTING_CONFLICT_SELF: No se puede negativizar 'profesor/clases' dentro del Grupo {variant} (destino propio).",
            )
        if variant in ("A", "B"):
            return (
                PolicyDecision.CANDIDATE,
                f"ROUTING_VALID: Grupo {variant} cede 'profesor/clases' hacia Grupo {dest}.",
            )

    # Any other routing signal not explicitly covered
    return (
        PolicyDecision.HOLD_REVIEW,
        f"ROUTING_UNRESOLVED: Término '{text}' en Grupo {variant} no tiene ruta explícita permitida.",
    )
