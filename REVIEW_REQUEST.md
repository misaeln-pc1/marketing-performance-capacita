# REVIEW_REQUEST

## PR objetivo

Alinear Marketing con el contrato corporativo GTM/RevOps mergeado en Global PR #88 y aplicar el primer baseline a Excel presencial V3.

## Issue

[#19 — Alinear Marketing con canónicos GTM y pilotear brief Excel presencial](https://github.com/misaeln-pc1/marketing-performance-capacita/issues/19)

## Problema

El repo ya había aprobado la separación Marketing / GTM, pero README, contexto y carpetas seguían describiendo buyer personas, journey y propuesta de valor como contenido propio. Faltaba una regla operativa para que cada campaña consumiera el canónico sin duplicarlo.

## Cambios

- Crea `docs/GTM_CONSUMPTION_BRIDGE.md`.
- Crea `templates/CAMPAIGN_BRIEF_GTM.md`.
- Crea `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md`.
- Actualiza:
  - `README.md`;
  - `PROJECT_CONTEXT.md`;
  - `core/README.md`;
  - `references/README.md`;
  - `campaigns/README.md`;
  - `automation/README.md`;
  - `TASK_STATUS.md`;
  - `DECISIONES.md`;
  - `CHANGELOG_AGENT.md`;
  - `REVIEW_REQUEST.md`.

## Criterio aplicado

- GTM/RevOps define buyer personas, propuesta de valor, journey y reglas transversales.
- Marketing selecciona perfiles, formula hipótesis, adapta copy/CTA, mide y aprende.
- Toda campaña registra ID/versión o documento/sección/versión.
- Marketing no inventa IDs ni redefine el canónico.
- Los resultados históricos conservan el baseline con que fueron diseñados.

## Hallazgo del piloto

La campaña V3 existente combina `BP-001` y `BP-002` en un copy general. Se conserva como antecedente, pero futuros tests deberían separar:

- productividad / `BP-001`;
- empleabilidad / `BP-002`.

Esto permite atribuir aprendizaje al mensaje sin cambiar simultáneamente oferta y landing.

## No se toca

- No se modifican campañas reales, presupuestos, bids, anuncios o plataformas Ads.
- No se modifica landing, Cloudflare, formularios, Zoho, n8n o WhatsApp.
- No se suben datos personales, exports, credenciales, tokens, IDs completos ni binarios.
- No se modifica `main` directo.
- No se inventan métricas o resultados.

## Validación esperada

- Cambios Markdown solamente.
- Rama basada en `main`.
- Sin borrados ni renombres.
- Sin implementación productiva.
- Marketing deja de presentarse como fuente canónica.
- El piloto Excel V3 referencia versiones GTM vigentes.

## Riesgo

**Amarillo metodológico:** esta estructura condiciona futuras campañas y automatizaciones. Se mitiga con versionado, `BP-000`, separación entre canónico e hipótesis y revisión humana antes de producción.

## Siguiente paso después del merge

Usar la plantilla para preparar el primer test nuevo y decidir una sola variante inicial: productividad (`BP-001`) o empleabilidad (`BP-002`).

## Decisión solicitada

- [ ] APROBADO PARA MERGE
- [ ] CORREGIR ANTES DE MERGE