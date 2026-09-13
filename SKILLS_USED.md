# SKILLS_USED — Marketing Performance

## Estado

```text
BASELINE=AI_OS_V4_2_INITIAL_SKILL_REFRESH
DATE=2026-09-13
CONSUMER=misaeln-pc1/marketing-performance-capacita
AI_OS=misaeln-pc1/capacita-ai-operating-system
PARALLEL_LOCAL_RADAR=NO
AUTOMATION_ACTIVATED=NO
```

Este archivo registra **decisiones materiales de consumo**, no cada ejecución. La regla vigente es:

```text
USAGE_EVENT != CONSUMPTION_DECISION != LIBRARY_VERSION
```

AI OS mantiene discovery, radar, versiones e impact check. Marketing conserva pruebas/contexto real, decisión local, evidencia y feedback reusable material.

## 1. Necesidades materiales del proyecto

| Necesidad | Estado | Tratamiento |
|---|---|---|
| Diagnóstico Google Ads | `YA_CUBIERTA` | Componer skill AI OS + canónicos locales de negativas, tracking y READ control plane. |
| Diagnóstico Meta Ads | `YA_CUBIERTA` | Componer skill AI OS + account routing, creatividades, READ y downstream local. |
| Performance cross-channel y Ads → web → CRM → venta | `PARCIALMENTE_CUBIERTA` | `paid-ads-performance-bridge-capacita` cubre el método; persisten gaps de tracking/downstream. |
| Liderazgo causal de campaña y diseño de experimento | `BRECHA_REAL_REUSABLE_CANDIDATE` | Existe contrato local candidato (#91), pero no una cobertura equivalente explícita en las skills Paid Ads vigentes. Devolver a AI OS para comparar contra #40 antes de crear skill. |
| Visibilidad de páginas: SEO/AEO/GEO/AI-readability/crawl/entidad | `YA_CUBIERTA` | Orquestador + cinco skills especializadas + runtime reusable externo al repo. |
| Demanda/SERP/canibalización | `YA_CUBIERTA` | `seo-demand-serp-research-capacita`; validar por caso con fuentes reales. |
| Competitive Intelligence / benchmarking / monitoring | `PARCIALMENTE_CUBIERTA` | AI OS #57 / PR #58 V03 sigue Draft/open; no tratar como baseline de biblioteca hasta merge/decisión vigente. |
| Content-to-diagnostic / short-form | `NO_PRIORITARIA_COMO_BINDING_DE_MARKETING` | Marketing es parent; consumidor editorial real es `capacita-content-factory` vía AI OS #82. No duplicar sus skills aquí. |

## 2. Baseline de consumo

### 2.1 `google-ads-campaign-audit-capacita`

```yaml
skill_or_capability: google-ads-campaign-audit-capacita
aios_version: 0.1.0
decision: MIX
local_status: in_use_local
consumption_profile: MIX
evidence_level: OBSERVED
scope_used:
  - diagnóstico READ de campañas, keywords, search terms, landings y conversiones
  - separación de métricas de plataforma vs resultado comercial
  - recomendaciones documentales sin writes
scope_not_used:
  - tratar la skill como fuente única para negativas
  - writes, OAuth nuevo o cambios de campañas
  - declarar conversiones/CPA final sin reconciliación downstream
local_delta_summary: política canónica de negativas por intención + Google Ads fast path/control plane + Campaign Leadership local cuando esté vigente
known_limits:
  - tracking y CRM pueden dejar conversiones provisionales
  - Campaign Leadership V01 sigue candidato de validación
  - PMax y superficies no observadas no se presumen cubiertas
evidence:
  - docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md
  - docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md
  - DECISIONES.md
```

### 2.2 `meta-ads-campaign-audit-capacita`

```yaml
skill_or_capability: meta-ads-campaign-audit-capacita
aios_version: 0.1.0
decision: MIX
local_status: in_use_local
consumption_profile: MIX
evidence_level: OBSERVED
scope_used:
  - análisis READ de campaign/adset/ad, creative, audience, placement y performance
  - coherencia anuncio → landing → señal downstream
  - routing de cuenta y evidencia agregada sin PII
scope_not_used:
  - writes en Ads Manager
  - datos personales de leads
  - inferir calidad comercial sólo desde CTR/CPC
local_delta_summary: account routing local + asset standards + Campaign Leadership/anti-tool-chasing candidato
known_limits:
  - downstream comercial incompleto puede volver provisional una decisión de audiencia
  - V3.2/Campaign Leadership aún no está activa validada
evidence:
  - docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md
  - docs/analytics/MARKETING_CAMPAIGN_LEADERSHIP_CONTRACT_V01.md
  - issue #91
```

### 2.3 `paid-ads-performance-bridge-capacita`

```yaml
skill_or_capability: paid-ads-performance-bridge-capacita
aios_version: 0.1.0
decision: MIX
local_status: in_use_local
consumption_profile: MIX
evidence_level: OBSERVED
scope_used:
  - separar Ads, web, CRM, Deal, CursoAlumno y venta real
  - normalizar métricas y gaps entre plataforma y resultado comercial
  - comparar fuentes sin tratar conversion de plataforma como venta
scope_not_used:
  - pipeline unificado completo y siempre-live
  - ROAS/CPA final cuando downstream no está reconciliado
local_delta_summary: fuentes READ locales + reglas GTM/RevOps + canónicos de campaña y tracking
known_limits:
  - atribución completa depende de fuentes externas y reconciliación autorizada
evidence:
  - docs/analytics/MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md
  - DECISIONES.md
```

### 2.4 `marketing-page-visibility-review-capacita`

```yaml
skill_or_capability: marketing-page-visibility-review-capacita
aios_version: 0.1.0
decision: ADOPTAR
local_status: in_use_local
consumption_profile: PARTIAL
evidence_level: OBSERVED
scope_used:
  - orquestación del protocolo de visibilidad del consumidor
  - selección proporcional de módulos
  - evidencia, P0/P1/P2, DO_NOT_CHANGE y handoff técnico
scope_not_used:
  - ejecutar todos los módulos por defecto
  - publicar o cambiar Edge/Cloudflare/robots
local_delta_summary: el protocolo local `MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md` conserva precedencia
known_limits:
  - evidencia real aún concentrada en pocos casos; no promover a VALIDATED por selección
evidence:
  - docs/seo-ai/README.md
  - docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md
  - TASK_STATUS.md
```

### 2.5 `seo-demand-serp-research-capacita`

```yaml
skill_or_capability: seo-demand-serp-research-capacita
aios_version: 0.1.0
decision: MIX
local_status: evaluating
consumption_profile: PARTIAL
evidence_level: OBSERVED
scope_used:
  - demanda/intención/SERP/canibalización como entrada de decisión
  - preferencia por GSC/SERP/datos reales sobre heurísticas
scope_not_used:
  - inferir demanda sólo por CPC
  - crear fan-out de URLs por keywords
local_delta_summary: se combina con Google Ads, GTM y protocolo de visibilidad local
known_limits:
  - disponibilidad de GSC/Keyword Planner/Trends varía por caso
evidence:
  - docs/seo-ai/README.md
  - docs/seo-ai/SEO_GEO_TECHNICAL_RESEARCH_BASELINE_V01.md
```

### 2.6 `aeo-ai-readability-capacita`

```yaml
skill_or_capability: aeo-ai-readability-capacita
aios_version: 0.1.0
decision: ADAPTAR_MINIMO
local_status: evaluating
consumption_profile: PARTIAL
evidence_level: OBSERVED
scope_used:
  - claridad answer-first y contenido recuperable
  - revisión de hechos y preguntas respondibles
  - Markdown/render como apoyo a AI-readability
scope_not_used:
  - llms.txt/schema/chunking como requisitos universales
  - cualquier claim de mejora garantizada
local_delta_summary: conservar CRO, hechos comerciales autorizados y protocolo local
known_limits:
  - no existe todavía evidencia suficiente para elevar a VALIDATED
evidence:
  - docs/seo-ai/README.md
  - TASK_STATUS.md
```

### 2.7 `geo-ai-search-benchmark-capacita`

```yaml
skill_or_capability: geo-ai-search-benchmark-capacita
aios_version: 0.1.0
decision: ADAPTAR_MINIMO
local_status: evaluating
consumption_profile: PARTIAL
evidence_level: OBSERVED
scope_used:
  - benchmark reproducible y separación observación/interpretación
  - Promptfoo como benchmark sintético controlado
scope_not_used:
  - presentar benchmark sintético como ranking real de ChatGPT/Google/Claude/Perplexity
  - atribuir causalidad a una edición aislada
local_delta_summary: el runtime técnico vive fuera de Marketing
known_limits:
  - REAL_AI_SEARCH_RANKING=NOT_VALIDATED
  - benchmark real multi-superficie sigue pendiente cuando sea material
evidence:
  - docs/seo-ai/README.md
  - TASK_STATUS.md
```

### 2.8 `ai-crawler-retrieval-access-audit-capacita`

```yaml
skill_or_capability: ai-crawler-retrieval-access-audit-capacita
aios_version: 0.1.0
decision: MIX
local_status: evaluating
consumption_profile: PARTIAL
evidence_level: OBSERVED
scope_used:
  - crawl técnico y sitemap/robots/access como señales
  - separación search/retrieval vs training
scope_not_used:
  - cambios productivos de robots/WAF/Cloudflare
  - bypass de challenges o políticas
local_delta_summary: SiteOne/advertools proveen runtime; Edge implementa cambios autorizados
known_limits:
  - un crawl técnico no prueba visibilidad generativa
evidence:
  - docs/seo-ai/README.md
  - TASK_STATUS.md
```

### 2.9 `entity-authority-corroboration-capacita`

```yaml
skill_or_capability: entity-authority-corroboration-capacita
aios_version: 0.1.0
decision: MIX
local_status: evaluating
consumption_profile: PARTIAL
evidence_level: PLANNED
scope_used:
  - seleccionada para páginas locales/institucionales cuando cambie la decisión
scope_not_used:
  - validación completa página local + no local
  - inventar reviews, backlinks o authority scores
local_delta_summary: usar sólo si entidad/GBP/schema/corroboración son materiales para el caso
known_limits:
  - PENDING_FIRST_MATERIAL_LOCAL_VALIDATION
evidence:
  - docs/seo-ai/README.md
```

### 2.10 `capacita-search-intelligence-toolchain` — capability package

```yaml
skill_or_capability: capacita-search-intelligence-toolchain
aios_version: AI_OS_PR_56 / registry handoff
base_version: fb5c4a9df255953fa6bad59a8866ddf610474d1b
decision: ADOPTAR
local_status: accepted_local
consumption_profile: PARTIAL
evidence_level: VALIDATED
scope_used:
  - SiteOne crawl/report/Markdown
  - advertools robots/sitemap/URL processing
  - Promptfoo synthetic benchmark without paid provider
scope_not_used:
  - SerpBear runtime
  - paid providers, credentials or new infrastructure
local_delta_summary: no duplicar instalación/runtime dentro de Marketing
known_limits:
  - SERPBEAR=PENDING_PROVIDER_SECURITY_REVIEW
  - synthetic benchmark != real AI Search ranking
evidence:
  - docs/seo-ai/README.md
  - TASK_STATUS.md
```

### 2.11 `marketing-event-taxonomy-attribution-capacita`

```yaml
skill_or_capability: marketing-event-taxonomy-attribution-capacita
aios_version: 0.1.0
decision: EXTRAER_PATRON
local_status: evaluating
consumption_profile: PATTERN_ONLY
evidence_level: PLANNED
scope_used:
  - patrón de IDs/eventos estables y separación de señal vs identidad
  - diseño local de pain_signal, bp_hypothesis, CTA y page_variant
scope_not_used:
  - taxonomía completa de juegos
  - activación real GA4/Meta/Zoho
local_delta_summary: Marketing conserva taxonomía operativa de páginas/campañas; Edge/Analytics implementan
known_limits:
  - tracking real de este patrón no está validado por este binding
evidence:
  - docs/analytics/MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md
```

### 2.12 `buyer-persona-signal-map-capacita`

```yaml
skill_or_capability: buyer-persona-signal-map-capacita
aios_version: 0.1.0
decision: EXTRAER_PATRON
local_status: evaluating
consumption_profile: PATTERN_ONLY
evidence_level: PLANNED
scope_used:
  - conducta/clic como señal, no identidad definitiva
  - buyer persona como hipótesis con evidencia/confianza
scope_not_used:
  - lógica específica de juegos
  - etiquetado definitivo de personas
local_delta_summary: buyer persona canónico sigue en GTM/RevOps; Marketing sólo aplica señales/hipótesis
known_limits:
  - no inferir atributos sensibles ni convertir click en verdad de buyer persona
evidence:
  - docs/analytics/MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md
```

### 2.13 `meta-ads-campaign-audit` — evaluación material no usada

```yaml
skill_or_capability: meta-ads-campaign-audit
aios_version: 0.1.0
decision: RECHAZAR_CON_MOTIVO
local_status: rejected_local
consumption_profile: EVALUATED_NOT_USED
evidence_level: OBSERVED
scope_used: []
scope_not_used:
  - consumo directo
local_delta_summary: `meta-ads-campaign-audit-capacita@0.1.0` cubre el mismo núcleo con mayor detalle de estructura, creative, audience, placement, UTM y CRM
known_limits:
  - revisar en AI OS si existe otro consumidor que justifique mantener ambas
rejection_reason: duplicación de menor cobertura para este consumidor
evidence:
  - comparación documental de ambos SKILL.md en refresh 2026-09-13
```

## 3. Candidatas existentes / WATCH — sin binding activo todavía

No son descubrimientos nuevos de este refresh; ya estaban registradas o en research AI OS. No abrir trabajo duplicado.

| Candidata | Estado | Decisión local actual | Condición de salida |
|---|---|---|---|
| Google Ads `account-performance-diagnostics` | AI OS #40 `PENDIENTE_AUDITORIA` | `MANTENER_EN_RADAR` | comparar contra local campaign audit + Campaign Leadership; adoptar sólo si reduce gap/material work. |
| Anthropic Marketing `performance-report` | AI OS #40 `PENDIENTE_AUDITORIA` | `MANTENER_EN_RADAR` | revisar si mejora diagnóstico cross-channel sin duplicar bridge/proactive scan. |
| Competitive Intelligence V03 / `competitive-brief` composition | AI OS #57 / PR #58 Draft/open | `MANTENER_EN_RADAR` | no consumir como biblioteca activa hasta decisión/merge vigente; después F2 local. |
| Google Ads MCP / GA4 MCP / Meta Ads AI connectors | platform candidates | `MANTENER_EN_RADAR` | sólo si una fuente READ nueva cambia materialmente la decisión; no reemplazar fast path/API validada por comodidad. |

## 4. Feedback reusable material hacia AI OS

### RF-01 — Campaign Leadership para Paid Ads

```text
LOCAL_EVIDENCE=Marketing #91 + Campaign Leadership V01
LOCAL_STATUS=CANDIDATE_NOT_VALIDATED
REUSABLE_DELTA=diagnóstico causal + counterargument + evidence discriminator + diseño completo de experimento/campaña + anti-tool-chasing
AI_OS_COMPARE_AGAINST=#40 / google-ads-campaign-audit-capacita / meta-ads-campaign-audit-capacita / paid-ads-performance-bridge-capacita / account-performance-diagnostics / performance-report
AUTO_VERSION=NO
SUGGESTED_DISPOSITION=AI_OS_TO_CLASSIFY_AFTER_COMPARE
```

No crear `campaign-leadership-capacita` desde el consumidor. Primero AI OS debe decidir si el delta cabe como MINOR de skills existentes, mix/orquestador, patrón o nueva variante.

### RF-02 — duplicación Meta audit

```text
LOCAL_FINDING=meta-ads-campaign-audit@0.1.0 overlaps meta-ads-campaign-audit-capacita@0.1.0
LOCAL_DECISION=use Capacita-specific version; reject generic locally
REUSABLE_DELTA=library hygiene / impact-check noise reduction
AUTO_DEPRECATE=NO
SUGGESTED_ACTION=AI_OS_COMPARE_AND_DEPRECATE_OR_JUSTIFY_BOTH
```

## 5. Radar e impact check

Marketing **no** mantiene radar externo propio.

```text
AI OS detects novelty
→ dedupe / compare / precheck
→ MATERIALITY
→ impact check against this baseline
→ issue/handoff only if material
→ Marketing decides locally and remains pinned until decision
```

Impact outcomes:

```text
NO_ACTION | OPTIONAL_UPDATE | REVIEW_REQUIRED | BREAKING_REVIEW
```

La actualización de este archivo ocurre sólo ante decisión material, cambio de perfil/evidence level/base version, adopción/rechazo, límite reusable o reemplazo. No por cada uso.
