# Estado de Tareas

Fecha de revisión: 2026-08-29

## Prioridad activa — Batch Editorial V01 / issue #71

Marketing está revisando el batch editorial completo producido por `capacita-content-factory` antes de QA final, assets y cualquier handoff posterior a Edge.

```text
MARKETING_ISSUE=71
BATCH_ID=CONTENT_PRE_MARKETING_V01_2026-08-29
FACTORY_ISSUE=capacita-content-factory#16
FACTORY_PR=capacita-content-factory#17
FACTORY_HEAD=641213040cd9fe86b28885ba15ea6322808a6f4c
ARTICLES=45/45_READ
EXCEL=5/5
AI=20/20
POWER_BI=10/10
PROJECT=10/10
MARKETING_XFER=READY
FACTORY_READBACK=PENDING
PUBLICATION=NO
EDGE_HTML=NO
ADS_CHANGE=NO
MAIN_MERGE=NO
```

Rama actual:

`docs/marketing-content-batch-v01-review-20260829`

XFER vigente del ciclo:

`docs/xfer/XFER__MARKETING__CONTENT_FACTORY__CONTENT_PRE_MARKETING_V01_REVIEW__20260829-213400__v01__READY__MARKETING_REVIEW.md`

### Resultado actual

```text
BATCH_45_READ=YES
KEYWORDS_REVIEWED=YES
INTENT_REVIEWED=YES
SERP_DEMAND_CHECKED=YES_WITH_GSC_DATA_GAP
CANNIBALIZATION_CHECKED=YES
SEO_AEO_GEO_REVIEWED=YES_EDITORIAL_STAGE
TOP_10_SELECTED=YES
IMAGE_BRIEFS_MESSAGE_REVIEWED=YES
NEW_SKILL_REQUIRED=NO
```

### Top 10 priorizado

1. E02 — Power Query Excel.
2. IA03 — prompts ChatGPT.
3. IA05 — agentes IA.
4. PBI06 — dashboard Power BI, con corrección Dashboard vs Report.
5. PBI04 — DAX Power BI.
6. IA06 — ChatGPT Work, fast-track coyuntural.
7. IA07 — Deep Research.
8. E03 — Copilot en Excel.
9. PBI03 — Power Query Power BI.
10. IA01 — IA para el trabajo como pillar.

### Decisiones de arquitectura relevantes

- E01 no debe crear una URL nueva: usar el contenido para actualizar/mergear `https://capacita.cl/funcion-buscarv-excel/` e incorporar BUSCARX sin perder el activo histórico.
- E05 funciona mejor como hub de productividad/automatización Excel que enlaza E01/E02/E03.
- IA01 es pillar general; IA02 es ChatGPT desde cero; IA03 prompts; IA04 comparación de herramientas; IA14/IA15/IA16 son spokes por plataforma.
- IA09 e IA10 pueden coexistir con intención distinta: verificación vs alucinaciones.
- IA11 debe funcionar como hub IA + Excel; E03 queda Copilot y E04 Python.
- PBI06 requiere corregir la semántica técnica: `Dashboard` nativo del Service no equivale a una `Report page` con filtros/segmentadores.
- PBI10 usa KPI sólo como ejemplos editoriales; las definiciones reales pertenecen al owner de cada proceso.
- PRJ01 y PRJ02 se solapan; no abrir dos URLs casi equivalentes.
- Project queda preservado editorialmente, pero `PROJECT_10_NEW_URLS=HOLD_PENDING_ARCHITECTURE`. PRJ09 / `curva s project` es la primera candidata independiente a evaluar.
- Los artículos Project deben mantener explícito el contexto `Project desktop` cuando corresponda; Project for the web fue retirado e integrado en Planner.

### Buyer persona / GTM

Fuente canónica:

`misaeln-pc1/capacita-global-control/docs/gtm-revops/BUYER_PERSONAS.md` v1.0.0

- BP-001 domina contenidos de productividad, Excel, Power BI y uso práctico de IA.
- BP-003/BP-004 aplican selectivamente en B2B, equipos, agentes y Power BI empresarial.
- Project usa `BP-000` cuando no existe match canónico suficientemente preciso; no se fuerza un perfil.

### Data gaps

