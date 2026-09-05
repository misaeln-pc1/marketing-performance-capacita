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

Documento de benchmark:

`docs/research/IA_TRABAJO_PRESENCIAL_SANTIAGO_MARKET_BENCHMARK_V01_2026-08-23.md`

Baseline consumidor verificado en Diseño de Cursos:

```text
COURSE_CODE=IA-TRAB-01
ACTIVE_VARIANT=IA-TRAB-01-PRES-V1
DURATION=16h
MODALITY=PRESENCIAL_SANTIAGO
PRICE=CLP 178000
PRIMARY_KEYWORD=curso inteligencia artificial
VALUE_PROPOSITION=IA aplicada al trabajo
```

Benchmark V01 identifica competencia presencial real en Artificiales, ClasesIA, UDD y NobleProg; Conekta Capacita queda como competidor directo por propuesta de valor pero con modalidad de la edición no inequívoca en su página. UAI, ESE y Universidad de Chile quedan como referencias online/sincrónicas. El próximo delta material se ejecuta cuando la Fábrica entregue preview/URL de Capacita.

Este frente no fue reemplazado ni cancelado por issue #71; queda en espera de preview/URL.

## Frente SEO / AEO / GEO / AI Search — estado vigente

### Skills AI OS

AI OS PR #55 quedó `MERGED / VIGENTE_EN_MAIN`, merge SHA:

`62575085c041796d67d8f49c0845c8668cc26ed3`

Skills disponibles para evaluación/uso local bajo gate de Marketing:

1. `seo-demand-serp-research-capacita`
2. `aeo-ai-readability-capacita`
3. `geo-ai-search-benchmark-capacita`
4. `ai-crawler-retrieval-access-audit-capacita`
5. `entity-authority-corroboration-capacita`
6. `marketing-page-visibility-review-capacita`

Estado de biblioteca: `0.1.0 draft/candidate`. No requieren `approved` global para uso local controlado.

### Runtime técnico reusable

Toolchain PR #2 quedó `MERGED / VIGENTE_EN_MAIN`.

- repo: `misaeln-pc1/capacita-search-intelligence-toolchain`
- head validado: `fe829a42e5348c745a8dc5fecebdbfd03dce9ee6`
- merge SHA: `fb5c4a9df255953fa6bad59a8866ddf610474d1b`

AI OS PR #56 quedó `MERGED / VIGENTE_EN_MAIN`, merge SHA:

`901c27a77f6c1fe06c1067723267314918dfb4d3`

Estado de consumo:

```text
SITEONE=READY
ADVERTOOLS=READY
PROMPTFOO=READY_NO_PAID_PROVIDER
SERPBEAR=CONFIG_VALIDATED/PENDING_PROVIDER_SECURITY_REVIEW
```

Reglas críticas:

- SiteOne: usar para crawl técnico, render opt-in, HTML/JSON/texto/Markdown y `AI_READABILITY_TEST`.
- advertools: usar para robots, sitemap multi-source, estructura URL/crawl y términos; no sustituye GSC/Keyword Planner como fuente de demanda.
- Promptfoo: usar sólo como benchmark sintético/reproducible mientras no exista provider real autorizado. `PROMPTFOO_SYNTHETIC_BENCHMARK != REAL_AI_SEARCH_RANKING`.
- SerpBear: no iniciar. Sigue bloqueado por provider + security review en `capacita-search-intelligence-toolchain#1`.
- No duplicar instalación o runtime dentro de Marketing.
- No crear credenciales, costos o providers sin autorización explícita.
- Para issue #71 no se requiere una skill nueva; la capacidad reusable existente es suficiente.

## Piloto real completado

URL piloto:

`https://capacita.cl/curso-excel-intermedio-avanzado-presencial-santiago`

Resultados relevantes:

- SiteOne: PASS, HTTP 200, canonical/indexabilidad, estructura, JSON-LD y Markdown utilizable para AI-readability.
- advertools: PASS, crawl HTTP 200 y sitemap multi-source corregido.
- Sitemap WordPress: 415 URLs / target `false`.
- Sitemap estático: 6 URLs / target `true`.
- Agregado deduplicado: 416 URLs / target `true`.
- `FALSE_NEGATIVE_SITEMAP_FIXED=PASS`.
- Marketing issue #65: `CLOSED / TOOL_FALSE_NEGATIVE_RESOLVED / NO_WEB_CHANGE_REQUIRED`.
- Promptfoo: 2/2 casos sintéticos PASS, costo/tokens/credenciales = 0.
- SerpBear: configuración validada, runtime no iniciado.

