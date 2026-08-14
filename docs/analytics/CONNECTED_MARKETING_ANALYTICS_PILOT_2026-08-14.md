# Connected Marketing Analytics Pilot — 2026-08-14

## Estado

- Context Gate: `Bootstrap`.
- Riesgo: **amarillo metodológico**; sólo lectura y documentación sanitizada.
- Repo dueño: `misaeln-pc1/marketing-performance-capacita`.
- Rama: `docs/marketing-connected-analytics-pilot-20260814`.
- No hay writes en Ads, GA4, CRM, landing, Cloudflare, GTM productivo, WhatsApp ni producción.
- No se crea OAuth ni se versionan secretos, PII, IDs completos, exports crudos o binarios.
- Piloto de negocio: **Excel B2C presencial Santiago**.

## 1. Fuentes y baseline recuperado

### Gobernanza

- Global vigente: V5.1 `ACTIVA_VALIDADA`; Global controla/documenta y el consumidor conserva ejecución, datos y evidencia local.
- AI OS V2.1: aplicar `Reuse Before Reinvent`; `reuse_decision` no equivale a estado lifecycle `approved`.
- Handoff canónico: `capacita-ai-operating-system/docs/handoffs/MARKETING_CONNECTED_ANALYTICS_SKILLS_HANDOFF_2026-08.md`.
- AI OS issue `#40`; PR `#41`; merge SHA `40ec5d26ec86d71a176dcf0c6bb526aa4c85aed7`.

### Google Ads

Baseline preservado:

- PR #14: pipeline API read-only.
- PR #17: Basic Access y primera ejecución.
- PR #18: PowerShell fast path.
- PR #26: export histórico read-only.
- PR #28: antecedente V02 **cerrado sin merge**; no se usa como fuente vigente paralela.
- PR #29: recuperación de search terms y landing pages, mergeado.
- PR #11: intento MCP antiguo; el PR fue mergeado, pero documentó que entonces el MCP no estaba disponible/autenticado. No invalida la ruta API actual.
- `docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md`: política vigente de negativas y routing A/B/C.
- `docs/google-ads/GOOGLE_ADS_POWERSHELL_FAST_PATH.md`: ruta validada.
- `docs/google-ads/GOOGLE_ADS_STATUS_ANALYSIS_PROCEDURE_V01.md`: estado completo = API fresca + histórico Drive; sólo una fuente = provisional.
- `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md`: diagnóstico sanitizado previo.
- Histórico conectado: `Historial_Rendimiento_GoogleAds`, con datos observados hasta `2026-08-13`.

### Meta Ads

- `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md`: routing canónico vigente; la cuenta operativa de V3 se identifica por inventario/campaña, no por asumir un portfolio comercial.
- Ruta operativa: `ads_read`; sin `ads_management`.
- PR #52 documenta Ruta A read-only y sigue sin ser fuente canónica mergeada por sí sola.
- El baseline operativo actual no se sustituye por un conector/MCP sólo por existir.

### Landing / GTM / atribución

- `docs/GTM_CONSUMPTION_BRIDGE.md` vigente.
- `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md`: BP-001 primario, BP-002 secundario; la V3 no se evalúa sólo por clics.
- `docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md`: routing A/B/C por intención; una hipótesis y buyer persona primario por prueba.
- `docs/audits/PAID_ADS_PERFORMANCE_BRIDGE_V1.md`: puente conceptual previo. La referencia histórica a `references/zoho-crm/MAPEO_LEADS_META_ADS.md` ya no existe en `main`; no se reutiliza como mapping vigente.

## 2. Decisión de skills P0

| Skill upstream | Decisión reusable | Qué se reutiliza | Delta Capacita obligatorio |
|---|---|---|---|
| Google `google-ads-api-account-diagnostics` / account performance diagnostics | `ADAPTAR_MINIMO` | secuencia de diagnóstico de pérdida de conversión, bajo flujo, impression share, device, conversion actions, change events | CLP, campañas reales Capacita, negativas canónicas, search terms, keywords, landings, UTMs/click IDs y downstream CRM; no WRITE |
| Anthropic Marketing `performance-report` | `ADAPTAR_MINIMO` | resumen ejecutivo, tendencias, wins/misses, priorización impacto/esfuerzo | Google + Meta + GA4 + landing + CRM + resultado comercial; no confundir conversión de plataforma con venta |
| Anthropic Marketing `competitive-brief` | `ADAPTAR_MINIMO` | posicionamiento, mensajes, pricing público, content gaps, oportunidades y amenazas | un producto prioritario Capacita, fuentes primarias cuando existan, Ads Library sólo pública, sin inventar tráfico/ventas/ROAS/presupuesto |

