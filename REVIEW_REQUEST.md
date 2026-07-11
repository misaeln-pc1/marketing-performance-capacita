# REVIEW_REQUEST

## Objetivo de revisión

Revisar el cierre documental del diagnóstico inicial de Marketing Performance sin confundirlo con autorización de cambios productivos.

## PR activos

### PR #29 — Google Ads

- Rama: `fix/marketing-google-ads-missing-reports-v02`.
- Alcance:
  - exportador read-only para los dos reportes faltantes;
  - protocolo de competencia y decisión de landing;
  - baseline agregado y sanitizado de 90 días.
- Evidencia local:
  - términos de búsqueda: 1.825 filas, `ok`;
  - landing pages: 8.482 filas, `ok`;
  - errores API: 0.
- No incluye SEO/GEO ni cambios en campañas.

### PR #30 — Estado y gobernanza local

- Rama: `docs/marketing-continuous-learning-routing-v01`.
- Alcance:
  - sincronizar `TASK_STATUS.md`;
  - corregir `REPO_RULES.md` para consumir GTM/RevOps;
  - actualizar `DECISIONES.md`;
  - actualizar `CHANGELOG_AGENT.md`;
  - actualizar esta solicitud de revisión.

### PR #31 — SEO, Local SEO y visibilidad IA

- Rama: `docs/marketing-seo-geo-baseline-v01`.
- Alcance:
  - baseline técnico;
  - benchmark de consultas;
  - modelo de medición;
  - fuentes primarias;
  - handoff a Capacita Edge #28.
- No implementa cambios en WordPress, Cloudflare, robots, sitemap, structured data o producción.

## Issues relacionados

- `marketing-performance-capacita#23`: validación de instrucciones V1; permanece abierto.
- `capacita-edge#27`: GTM/Google tag y atribución.
- `capacita-edge#28`: SEO/GEO técnico.
- `capacita-global-control#101`: candidatos transversales en observación.

## Validación solicitada

1. Confirmar que PR #29 contiene solo Google Ads y tres archivos.
2. Confirmar que PR #30 contiene solo estado, reglas, decisiones y changelog/revisión.
3. Confirmar que PR #31 contiene solo seis documentos SEO/GEO.
4. Confirmar ausencia de PII, secretos, IDs completos, exports crudos y binarios.
5. Confirmar que ninguna rama modifica campañas, GTM, WordPress, Cloudflare, Zoho o producción.
6. Confirmar que Auction Insights y CSV reales permanecen privados.
7. No declarar diagnóstico final: faltan competencia nominal, tracking y reconciliación con Zoho.

## Orden de merge recomendado

1. PR #29.
2. PR #30.
3. PR #31 solo cuando GitHub lo reporte mergeable y se resuelva su historial de rama si corresponde.

Usar `squash merge` para evitar conservar commits intermedios de separación y corrección.

## Pendiente separado

PR #8 no forma parte de este cierre. Contiene un estándar útil de video por placement, pero está desfasado y no debe mergearse sin revisión/rebase independiente.