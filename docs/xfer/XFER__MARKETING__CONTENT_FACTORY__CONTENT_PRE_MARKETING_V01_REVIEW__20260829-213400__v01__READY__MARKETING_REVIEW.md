# XFER — Marketing → Content Factory — Batch Editorial V01

## Estado

```text
FROM=misaeln-pc1/marketing-performance-capacita
TO=misaeln-pc1/capacita-content-factory
SOURCE_ISSUE=marketing-performance-capacita#71
SOURCE_BATCH=CONTENT_PRE_MARKETING_V01_2026-08-29
SOURCE_FACTORY_ISSUE=capacita-content-factory#16
SOURCE_FACTORY_PR=capacita-content-factory#17
SOURCE_FACTORY_HEAD=641213040cd9fe86b28885ba15ea6322808a6f4c
XFER_VERSION=v01
XFER_STATUS=READY
MARKETING_REVIEW=PASS_WITH_DELTAS
ARTICLES_READ=45/45
EXCEL=5/5
AI=20/20
POWER_BI=10/10
MICROSOFT_PROJECT=10/10
PUBLICATION=NO
CONTENT_READY_FOR_EDGE=NO
EDGE_HTML=NO
ADS_CHANGE=NO
MAIN_MERGE=NO
```

`READY` significa que este XFER está listo para ser consumido por Content Factory. **No significa que los 45 artículos estén autorizados para publicación o Edge.**

---

## 1. Fuentes y evidencia usada

### Canónicos

- Marketing: `TASK_STATUS.md`, `DECISIONES.md`, `PROJECT_CONTEXT.md`, `AGENTS.md`.
- Marketing: `docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md`.
- GTM/RevOps: `misaeln-pc1/capacita-global-control/docs/gtm-revops/BUYER_PERSONAS.md`, **v1.0.0**.
- Factory: los 45 artículos completos del commit fijado `641213040cd9fe86b28885ba15ea6322808a6f4c`.

### Demanda / SERP / mercado

- HYPD Keyword Research: Chile, español.
- HYPD SERP real Google Chile para consultas materiales por cluster, no 45 búsquedas mecánicamente repetidas.
- Sitio actual `capacita.cl` para canibalización/hubs existentes.
- Documentación oficial Microsoft/OpenAI/Google/Anthropic cuando una capacidad cambia con el producto.

### Data gaps

```text
GSC=DATA_GAP_PAYMENT_REQUIRED
GOOGLE_ADS_ACCOUNT_INVENTORY=NO_ACCOUNT_SELECTED_IN_SESSION
SEMRUSH=NOT_REQUIRED_FOR_THIS_CUT / FACTORY_REPORTED_INSUFFICIENT_API_UNITS
```

No se inventan rankings, tráfico propio, KD, CPC ni resultados comerciales faltantes. Keyword Planner/HYPD se usa como **señal**, no como decisión automática.

### Skills / reuse

```text
EXISTING_REUSABLE_METHOD=SUFFICIENT
NEW_SKILL_REQUIRED=NO
AI_OS_BLOCKING=NO
```

No se deriva trabajo adicional a Skills: Marketing ya dispone de protocolo y tooling suficiente para esta revisión. Sólo corresponde volver a AI OS si aparece una brecha reusable real.

---

## 2. Evidencia cuantitativa principal

Señales mensuales aproximadas observadas para Chile/español, útiles para ordenar investigación:

| Consulta | Señal aprox. |
|---|---:|
| `power bi` | 40.500 |
| `power bi desktop` | 3.600 |
| `power query` | 2.400 |
| `prompts chatgpt` | 1.300 |
| `dashboard power bi` | 1.000 |
| `power bi service` | 1.000 |
| `buscarv` | 1.000 |
| `dashboard excel` | 880 |
| `tablas dinamicas excel` | 880 |
| `agentes ia` | 590 |
| `power query excel` | 480 |
| `deep research` | 480 |
| `buscarx` | 390 |
| `agentes de ia` | 390 |
| `dax power bi` | 210 |
| `curso microsoft project` | 210 |
| `chatgpt pdf` | 210 |
| `chatgpt work` | 140 promedio; pico coyuntural ~1.600 en jul-2026 |
| `curva s project` | 110 |
| `copilot microsoft 365` | 110 |
| `copilot en excel` | 90 |
| `power query power bi` | 90 |