Ninguna skill cambia su estado lifecycle a `approved` por este trabajo.

## 3. Contrato de análisis y atribución

Todo hallazgo debe separar:

```text
HECHO
INTERPRETACIÓN
RECOMENDACIÓN
ACCIÓN PROPUESTA
```

Capas que **nunca** se colapsan:

```text
ADS_PLATFORM_SIGNAL
!= GA4_SITE_SIGNAL
!= CRM_LEAD_OR_CONTACT
!= DEAL
!= CURSOALUMNO
!= VENTA_REAL
```

### Contrato mínimo de salida

| Capa | Señales permitidas | Fuente de verdad |
|---|---|---|
| Ads | gasto, impresiones, clics, conversiones/acciones de plataforma | Google Ads / Meta Ads |
| Web | sesión, usuario, source/medium/campaign, landing, key event, funnel/drop-off | GA4 / Edge |
| CRM | lead/contact, contactado, respondido, calificado | Zoho CRM |
| Pipeline | Deal creado/ganado/perdido | Zoho CRM Deals |
| Operación | CursoAlumno vinculado | módulo dueño de CursoAlumno |
| Comercial | venta real/valor confirmado | fuente comercial/contable autoritativa definida para el caso |

### Claves conceptuales

Persistir sólo agregados sanitizados. Cuando existan y estén validadas, usar:

- fecha y canal;
- campaign / ad group o ad set / ad o creative;
- keyword / search term;
- landing normalizada / `landing_code`;
- `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`;
- presencia de click ID, no el valor crudo en GitHub;
- conteos por cada capa del funnel.

Los API names reales de CRM deben validarse antes del join. No se infieren desde documentos históricos ausentes.

### Confianza del join

```text
DIRECT_ID
UTM_MATCH
AGGREGATE_ONLY
UNATTRIBUTED
```

Nunca convertir `AGGREGATE_ONLY` en atribución individual.

## 4. Micro-piloto Google Ads: API/PowerShell vs MCP oficial

### Objetivo

Comparar, no migrar:

```text
METHOD_A = API/POWERSHELL ACTUAL
METHOD_B = GOOGLE ADS MCP OFICIAL
```

El MCP oficial actual se trata como candidato read-only. La ruta API/PowerShell sigue siendo fallback validado.

### Condiciones de paridad

- misma cuenta, identificada de forma sanitizada;
- mismas ventanas: 7 y 30 días completos;
- misma zona horaria y CLP;
- mismos filtros de estado/canal;
- misma agregación;
- ningún WRITE;
- registrar correcciones manuales, errores y pasos necesarios;
- no persistir secretos ni IDs completos.

### Preguntas idénticas

| # | Tarea | METHOD_A | METHOD_B | Winner |
|---:|---|---|---|---|
| 1 | campañas activas | baseline disponible | ejecutar piloto | `PENDING_PILOT` |
| 2 | gasto 7/30 días | baseline disponible | ejecutar piloto | `PENDING_PILOT` |
| 3 | performance por campaña | baseline disponible | ejecutar piloto | `PENDING_PILOT` |
| 4 | search terms | baseline disponible | ejecutar piloto | `PENDING_PILOT` |
| 5 | keywords | baseline disponible | ejecutar piloto | `PENDING_PILOT` |
| 6 | Quality Score cuando exista | baseline disponible | ejecutar piloto | `PENDING_PILOT` |
| 7 | landing pages | baseline disponible | ejecutar piloto | `PENDING_PILOT` |
| 8 | device/network | baseline disponible | ejecutar piloto | `PENDING_PILOT` |
| 9 | conversion actions | baseline disponible | ejecutar piloto | `PENDING_PILOT` |
| 10 | datos faltantes | registrar | registrar | `PENDING_PILOT` |
| 11 | tiempo/corrección manual | medir | medir | `PENDING_PILOT` |
| 12 | mantenimiento | estimar evidencia real | estimar evidencia real | `PENDING_PILOT` |

