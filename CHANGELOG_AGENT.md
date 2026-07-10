# Changelog Agent

## 2026-05-26

- Se preparó auditoría documental V1 de Meta Ads sin usar API, sin tocar campañas reales y sin inventar métricas faltantes.
- Se agregó puente de performance pagada para trazar Meta → landing/formulario → Zoho CRM → contacto → matrícula.
- Se intentó validar Google Ads MCP read-only; quedó bloqueado porque no había herramienta MCP disponible/autenticada.

## 2026-07-05

- Se preparó plan V0.1 para pipeline Google Ads read-only local sin depender de MCP.
- Se agregaron runbook, semillas iniciales y carpeta de output local.
- Se agregaron scripts esqueleto con configuración externa y guardas de seguridad.
- Se corrigió `generate_keyword_ideas.py` según el patrón oficial del cliente Python.

## 2026-07-06

- PR #14 fue mergeado con el pipeline Google Ads read-only.
- Se validó ejecución local hasta llamada API read-only.
- Se solicitó Google Ads API Basic Access.

## 2026-07-08

- Google aprobó Basic Access.
- `list_accessible_customers.py` mostró dos cuentas accesibles enmascaradas.
- `generate_keyword_ideas.py` generó output TSV local no versionado.
- Se documentó que las primeras semillas eran demasiado específicas para concluir demanda.
- `export_campaign_summary.py` permaneció bloqueado.

## 2026-07-10

- Se verificó el merge del contrato corporativo GTM/RevOps en Global PR #88.
- Se abrió issue #19 y se mergeó Marketing PR #20 para alinear el repo con los canónicos.
- Se creó `docs/GTM_CONSUMPTION_BRIDGE.md`.
- Se creó `templates/CAMPAIGN_BRIEF_GTM.md`.
- Se actualizaron README, contexto y carpetas para eliminar propiedad paralela de buyer personas, journey y propuesta de valor.
- Se creó `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md` como primer consumidor.
- Se registró `BP-001` primario y `BP-002` secundario para el antecedente V3.
- Se detectó que futuros experimentos deben separar productividad y empleabilidad si se desea atribuir resultados por perfil.
- Se abrió issue #21 para preparar los briefs operativos de los buyer personas activos.
- Se creó el índice `campaigns/excel-basico-intermedio-presencial-santiago/briefs/README.md`.
- Se crearon cuatro briefs v1.0.0:
  - `BP-001 — Desbordado Operativo`;
  - `BP-002 — Reinserción Laboral`;
  - `BP-003 — Coordinador B2B`;
  - `BP-004 — Dueño o Jefatura PyME`.
- Se dejó `BP-000` como control y no como audiencia de campaña.
- Se separaron los carriles B2C y B2B y se documentaron requisitos previos de activación.
- Se priorizó `BP-001` como primer desarrollo creativo recomendado y `BP-002` como segunda prueba.
- No se tocaron campañas, landing, CRM, Cloudflare, n8n, WhatsApp, datos reales ni producción.