Notas:

- una keyword literal con bajo volumen puede pertenecer a un cluster con demanda alta;
- una keyword de marca puede ser principalmente navegacional;
- volumen alto no reemplaza intención, canibalización, fit comercial ni riesgo.

---

## 3. Canibalización y arquitectura detectada

### Excel

Capacita ya mantiene:

- `https://capacita.cl/funcion-buscarv-excel/`;
- `https://capacita.cl/cursos-vigentes/cursos-de-excel/`.

Por lo tanto:

```text
E01=UPDATE_EXISTING / MERGE_WITH_EXISTING
E02=NEW_SPOKE_POWER_QUERY
E03=NEW_SPOKE_COPILOT
E04=NEW_SPOKE_PYTHON
E05=PRODUCTIVITY_HUB
```

### IA

Arquitectura recomendada:

```text
IA01=PILLAR_IA_PARA_EL_TRABAJO
IA02=CHATGPT_DESDE_CERO
IA03=PROMPTS_OPERACIONALES
IA04=TOOL_SELECTION_HUB
IA05=AGENTES_EMPRESA
IA06=CHATGPT_WORK_COYUNTURAL
IA07=DEEP_RESEARCH
IA08=DOCUMENTOS_PDF
IA09=VERIFICACION
IA10=ALUCINACIONES
IA11=IA_EXCEL_HUB
IA14/IA15/IA16=PLATFORM_SPOKES
IA20=CAPACIDADES_EQUIPO_B2B
```

No fusionar IA09/IA10: son complementarios. Sí separar estrictamente IA11 de E03/E04.

### Power BI

Capacita ya tiene hub y landing comercial con Power Query, modelado, DAX y dashboards. Los artículos deben operar como capa informacional y enlazar al activo comercial; no copiar su promesa comercial.

```text
PBI01=INTRO_PILLAR_INFORMATIONAL
PBI03=POWER_QUERY_SPOKE
PBI04=DAX_SPOKE
PBI05=MODELING_SPOKE
PBI06=DASHBOARD/REPORT_DECISION_SPOKE
PBI07=DESKTOP_SERVICE_SPOKE
PBI08=COPILOT_SPOKE
PBI10=B2B_KPI_USE_CASE
```

### Microsoft Project

Capacita ya cubre en sus hubs/cursos actuales tareas, recursos, costos, ruta crítica, línea base, seguimiento, curva S y valor ganado.

Además, Microsoft retiró **Project for the web** en agosto de 2025 integrándolo en Planner, mientras **Project desktop** continúa soportado. Estos artículos deben mantener explícito el contexto `Project desktop` cuando describan funciones de escritorio.

```text
PRJ01+PRJ02=MERGE/PILLAR_OR_UPDATE_EXISTING
PRJ03-PRJ08=HOLD_URL_PENDING_ARCHITECTURE
PRJ09=FIRST_INDEPENDENT_URL_CANDIDATE
PRJ10=HOLD_URL_PENDING_ARCHITECTURE
```

---

## 4. TOP 10 recomendado para Factory

`E01` no entra como nueva pieza: es una acción separada de actualización del activo histórico.

