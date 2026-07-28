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
- Se crearon cuatro briefs v1.0.0 para `BP-001` a `BP-004`.
- Se dejó `BP-000` como control y no como audiencia de campaña.
- Se separaron los carriles B2C y B2B y se documentaron requisitos previos de activación.
- Se priorizó `BP-001` como primer desarrollo creativo recomendado y `BP-002` como segunda prueba.
- No se tocaron campañas, landing, CRM, Cloudflare, n8n, WhatsApp, datos reales ni producción.

## 2026-07-11

- Se ejecutó un diagnóstico Google Ads read-only de 90 días con configuración y outputs fuera del repo.
- El primer export produjo siete reportes válidos y dos errores GAQL acotados.
- PR #29 agregó `export_missing_reports.py` para corregir términos de búsqueda y landing pages.
- La ejecución corregida produjo 1.825 filas de términos y 8.482 filas de landing pages, sin errores.
- Se analizaron campañas, keywords, Quality Score, términos, dispositivos, destinos y conversiones registradas.
- Se confirmó deterioro de `curso excel básico e intermedio` por crecimiento de volumen y baja conversión registrada.
- Se confirmó mezcla de intención y fuga hacia páginas secundarias.
- Se dejó pendiente Auction Insights nominal, assets/sitelinks, histórico 12/24 meses y reconciliación con Zoho.
- Se abrió Edge #27 para auditar GTM/Google tag y atribución.
- Se abrió Edge #28 para auditar SEO técnico, SEO local y visibilidad IA.
- Se abrió Global #101 para evaluar, después de evidencia, posibles activos transversales.
- Se creó PR #30 para sincronizar `TASK_STATUS.md`, decisiones, reglas locales y mejora continua.

## 2026-07-12

- Se separó el alcance de PR #29: quedó limitado a Google Ads y diagnóstico agregado.
- Los seis documentos SEO/GEO se trasladaron sin pérdida a la rama `docs/marketing-seo-geo-baseline-v01`.
- Se abrió PR #31 para la metodología SEO, Local SEO y visibilidad en motores generativos.
- Se agregó `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md` con hallazgos sanitizados.
- Se alineó `REPO_RULES.md` con GTM/RevOps como fuente canónica.
- Se actualizaron `TASK_STATUS.md` y `DECISIONES.md` con el estado real y la secuencia vigente.
- PR #29, PR #30 y PR #31 quedaron mergeados.
- Se validó acceso al archivo de Drive `Historial_Rendimiento_GoogleAds` y sus pestañas operativas.
- Se definió `GOOGLE_ADS_STATUS_ANALYSIS_PROCEDURE_V01.md`: todo estatus recurrente debe combinar PowerShell/API fresco y Drive; si falta una fuente, el análisis se declara provisional.
- No se modificaron plataformas Ads, GTM, WordPress, Cloudflare, Zoho, campañas ni producción.

## 2026-07-28

- Se preparó consolidación documental mínima para tres landings Excel B2C pagadas sin mergear completo PR #35.
- Se creó `docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md`.
- Se creó XFER de respuesta Marketing → Edge `v02` para consumir Edge XFER `v05` como `CONSUMED_WITH_CHANGES`.
- Se creó `docs/BITACORA_XFER.md` para registrar el XFER producido y el XFER externo consumido.
- Se actualizaron `TASK_STATUS.md`, `DECISIONES.md` y `REVIEW_REQUEST.md` con el estado vigente del frente PR #35 / issue #43 / Edge PR #36.
- PR #46 fue mergeado en `main` con SHA `4404ddbe2c6b6d0ec209cc7dc11e0480da85771d`.
- Se preparó PR limpio desde `main` para rescatar PageSense/CRO sin mergear PR #34 antiguo.
- Se agregaron `docs/pagesense/PAGESENSE_CRO_REPORTING_BASELINE_V01.md` y `docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md`.
- Se documentó que goals de clic no son submits confirmados ni leads, y que la URL de redirección B2C con nombre/correo es riesgo rojo de privacidad.
- PR #47 fue mergeado en `main` con SHA `1faf07729b3c3208465d4aabebd91437b1069dab` y PR #34 quedó cerrado como `SUPERSEDED`.
- Se cerró PR #28 como `SUPERSEDED/PARCIAL`, se cerró issue #27 como cierre administrativo y se creó issue #48 para residuales manuales Google Ads.
- Se preparó PR limpio desde `main` para normalizar el XFER comercial de Learning Games `GAME-EXCEL-BASICO-BLOCKS-001`, sin mergear PR #41 draft.
- Se agregó `docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md` y se registró en `docs/BITACORA_XFER.md`.
- No se modificaron campañas, Google Ads, Meta Ads, Edge, Cloudflare, Worker, DNS, sitemap, GTM, PageSense, Turnstile, Zoho, APIs, scripts, exports ni producción.
