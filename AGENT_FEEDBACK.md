# AGENT_FEEDBACK

## Fecha
2026-09-05

## Agente
Gemini/Antigravity.

## Tarea recibida
Ejecutar exclusivamente FASE 0 y FASE 1 de `misaeln-pc1/capacita-task-hub#215` (Issue padre: `misaeln-pc1/marketing-performance-capacita#85`) en la rama existente `feature/marketing-official-read-control-plane-p0`:
1. Fase 0: Saneamiento de PR #52 mediante un rescate limpio desde main, sin mergear, sin borrar, sin cerrar, sin reescribir ni tocar su rama histórica, sanitizando IDs reales, tokens y corrigiendo rutas canónicas de pesados a SharePoint.
2. Fase 1: Control plane oficial-first estrictamente READ para Google Ads, GA4, Search Console, Meta Ads y downstream agregado, más un Negative Keyword Guard vivo e idempotente con deduplicación, separación B2C/B2B y emisión de `HOLD_DATA_GAP` ante ausencia de lectura viva.

## Resultado
Hecho.

## Evidencia
* Rama: `feature/marketing-official-read-control-plane-p0`
* Commit SHA: `22794c505fe4da126d21639e9a3218338ce13696`
* PR: Pendiente de creación tras push.
* Diff stat: 21 files changed, 2598 insertions(+), 53 deletions(-)
* Comandos ejecutados:
  - `git fetch origin`
  - `git checkout feature/marketing-official-read-control-plane-p0`
  - `python scripts/google_ads_readonly/list_accessible_customers.py --config-path ...0-Origen\google-ads.yaml --execute` (smoke-read Fast Path)
  - `python -m unittest tests/test_negative_guard.py` (suite de 10 tests unitarios)
  - `python scripts/google_ads_readonly/run_negative_guard.py --snapshot-path tests/fixtures/negative_snapshot_fixtures.json --idempotency-check`
  - `python scripts/run_offline_validations.py` (runner integral de validaciones, secret scan, pii scan, full ID scan y git diff --check)
* Pruebas realizadas:
  - 10 tests unitarios PASS en 0.021s.
  - Idempotencia comprobada: 0 recomendaciones duplicadas en segundo run.
  - Comprobación de excepción "paso a paso": rechazada como negativa global con veredicto CONFLICT.
  - Detección de conflicto B2C vs B2B: rechazada aplicación de términos B2B a campaña B2B Empresa con veredicto CONFLICT.
  - Emisión de `HOLD_DATA_GAP` ante ausencia de snapshot vivo o auth insuficiente.
  - Verificación de sintaxis PowerShell: `SYNTAX_OK`.
  - Escaneo de secretos, tokens, PII e IDs en diff: 0 hallazgos.

## Objeciones o desacuerdos
Estoy de acuerdo con el plan canónico de ChatGPT / Global Control. No hay objeciones metodológicas.
Se destaca positivamente la decisión de no forzar un merge de PR #52 ni tocar su rama histórica, permitiendo un rescate 100% sanitizado.
Asimismo, la arquitectura de paridad METHOD_A (Fast Path) vs METHOD_B (Google Ads MCP) demostró que el Fast Path existente en el repo es superior en reproducibilidad, control y volumen de datos (search terms paginados a CSV/TSV) sin incurrir en consumo excesivo de contexto LLM ni pasos conversacionales manuales.

## Riesgos detectados
1. **Scope Insuficiente en ADC Local:** El archivo `google-ads.yaml` depende de Application Default Credentials (ADC) que actualmente no poseen el scope `https://www.googleapis.com/auth/adwords`, arrojando `ACCESS_TOKEN_SCOPE_INSUFFICIENT`. Se requiere un flujo OAuth con refresh token autorizado cuando Misael decida activar la lectura viva regular.
2. **Expiración de Tokens de Usuario en Meta Ads:** Como se documentó en el procedimiento saneado de Meta Ads, los tokens generados por Graph API Explorer son efímeros. Para automatizaciones futuras sostenibles se requerirá formalizar un System User en el Business correspondiente.

## Archivos modificados
- `DECISIONES.md`
- `CHANGELOG_AGENT.md`
- `TASK_STATUS.md`
- `REVIEW_REQUEST.md`

## Archivos creados
- `docs/meta-ads/META_ADS_READONLY_LOCAL_ENV_TEMPLATE.env.example`
- `docs/meta-ads/META_ADS_READONLY_EXPORT_RUNBOOK_V01.md`
- `docs/meta-ads/META_ADS_READONLY_API_ROUTE_A_PROCEDURE_V01.md`
- `scripts/meta_ads_readonly/export_meta_ads_readonly.ps1`
- `docs/google-ads/GOOGLE_ADS_NEGATIVE_GUARD_SPECIFICATION_V01.md`
- `docs/analytics/MARKETING_OFFICIAL_READ_CONTROL_PLANE_V01.md`
- `core/negative_guard/__init__.py`
- `core/negative_guard/models.py`
- `core/negative_guard/classifier.py`
- `core/negative_guard/guard.py`
- `core/negative_guard/snapshot.py`
- `tests/fixtures/negative_snapshot_fixtures.json`
- `tests/test_negative_guard.py`
- `scripts/google_ads_readonly/run_negative_guard.py`
- `scripts/run_offline_validations.py`
- `AGENT_FEEDBACK.md`

## Qué no se tocó
- La rama histórica de PR #52 (`docs/marketing-meta-ads-readonly-api-route-a-20260729-use-this3`) permaneció completamente intacta.
- No se hizo merge de PR #52.
- No se modificaron campañas reales, presupuestos, pujas, anuncios ni palabras clave en Google Ads ni Meta Ads.
- No se interactuó con Zoho CRM en modo write ni se modificó producción o Cloudflare.
- No se tocó la rama `main`.

## Siguiente recomendación
Hacer commit de la rama `feature/marketing-official-read-control-plane-p0`, push a `origin` y abrir un PR en GitHub enlazando a `misaeln-pc1/capacita-task-hub#215` y `misaeln-pc1/marketing-performance-capacita#85` para revisión de Misael y ChatGPT / Global Control.
