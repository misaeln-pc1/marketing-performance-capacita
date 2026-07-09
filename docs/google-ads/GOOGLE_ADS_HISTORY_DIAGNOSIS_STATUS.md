# Google Ads History Diagnosis Status

## Estado

- Rama: `docs/google-ads-history-diagnosis-v01`.
- Objetivo: preparar diagnostico historico read-only para explicar gasto alto, clicks y baja llegada de leads.
- No se ejecuta API desde GitHub.
- No se suben CSV brutos, credenciales, tokens, YAML, customer IDs completos, screenshots ni PII.

## Artefactos principales

- `docs/google-ads/GOOGLE_ADS_HISTORY_DIAGNOSIS_CONTRACT_V01.md`
- `docs/google-ads/GOOGLE_ADS_HISTORY_DIAGNOSIS_LOCAL_COMMANDS.md`
- `scripts/google_ads_readonly/export_search_history.py`
- `automation/google-ads-readonly/GOOGLE_ADS_READONLY_RUNBOOK.md`

## Siguiente paso

1. Revisar PR.
2. Ejecutar localmente primero en dry-run.
3. Si pasa, ejecutar con `--execute`.
4. Mantener outputs solo locales.
5. Compartir solo conteos por archivo o errores sanitizados.
