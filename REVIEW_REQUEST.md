# REVIEW_REQUEST

## PR objetivo

Documentar la aprobacion de Google Ads API Basic Access, la primera ejecucion local exitosa de Keyword Ideas y el radar sanitizado V0 para Excel presencial Santiago.

## Contexto vigente del repo

El repo mantiene una linea acotada para Google Ads read-only orientada al radar comercial de cursos presenciales en Santiago Centro.

La linea vigente:

- no usa MCP;
- usa pipeline local Python read-only;
- mantiene `google-ads.yaml`, scripts `.ps1`, outputs TSV/CSV y credenciales fuera del repo;
- no toca campanas reales ni configuraciones de Google Ads;
- documenta solo estado, metodologia, guardrails y resultados agregados/sanitizados.

## Resumen del PR

Este PR actualiza el estado posterior al PR #16:

- Google aprobo Basic Access para el Developer Token asociado al MCC de Capacita.
- `list_accessible_customers.py` funciono y mostro 2 cuentas accesibles enmascaradas.
- `generate_keyword_ideas.py` funciono localmente contra la cuenta publicitaria real.
- El output bruto quedo local y no versionado.
- Primer barrido: valido API, pero uso semillas demasiado especificas.
- Segundo barrido con keywords reales de Google Ads como semillas genero radar local con 1676 filas.
- Se documento lectura comercial V0: usar demanda general de Excel con filtro presencial en anuncio/landing; no depender solo de keywords `presencial`/`santiago`.

## Rama

`docs/google-ads-basic-access-approved-2026-07-08`

## Archivos creados

- `docs/google-ads/GOOGLE_ADS_KEYWORD_IDEAS_FIRST_RUN_LOG.md`
- `docs/google-ads/GOOGLE_ADS_RADAR_EXCEL_PRESENCIAL_V0_SUMMARY.md`

## Archivos modificados

- `docs/google-ads/GOOGLE_ADS_BASIC_ACCESS_REQUEST_LOG.md`
- `TASK_STATUS.md`
- `CHANGELOG_AGENT.md`
- `REVIEW_REQUEST.md`

## No se toca

- No se sube `google-ads.yaml`.
- No se suben tokens, OAuth JSON, refresh tokens ni access tokens.
- No se suben customer IDs completos.
- No se suben TSV/CSV brutos ni outputs reales.
- No se modifica `main` directo.
- No se ejecuta MCP.
- No se ejecuta `export_campaign_summary.py`.
- No se crean ni modifican campanas, presupuestos, bids, anuncios, assets, conversiones ni configuraciones.

## Validacion esperada

- Cambios documentales solamente.
- Sin secretos ni IDs completos.
- Sin outputs reales.
- Sin archivos binarios.
- Sin mutaciones de Google Ads.
- Siguiente accion acotada: crear lista accionable filtrada para Search, todavia sin tocar campanas reales.

## Riesgos o pendientes

- El radar V0 confirma demanda, pero requiere validacion comercial antes de ejecutar pauta nueva.
- Falta validar si el geo target actual estrecha demasiado la demanda.
- Falta definir estructura de grupos de anuncios y negativas iniciales.
- Falta definir contrato antes de habilitar cualquier resumen de campanas.

## Decision solicitada

- [ ] APROBADO CON OBSERVACIONES
- [ ] CORREGIR ANTES DE MERGE