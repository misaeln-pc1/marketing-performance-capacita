# Estado de Tareas

## Estado Actual

- **Estado:** Clasificación Marketing / GTM-RevOps documentada y pendiente de revisión por PR correctivo.
- **Rama actual de trabajo:** `docs/fix-marketing-gtm-classification-followup-2026-06-21`.
- **Documento nuevo en revisión:** `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md`.
- **Campaña V3 documentada:** `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`.
- **Carpeta reutilizada:** `campaigns/excel-basico-intermedio-presencial-santiago/`.
- **Landing documentada:** `https://capacita.cl/curso-de-excel-presencial-en-santiago`.

## Registro de Actividad

- Se mantuvo la estructura existente de la campaña Excel presencial, sin crear un proyecto nuevo ni una carpeta duplicada.
- Se documentó que V3 debe ser una campaña nueva, separada de las pruebas anteriores con Lead Ads/formulario instantáneo.
- Se registró el motivo: V1/V2 generaron volumen pero baja respuesta, por lo que V3 prueba una landing con fricción comercial antes del contacto.
- Se documentó configuración Meta Ads V3:
  - objetivo Tráfico;
  - campaña manual de tráfico;
  - conjunto `AS01_LANDING_PAGADO_EXCEL_PRESENCIAL`;
  - ubicación de conversión Sitio web;
  - objetivo de rendimiento Maximizar visitas a la página de destino;
  - CTA Cotizar;
  - presupuesto test CLP $5.000 a $8.000 diarios por 24-48 horas.
- Se documentó el anuncio inicial `AD01_REEL_9X16_LANDING_PAGADO` como video 9:16, 1080x1920, sin activar inicialmente versiones 1:1 ni 16:9.
- Se registró backlog para posibles pruebas posteriores:
  - `AD02_FEED_1X1_LANDING_PAGADO`;
  - `AD03_HORIZONTAL_16X9_LANDING_PAGADO`.
- Se creó checklist de medición V3 con métricas publicitarias y comerciales.
- Se agregó archivo de referencias oficiales Meta Ads para Tráfico, Reels/9:16, Advantage+ Creative y Advantage+ Placements.
- Se creó `docs/audits/META_ADS_CAMPAIGN_AUDIT_V1.md` sin inventar métricas faltantes.
- Se creó `docs/audits/PAID_ADS_PERFORMANCE_BRIDGE_V1.md` para documentar trazabilidad Meta -> landing/formulario -> Zoho CRM -> contacto -> matrícula.
- Se documentó bloqueo de Google Ads MCP read-only en `docs/google-ads/GOOGLE_ADS_MCP_READONLY_AUDIT.md`.
- Se documentó la clasificación conceptual Marketing / GTM-RevOps / Skills / Edge / Zoho / WhatsApp+n8n en `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md`.
- Se registró incidencia operativa: creación accidental directa en `main` de documentación vacía/de prueba, corregida inmediatamente con contenido válido. Esta rama correctiva evita nuevos cambios directos a `main`.

## Próxima Acción Recomendada

Antes de mover o reordenar archivos:

1. Revisar y mergear el PR correctivo de clasificación Marketing / GTM-RevOps.
2. Revisar `core/`, `references/` y `automation/` archivo por archivo.
3. Decidir qué queda como referencia en Marketing y qué se convierte en fuente canónica en GTM/RevOps dentro de Global.
4. No mover archivos físicos sin un PR específico posterior.
5. Mantener Marketing como ejecución de campañas y performance; GTM/RevOps como dueño de la lógica comercial transversal.

## Pendientes / Bloqueos

- Confirmar fecha, precio y cupos vigentes antes de publicar.
- Confirmar herramienta de analítica para clics internos en WhatsApp/formulario dentro de landing.
- Confirmar si Zoho CRM recibirá UTM desde formularios de landing.
- No hay resultados documentados aún para V3; cualquier métrica debe agregarse solo cuando exista dato real.
- No hay CSV agregado versionado para calcular CPL, CPQL, CPA, tasa de contacto o tasa de matrícula.
- Google Ads MCP no está disponible o no autentica en el entorno actual.
- Clasificación GTM/RevOps requiere revisión humana antes de cualquier migración física.

## Notas de Alcance

- No crear estructura duplicada de campaña.
- No subir assets binarios pesados.
- No subir datos reales de leads.
- No subir capturas, exportaciones CRM, secretos ni credenciales.
- No modificar campañas reales desde el repositorio.
- No modificar landing de producción desde el repositorio.
- No mover archivos reales de Marketing hacia GTM/RevOps sin PR posterior específico.
