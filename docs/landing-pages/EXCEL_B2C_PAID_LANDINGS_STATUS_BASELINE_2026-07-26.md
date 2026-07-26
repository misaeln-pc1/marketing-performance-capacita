# Estado operativo — Landings pagadas B2C Excel — baseline de medición — 2026-07-26

## Estado

- Estado: `BASELINE_OPERATIVO_PRE_PUBLICACION_V01`.
- Semáforo: amarillo.
- Repo: `misaeln-pc1/marketing-performance-capacita`.
- Rama: `docs/marketing-excel-b2c-two-page-plan-v01`.
- PR relacionado: #35.
- Dueño táctico: Marketing Performance / Campañas & Growth Capacita.
- Implementador esperado: Capacita Edge.
- Alcance: landings pagadas B2C para Google Search Excel presencial.
- Fuera de alcance: cambios productivos en Google Ads, presupuestos, pujas, anuncios, GTM, PageSense, Zoho, Cloudflare, DNS, formularios reales y producción sin autorización explícita.

Este no es un estado cero. Es un baseline operativo de medición para una iniciativa ya iniciada, con histórico Google Ads, Keyword Planner, listas negativas, buyer persona e intención de búsqueda ya revisados.

## Contexto vigente

La página orgánica actual se mantiene como activo SEO y control:

```text
https://capacita.cl/curso-de-excel-presencial-en-santiago/
```

Las nuevas landings son pagadas, `noindex,follow`, no sustituyen la página orgánica y deben medirse por separado.

## Landings en construcción

| Código | Landing | URL propuesta | Buyer persona | Intención primaria | Estado |
|---|---|---|---|---|---|
| A | Básico–Intermedio presencial | `/lp/curso-excel-basico-intermedio-presencial-santiago/` | `BP-001 — Desbordado Operativo` | curso presencial completo/ruta laboral | pendiente publicación Edge |
| B | Excel desde cero | `/lp/curso-excel-desde-cero-presencial-santiago/` | `BP-002 — Reinserción Laboral` | comenzar desde baja seguridad o base inicial | pendiente publicación Edge |
| C | Clases presenciales con profesor | `/lp/clases-excel-presenciales-profesor-santiago/` | `BP-001 — Desbordado Operativo` | clases/profesor en vivo como alternativa estructurada | pendiente publicación Edge |

## Hipótesis general

Separar la intención de búsqueda en tres landings reducirá mezcla de mensajes, mejorará experiencia post-click y permitirá optimizar CTR, CVR y calidad de lead por intención.

La arquitectura se ordena así:

```text
intención de búsqueda -> landing -> buyer persona -> mensaje -> medición -> aprendizaje
```

No se segmenta primero por buyer persona. El buyer persona ayuda a diseñar objeciones, tono, CTA y bloques de confianza.

## Baseline Google Ads disponible

Fuente privada:

```text
CAPACITA/Proyectos/0-Origen/google/exports/google-ads-current-campaign-history-20260726-030015
```

Resumen 730/30/7 días:

| Ventana | Clics | Costo CLP | CPC medio CLP | Conversiones | CVR | CPA CLP |
|---:|---:|---:|---:|---:|---:|---:|
| 7 días | 47 | 44.885 | 955 | 1 | 2,13% | 44.885 |
| 30 días | 215 | 215.294 | 1.001 | 12 | 5,58% | 17.941 |
| 730 días | 12.382 | 8.549.828 | 691 | 388,75 | 3,14% | 21.993 |

Lectura: el deterioro reciente se observa principalmente en conversión post-click, no sólo en CPC.

## Baseline por intención

Clasificación preliminar usando `05_search_terms_daily.csv`:

| Categoría | Clics | Costo aprox. CLP | Conversiones | CPC aprox. CLP | CVR aprox. | CPA aprox. CLP | Decisión |
|---|---:|---:|---:|---:|---:|---:|---|
| A — Básico/intermedio/presencial | 4.162 | 2.635.226 | 179,01 | 633 | 4,30% | 14.721 | núcleo B2C |
| B — Desde cero/básico | 780 | 517.656 | 13,84 | 664 | 1,77% | 37.397 | crear landing con control |
| C — Clases/profesor compatible | 182 | 115.860 | 8,5 | 637 | 4,67% | 13.631 | experimento viable |
| Riesgo particular/domicilio | 24 | 36.644 | 2 | 1.527 | 8,33% | 18.322 | no prometer / bloquear fuerte |
| Negativas globales | 940 | 608.979 | 14,55 | 648 | 1,55% | 41.867 | bloquear / limpiar |
| B2B backlog | 19 | 20.934 | 0 | 1.102 | 0% | — | diferir a campaña B2B |
| Revisar manual | 2.259 | 1.419.608 | 38 | 628 | 1,68% | 37.358 | clasificar en iteración posterior |

## Hipótesis por landing

### A — Básico–Intermedio presencial

Hipótesis:

> Si el tráfico de curso presencial completo aterriza en una página que refuerza ruta laboral, práctica guiada y modalidad presencial, debería sostener o mejorar el CPA histórico del núcleo B2C.

Indicadores principales:

- CTR del anuncio por grupo A.
- CVR landing A.
- CPA por submit confirmado.
- Lead contactable.
- Cotización.
- Matrícula.

Criterio inicial:

- Mantener si CPA y calidad se sostienen frente a la página orgánica/control.
- Ajustar mensaje si hay clics sin interacción/form start.
- Revisar keyword/negativas si hay gasto sin submit.

### B — Excel desde cero

Hipótesis:

