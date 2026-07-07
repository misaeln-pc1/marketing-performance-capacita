# Changelog Agent

## 2026-05-26

- Se preparo auditoria documental V1 de Meta Ads sin usar API, sin tocar campanas reales y sin inventar metricas faltantes.
- Se agrego puente de performance pagada para trazar Meta -> landing/formulario -> Zoho CRM -> contacto -> matricula.
- Se intento validar Google Ads MCP read-only; quedo bloqueado porque no hay herramienta MCP disponible/autenticada en el entorno.

## 2026-07-05

- Se preparo plan V0.1 para un pipeline Google Ads read-only local sin depender de MCP.
- Se agregaron runbook, semillas iniciales y carpeta de output vacia para trabajo local.
- Se agregaron tres scripts esqueleto con configuracion externa y guardas para evitar secretos versionados y mutaciones.
- Se corrigio `generate_keyword_ideas.py` para usar resource names de idioma y geo segun el patron oficial del cliente Python y para imprimir metricas de ideas si la API las entrega.

## 2026-07-06

- PR #14 fue mergeado a `main` con el pipeline local Google Ads read-only.
- Se valido ejecucion local hasta llamada API read-only.
- La consulta de ideas de keywords contra cuenta real quedo bloqueada por nivel de acceso de prueba.
- Se envio solicitud de Google Ads API Basic Access desde API Center del MCC de Capacita.
- Se documento el estado en `docs/google-ads/GOOGLE_ADS_BASIC_ACCESS_REQUEST_LOG.md`.
