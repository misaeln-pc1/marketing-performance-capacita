# REVIEW_REQUEST

## PR objetivo

Documentar la aprobacion de Google Ads API Basic Access y la primera ejecucion local exitosa de Keyword Ideas en modo read-only.

## Contexto vigente del repo

El repo mantiene una linea acotada para Google Ads read-only orientada al radar comercial de cursos presenciales en Santiago Centro.

La linea vigente:

- no usa MCP;
- usa pipeline local Python read-only;
- mantiene `google-ads.yaml`, scripts `.ps1`, outputs TSV y credenciales fuera del repo;
- no toca campanas reales ni configuraciones de Google Ads;
- documenta solo estado, metodologia, guardrails y resultados agregados/sanitizados.

## Resumen del PR

Este PR actualiza el estado posterior al PR #16:

- Google aprobo Basic Access para el Developer Token asociado al MCC de Capacita.
- `list_accessible_customers.py` funciono y mostro 2 cuentas accesibles enmascaradas.
- `generate_keyword_ideas.py` funciono localmente contra la cuenta publicitaria real.
- El output bruto quedo local y no versionado.
- El primer barrido mostro volumen bajo/cero para semillas muy especificas, por lo que se recomienda ampliar semillas y validar geografia antes de sacar conclusiones comerciales.

## Rama

`docs/google-ads-basic-access-approved-2026-07-08`

## Archivos creados

- `docs/google-ads/GOOGLE_ADS_KEYWORD_IDEAS_FIRST_RUN_LOG.md`

## Archivos modificados

- `docs/google-ads/GOOGLE_ADS_BASIC_ACCESS_REQUEST_LOG.md`
- `TASK_STATUS.md`
- `CHANGELOG_AGENT.md`
- `REVIEW_REQUEST.md`

## No se toca

- No se sube `google-ads.yaml`.
- No se suben tokens, OAuth JSON, refresh tokens ni access tokens.
- No se suben customer IDs completos.
- No se sube TSV bruto ni outputs reales.
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
- Siguiente accion acotada: segundo barrido con semillas mas amplias y salida local no versionada.

## Riesgos o pendientes

- El primer output no es suficiente para decidir inversion porque usa semillas demasiado especificas.
- Falta validar si el geo target actual estrecha demasiado la demanda.
- Falta construir un radar agregado por curso/intencion/volumen/competencia.
- Falta definir contrato antes de habilitar cualquier resumen de campanas.

## Decision solicitada

- [ ] APROBADO CON OBSERVACIONES
- [ ] CORREGIR ANTES DE MERGE