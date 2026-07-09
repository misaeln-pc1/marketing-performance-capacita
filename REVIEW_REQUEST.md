# REVIEW_REQUEST

## PR objetivo

Preparar diagnostico historico Google Ads read-only para explicar gasto alto, clicks y baja llegada de leads antes de modificar campanas reales.

## Contexto vigente del repo

El repo mantiene Google Ads como linea comercial-publicitaria read-only para radar, aprendizaje de campanas y diagnostico de performance.

El usuario reporta:

- gasto diario aproximado CLP $20.000;
- 16-18 clicks aprox.;
- 0-2 leads aprox.;
- sospecha de errores en keywords, landing, calidad post-click, competencia o estructura de campana.

## Resumen del PR

Este PR agrega:

- contrato V0.1 de diagnostico historico Google Ads read-only;
- script `export_search_history.py` para exportar localmente:
  - search terms;
  - keywords;
  - landing pages;
  - campaign daily;
- actualizacion del runbook con comando local;
- actualizacion de `TASK_STATUS.md` y `CHANGELOG_AGENT.md`.

## Rama

`docs/google-ads-history-diagnosis-v01`

## Archivos creados

- `docs/google-ads/GOOGLE_ADS_HISTORY_DIAGNOSIS_CONTRACT_V01.md`
- `scripts/google_ads_readonly/export_search_history.py`

## Archivos modificados

- `automation/google-ads-readonly/GOOGLE_ADS_READONLY_RUNBOOK.md`
- `TASK_STATUS.md`
- `CHANGELOG_AGENT.md`
- `REVIEW_REQUEST.md`

## Validacion esperada

- Script solo read-only.
- Requiere `--execute` para llamar API.
- Lee config externa fuera del repo.
- Escribe CSV solo en `automation/google-ads-readonly/output/` o ruta local externa.
- No crea ni modifica campanas.
- No toca presupuestos, bids, anuncios, keywords, negativas, assets, conversiones ni configuraciones.
- No versiona outputs, customer IDs completos, tokens, YAML ni PII.

## Riesgos o pendientes

- No se ejecuto el script desde GitHub; debe probarse localmente.
- Algunas consultas GAQL pueden requerir ajuste si la cuenta/campana no tiene datos o si una vista no soporta un campo esperado.
- Los CSV brutos pueden contener nombres de campanas, grupos, terminos y URLs; deben quedar solo local.
- El diagnostico aun no resuelve tracking Zoho/CRM; solo entrega evidencia Google Ads.

## Decision solicitada

- [ ] APROBADO CON OBSERVACIONES
- [ ] CORREGIR ANTES DE MERGE