# Content Diagnostic Funnel Pilot V01 — Excel + Power BI + IA

Fecha de definición: 2026-09-06  
Owner: Marketing Performance / Growth & Market Intelligence Capacita  
Estado tras merge de este PR: `VIGENTE_EN_MAIN`  
Issue maestro: `marketing-performance-capacita#89`  
Task Hub Marketing: `capacita-task-hub#227`

## Decisión operativa

Capacita adopta como piloto P0 un sistema de adquisición orgánica basado en unidades de contenido comercial que conectan problema/intención real con diagnóstico gratuito y ruta a curso.

```text
DEMANDA / PROBLEMA REAL
→ ARTÍCULO WEB
→ CÁPSULA 30–45 s
→ DIAGNÓSTICO GRATUITO
→ RESULTADO ÚTIL
→ CURSO RECOMENDADO
→ LEAD
→ DEAL / VENTA cuando exista evidencia
```

El objetivo no es maximizar vistas aisladas. Se prioriza tráfico cualificado, uso del diagnóstico y resultado downstream verificable.

## Alcance P0 aprobado

Nueve Content Units: tres Excel, tres Power BI y tres Inteligencia Artificial aplicada al trabajo. Cada unidad produce una pieza madre web y un derivado short-form con el mismo objetivo/evidencia, sin copiar mecánicamente el artículo.

### Excel

1. `CCU-EXCEL-01` — **7 señales de que tu nivel de Excel ya no es básico**.
2. `CCU-EXCEL-02` — **¿Sabes Excel intermedio o sólo haces lo básico más rápido?**.
3. `CCU-EXCEL-03` — **7 tareas manuales que indican que Excel te está haciendo perder tiempo**.

### Power BI

1. `CCU-PBI-01` — **¿Sabes Power BI o sólo sabes hacer gráficos?**.
2. `CCU-PBI-02` — **Si copias y pegas datos para actualizar tu reporte, tienes una brecha de Power BI**.
3. `CCU-PBI-03` — **7 señales para saber qué nivel de Power BI tienes realmente**.

### Inteligencia Artificial

1. `CCU-IA-01` — **¿Usas inteligencia artificial o sólo le haces preguntas a ChatGPT?**.
2. `CCU-IA-02` — **ChatGPT te hizo un informe perfecto: ¿comprobaste de dónde salieron los datos?**.
3. `CCU-IA-03` — **7 señales de que todavía estás usando IA a nivel básico en tu trabajo**.

Los títulos son `WORKING_TITLE`: pueden optimizarse por claridad/conversión sin cambiar la intención ni el problema central.

## Contrato de una Content Unit

Cada unidad debe conservar:

```text
CONTENT_ID
DECISION / RESULTADO_COMERCIAL
PRIMARY_AUDIENCE
SEARCH_INTENT
PRIMARY_KEYWORD
SECONDARY_TOPICS
PAIN_SIGNAL
ARTICLE_WORKING_TITLE
ARTICLE_ANGLE
SHORT_HOOK
SHORT_SCRIPT_JOB
DIAGNOSTIC_CTA
DIAGNOSTIC_DESTINATION
COURSE_ROUTE
TRACKING_REQUIREMENTS
MUST_INCLUDE
MUST_NOT_CLAIM
COURSE_SOURCE_VERSION
SOURCES
DATA_GAPS
DO_NOT_CHANGE
ACCEPTANCE_CRITERIA
```

`DIAGNOSTIC_DESTINATION=PENDING` mientras no exista una URL real verificada. No inventar rutas.

## CTA por familia

### Excel

Promesa base: descubrir el nivel real y las principales brechas de Excel.

### Power BI

Promesa base: identificar qué parte del trabajo con datos necesita fortalecerse y qué nivel tiene realmente el usuario.

### IA

Promesa base: identificar el nivel de uso productivo de IA en el trabajo y las principales brechas.

El diagnóstico debe entregar valor antes de la venta. No usar un resultado vacío tipo “63% → compra este curso”. Debe devolver fortalezas, brechas y siguiente competencia/ruta cuando exista una matriz válida.

## Owners

### Marketing

- demanda e intención;
- buyer persona aplicado;
- pain signal;
- keywords/competencia;
- objetivo comercial;
- CTA;
- tracking requerido;
- QA comercial final;
- `NEXT_BEST_ACTION`.

