# REVIEW_REQUEST

## PR objetivo

Google Ads read-only pipeline local para operar sin MCP, manteniendo intacta la trazabilidad vigente de Marketing / GTM / RevOps.

## Contexto vigente del repo

El repo ya tiene una linea documental activa para:

- Marketing como ejecucion de campanas, pauta, performance y aprendizajes tacticos.
- GTM/RevOps como destino canonico futuro de buyer persona, segmentacion, journey, scoring, nurturing y touch strategy.
- Skills / AI OS y repos tecnicos como capas separadas de implementacion.

Este PR no reemplaza ese estado. Agrega un bloque nuevo y acotado para Google Ads read-only.

## Resumen del PR

Se preparo una alternativa propia, simple y read-only al Google Ads MCP para poder operar fuera de MCP cuando Codex no expone tools invocables.

Se documentaron los guardrails, el flujo local, las semillas iniciales y tres scripts Python esqueleto con configuracion externa y validaciones de seguridad.

Ademas, `generate_keyword_ideas.py` se corrigio para:

- construir `language` y `geo_target_constants` con resource names segun el patron oficial del cliente Python;
- mantener `KeywordPlanIdeaService` solo para `generate_keyword_ideas`;
- imprimir, si la API los entrega, `text`, `avg_monthly_searches`, `competition`, `low_top_of_page_bid_micros` y `high_top_of_page_bid_micros`.

## Rama

`docs/google-ads-readonly-pipeline-v01`

## Archivos creados

- `docs/google-ads/GOOGLE_ADS_READONLY_PIPELINE_PLAN.md`
- `automation/google-ads-readonly/README.md`
- `automation/google-ads-readonly/GOOGLE_ADS_READONLY_RUNBOOK.md`
- `automation/google-ads-readonly/keyword_seeds_presencial_santiago.csv`
- `automation/google-ads-readonly/output/.gitkeep`
- `scripts/google_ads_readonly/list_accessible_customers.py`
- `scripts/google_ads_readonly/generate_keyword_ideas.py`
- `scripts/google_ads_readonly/export_campaign_summary.py`
- `.gitignore`

## Archivos modificados

- `TASK_STATUS.md`
- `REVIEW_REQUEST.md`
- `CHANGELOG_AGENT.md`

## No se toca

- No se mueven archivos reales de Marketing / GTM / RevOps.
- No se renombran carpetas existentes.
- No se modifica `main` directo.
- No se ejecuta Google Ads API en esta tarea.
- No se ejecuta MCP.
- No se modifican campanas reales.
- No se suben secretos, `.env`, OAuth JSON, `google-ads.yaml` real, customer IDs reales, PII ni exports reales.

## Validacion esperada

- El alcance se mantiene read-only.
- `export_campaign_summary.py` sigue bloqueado.
- `automation/google-ads-readonly/output/` queda ignorado por git, excepto `.gitkeep`.
- La configuracion se lee solo desde env vars o rutas externas al repo.
- La salida de keyword ideas queda lista para mostrar metricas historicas si la API las devuelve.

## Riesgos o pendientes

- Falta probar localmente con credenciales externas fuera del repo.
- Falta definir el contrato del resumen agregado de campanas.
- Falta decidir si ese resumen aceptara GAQL read-only o quedara fuera de la V0.1.
- Falta unir resultados Ads con CRM agregado para CPQL real.

## Decision solicitada

- [ ] APROBADO CON OBSERVACIONES
- [ ] CORREGIR ANTES DE MERGE