| Orden | ID | Decisión | Prioridad | Keyword / enfoque |
|---:|---|---|---|---|
| 1 | E02 | `PASS_WITH_DELTA` | P0 | `power query excel` |
| 2 | IA03 | `PASS_WITH_DELTA` | P0 | `prompts chatgpt` |
| 3 | IA05 | `PASS_WITH_DELTA` | P0 | `agentes ia` |
| 4 | PBI06 | `PASS_WITH_DELTA` | P0 | `dashboard power bi` |
| 5 | PBI04 | `PASS_WITH_DELTA` | P0 | `dax power bi` + principiantes |
| 6 | IA06 | `PASS_WITH_DELTA` | P0 | `chatgpt work` / fast-track coyuntural |
| 7 | IA07 | `PASS_WITH_DELTA` | P0/P1 | `deep research` |
| 8 | E03 | `PASS_WITH_DELTA` | P1 | `copilot en excel` |
| 9 | PBI03 | `PASS_WITH_DELTA` | P1 | `power query power bi` |
| 10 | IA01 | `PASS_WITH_DELTA` | P1 | `inteligencia artificial para el trabajo` / pillar |

### Acción P0 adicional

```text
E01=MERGE_WITH_EXISTING
TARGET_EXISTING_URL=https://capacita.cl/funcion-buscarv-excel/
PRIMARY_INTENT=buscarv + modernización BUSCARX
DO_NOT_CREATE_DUPLICATE_URL=YES
```

---

## 5. Deltas exactos del Top 10

### E02 — Power Query en Excel

```text
CONTENT_ID=E02
PRIMARY_KEYWORD=CHANGE -> power query excel
SECONDARY_KEYWORDS=power query en excel | limpiar datos excel | transformar datos excel | automatizar limpieza excel
SEARCH_INTENT=informacional/práctica
SERP_EVIDENCE=AI Overview + PAA; Microsoft fuerte en documentación
DEMAND_EVIDENCE=power query excel ~480 vs frase candidata power query en excel ~30
CANNIBALIZATION_CHECK=WARN_THEME_ONLY
EXISTING_URL_IF_OVERLAP=https://capacita.cl/cursos-vigentes/cursos-de-excel/
COMPETITIVE_GAPS=flujo repetible real + actualización + control de errores, no sólo tutorial de botones
SEO_REQUIREMENTS=primary en title/H1 de forma natural; responder qué es/cuándo usar/qué automatiza
LOCAL_SEO_REQUIREMENTS=N/A
AEO_REQUIREMENTS=respuesta directa a qué es Power Query y diferencia con fórmulas/manual
GEO_AI_SEARCH_REQUIREMENTS=secciones autosuficientes, definición clara, ejemplos verificables
ENTITY_REQUIREMENTS=Excel | Microsoft Power Query | tablas | consultas | actualización
PRIORITY=P0
JOURNEY_STAGE=descubrimiento/consideración
BUYER_PERSONA=BP-001 v1.0.0
GTM_SOURCE=BUYER_PERSONAS.md v1.0.0
CTA=explorar capacitación Excel / consulta de curso
INTERNAL_LINK_STRATEGY=E05 + PBI03 + hub/cursos Excel
MUST_INCLUDE_DELTA=cambiar primary; diferenciar Power Query de trabajo manual y de DAX
MUST_NOT_CLAIM_DELTA=no prometer que elimina toda limpieza ni que reemplaza criterio de datos
FRESHNESS_REQUIREMENT=BAJA/MEDIA
IMAGE_MESSAGE_DELTA=sin cambio material; visual de flujo debe mostrar refresh/repetibilidad
MARKETING_DECISION=PASS_WITH_DELTA
```

### IA03 — Prompts

