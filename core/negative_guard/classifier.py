"""Classification logic for Campaigns and Keyword Intents based on canonical policy."""

from __future__ import annotations

import re
from typing import Optional

from .campaign_contract import CampaignContract, CampaignRegistry
from .models import CampaignType, IntentClass, normalize_keyword_text

DEFAULT_REGISTRY = CampaignRegistry()

# Canonical keyword signals based on docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md
SOLUCION_PUNTUAL_PATTERNS = [
    r"\bejemplos?\b",
    r"\bejercicios?\b",
    r"\batajos?\b",
    r"\bfunciones?\b",
    r"\bformulas?\b",
    r"\bbuscarv\b",
    r"\bsumar\.si\b",
    r"\btablas?\s+dinamicas?\b",
    r"\blistas?\s+desplegables?\b",
    r"\bformatos?\b",
    r"\bmanuales?\b",
    r"\btutoriales?\b",
    r"\bcomo\s+hacer\b",
    r"\bplantillas?\b",
    r"\bsintaxis\b",
    r"\batajo\b",
    r"\bcomando\b",
    r"\bgratis\b",
    r"\bgratuit[oa]s?\b",
    r"\bfree\b",
    r"\bdescargar?\b",
]

EMPLEO_PATTERNS = [
    r"\bempleo\b",
    r"\bvacantes?\b",
    r"\bofertas?\s+laborales?\b",
    r"\bbolsa\s+de\s+trabajo\b",
    r"\bbusqueda\s+de\s+trabajo\b",
    r"\bpostular\b",
    r"\bcv\b",
    r"\bcurriculum\b",
]

MODALIDAD_NO_PRESENCIAL_PATTERNS = [
    r"\bonline\b",
    r"\ben\s+linea\b",
    r"\bvirtual\b",
    r"\bremoto\b",
    r"\be-learning\b",
    r"\bzoom\b",
    r"\ba\s+distancia\b",
    r"\bstreaming\b",
]

B2B_SENCE_PATTERNS = [
    r"\bempresas?\b",
    r"\bsence\b",
    r"\botic\b",
    r"\bfranquicia\s+tributaria\b",
    r"\bcotizacion(\s+empresa)?\b",
    r"\bfactura\b",
    r"\bpara\s+empresas\b",
    r"\bclases\s+para\s+empresas\b",
    r"\bcurso\s+para\s+empresas\b",
    r"\bcorporativ[oa]s?\b",
    r"\bin[- ]company\b",
]

CLASES_PARTICULARES_PATTERNS = [
    r"\bparticulares?\b",
    r"\bprofesor\s+particular\b",
    r"\bclases?\s+particulares?\b",
    r"\ba\s+domicilio\b",
    r"\b1\s+a\s+1\b",
]

FUERA_ALCANCE_PATTERNS = [
    r"\bvba\b",
    r"\bmacros?\b",
    r"\baccess\b",
    r"\bpower\s*bi\b",
    r"\bpython\b",
    r"\bsql\b",
]

# Signals intended for routing across A/B/C ad groups, NOT global exclusions
ROUTING_A_B_C_PATTERNS = [
    r"\bdesde\s+cero\b",
    r"\bprincipiantes?\b",
    r"\bprofesor\b",
    r"\bclases\b",
    r"\bpaso\s+a\s+paso\b",
    r"\bpersonalizado\b",
]


def classify_campaign(
    campaign_id_hash: str = "none",
    campaign_name: str = "",
    registry: Optional[CampaignRegistry] = None,
) -> CampaignType:
    """Classifies a campaign as B2C, B2B_EMPRESA, or UNKNOWN strictly fail-closed via CampaignRegistry."""
    reg = registry or DEFAULT_REGISTRY
    contract = reg.resolve(campaign_id_hash, campaign_name)
    if contract:
        return contract.audience

    return CampaignType.UNKNOWN


def classify_keyword_intent(raw_keyword: str) -> IntentClass:
    """Classifies keyword intent into canonical classes with strict B2B precedence."""
    text, _ = normalize_keyword_text(raw_keyword)
    if not text:
        return IntentClass.DESCONOCIDO

    # 1. Clases particulares (evaluate before generic routing)
    for pat in CLASES_PARTICULARES_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.CLASES_PARTICULARES

    # 2. B2B / SENCE (Evaluated BEFORE ROUTING_A_B_C so 'clases para empresas' is classified as B2B)
    for pat in B2B_SENCE_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.B2B_SENCE

    # 3. Check routing signals (e.g., desde cero, paso a paso, profesor, clases)
    for pat in ROUTING_A_B_C_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.ROUTING_A_B_C

    # 4. Modalidad no presencial
    for pat in MODALIDAD_NO_PRESENCIAL_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.MODALIDAD

    # 5. Fuera de alcance (VBA, Power BI, Python)
    for pat in FUERA_ALCANCE_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.FUERA_ALCANCE

    # 6. Solución puntual (fórmulas, tutoriales, atajos, etc.)
    for pat in SOLUCION_PUNTUAL_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.SOLUCION_PUNTUAL

    # 7. Empleo
    for pat in EMPLEO_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            # Exception: "para el trabajo" is valid commercial intent, not job seeking
            if "para el trabajo" in text:
                continue
            return IntentClass.EMPLEO

    return IntentClass.DESCONOCIDO
