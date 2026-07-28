# Auditoría PR #35 + Marketing #43 + Edge PR #36 — Normalización operativa

Fecha: 2026-07-28

Repo dueño: `misaeln-pc1/marketing-performance-capacita`

Rama de esta auditoría: `docs/marketing-pr35-edge43-audit-20260728`

Estado de este documento: `DRAFT_AUDIT / NO_MERGEAR_TODAVIA / REQUIERE_DECISION_MISAEL`

## 1. Context Gate

```text
Context Gate: Bootstrap
Fuentes revisadas:
- Global CURRENT.md, V1 y V0 de Marketing.
- Global: lectura obligatoria, diccionario, estándar, routing issue/task, control de cambios, Read Gate y matriz de alcance.
- Marketing main: AGENTS.md, README.md, PROJECT_CONTEXT.md, REPO_RULES.md, TASK_STATUS.md, DECISIONES.md, CHANGELOG_AGENT.md, REVIEW_REQUEST.md, GTM_CONSUMPTION_BRIDGE.md, CAMPAIGN_BRIEF_GTM.md, Google Ads baseline y procedimiento recurrente.
- Marketing PR #35, issue #43, PRs abiertos y issues abiertos.
- Capacita Edge PR #36, XFER v05 y respuesta Marketing v01 existente en la rama Edge.

Regla crítica recuperada:
Solo main gobierna futuros Bootstrap. Un PR abierto, issue, comentario o chat no vuelve vigente una definición.

Bloqueo de acceso:
No hay ruta local Windows verificada. No se ejecutaron scripts, APIs, exports ni checks locales.
```

## 2. Alcance de esta auditoría

Esta auditoría revisa el frente prioritario identificado:

```text
Marketing PR #35
Marketing issue #43
Capacita Edge PR #36
XFER Edge -> Marketing v05
XFER Marketing -> Edge v01
```

No ejecuta ni autoriza:

- publicación de landings;
- cambios en Google Ads;
- cambios en Cloudflare, Worker, DNS, sitemap o rutas `/lp`;
- GTM, PageSense, Turnstile o Zoho reales;
- APIs, scripts, exports o credenciales;
- cierre de issues;
- merge a main.

## 3. Estado real observado

| Elemento | Estado observado | Está en main | Lectura operativa |
|---|---|---:|---|
| Marketing PR #35 | Abierto, mergeable, 19 commits, 16 archivos, branch divergida | No | Contiene decisión de tres landings pagadas, Search Console, matrices, XFER inicial a Edge y cambios a estado local. Es demasiado amplio para merge automático. |
| Marketing issue #43 | Abierto | No aplica | Solicita revisión de Edge PR #36 y XFER de respuesta desde Marketing. No tiene cierre ni callback final en el issue. |
| Edge PR #36 | Abierto, draft, no mergeable, 105 commits, 35 archivos, branch divergida | No | Implementa previews y documentos Edge; mantiene `REQUIERE_REVISION_MISAEL`, `REQUIERE_REVISION_MARKETING`, `REQUIERE_CHECKS`, `NO_MERGEAR_TODAVIA`. |
| XFER Edge -> Marketing v05 | `READY` en Edge branch | No | Es la versión que Marketing debe consumir; reemplaza v04. |
| XFER Marketing -> Edge v01 | `READY`, pero existe dentro de la rama Edge | No en Marketing main | Respuesta útil, pero su ubicación no satisface completamente la trazabilidad solicitada por Marketing #43, que pedía crear el XFER en el repo Marketing. |

## 4. Hallazgos principales

### 4.1 PR #35 no debe mergearse como paquete completo todavía

Motivo:

- mezcla decisiones de landings, Search Console, SEO/IA, keywords/negativas, XFER y cambios de `TASK_STATUS.md` / `DECISIONES.md`;
- la rama está divergida respecto de `main`;
- contiene definiciones con efecto futuro que todavía no están consolidadas;
- Edge avanzó después del XFER inicial y generó v05, por lo que parte de PR #35 ya quedó como antecedente, no como estado final.