```text
CONTENT_ID=IA03
PRIMARY_KEYWORD=CHANGE -> prompts chatgpt
SEARCH_INTENT=informacional/práctica
SERP_EVIDENCE=SERP con OpenAI + listicles/guías; oportunidad de diferenciar por método operacional y verificación
DEMAND_EVIDENCE=prompts chatgpt ~1.300
CANNIBALIZATION_CHECK=PASS_INTERNAL_IF_LINKED
COMPETITIVE_GAPS=menos listas de prompts; más contrato de tarea, contexto, reglas, formato y verificación
PRIORITY=P0
JOURNEY_STAGE=descubrimiento/aprendizaje
BUYER_PERSONA=BP-001 v1.0.0
CTA=curso IA aplicada al trabajo
INTERNAL_LINK_STRATEGY=IA01 + IA02 + IA09 + IA10
MUST_INCLUDE_DELTA=mantener el método práctico propio; usar ChatGPT como query de entrada sin volver el artículo exclusivo de una interfaz
MUST_NOT_CLAIM_DELTA=no presentar prompts como garantía contra errores
FRESHNESS_REQUIREMENT=MEDIA
MARKETING_DECISION=PASS_WITH_DELTA
```

### IA05 — Agentes IA

```text
CONTENT_ID=IA05
PRIMARY_KEYWORD=CHANGE -> agentes ia
SEARCH_INTENT=informacional/empresa
SERP_EVIDENCE=AI Overview + proveedores enterprise; Google Cloud/IBM y similares compiten por definición
DEMAND_EVIDENCE=agentes ia ~590; agentes de ia ~390
CANNIBALIZATION_CHECK=PASS
COMPETITIVE_GAPS=Capacita puede diferenciar por READ/DRAFT/WRITE/SEND, permisos, gates, evidencia y procesos
PRIORITY=P0
JOURNEY_STAGE=consideración
BUYER_PERSONA=BP-004 v1.0.0
CTA=diagnóstico/capacitación IA para equipos
INTERNAL_LINK_STRATEGY=IA01 + IA20 + IA17
MUST_INCLUDE_DELTA=separar agente de chatbot simple; permisos y evidencia antes de acción
MUST_NOT_CLAIM_DELTA=no prometer autonomía segura ni ROI automático
FRESHNESS_REQUIREMENT=ALTA
MARKETING_DECISION=PASS_WITH_DELTA
```

### PBI06 — Dashboard Power BI

```text
CONTENT_ID=PBI06
PRIMARY_KEYWORD=CONFIRM -> dashboard power bi
SEARCH_INTENT=informacional/práctica
SERP_EVIDENCE=AI Overview/PAA; Microsoft distingue Dashboard de Report
DEMAND_EVIDENCE=dashboard power bi ~1.000
CANNIBALIZATION_CHECK=WARN_EXISTING_COMMERCIAL
EXISTING_URL_IF_OVERLAP=https://capacita.cl/cursos-vigentes/cursos-de-power-bi/
COMPETITIVE_GAPS=decisión/KPI/diseño + aclaración semántica de dashboard nativo vs report page
PRIORITY=P0
JOURNEY_STAGE=aprendizaje/consideración
BUYER_PERSONA=BP-001 v1.0.0
CTA=curso Power BI
INTERNAL_LINK_STRATEGY=PBI01 + PBI03 + PBI04 + PBI05 + landing/hub Power BI
MUST_INCLUDE_DELTA=explicar que Dashboard nativo pertenece al Service y no es igual a una report page; filtros/segmentadores son propios del reporte en este contexto
MUST_NOT_CLAIM_DELTA=no enseñar como Dashboard nativo una página de reporte filtrable
FRESHNESS_REQUIREMENT=MEDIA
IMAGE_MESSAGE_DELTA=hero y apoyos deben rotular claramente REPORT PAGE vs DASHBOARD SERVICE cuando corresponda
MARKETING_DECISION=PASS_WITH_DELTA
```

### PBI04 — DAX

