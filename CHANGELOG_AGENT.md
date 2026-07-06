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
