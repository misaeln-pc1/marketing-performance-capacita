# Estado de Tareas

## Estado Actual

- **Estado vigente del repo:** Diagnostico Google Ads historico read-only en PR para revisar gasto/clicks/leads antes de tocar campanas reales.
- **Rama vigente documentada:** `docs/google-ads-history-diagnosis-v01`.
- **Documento nuevo en revision:** `docs/google-ads/GOOGLE_ADS_HISTORY_DIAGNOSIS_CONTRACT_V01.md`.
- **Campana V3 documentada:** `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`.
- **Carpeta reutilizada:** `campaigns/excel-basico-intermedio-presencial-santiago/`.
- **Landing documentada:** `https://capacita.cl/curso-de-excel-presencial-en-santiago`.

## Registro de Actividad

- Se mantuvo la estructura existente de la campana Excel presencial, sin crear un proyecto nuevo ni una carpeta duplicada.
- Se documento que V3 debe ser una campana nueva, separada de las pruebas anteriores con Lead Ads/formulario instantaneo.
- Se registro el motivo: V1/V2 generaron volumen pero baja respuesta, por lo que V3 prueba una landing con friccion comercial antes del contacto.
- Se documento configuracion Meta Ads V3:
  - objetivo Trafico;
  - campana manual de trafico;
  - conjunto `AS01_LANDING_PAGADO_EXCEL_PRESENCIAL`;
  - ubicacion de conversion Sitio web;
  - objetivo de rendimiento Maximizar visitas a la pagina de destino;
  - CTA Cotizar;
  - presupuesto test CLP $5.000 a $8.000 diarios por 24-48 horas.
- Se documento el anuncio inicial `AD01_REEL_9X16_LANDING_PAGADO` como video 9:16, 1080x1920, sin activar inicialmente versiones 1:1 ni 16:9.
- Se registro backlog para posibles pruebas posteriores:
  - `AD02_FEED_1X1_LANDING_PAGADO`;
  - `AD03_HORIZONTAL_16X9_LANDING_PAGADO`.
- Se creo checklist de medicion V3 con metricas publicitarias y comerciales.
- Se agrego archivo de referencias oficiales Meta Ads para Trafico, Reels/9:16, Advantage+ Creative y Advantage+ Placements.
- Se creo `docs/audits/META_ADS_CAMPAIGN_AUDIT_V1.md` sin inventar metricas faltantes.
- Se creo `docs/audits/PAID_ADS_PERFORMANCE_BRIDGE_V1.md` para documentar trazabilidad Meta -> landing/formulario -> Zoho CRM -> contacto -> matricula.
- Se documento bloqueo de Google Ads MCP read-only en `docs/google-ads/GOOGLE_ADS_MCP_READONLY_AUDIT.md`.
- Se documento la clasificacion conceptual Marketing / GTM-RevOps / Skills / Edge / Zoho / WhatsApp+n8n en `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md`.
- Se registro incidencia operativa: creacion accidental directa en `main` de documentacion vacia/de prueba, corregida inmediatamente con contenido valido.
- Se agrego plan de migracion archivo/carpeta en `docs/MARKETING_FILE_LEVEL_MIGRATION_PLAN.md`, sin mover archivos reales.

## Google Ads Read-Only

- Se preparo plan V0.1 de pipeline Google Ads read-only local, sin MCP y sin ejecucion de API inicial.
- PR #14 `docs: plan Google Ads read-only pipeline` fue mergeado a `main`.
- PR #16 `docs: log Google Ads Basic Access request` fue mergeado a `main`.
- PR #17 documento aprobacion Basic Access y radar Excel V0.
- Google aprobo Basic Access para el Developer Token asociado al MCC de Capacita.
- Se documento un pipeline local basado en Google Ads API Python client con configuracion externa y guardas de seguridad.
- Se agrego la carpeta minima `automation/google-ads-readonly/` con runbook, semillas iniciales y `output/` local ignorado por git.
- Se prepararon scripts read-only:
  - `list_accessible_customers.py` para listado de cuentas accesibles;
  - `generate_keyword_ideas.py` para ideas de keywords desde semillas CSV;
  - `export_campaign_summary.py` como scaffold bloqueado hasta aprobar su contrato de reporte;
  - `export_search_history.py` para exportar diagnostico historico real de Search Terms, Keywords, Landing Pages y Campaign Daily.
