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
- No se modificaron plataformas Ads, GTM, WordPress, Cloudflare, Zoho, campañas ni producción.