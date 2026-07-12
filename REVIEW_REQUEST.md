# REVIEW_REQUEST

## Objetivo de revisión

Revisar el cierre documental de la arquitectura de landings pagadas Excel, PageSense y Search Console sin confundirlo con autorización de cambios productivos.

## PR activo principal

### PR #35 — Landings pagadas, CRO y Search Console

- Rama: `docs/marketing-excel-b2c-two-page-plan-v01`.
- Alcance actualizado:
  - proteger la página orgánica actual;
  - documentar tres landings pagadas `noindex`;
  - asignar buyer persona primario e hipótesis por landing;
  - registrar hallazgos PageSense y formulario;
  - excluir SENCE/gratuidad de B2C;
  - conservar el puente B2B como derivación secundaria;
  - definir Search Console API read-only;
  - crear handoff exportable para continuidad.

### Landings documentadas

1. Básico–Intermedio / `BP-001`.
2. Excel Básico desde cero / `BP-002`.
3. Clases presenciales con profesor / `BP-001`.

La tercera landing debe declarar que se trata de un curso grupal presencial Básico–Intermedio en sede. No promete clases particulares, uno a uno ni a domicilio.

## Issues relacionados

- `marketing-performance-capacita#36`: Search Console API read-only.
- `capacita-edge#27`: GTM/Google tag y atribución.
- `capacita-edge#28`: SEO/GEO técnico.
- `capacita-global-control#101`: candidatos transversales en observación.

## Validación solicitada

1. Confirmar que la página orgánica actual queda indexable y protegida.
2. Confirmar que las tres nuevas landings se documentan inicialmente como `noindex,follow` y fuera del sitemap.
3. Confirmar un buyer persona primario y una hipótesis por landing.
4. Confirmar que la landing de clases no presenta el curso grupal como particular o domiciliario.
5. Confirmar exclusión de SENCE, beneficio tributario y gratuidad en B2C.
6. Confirmar que el puente B2B permanece secundario y separado.
7. Confirmar que PageSense goals de clic no se usan como submits.
8. Confirmar que la medición exige URL, landing code, UTM, funnel y reconciliación Zoho por landing.
9. Confirmar que Search Console API es read-only y separada de Google Ads API.
10. Confirmar ausencia de PII, secretos, credenciales, IDs completos, exports crudos y binarios.
11. Confirmar que ninguna rama modifica campañas, GTM, WordPress, Cloudflare, Zoho o producción.

## Archivos principales del PR #35

- `docs/landing-pages/EXCEL_B2C_TWO_PAGE_PLAN_AND_CRO_BASELINE_2026-07-12.md` — antecedente inicial.
- `docs/landing-pages/EXCEL_B2C_CLARIFICATIONS_B2B_BRIDGE_HISTORY_PERSONAS_2026-07-12.md`.
- `docs/landing-pages/EXCEL_B2C_SENCE_EXCLUSION_AND_ORGANIC_PAID_OPTIONS_2026-07-12.md`.
- `docs/search-console/SEARCH_CONSOLE_API_SCOPE_AND_PAID_LANDING_DECISION_V01.md`.
- `docs/handoffs/HANDOFF_EXCEL_PAID_LANDINGS_SEARCH_CONSOLE_2026-07-12.md` — fuente vigente de continuidad.
- `DECISIONES.md`.
- `TASK_STATUS.md`.

## Regla de precedencia

Cuando exista contradicción entre documentos exploratorios tempranos y el handoff final, prevalecen:

1. `DECISIONES.md` actualizado;
2. `TASK_STATUS.md` actualizado;
3. `docs/handoffs/HANDOFF_EXCEL_PAID_LANDINGS_SEARCH_CONSOLE_2026-07-12.md`.

## No autoriza

- construcción o publicación de landings;
- cambios de campañas, grupos, keywords, negativas, anuncios, presupuesto o pujas;
- configuración OAuth;
- cambios de Search Console, GA4, PageSense, GTM, Cloudflare, Zoho o producción;
- merge automático.

## Semáforo

Amarillo documental. La implementación requiere un PR separado en Capacita Edge y autorización separada para Google Ads y OAuth.
