# Estado de Tareas

## Estado Actual

- **Estado:** Se preparo auditoria documental V1 de Meta Ads y puente de performance pagada.
- **Rama actual de trabajo:** `docs/meta-ads-v1-audit`.
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

## Proxima Accion Recomendada

Antes de tomar decisiones de optimizacion:

1. Preparar exportacion agregada Meta Ads sin datos personales.
2. Preparar exportacion agregada Zoho CRM sin datos personales.
3. Confirmar captura de UTMs y `f_ads_fbclid` desde landing/formulario hacia CRM.
4. Definir lead calificado para calcular CPQL.
5. Evaluar calidad comercial, no solo CPL.

## Pendientes / Bloqueos

- Confirmar fecha, precio y cupos vigentes antes de publicar.
- Confirmar herramienta de analitica para clics internos en WhatsApp/formulario dentro de landing.
- Confirmar si Zoho CRM recibira UTM desde formularios de landing.
- No hay resultados documentados aun para V3; cualquier metrica debe agregarse solo cuando exista dato real.
- No hay CSV agregado versionado para calcular CPL, CPQL, CPA, tasa de contacto o tasa de matricula.

## Notas de Alcance

- No crear estructura duplicada de campana.
- No subir assets binarios pesados.
- No subir datos reales de leads.
- No subir capturas, exportaciones CRM, secretos ni credenciales.
- No modificar campanas reales desde el repositorio.
- No modificar landing de produccion desde el repositorio.
