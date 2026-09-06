"""Classification logic for Campaigns and Keyword Intents based on canonical policy."""

from __future__ import annotations

import re
from typing import Optional

from .models import CampaignType, IntentClass, normalize_keyword_text


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
    r"\bcotizacion\s+empresa\b",
    r"\bfactura\b",
    r"\bpara\s+empresas\b",
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


def classify_campaign(campaign_name: str) -> CampaignType:
    """Classifies a campaign as B2C, B2B_EMPRESA, or UNKNOWN strictly based on nomenclature and explicit tokens."""
    if not campaign_name:
        return CampaignType.UNKNOWN

    name_upper = campaign_name.strip().upper()

    # Explicit B2B signals
    b2b_tokens = ["B2B", "EMPRESA", "EMPRESAS", "SENCE", "CORPORATIVO", "INCOMPANY", "IN-COMPANY"]
    # Explicit B2C signals
    b2c_tokens = [
        "B2C",
        "PRESENCIAL_SANTIAGO_B2C",
        "EXCEL_PRESENCIAL_B2C",
        "LANDING_A",
        "LANDING_B",
        "LANDING_C",
        "SCL-EXCEL-B2C",
    ]

    has_b2b = any(token in name_upper for token in b2b_tokens)
    has_b2c = any(token in name_upper for token in b2c_tokens)

    if has_b2b and not has_b2c:
        return CampaignType.B2B_EMPRESA
    if has_b2c and not has_b2b:
        return CampaignType.B2C

    # If both or neither, check known campaign baseline names from context
    if "META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3" in name_upper:
        return CampaignType.B2C
    if "EXCEL_BASICO_INTERMEDIO_PRESENCIAL" in name_upper and "EMPRESA" not in name_upper:
        return CampaignType.B2C

    return CampaignType.UNKNOWN


def classify_keyword_intent(raw_keyword: str) -> IntentClass:
    """Classifies keyword intent into canonical classes."""
    text, _ = normalize_keyword_text(raw_keyword)
    if not text:
        return IntentClass.DESCONOCIDO

    # Clases particulares (evaluate before generic 'clases' routing)
    for pat in CLASES_PARTICULARES_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.CLASES_PARTICULARES

    # Check routing signals (e.g., desde cero, paso a paso, profesor)
    for pat in ROUTING_A_B_C_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.ROUTING_A_B_C

    # B2B / SENCE
    for pat in B2B_SENCE_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.B2B_SENCE

    # Modalidad no presencial
    for pat in MODALIDAD_NO_PRESENCIAL_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.MODALIDAD

    # Fuera de alcance (VBA, Power BI, Python)
    for pat in FUERA_ALCANCE_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.FUERA_ALCANCE

    # Solución puntual (fórmulas, tutoriales, atajos, etc.)
    for pat in SOLUCION_PUNTUAL_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            return IntentClass.SOLUCION_PUNTUAL

    # Empleo
    for pat in EMPLEO_PATTERNS:
        if re.search(pat, text, re.IGNORECASE):
            # Exception: "para el trabajo" is valid commercial intent, not job seeking
            if "para el trabajo" in text:
                continue
            return IntentClass.EMPLEO

    return IntentClass.DESCONOCIDO