Estado recomendado:

```text
TRANSITORIO_NO_VIGENTE_EN_MAIN
REQUIERE_REVISION_MISAEL
NO_MERGEAR_TODAVIA
```

### 4.2 La decisión de tres landings es útil, pero debe consolidarse de forma más controlada

Decisión candidata:

1. conservar la página orgánica actual;
2. crear tres landings pagadas `noindex,follow`, fuera del sitemap;
3. mantener el mismo producto real: curso grupal Excel Básico-Intermedio presencial;
4. separar intenciones:
   - Básico-Intermedio / BP-001;
   - Desde cero / BP-002;
   - Clases con profesor / BP-001;
5. excluir SENCE, gratuidad, franquicia y beneficio tributario de B2C;
6. no prometer clases particulares, uno a uno ni domicilio;
7. medir cada landing con URL, `landing_code`, UTM, submit confirmado y reconciliación posterior con Zoho.

Problema: esta decisión vive en PR abierto y en XFER, no en `main`. Por regla de vigencia, no debe gobernar futuros Bootstrap hasta consolidarse.

### 4.3 Issue #43 no está resuelto aunque Edge ya tenga una respuesta Marketing

Marketing #43 solicitó explícitamente:

- crear XFER de respuesta en Marketing;
- actualizar bitácora XFER de Marketing;
- comentar callback en Edge PR #36;
- no tocar producción.

Estado observado:

- existe respuesta `XFER__MARKETING__CAPACITA_EDGE__EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE__20260727-053500__v01__READY__MARKETING_REVIEW.md` dentro de la rama Edge;
- no se observó esa respuesta consolidada en Marketing `main`;
- #43 sigue abierto.

Interpretación:

```text
CIERRE_ADMINISTRATIVO_PENDIENTE
TRAZABILIDAD_INCOMPLETA
```

### 4.4 Edge PR #36 sigue bloqueado correctamente

Edge mantiene gates explícitos:

```text
REQUIERE_REVISION_MISAEL
REQUIERE_REVISION_MARKETING
REQUIERE_CHECKS
NO_MERGEAR_TODAVIA
```

Bloqueos vigentes antes de publicar o mergear:

1. revisión visual humana en escritorio y celular;
2. `scripts/audit-local.py`;
3. `git diff --check` local;
4. confirmar `duration`;
5. confirmar `download_resource_code`;
6. confirmar `course_instance_name`;
7. consolidar `CourseInstance` directo en HTML antes de publicable;
8. confirmar mapping Zoho Forms;
9. validar claims/sellos e imágenes;
10. autorización explícita para GTM/PageSense/Turnstile/Zoho reales.

### 4.5 La respuesta Marketing v01 es útil, pero debe tratarse como antecedente

La respuesta Marketing v01 en Edge indica:

```text
CONSUMED_WITH_CHANGES
```

Corrección principal:

- retirar textos internos visibles en Landing C;
- conservar copy natural:
  `Una alternativa estructurada a clases sueltas: curso grupal, práctico y con profesor en vivo.`

Edge documenta luego que esa corrección visual fue aplicada, pero quedan pendientes técnicos y humanos. Por tanto, no corresponde declarar `CONSUMED_PASS`.

Estado recomendado:

```text
CONSUMED_WITH_CHANGES
REQUIERE_CHECKS
NO_MERGEAR_TODAVIA
```

## 5. Contradicciones / fricción de trazabilidad

