# REVIEW_REQUEST_FAST_PATH

## PR objetivo

Documentar en rama limpia la via rapida validada para Google Ads API desde PowerShell, el radar Excel presencial V0 y el contrato del siguiente diagnostico historico read-only.

## Rama

`docs/google-ads-fast-path-v01`

## Archivos creados

- `docs/google-ads/GOOGLE_ADS_POWERSHELL_FAST_PATH.md`
- `docs/google-ads/GOOGLE_ADS_RADAR_EXCEL_PRESENCIAL_V0_SUMMARY.md`
- `docs/google-ads/GOOGLE_ADS_HISTORICAL_DIAGNOSIS_CONTRACT_V01.md`

## Resumen

Este PR corrige una brecha documental detectada despues del PR #17:

- deja la solucion PowerShell correcta para no repetir iteraciones;
- registra errores resueltos y su mitigacion;
- documenta las semillas reales usadas;
- documenta el radar V0 con 1676 filas procesadas localmente;
- define el contrato del siguiente diagnostico historico real de Ads.

## No se toca

- No se sube `google-ads.yaml`.
- No se suben tokens, OAuth JSON, refresh tokens ni access tokens.
- No se suben customer IDs completos.
- No se suben TSV/CSV brutos ni outputs reales.
- No se modifica `main` directo.
- No se ejecuta MCP.
- No se ejecuta `export_campaign_summary.py`.
- No se crean ni modifican campanas, presupuestos, bids, anuncios, assets, conversiones ni configuraciones.

## Decision solicitada

- [ ] APROBADO CON OBSERVACIONES
- [ ] CORREGIR ANTES DE MERGE