### Criterio de decisión

`METHOD_B` sólo reemplaza una tarea si:

1. entrega paridad de significado y agregación sin divergencia inexplicada;
2. reduce materialmente copy/paste, transformaciones o correcciones manuales;
3. no aumenta dependencia de secretos/OAuth nuevos para Marketing;
4. conserva las señales necesarias para el diagnóstico;
5. no introduce superficie WRITE en el flujo de análisis.

Salida obligatoria:

```text
WINNER_BY_TASK
FALLBACK=METHOD_A
NO_MIGRATION_IF_NO_MATERIAL_GAIN=YES
```

## 5. Requisitos GA4 vía Google Analytics MCP

Marketing necesita consultar, en modo lectura:

1. cuentas y propiedades accesibles;
2. metadata de propiedad;
3. usuarios y sesiones;
4. source / medium / campaign;
5. landing pages;
6. key events;
7. funnel y drop-off;
8. realtime sólo cuando sea útil para una incidencia o lanzamiento;
9. custom dimensions/metrics existentes;
10. Google Ads links;
11. device cuando explique una diferencia;
12. fecha/zona horaria consistente con Ads.

No crear custom dimensions, eventos, credenciales u OAuth desde este trabajo. `GA4 key event` sigue siendo distinto de `lead CRM`.

## 6. Decisión Meta connector/MCP

### Hecho

Meta mantiene públicamente una capa de Ads AI Connectors en open beta para trabajar con herramientas de IA de terceros. La ruta Capacita validada hoy sigue siendo API `ads_read` con account routing canónico.

### Interpretación

El conector oficial puede reducir copy/paste, pero su mera existencia no prueba mejor cobertura, autenticación más estable o mejor diagnóstico que la API actual. Además, Marketing no necesita WRITE para este caso.

### Recomendación

```text
KEEP_CURRENT_API_ADS_READ_AS_BASELINE
PILOT_OFFICIAL_META_CONNECTOR_READ_ONLY_IF_ALREADY_AVAILABLE_AUTHENTICATED
NO_MIGRATION_WITHOUT_MATERIAL_GAIN
```

Comparar como mínimo:

- account inventory/routing;
- campaign/adset/ad status;
- gasto 7/30;
- impresiones, alcance, frecuencia;
- clicks/landing page views cuando estén disponibles;
- metadata de anuncio/creative;
- errores, pasos manuales y mantenimiento.

Patrones comunitarios útiles para **extraer**, no adoptar ciegamente: read-only por defecto, writes opt-in, confirm/dry-run, límites de presupuesto y acceso público a Ads Library cuando corresponda.

## 7. Primer piloto E2E — Excel B2C presencial Santiago

Estado de lectura: **provisional**. Se recuperó el histórico conectado hasta `2026-08-13`, pero el procedimiento canónico exige combinarlo con una lectura API/MCP fresca equivalente para declarar estado completo.

### 7.1 Performance Google — últimos 7 días observados

Ventana `2026-08-07` a `2026-08-13` de `EXCEL-PRE-STGO`:

- 54 clics;
- 416 impresiones;
- gasto aproximado CLP 49.539;
- 5 conversiones **de plataforma**;
- CTR aproximado 12,98%;
- CPC aproximado CLP 917;
- CVR de plataforma aproximada 9,26%;
- CPA de plataforma aproximado CLP 9.908.

Ventana anterior comparable `2026-07-31` a `2026-08-06`:

- 77 clics;
- 521 impresiones;
- gasto aproximado CLP 84.368;
- 6 conversiones de plataforma;
- CPC aproximado CLP 1.096;
- CVR de plataforma aproximada 7,79%;
- CPA de plataforma aproximado CLP 14.061.

**HECHO:** baja el volumen y el gasto; mejora CPC, CVR y CPA de plataforma en la ventana reciente.

**INTERPRETACIÓN:** hay señal de mejor eficiencia de plataforma, no evidencia suficiente de mejora comercial.

**RECOMENDACIÓN:** no escalar ni recortar por este indicador hasta unir GA4 + CRM downstream.

**ACCIÓN PROPUESTA:** repetir exactamente esta lectura con METHOD_A y METHOD_B en el piloto de paridad.