| Tema | Evidencia | Riesgo | Resolución recomendada |
|---|---|---|---|
| Respuesta Marketing ubicada en Edge | El XFER Marketing -> Edge v01 existe dentro de rama Edge, no consolidado en Marketing main | Un futuro Bootstrap de Marketing no la verá como fuente local vigente | Crear/traer respuesta equivalente en Marketing mediante PR propio o incorporar al PR de normalización. |
| PR #35 muy amplio | 16 archivos y varias decisiones transversales | Merge de una mezcla de decisiones sin revisión granular | Dividir mentalmente en paquetes: landings, Search Console, SEO/IA, keywords/negativas, XFER. |
| Edge PR #36 divergido | 105 commits, draft, no mergeable | No puede considerarse listo aunque haya preview | Mantener gate; pedir a Edge delta técnico cuando Marketing cierre respuesta. |
| Decisión de tres landings no está en main | Vive en PR #35/XFER | Otro chat puede perderla o tratarla como no vigente | Consolidar una fuente mínima en main antes de usar como baseline. |

## 6. Recomendación principal

No intentar mergear PR #35 completo.

Ruta recomendada:

1. crear un PR documental corto desde `main` que consolide solo el estado y decisión mínima de las tres landings pagadas;
2. registrar que el XFER Edge v05 fue consumido por Marketing como `CONSUMED_WITH_CHANGES`, no `CONSUMED_PASS`;
3. actualizar `TASK_STATUS.md`, `DECISIONES.md`, `CHANGELOG_AGENT.md` y `REVIEW_REQUEST.md` con el estado real;
4. dejar PR #35 como fuente histórica/transitoria hasta decidir si se cierra o se rescata por partes;
5. pedir a Edge una respuesta final posterior solo cuando complete checks y slots.

## 7. Decisiones que debe tomar Misael

### Decisión 1 — Consolidación de tres landings

```text
¿Autorizas consolidar en Marketing main la decisión mínima de tres landings B2C pagadas noindex, sin mergear PR #35 completo?
```

Recomendación: Sí.

Motivo: reduce pérdida de contexto y evita que PR #35 siga siendo la única fuente.

### Decisión 2 — Tratamiento de PR #35

Opciones:

| Opción | Acción | Recomendación |
|---|---|---|
| A | Mantener #35 abierto como fuente transitoria hasta extraer lo útil | Preferida ahora |
| B | Rebasear #35 completo | No recomendado: demasiado amplio |
| C | Cerrar #35 como superseded después de PR de consolidación | Recomendado después, no ahora |

### Decisión 3 — XFER Marketing #43

```text
¿Quieres que Marketing genere en su propio repo el XFER de respuesta formal a Edge usando como base la respuesta v01 ya existente en Edge?
```

Recomendación: Sí, pero en PR documental separado o dentro del PR corto de consolidación.

### Decisión 4 — Publicación / activación

No decidir todavía.

Antes faltan:

- checks Edge;
- slots finales;
- visual humano;
- mappings Zoho;
- autorización GTM/PageSense/Turnstile/Zoho;
- ruta `/lp` real;
- campaña Google Ads.

## 8. Próxima acción operativa propuesta

Preparar un PR documental corto en Marketing desde `main` con:

```text
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_CANONICAL_STATUS_2026-07-28.md
docs/xfer/XFER__MARKETING__CAPACITA_EDGE__EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE__20260728-STATUS__v02__READY__MARKETING_REVIEW.md
TASK_STATUS.md
DECISIONES.md
CHANGELOG_AGENT.md
REVIEW_REQUEST.md
```

Límites:

- no tocar Google Ads;
- no tocar Edge;
- no cerrar #43 todavía;
- no cerrar PR #35 todavía;
- no crear Task Hub todavía;
- no mergear.

## 9. Estado de cierre de esta auditoría

```text
Gate: Bootstrap
Objetivo: Auditar PR #35 + Marketing #43 + Edge #36
Resultado: PASS_DOCUMENTAL_CON_BLOQUEOS
Rama: docs/marketing-pr35-edge43-audit-20260728
Cambios productivos: NO
APIs/scripts/exports: NO
Merge: NO
Riesgo: Amarillo documental
Siguiente paso: decisión de Misael sobre consolidación mínima
```