```text
CONTENT_ID=PBI04
PRIMARY_KEYWORD=CHANGE -> dax power bi
SECONDARY_KEYWORD=dax para principiantes
SEARCH_INTENT=informacional/aprendizaje
DEMAND_EVIDENCE=dax power bi ~210 vs dax para principiantes ~10
CANNIBALIZATION_CHECK=WARN_THEME_ONLY
PRIORITY=P0
JOURNEY_STAGE=aprendizaje
BUYER_PERSONA=BP-001 v1.0.0
CTA=curso Power BI
INTERNAL_LINK_STRATEGY=PBI01 + PBI05 + PBI09
MUST_INCLUDE_DELTA=principiantes como modificador; no diluir el foco DAX/Power BI
MARKETING_DECISION=PASS_WITH_DELTA
```

### IA06 — ChatGPT Work

```text
CONTENT_ID=IA06
PRIMARY_KEYWORD=CONFIRM -> chatgpt work
SEARCH_INTENT=informacional/coyuntural
DEMAND_EVIDENCE=~140 promedio con pico ~1.600 en jul-2026 tras lanzamiento
CANNIBALIZATION_CHECK=PASS_IF_IA02_ONLY_SUMMARIZES
PRIORITY=P0_FAST_TRACK
JOURNEY_STAGE=descubrimiento/consideración
BUYER_PERSONA=BP-001 v1.0.0
CTA=curso IA aplicada al trabajo
INTERNAL_LINK_STRATEGY=IA02 + IA07 + IA01
MUST_INCLUDE_DELTA=fact-check de disponibilidad/capacidades inmediatamente antes de publicar
MUST_NOT_CLAIM_DELTA=no universalizar disponibilidad por plan/superficie
FRESHNESS_REQUIREMENT=MUY_ALTA
UPDATE_TRIGGER=cambio de producto, planes, rollout o capacidades Work
MARKETING_DECISION=PASS_WITH_DELTA
```

### IA07 — Deep Research

```text
CONTENT_ID=IA07
PRIMARY_KEYWORD=CHANGE -> deep research
SEARCH_INTENT=informacional/práctica
DEMAND_EVIDENCE=deep research ~480
CANNIBALIZATION_CHECK=PASS_IF_IA02_REMAINS_INTRO
PRIORITY=P0/P1
JOURNEY_STAGE=aprendizaje/consideración
BUYER_PERSONA=BP-001 v1.0.0
CTA=curso IA aplicada al trabajo
INTERNAL_LINK_STRATEGY=IA02 + IA08 + IA09
MUST_INCLUDE_DELTA=priorizar fuentes, plan de investigación, revisión y límites; no venderlo como verdad automática
FRESHNESS_REQUIREMENT=ALTA
MARKETING_DECISION=PASS_WITH_DELTA
```

### E03 — Copilot en Excel

```text
CONTENT_ID=E03
PRIMARY_KEYWORD=CONFIRM -> copilot en excel
SEARCH_INTENT=informacional/producto
DEMAND_EVIDENCE=copilot en excel ~90; señal reciente superior al baseline histórico
CANNIBALIZATION_CHECK=WARN_IA11
PRIORITY=P1
JOURNEY_STAGE=aprendizaje/consideración
BUYER_PERSONA=BP-001 v1.0.0
CTA=curso Excel / IA aplicada al trabajo según contexto
INTERNAL_LINK_STRATEGY=E02 + E05 + IA11
MUST_INCLUDE_DELTA=mantener E03 exclusivamente en Copilot; IA11 debe ser hub más amplio
MUST_NOT_CLAIM_DELTA=no asumir misma capacidad/licencia para todos los usuarios
FRESHNESS_REQUIREMENT=ALTA
MARKETING_DECISION=PASS_WITH_DELTA
```

### PBI03 — Power Query Power BI

```text
CONTENT_ID=PBI03
PRIMARY_KEYWORD=CONFIRM -> power query power bi
SEARCH_INTENT=informacional/práctica
DEMAND_EVIDENCE=power query power bi ~90 dentro de cluster Power Query mucho mayor
CANNIBALIZATION_CHECK=WARN_E02
PRIORITY=P1
BUYER_PERSONA=BP-001 v1.0.0
CTA=curso Power BI
INTERNAL_LINK_STRATEGY=E02 + PBI01 + PBI05
MUST_INCLUDE_DELTA=explicar frontera: E02 = flujo Excel; PBI03 = transformación antes del modelo Power BI
MARKETING_DECISION=PASS_WITH_DELTA
```