### 7.2 Keyword crítica

`curso excel básico e intermedio`, misma ventana reciente:

- 34 clics;
- gasto aproximado CLP 33.072;
- 2 conversiones de plataforma;
- CPA de plataforma aproximado CLP 16.536;
- concentra cerca de 63% de los clics y 67% del gasto de la campaña, pero 40% de sus conversiones de plataforma.

**HECHO:** sigue concentrando gasto con eficiencia inferior al promedio de campaña.

**INTERPRETACIÓN:** es la señal prioritaria de mezcla de intención/routing; no demuestra por sí sola una negativa necesaria.

**RECOMENDACIÓN:** aplicar primero la política canónica de intención y routing A/B/C.

**ACCIÓN PROPUESTA:** analizar search terms + destino + GA4 + downstream antes de cualquier cambio de keyword/negativa.

### 7.3 Search term

El `2026-08-13`, `clases de excel basico` registró la única conversión de plataforma visible de ese día dentro del conjunto observado y fue activado por la keyword crítica.

**HECHO:** existe una señal puntual de intención `clases`.

**INTERPRETACIÓN:** una observación diaria/una conversión no permite declararlo ganador.

**RECOMENDACIÓN:** tratarlo como evidencia para routing experimental, no como decisión de negativa o expansión.

**ACCIÓN PROPUESTA:** medir el cluster de intención en 7/30 días y con downstream.

### 7.4 Landing

El `2026-08-13`, la landing principal de Excel presencial recibió 5 clics y registró 1 conversión de plataforma; una página legacy de Excel básico recibió 1 clic y 0 conversiones. El histórico continúa mostrando tráfico/impresiones hacia URLs legacy u otras rutas.

**HECHO:** la landing principal es el mejor destino observado a nivel de conversión de plataforma en esta lectura puntual; persiste fuga de destino.

**INTERPRETACIÓN:** no demuestra todavía qué variante A/B/C produce mejor lead o venta.

**RECOMENDACIÓN:** preservar la landing principal como control y cerrar atribución antes de multiplicar destinos.

**ACCIÓN PROPUESTA:** GA4 debe mostrar landing → key event → submit; CRM debe confirmar lead/contact/Deal/CursoAlumno/venta.

### 7.5 Creative

`DATA_GAP`.

- Google: el baseline histórico no ofrece un test creativo comparable suficiente para declarar ganador.
- Meta: existe baseline/routing V3, pero en este run no se realizó una lectura conectada de métricas Meta por anuncio.

No se declara creative ganador.

### 7.6 Downstream comercial

```text
GA4 = DATA_GAP
Lead/Contact = DATA_GAP
Deal = DATA_GAP
CursoAlumno = DATA_GAP
Venta real = DATA_GAP
Lead quality = DATA_GAP
```

El conector CRM está disponible en lectura, pero el mapping canónico de API names de atribución debe validarse antes de unir datos. No se consulta PII ni se infiere un mapping inexistente.

## 8. Competitive brief V1 — B2C Excel presencial Santiago

Investigación pública al `2026-08-14`. No se inventan tráfico, ventas, ROAS, presupuestos o conversiones de terceros.

| Competidor | Evidencia pública relevante | Amenaza / oportunidad |
|---|---|---|
| Activa Latam | talleres prácticos; Excel; presencial Santiago Centro; 12 h; precio público observado CLP 85.000; material/certificación/coffee; promoción por referido | **amenaza directa** por geografía + precio + propuesta práctica; Capacita no debe responder sólo con descuento |
| EFTEC | Excel Básico 30 h; presencial; oferta a particulares/empresas; SENCE; enfoque personalizado y mundo laboral; precio público observado CLP 228.000 | oportunidad para posicionar Capacita entre alternativa económica y oferta premium, con acompañamiento práctico verificable |
| INACAP | Educación Continua; Excel básico/intermedio presencial de 30 h; fuerte marca institucional; calendarios públicos muestran valores variables según convenio/sede | amenaza de confianza/marca; oportunidad para competir en agilidad, grupo acotado y experiencia guiada, sin reclamar superioridad no demostrada |
| Pro-Active | registro público secundario observado: Excel Básico presencial Santiago, 20 h, precio CLP 140.000 | referencia media de precio/duración; requiere validación primaria adicional antes de usar como benchmark fuerte |