### Content Factory

- investigación editorial complementaria;
- redacción y arquitectura;
- fuentes/claims;
- naturalidad y originalidad;
- artículo final;
- guion short-form;
- QA editorial.

Consumidor: `capacita-content-factory#25` / Task Hub `#229`.

### AI OS / Skills

- discovery, auditoría y adaptación de skills/patrones reutilizables;
- no valida el contenido real como laboratorio central.

Skill request: `capacita-ai-operating-system#82` / Task Hub `#228`.

### Diseño de Cursos

Fuente exclusiva para currículo, competencias y definición de nivel. No inferir básico/intermedio/avanzado sin fuente vigente.

### Edge

Implementación y publicación web posterior. Fuera del alcance de esta fase.

### YouTube

Configuración del canal y publicación se resuelven después del QA del contenido. En esta fase se produce el guion, no se publica.

## Secuencia vinculante

### Wave 0 — vertical slice

Primero `CCU-EXCEL-01`.

Objetivo: validar una vez el contrato editorial, la relación artículo→short→diagnóstico y el uso real de skills antes de multiplicar producción.

Si no aparece `HOLD` material, Content Factory continúa automáticamente con Wave 1 sin una nueva decisión de alcance.

### Wave 1 — completar las otras ocho

Producir las otras 8 Content Units con el mismo contrato, manteniendo diferenciación real por tema y familia.

### QA

Marketing revisa los 9 pares y devuelve sólo deltas/brechas concretas. No reescribe silenciosamente la producción.

### Fase posterior

Después del QA y autorización correspondiente:

```text
Content Factory
→ Edge / página
→ producción audiovisual
→ YouTube
→ diagnóstico real
→ tracking
→ medición contenido → diagnóstico → lead → Deal/venta
```

## Skills / Reuse

Reutilizar antes de crear:

- `seo-demand-serp-research-capacita`;
- `aeo-ai-readability-capacita`;
- `conversion-copy-cta-patterns-capacita`;
- `marketing-event-taxonomy-attribution-capacita`;
- `buyer-persona-signal-map-capacita`;
- `learning-game-engagement-design-capacita`;
- `multichannel-content-repurposing-capacita`;
- stack editorial vigente de Content Factory.

AI OS #82 evalúa patrones externos de short-form. Content Factory no bloquea Wave 0 esperando ese delta.

## Tracking conceptual

Mantener como mínimo:

```text
content_id
course/topic
modality_if_relevant
audience
pain_signal
cta_action=diagnostic_start
cta_location=article|short
source_content_id
```

Regla dura:

```text
VIEW != DIAGNOSTIC_START != DIAGNOSTIC_COMPLETE != LEAD != DEAL != VENTA
```

## DO_NOT_CHANGE

- Tres áreas P0: Excel, Power BI, IA aplicada al trabajo.
- Nueve artículos + nueve guiones short.
- Diagnóstico como CTA común por familia.
- Una hipótesis y buyer persona primario por unidad.
- Artículo y short comparten evidencia/objetivo pero no texto mecánicamente duplicado.
- No inventar URL, scoring, nivel, currículo, precio, fecha, cupos, claims o métricas.
- Claims sobre herramientas IA actuales requieren freshness check.
- No publicar web/YouTube, no tocar Ads/CRM/producción durante la fase editorial.

## Evidencia y routing

- Marketing issue: `#89`.
- Marketing Task Hub: `#227`.
- AI OS issue: `#82`.
- AI OS Task Hub: `#228`.
- Content Factory issue: `#25`.
- Content Factory Task Hub: `#229`.

## Definition of Done del piloto editorial

- 9 briefs trazables;
- 9 artículos originales;
- 9 guiones de cápsula 30–45 s;
- tres familias diferenciadas;
- fuentes/claims y currículo trazables;
- `DATA_GAP` y `DO_NOT_CHANGE` visibles;
- cero URL/scoring/niveles inventados;
- QA editorial pasado;
- entrega a Marketing para QA;
- cero publicación/producción antes de autorización.

## Continuidad

Ante un chat nuevo o Bootstrap de Marketing, leer este archivo junto con `TASK_STATUS.md`, `DECISIONES.md` y los issues/tareas enlazados. No reconstruir el programa desde cero; aplicar sólo Delta sobre evidencia nueva.
