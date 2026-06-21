# REVIEW_REQUEST

## PR objetivo

Plan documental de migración archivo/carpeta Marketing -> GTM/RevOps.

## Resumen

Este PR registra la propuesta aprobada para ordenar el repo `marketing-performance-capacita` sin mover archivos todavía.

El objetivo es separar:

- Marketing (Campañas & Growth): campañas, pauta, copies, assets documentales, performance y aprendizajes tácticos.
- GTM/RevOps: buyer persona, value persona, segmentación, journey, scoring, nurturing y touch strategy.
- Skills / AI OS: capacidades reutilizables.
- Repos técnicos: Capacita Edge, Zoho Deluge Core, WhatsApp + n8n + Zoho.

## Archivos modificados

- `docs/MARKETING_FILE_LEVEL_MIGRATION_PLAN.md`: nuevo plan de migración archivo/carpeta.
- `TASK_STATUS.md`: actualiza estado y próxima acción.
- `DECISIONES.md`: registra aprobación del plan.
- `REVIEW_REQUEST.md`: esta solicitud de revisión.

## No se toca

- No se mueven archivos reales.
- No se renombran carpetas.
- No se modifica `main` directo.
- No se modifican campañas reales.
- No se toca Meta Ads, Google Ads, Zoho, n8n, WhatsApp, Cloudflare ni producción.
- No se suben datos personales, credenciales, archivos de configuración sensible ni binarios.

## Validación esperada

- Solo cambios documentales.
- El plan no ejecuta migración física.
- Marketing conserva ejecución táctica.
- GTM/RevOps queda como destino canónico futuro de estrategia comercial transversal.
- Repos técnicos quedan como destinos de implementación, no de estrategia.

## Recomendación

Mergear si el diff confirma que el PR solo agrega el plan y actualiza estado/decisiones. El siguiente PR debería crearse en `capacita-global-control` para preparar `docs/gtm-revops/`.
