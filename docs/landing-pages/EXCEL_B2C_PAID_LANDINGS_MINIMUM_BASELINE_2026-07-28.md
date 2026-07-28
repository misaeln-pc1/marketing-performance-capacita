# Baseline mínimo — Tres landings Excel B2C pagadas

Fecha: 2026-07-28

Estado en esta rama: `PR_LISTO_PARA_REVISION`

Repo dueño: `misaeln-pc1/marketing-performance-capacita`

Repos dependientes:

- `misaeln-pc1/capacita-edge`
- `misaeln-pc1/capacita-global-control`

## 1. Objetivo

Consolidar en `main` de Marketing una definición mínima y trazable para las tres landings B2C pagadas de Excel, sin arrastrar completo el PR #35 ni convertir una rama o conversación en fuente de verdad.

Esta consolidación permite que futuros Bootstrap lean una fuente vigente en `main` después del merge y no dependan de:

- Marketing PR #35 completo;
- Marketing issue #43 abierto;
- XFER ubicados solo en rama de Edge;
- memoria conversacional.

## 2. Decisión mínima propuesta

Se aprueba documentalmente preparar tres landings pagadas B2C para pruebas controladas, inicialmente:

```text
noindex,follow
fuera de sitemap
fuera de navegación orgánica
sin reemplazar la página orgánica actual
sin activar campañas ni tráfico por este PR
```

Las tres landings venden el mismo producto real:

```text
Curso Excel Básico–Intermedio presencial, grupal, en Santiago Centro.
```

## 3. Landings

| Landing | Intención | Buyer persona primario | Hipótesis | URL propuesta |
|---|---|---|---|---|
| A | Curso Excel Básico–Intermedio presencial | `BP-001 — Desbordado Operativo` | La ruta completa básica-intermedia mejora la consulta de personas que ya usan Excel y necesitan orden, autonomía y productividad. | `/lp/curso-excel-basico-intermedio-presencial-santiago` |
| B | Curso Excel desde cero presencial | `BP-002 — Reinserción Laboral` | Un mensaje de inicio desde cero y acompañamiento reduce inseguridad y aumenta consulta/matrícula. | `/lp/curso-excel-desde-cero-presencial-santiago` |
| C | Clases de Excel presenciales con profesor | `BP-001 — Desbordado Operativo` | Una alternativa grupal estructurada con profesor en vivo puede captar búsquedas de clases presenciales sin prometer atención particular. | `/lp/clases-excel-presenciales-profesor-santiago` |

## 4. Verdad obligatoria de oferta

La landing C debe representar honestamente la oferta:

```text
Curso grupal presencial con profesor en vivo.
No corresponde a clases particulares, atención uno a uno ni clases a domicilio.
```

El copy puede usar lenguaje compatible con la intención de búsqueda, por ejemplo:

```text
clases de Excel presenciales
clases con profesor
profesor de Excel presencial
```

pero no debe prometer:

- profesor exclusivo;
- clases a domicilio;
- horarios personalizados;
- atención individual permanente;
- servicio uno a uno.

## 5. Exclusiones B2C

En comunicación B2C de estas landings no usar:

- SENCE;
- franquicia tributaria;
- beneficio tributario;
- gratuidad;
- curso gratis o gratuito;
- promesas de empleabilidad, ROI o resultado garantizado.

El puente B2B puede existir como derivación secundaria, pero no debe competir con el CTA individual ni mencionar SENCE en la tarjeta B2C.

## 6. Medición mínima requerida antes de producción

Cada landing debe tener, antes de cualquier publicación o tráfico real:

- URL propia;
- `landing_code` propio;
- UTM y click IDs persistentes (`gclid`, `gbraid`, `wbraid` cuando aplique);
- identificación de variante, intención y buyer persona primario;
- submit confirmado como conversión técnica primaria;
- descarga de temario, WhatsApp y puente B2B como conversiones secundarias;
- reconciliación posterior con Zoho para lead contactable, cotización y matrícula.

No tratar goals de clic como leads ni submits confirmados.

No inventar eventos, API names ni campos Zoho. Deben validarse en Edge, GTM, PageSense y Zoho antes de integración real.

## 7. Estado XFER con Edge

Marketing consume como vigente para este ciclo:

```text
docs/xfer/XFER__CAPACITA_EDGE__MARKETING__EXCEL_B2C_PAID_LANDINGS_REVIEW__20260727-041500__v05__READY__LANDING_REVIEW_REQUEST.md
```

Respuesta Marketing consolidada en este PR:

```text
docs/xfer/XFER__MARKETING__CAPACITA_EDGE__EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE__20260728-174500__v02__READY__MARKETING_REVIEW.md
```

Estado de consumo:

```text
CONSUMED_WITH_CHANGES
```

## 8. Bloqueos vigentes antes de publicar o integrar

No publicar ni integrar todavía mientras falte:

1. revisión visual humana final en escritorio y celular;
2. `scripts/audit-local.py` y `git diff --check` en workspace local Edge;
3. confirmar `duration`;
4. confirmar `download_resource_code`;
5. confirmar `course_instance_name`;
6. consolidar `CourseInstance` directo en HTML antes de versión publicable;
7. confirmar mapping exacto de Zoho Forms;
8. validar claims/sellos institucionales y consentimiento de imágenes;
9. autorizar GTM, PageSense, Turnstile, Zoho y endpoints internos;
10. autorizar cualquier cambio en Google Ads.

## 9. No autorizado por esta consolidación

Este PR no autoriza:

- publicar rutas `/lp`;
- agregar al sitemap;
- quitar `noindex`;
- tocar Worker real;
- tocar Cloudflare Dashboard;
- tocar DNS;
- activar GTM real;
- activar PageSense real;
- activar Turnstile real;
- activar Zoho real;
- enviar tráfico pagado;
- modificar Google Ads;
- modificar campañas, presupuestos, pujas, anuncios, keywords, negativas, conversiones o audiencias;
- hacer merge sin autorización expresa de Misael.

## 10. Relación con PR #35

PR #35 queda como antecedente amplio y transitorio.

Recomendación:

- no mergear PR #35 completo;
- rescatar solo del PR #35 lo que reduzca riesgo o desbloquee continuidad;
- cerrar o supersedear partes después de que este baseline mínimo quede en `main` y Misael decida sobre los remanentes.

## 11. Condición de cierre

Este baseline queda vigente solo cuando el PR que lo contiene sea mergeado a `main` con SHA verificable.

Hasta entonces, su estado es:

```text
PR_LISTO_PARA_REVISION
TRANSITORIO_NO_VIGENTE_EN_MAIN
```