> Si el tráfico de principiantes aterriza en una página más simple, paso a paso y orientada a seguridad, debería mejorar la conversión del segmento básico/desconfiado.

Indicadores principales:

- CVR landing B.
- Tiempo de permanencia / scroll / interacción PageSense.
- Form start.
- Submit confirmado.
- Calidad del lead.

Criterio inicial:

- Presupuesto controlado.
- No juzgar sólo por clics; evaluar si mejora form start y contacto.
- Ajustar hero si se detecta miedo, confusión o abandono temprano.

### C — Clases presenciales con profesor

Hipótesis:

> Si el tráfico de clases/profesor aterriza en una página que ofrece profesor en vivo, curso grupal estructurado y respaldo institucional, se puede capturar intención compatible sin prometer clase particular ni domicilio.

Indicadores principales:

- Search terms con `clases`, `profesor`, `presencial`.
- CPA de grupo C.
- Preguntas/reclamos por clases particulares o domicilio.
- Leads que aceptan modalidad grupal.
- Contactabilidad y matrícula.

Criterio inicial:

- Bloquear fuerte `a domicilio`, `uno a uno`, `profesor particular`, `clases particulares` si contamina.
- Mantener el bloque de confianza institucional después del hero.
- No mencionar marcas de competidores.

## Medición mínima obligatoria

Cada landing debe tener trazabilidad diferenciada:

| Elemento | Requerido |
|---|---|
| URL única | sí |
| `landing_code` | sí |
| UTM | sí |
| variante | sí |
| intención | sí |
| buyer persona hipótesis | sí |
| GA4/PageSense/GTM | validar en Edge |
| Zoho lead source/campaign | validar antes de activación Ads |
| submit confirmado | conversión principal |
| lead contactable | métrica de calidad |
| cotización | métrica comercial |
| matrícula | métrica final |

Códigos conceptuales:

```text
LP_EXCEL_BASICO_INTERMEDIO_B2C_BP001_V1
LP_EXCEL_DESDE_CERO_B2C_BP002_V1
LP_CLASES_EXCEL_PROFESOR_B2C_BP001_V1
```

## Cadencia de evaluación

### Día 0 — Publicación técnica

Validar:

- Página accesible.
- `noindex,follow`.
- Fuera de sitemap.
- Formulario visible y funcional.
- CTA correcto.
- UTM/landing_code persistente.
- PageSense/GA4/GTM sin duplicidad.
- No hay promesas SENCE/gratuidad/empleo/resultado garantizado.
- C no promete clase particular, domicilio ni 1:1.

### Día 1–3 — Sanity check

Revisar:

- Tráfico llega a la URL correcta.
- Search terms por grupo.
- CPC anómalo.
- Rebote/interacción inicial.
- Form start.
- Submit confirmado.
- Leads malos por intención equivocada.

No tomar decisiones fuertes salvo errores técnicos o gasto claramente contaminado.

### Día 7 — Primera lectura táctica

Comparar:

- CTR por grupo.
- CPC por grupo.
- CVR por landing.
- CPA por submit.
- Lead contactable.
- Search terms contaminantes.
- Primeros aprendizajes PageSense.

Acciones posibles:

- Ajustar copy/hero.
- Ajustar negativas.
- Pausar keywords contaminantes.
- Mantener hipótesis si hay señal suficiente.

### Día 14 — Variantes de mensaje

Sólo si hay datos suficientes:

- Variante A: foco productividad/ruta laboral.
- Variante B: foco seguridad/paso a paso.
- Variante C: foco profesor + respaldo institucional.

No cambiar todo a la vez. Una variable por prueba.

### Día 30 — Decisión

Decidir:

- Mantener landing.
- Ajustar mensaje.
- Separar más keywords.
- Consolidar grupos.
- Mover presupuesto.
- Escalar o pausar hipótesis.

## Variables que no se deben mezclar

- No mezclar B2C y B2B.
- No mezclar presencial con online/e-learning.
- No mezclar curso grupal con clase particular.
- No mezclar intención SENCE/gratis/franquicia en B2C.
- No cambiar simultáneamente landing, keywords, negativos, puja y presupuesto si se quiere aprender algo.

## Riesgos actuales

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Publicar sin medición diferenciada | no se aprende qué landing funcionó | landing_code + UTM + GA4/PageSense/Zoho |
| Mezclar búsquedas de clases particulares | leads confundidos | negativas y bloque de transparencia |
| Usar SENCE como gancho B2C | atrae intención equivocada | usar respaldo institucional sólo como confianza secundaria |
| Cambiar Ads demasiado rápido | se pierde línea base | migración controlada por grupos |
| Juzgar por conversiones de Google sin Zoho | optimización engañosa | reconciliar lead contactable/cotización/matrícula |

## Estado actual

- Marketing: copy, intención, buyer persona, keywords y negativas documentadas.
- Edge: pendiente construir/publicar landings.
- Ads: no modificar todavía.
- Medición: preparar validación antes de enviar tráfico pagado.
- B2B: diferido a backlog separado.

## Próximo paso operativo

1. Edge consume `docs/xfer/XFER__MARKETING__CAPACITA_EDGE__EXCEL_B2C_PAID_LANDINGS__20260726-032000__v01__READY__HTML_COPY_BRIEF.md`.
2. Edge publica previews o PR técnico no-main.
3. Marketing valida copy, intención y exclusiones.
4. Después de publicación, levantar checkpoint Día 0.
5. Sólo después preparar propuesta de migración Ads controlada.

## Cierre

Este documento fija el baseline de medición para las landings pagadas B2C Excel. No autoriza activación de Ads ni cambios productivos por sí mismo.