- Se corrigio `generate_keyword_ideas.py` para construir resource names de idioma y geo siguiendo el patron oficial del cliente Python y para imprimir metricas si la API las entrega.
- Se instalo localmente la libreria `google-ads`.
- Se preparo `google-ads.yaml` fuera del repo y se valido que no mezcla metodos de autenticacion.
- Se regenero ADC/OAuth con scope Google Ads.
- `list_accessible_customers.py` funciono en modo read-only y mostro 2 cuentas accesibles con IDs enmascarados.
- `generate_keyword_ideas.py` funciono en modo read-only despues de Basic Access y genero output TSV local no versionado.
- Primer barrido: valido API, pero fue demasiado estrecho para lectura comercial.
- Segundo barrido usando keywords reales de Google Ads como semillas genero radar local con 1676 filas.
- Lectura V0: existe demanda capturable para Excel, pero la demanda estrictamente presencial/local aparece baja si se usa solo como keyword directa.
- Nuevo diagnostico V0.1: extraer historico real de terminos, keywords, landing pages y campanas para explicar gasto alto/clicks/leads bajos antes de modificar pauta.

## Proxima Accion Recomendada

Antes de mover o reordenar archivos:

1. Revisar y mergear PR vigente de diagnostico Google Ads historico read-only.
2. Ejecutar localmente `export_search_history.py` con rango 30-90 dias.
3. Mantener outputs CSV en local no versionado.
4. Analizar top gasto/clicks sin conversion y decidir negativas/landing/grupos solo con evidencia.

## Proxima Accion Recomendada: Google Ads Read-Only

1. Exportar historial real:
   - search terms;
   - keywords;
   - landing pages;
   - campaign daily.
2. Construir resumen agregado:
   - gasto sin conversion;
   - clicks sin lead;
   - negativas obvias;
   - landings mal alineadas;
   - keywords buenas/caras.
3. No depender solo de Keyword Planner ni Keyword Ideas.
4. No tocar campanas reales hasta revisar el diagnostico.
5. Mantener `export_campaign_summary.py` bloqueado hasta aprobar contrato de reporte separado.

## Pendientes / Bloqueos

- Confirmar fecha, precio y cupos vigentes antes de publicar.
- Confirmar herramienta de analitica para clics internos en WhatsApp/formulario dentro de landing.
- Confirmar si Zoho CRM recibira UTM desde formularios de landing.
- No hay resultados documentados aun para V3; cualquier metrica debe agregarse solo cuando exista dato real.
- No hay CSV agregado versionado para calcular CPL, CPQL, CPA, tasa de contacto o tasa de matricula.
- Google Ads MCP no se usara para esta linea porque Codex no expuso tools invocables de forma confiable.
- Clasificacion GTM/RevOps requiere revision humana antes de cualquier migracion fisica.
- Falta PR posterior en Global para crear canonicos GTM/RevOps.
- El script de resumen de campanas queda bloqueado hasta decidir si el reporte se acepta con GAQL read-only o con export UI fuera del repo.
- No hay outputs reales versionados para la linea Google Ads read-only.
- Sigue pendiente la union comercial Google Ads -> landing -> CRM -> matricula para CPQL real.

## Notas de Alcance

- No crear estructura duplicada de campana.
- No subir assets binarios pesados.
- No subir datos reales de leads.
- No subir capturas, exportaciones CRM, secretos ni credenciales.
- No modificar campanas reales desde el repositorio.
- No modificar landing de produccion desde el repositorio.
- No mover archivos reales de Marketing hacia GTM/RevOps sin PR posterior especifico.
- No usar MCP para la linea Google Ads read-only.
- No ejecutar mutaciones ni cambios sobre Google Ads reales.
- No tocar `main` directo.