### IA01 — IA para el trabajo

```text
CONTENT_ID=IA01
PRIMARY_KEYWORD=CONFIRM -> inteligencia artificial para el trabajo
SEARCH_INTENT=informacional/práctica
DEMAND_EVIDENCE=keyword literal menor que marcas; prioridad estratégica por cluster y activo comercial IA
CANNIBALIZATION_CHECK=WARN_INTERNAL_PILLAR
PRIORITY=P1
JOURNEY_STAGE=descubrimiento
BUYER_PERSONA=BP-001 v1.0.0
CTA=curso IA aplicada al trabajo
INTERNAL_LINK_STRATEGY=funcionar como pillar hacia IA02/03/05/07/08/09/12/13 y artículos por plataforma
MUST_INCLUDE_DELTA=reducir profundidad de temas que tienen spoke propio; añadir enlaces naturales a los spokes
MUST_NOT_CLAIM_DELTA=no convertirse en mega-artículo que compita con todos los demás
MARKETING_DECISION=PASS_WITH_DELTA
```

---

## 6. Matriz 45/45

| ID | Decisión Marketing | Prioridad | Primary recomendado | Buyer persona | Delta principal |
|---|---|---:|---|---|---|
| E01 | `MERGE_WITH_EXISTING` | P0 acción | `buscarv` + `buscarx` secundario | BP-001 | modernizar URL histórica; no URL nueva |
| E02 | `PASS_WITH_DELTA` | P0 | `power query excel` | BP-001 | cambio keyword |
| E03 | `PASS_WITH_DELTA` | P1 | `copilot en excel` | BP-001 | separar IA11 + freshness |
| E04 | `PASS_WITH_DELTA` | P2 | `python en excel` | BP-001 | disponibilidad + complementariedad |
| E05 | `PASS_WITH_DELTA` | P2 | `automatizar excel` | BP-001 | convertir en hub productividad |
| IA01 | `PASS_WITH_DELTA` | P1 | `inteligencia artificial para el trabajo` | BP-001 | pillar, reducir solapamiento |
| IA02 | `PASS_WITH_DELTA` | P1 | `chatgpt para el trabajo` | BP-001 | sólo ChatGPT desde cero |
| IA03 | `PASS_WITH_DELTA` | P0 | `prompts chatgpt` | BP-001 | cambio keyword + método operacional |
| IA04 | `PASS_WITH_DELTA` | P1 | comparativa multi-tool | BP-001 | hub selección, no tutorial profundo |
| IA05 | `PASS_WITH_DELTA` | P0 | `agentes ia` | BP-004 | permisos/gates/evidencia |
| IA06 | `PASS_WITH_DELTA` | P0 | `chatgpt work` | BP-001 | fast-track/freshness |
| IA07 | `PASS_WITH_DELTA` | P0/P1 | `deep research` | BP-001 | cambio keyword + sources-first |
| IA08 | `PASS_WITH_DELTA` | P2 | `analizar pdf con inteligencia artificial` | BP-001 | supporting / trazabilidad |
| IA09 | `PASS_WITH_DELTA` | P1/P2 | `verificar respuestas inteligencia artificial` | BP-001 | método FACTS; cross-link IA10 |
| IA10 | `PASS_WITH_DELTA` | P1/P2 | `alucinaciones ia` | BP-001 | causas/prevención; cross-link IA09 |
| IA11 | `PASS_WITH_DELTA` | P1 | `inteligencia artificial en excel` | BP-001 | hub IA+Excel; no duplicar E03/E04 |
| IA12 | `PASS_AS_IS` | P2 | candidata actual | BP-001 | supporting content |
| IA13 | `PASS_AS_IS` | P2 | candidata actual | BP-001 | supporting content |
| IA14 | `PASS_WITH_DELTA` | P2 | `gemini en google workspace` | BP-001 | spoke + freshness |
| IA15 | `PASS_WITH_DELTA` | P1/P2 | `copilot microsoft 365` | BP-001 | keyword más compacta + freshness |
| IA16 | `PASS_WITH_DELTA` | P2 | `claude para el trabajo` | BP-001 | spoke + freshness |
| IA17 | `PASS_WITH_DELTA` | P2 | candidata actual | BP-004 | higher review privacidad/claims |
| IA18 | `PASS_WITH_DELTA` | P2 | `inteligencia artificial recursos humanos` | BP-000 | no decision automation / higher review |
| IA19 | `PASS_WITH_DELTA` | P1/P2 | candidata actual | BP-001 | B2B use cases, no integración inventada |
| IA20 | `PASS_WITH_DELTA` | P1 | candidata actual | BP-003 | estratégico B2B / competencias |
| PBI01 | `PASS_WITH_DELTA` | P1 | `power bi desde cero` | BP-001 | separar de landing comercial |
| PBI02 | `PASS_AS_IS` | P1 | `excel vs power bi` | BP-001 | comparativa clara |
| PBI03 | `PASS_WITH_DELTA` | P1 | `power query power bi` | BP-001 | frontera con E02 |
| PBI04 | `PASS_WITH_DELTA` | P0 | `dax power bi` | BP-001 | cambio keyword |
| PBI05 | `PASS_AS_IS` | P1 | `modelo de datos power bi` | BP-001 | autoridad técnica |
| PBI06 | `PASS_WITH_DELTA` | P0 | `dashboard power bi` | BP-001 | corregir Dashboard vs Report |
| PBI07 | `PASS_WITH_DELTA` | P1 | `power bi desktop vs service` | BP-001 | freshness/product boundary |
| PBI08 | `PASS_WITH_DELTA` | P1/P2 | `copilot power bi` | BP-001 | freshness/requisitos |
| PBI09 | `PASS_AS_IS` | P2 | candidata actual | BP-001 | supporting content |
| PBI10 | `PASS_WITH_DELTA` | P1 | `power bi para empresas` | BP-004 | KPI ilustrativos, no canónicos |
| PRJ01 | `MERGE_WITH_EXISTING` | HOLD | pendiente arquitectura | BP-000 | solapa PRJ02 + hub Project |
| PRJ02 | `MERGE_WITH_EXISTING` | HOLD | pendiente arquitectura | BP-000 | solapa PRJ01 + hub Project |
| PRJ03 | `HOLD` | P3 | candidata actual | BP-000 | conservar texto; no URL aún |
| PRJ04 | `HOLD` | P2/P3 | candidata actual | BP-000 | conservar texto; no URL aún |
| PRJ05 | `HOLD` | P3 | candidata actual | BP-000 | conservar texto; no URL aún |
| PRJ06 | `HOLD` | P3 | candidata actual | BP-000 | conservar texto; no URL aún |
| PRJ07 | `HOLD` | P3 | candidata actual | BP-000 | conservar texto; no URL aún |
| PRJ08 | `HOLD` | P2/P3 | candidata actual | BP-000 | conservar texto; no URL aún |
| PRJ09 | `HOLD` | P2 | `curva s project` | BP-000 | primera candidata independiente; cerrar arquitectura antes |
| PRJ10 | `HOLD` | P2/P3 | candidata actual | BP-000 | conservar texto; no URL aún |