La landing no requirió cambio web por el hallazgo de sitemap.

## Regla de continuidad

Antes de recomendar sobre un frente ya trabajado, leer `DECISIONES.md`, este archivo y el documento canónico específico. Aplicar primero la decisión vigente y analizar sólo evidencia nueva o delta. No reiniciar estrategia desde recomendaciones genéricas de plataforma.

## Google Ads — frente separado vigente

Fuentes principales al retomarlo:

```text
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md
docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md
```

Reglas vigentes:

- priorizar intención de asistir/comprar curso;
- preservar negativas históricas de solución puntual mientras no exista evidencia real que justifique retirarlas;
- excluir deliberadamente intención informativa puntual y empleo cuando corresponda;
- `paso a paso` no es negativa global;
- separar exclusión global de tráfico versus routing A/B/C a nivel grupo;
- no modificar listas reales sin autorización explícita.

Baseline Excel B2C pagado:

- Landing A: Curso Excel Básico-Intermedio presencial, `BP-001`.
- Landing B: Excel desde cero presencial, `BP-002`.
- Landing C: clases de Excel presenciales con profesor, `BP-001`.
- Las tres venden el mismo curso grupal presencial Básico-Intermedio en Santiago Centro.
- Parten `noindex,follow`, fuera de sitemap y navegación orgánica.
- La página orgánica actual se conserva protegida.

## Meta Ads / Facebook Ads

Fuentes vigentes:

```text
assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md
docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md
```

Reglas críticas:

- cuenta operativa V3: cuenta personal/standalone bajo `Otros activos`, referencia sanitizada `...2327`;
- no identificar la cuenta por Business Portfolio;
- no propagar restricciones históricas entre activos sin evidencia;
- creatividades como set por placement; video 9:16 para Stories/Reels y 4:5 para Feed cuando aplique;
- no subir assets pesados a GitHub.

## PageSense / CRO

Fuentes vigentes:

```text
docs/pagesense/PAGESENSE_CRO_REPORTING_BASELINE_V01.md
docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md
```

- PageSense es fuente complementaria de CRO, no fuente de leads ni matrículas.
- Goals de clic no equivalen a submits confirmados.
- Zoho CRM sigue siendo fuente de verdad comercial.
- Nombre/correo en URL de redirección B2C sigue siendo riesgo rojo de privacidad y debe resolverse fuera de Marketing con autorización específica.

## Archivos pesados

- GitHub conserva Markdown, manifests, hashes, síntesis y trazabilidad liviana.
- Bodega definitiva: SharePoint/OneDrive Empresa.
- `external-files/marketing-performance-capacita` es staging local operativo.
- Google Drive o Cloudflare R2 sólo se usan como capas específicas cuando exista decisión documentada; no son la bóveda canónica general.

## Reglas operativas vigentes

- No trabajar directo en `main`.
- No modificar campañas, presupuesto, pujas, anuncios, keywords, negativas, conversiones, landings productivas, GTM, PageSense, Turnstile, Zoho, Cloudflare, Worker, DNS ni sitemap sin autorización explícita.
- No subir PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios.
- No inventar métricas, claims, IDs, eventos ni API names.
- Mantener un buyer persona primario y una hipótesis por prueba.
- Separar B2C y B2B en campaña, landing y medición.
- No usar SENCE, franquicia, beneficio tributario, gratuidad ni promesas garantizadas en B2C.

## Secuencia inmediata

1. Content Factory consume el XFER de issue #71 y devuelve readback con commit/diff/QA.
2. Marketing revisa sólo ese delta y mantiene #71 abierto hasta `CONSUMED_PASS` o gaps explícitos.
3. El frente IA landing continúa cuando exista preview/URL, sin mezclarlo con el batch editorial.
4. Reutilizar GSC, Keyword Planner, SERP y evidencia existente antes de generar nueva investigación; declarar data gaps si una fuente no está disponible.
5. Usar SiteOne + advertools como evidencia técnica/readability cuando exista página real; Promptfoo sólo como benchmark sintético controlado.
6. Mantener SerpBear bloqueado hasta resolver provider, seguridad, retención, owner y costo.
7. Retomar Google Ads/Meta Ads por separado cuando Misael lo indique, leyendo primero sus canónicos específicos.

## Estado de frentes históricos

Los estados detallados de PR/issues anteriores al 2026-08-29 deben revalidarse al retomar cada frente. No usar una tabla histórica como estado vivo sin readback del PR/issue correspondiente.

## Gate actual

```text
NO_MERGEAR_TODAVIA
PENDING_FACTORY_READBACK
```