- GSC Wizard responde `payment_required`; no existe evidencia fresca de consultas/ranking propio en esta sesión.
- HYPD Keyword Research y SERP real Google Chile sí están disponibles y se usaron como señal.
- No se inventa tráfico, ranking, KD, CPC ni resultado comercial faltante.

### Siguiente condición

Content Factory debe consumir el XFER y devolver readback con:

```text
CONSUMED_PASS|CONSUMED_WITH_GAPS
commit
changed CONTENT_IDs
diff/QA
open gaps
```

Marketing mantiene issue #71 abierto hasta revisar ese retorno.

---

## Frente vigente no cancelado — IA Aplicada al Trabajo presencial Santiago

El benchmark de mercado anterior sigue siendo válido y no fue reemplazado por el batch editorial.

Documento:

`docs/research/IA_TRABAJO_PRESENCIAL_SANTIAGO_MARKET_BENCHMARK_V01_2026-08-23.md`

Baseline consumidor:

```text
COURSE_CODE=IA-TRAB-01
ACTIVE_VARIANT=IA-TRAB-01-PRES-V1
DURATION=16h
MODALITY=PRESENCIAL_SANTIAGO
PRIMARY_KEYWORD=curso inteligencia artificial
VALUE_PROPOSITION=IA aplicada al trabajo
```

Cuando exista preview/URL de la landing, corresponde aplicar el protocolo integral y comparar contra el benchmark. Este frente no se mezcla con la revisión editorial #71.

---

## SEO / AEO / GEO / AI Search — capacidades vigentes

Fuente local obligatoria:

```text
docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md
docs/seo-ai/README.md
DECISIONES.md
```

Skills AI OS disponibles para uso local controlado:

1. `seo-demand-serp-research-capacita`
2. `aeo-ai-readability-capacita`
3. `geo-ai-search-benchmark-capacita`
4. `ai-crawler-retrieval-access-audit-capacita`
5. `entity-authority-corroboration-capacita`
6. `marketing-page-visibility-review-capacita`

Runtime reusable vigente:

```text
SITEONE=READY
ADVERTOOLS=READY
PROMPTFOO=READY_NO_PAID_PROVIDER
SERPBEAR=CONFIG_VALIDATED/PENDING_PROVIDER_SECURITY_REVIEW
```

Reglas:

- no duplicar runtime dentro de Marketing;
- no crear credenciales, costos o providers sin autorización;
- SiteOne/advertools se usan cuando exista página real;
- Promptfoo sintético no equivale a ranking real AI Search;
- SerpBear permanece bloqueado hasta resolver provider/seguridad/costo.

Para issue #71 no se requiere una nueva skill: la capacidad existente es suficiente.

---

## Otros frentes vigentes — retomar sólo con sus canónicos

### Google Ads

Fuentes:

```text
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md
docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md
```

No modificar listas/campañas reales sin autorización. Preservar intención comercial y reglas históricas documentadas.

### Meta Ads

Fuentes:

```text
assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md
docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md
```

La cuenta operativa V3 sigue identificándose por inventario real de campañas y referencia sanitizada `...2327`, no por Business Portfolio.

### PageSense / CRO

Fuentes:

```text
docs/pagesense/PAGESENSE_CRO_REPORTING_BASELINE_V01.md
docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md
```

PageSense es señal CRO, no fuente de leads/matrículas. Zoho CRM sigue siendo fuente comercial agregada cuando corresponda.

---

## Reglas operativas vigentes

- No trabajar directo en `main`.
- No modificar campañas, presupuestos, pujas, anuncios, keywords, negativas, conversiones, landings productivas, GTM, PageSense, Zoho, Cloudflare, Worker, DNS, sitemap ni producción sin autorización explícita.
- No subir PII, secretos, tokens, exports crudos ni binarios.
- No inventar métricas, claims, IDs, eventos ni API names.
- Antes de retomar un frente histórico, leer `DECISIONES.md`, este archivo y el canónico específico; analizar sólo el delta.
- SharePoint/OneDrive Empresa sigue siendo bodega definitiva de pesados; GitHub conserva documentación y trazabilidad liviana.

## Gate actual

```text
NO_MERGEAR_TODAVIA
PENDING_FACTORY_READBACK
```