`BP-000` se usa deliberadamente cuando el perfil técnico del lector no encaja con suficiente precisión en los buyer personas canónicos; no se fuerza un match.

---

## 7. NEXT 10

```text
PBI01
PBI02
PBI05
PBI07
IA02
IA04
IA11
IA20
PBI10
PRJ09
```

### Backlog controlado

```text
E04 E05
IA08 IA09 IA10 IA12 IA13 IA14 IA15 IA16 IA17 IA18 IA19
PBI08 PBI09
PRJ03 PRJ04 PRJ05 PRJ06 PRJ07 PRJ08 PRJ10
```

Backlog no significa rechazo: significa no invertir primero en assets/Edge cuando el beneficio marginal es menor o falta arquitectura.

---

## 8. Briefs visuales — revisión Marketing

Los briefs son conceptualmente utilizables y no requieren render antes del cierre editorial.

Cambios obligatorios:

- **PBI06:** todo visual debe distinguir `Report page` de `Dashboard (Service)` cuando corresponda.
- **E01:** no generar paquete visual para una URL nueva; adaptar a actualización del artículo histórico.
- **IA06 / IA07 / E03 / IA14 / IA15 / IA16 / PBI08:** evitar capturas o claims de interfaz que queden obsoletos rápidamente; priorizar diagramas conceptuales originales y verificar cualquier UI antes de producción.
- **Project:** no generar los 60 assets del bloque mientras las URLs estén `HOLD`; evita retrabajo.