### Gaps competitivos

- `REVIEWS=DATA_GAP`: no se completó una muestra robusta y comparable de reviews verificadas.
- `ADS_LIBRARY=DATA_GAP`: no se fuerza login/captcha ni se atribuyen anuncios sin página/identidad confirmada.
- `SEO_TRAFFIC=DATA_GAP`: se pueden comparar temas y mensajes visibles, no tráfico estimado como hecho.
- precio público actual de Capacita: tratar como `DATA_GAP/por confirmar` cuando la landing vigente lo indique; no rescatar un precio histórico como actual.

### Lectura

**HECHO:** Activa Latam presenta la superposición más directa observada por Santiago Centro, propuesta práctica y precio público bajo.

**INTERPRETACIÓN:** la amenaza principal para el piloto es una propuesta suficientemente parecida a menor precio, no necesariamente una marca institucional mayor.

**RECOMENDACIÓN:** probar diferenciación por acompañamiento práctico guiado, progresión básico→intermedio, recursos/equipamiento efectivamente disponibles y confianza presencial, sin prometer empleabilidad o resultados garantizados.

**ACCIÓN PROPUESTA:** diseñar una variante BP-001 controlada contra el mensaje vigente, manteniendo oferta/destino constantes cuando se quiera aislar el efecto del mensaje.

## 9. Top 3 acciones de mayor impacto

1. **Cerrar la atribución E2E antes de optimizar por vanity metrics.** Conectar lectura GA4 y validar mapping CRM agregado; medir Ads → landing → key event/submit → Lead/Contact → Deal → CursoAlumno/venta.
2. **Diagnosticar la keyword crítica por intención, no por semántica genérica.** Comparar search terms 7/30, landing y downstream usando la política A/B/C; no cambiar negativas todavía.
3. **Hacer el piloto comparativo de conectores y el test competitivo controlado.** API/PowerShell queda fallback; MCP/conectores sólo ganan por tarea con paridad y ahorro material. En mensaje, evaluar diferenciación práctica frente a Activa sin cambiar simultáneamente oferta, landing y buyer persona.

## 10. Gaps para System Integration

```text
GOOGLE_ADS_MCP_READ_PARITY
GA4_MCP_EXISTING_AUTH_READ
META_OFFICIAL_CONNECTOR_TOOL_AUTH_PARITY
CRM_ATTRIBUTION_FIELD_MAPPING
```

Marketing entrega un XFER `READY` específico. System Integration debe detenerse si requiere OAuth nuevo, instalación, write scope, credencial nueva o cambio productivo.

## 11. Feedback scan

- `TASK_STATUS.md`, `DECISIONES.md` y documentos canónicos del frente fueron recuperados antes de recomendar.
- No existen actualmente `AGENT_FEEDBACK.md` ni `GEMINI.md` en raíz/docs.
- Issue #60: este trabajo puede aportar el **Bootstrap PASS** solicitado; la prueba **Delta** posterior sigue pendiente y no debe cerrarse como parte de este PR.
- No se crea deuda documental por copiar catálogos completos de AI OS.

## 12. Estado del piloto documental

```text
BOOTSTRAP_MARKETING=PASS
GOOGLE_ACCOUNT_PERFORMANCE_SKILL=ADAPTAR_MINIMO
ANTHROPIC_PERFORMANCE_REPORT=ADAPTAR_MINIMO
ANTHROPIC_COMPETITIVE_BRIEF=ADAPTAR_MINIMO
GOOGLE_ADS_BASELINE_RECOVERED=PASS
META_BASELINE_RECOVERED=PASS
GOOGLE_ADS_MCP_PILOT_DESIGN=PASS
GA4_REQUIREMENTS=PASS
META_CONNECTOR_DECISION=PASS
CROSS_SOURCE_ATTRIBUTION_CONTRACT=PASS
COMPETITIVE_BRIEF_PILOT=PASS
PERFORMANCE_REPORT_PILOT=PASS
EXTERNAL_WRITES=0
NEW_OAUTH=NO
```

El `PASS` es del **diseño y Bootstrap documental**. La ejecución técnica comparativa y el cierre E2E comercial permanecen condicionados a los `DATA_GAP` declarados.