```text
IMAGE_BRIEFS_MESSAGE_REVIEWED=YES
RENDER_IMAGES_NOW=NO
STYLE_PROFILE_REQUIRED_BEFORE_FINAL_ASSETS=YES
```

---

## 9. Qué debe hacer Content Factory

### Aplicar ahora

1. Corregir los deltas del Top 10.
2. Preparar E01 como actualización/merge del artículo histórico, no como nueva URL.
3. Aplicar arquitectura de hubs/spokes IA y Power BI.
4. Corregir PBI06 Dashboard vs Report.
5. Mantener Project como contenido editorial preservado, pero no pasar las 10 piezas a assets/Edge.
6. Revalidar facts coyunturales inmediatamente antes del QA final de IA06/IA07/E03/IA14/IA15/IA16/PBI08.

### No hacer todavía

- no generar 270 assets finales;
- no crear HTML;
- no publicar;
- no decidir redirects productivos;
- no tocar sitemap/canonical/robots;
- no modificar Ads;
- no convertir buyer personas emergentes en canónicos;
- no mergear `main` por efecto de este XFER.

---

## 10. DoD Marketing

```text
BATCH_45_READ=YES
KEYWORDS_REVIEWED=YES
INTENT_REVIEWED=YES
SERP_DEMAND_CHECKED=YES_WITH_DECLARED_GSC_GAP
CANNIBALIZATION_CHECKED=YES
COMPETITIVE_GAPS_REVIEWED=YES_PROPORTIONAL_BY_CLUSTER
SEO_AEO_GEO_REVIEWED=YES_EDITORIAL_STAGE
PRIORITY_ASSIGNED=YES
CTA_ASSIGNED=YES_TOP10
TOP_10_SELECTED=YES
IMAGE_BRIEFS_MESSAGE_REVIEWED=YES
XFER_TO_CONTENT_FACTORY=READY
PUBLICATION=NO
EDGE_HTML=NO
MAIN_MERGE=NO
```

## 11. Cierre y retorno esperado

Content Factory debe consumir este XFER como mayor versión vigente del caso y devolver sólo el delta aplicado:

```text
RETURN_TO=marketing-performance-capacita#71
EXPECTED_FACTORY_STATUS=CONSUMED_PASS|CONSUMED_WITH_GAPS
EXPECTED_EVIDENCE=commit + diff + QA + lista de CONTENT_ID modificados
```

Marketing mantiene #71 abierto hasta revisar el readback de Factory. Después del `CONSUMED_PASS`, los artículos priorizados pueden pasar a QA editorial final/Style Profile/assets y posterior handoff a Edge bajo sus gates.