# DECISIONES

Registro de decisiones operativas del repo `marketing-performance-capacita`.

## Decisiones vigentes

| Fecha | Decision | Alcance | Riesgo | Evidencia |
|---|---|---|---:|---|
| 2026-06-21 | Mantener el repo `marketing-performance-capacita` sin renombrar y adoptar el alias operativo **Marketing (Campanas & Growth)**. | Naming, documentacion, control operativo | Amarillo | `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` |
| 2026-06-21 | GTM/RevOps es dueno de buyer persona, propuesta de valor, segmentacion, journey, scoring, nurturing y touch strategy. Marketing queda como ejecucion de campanas y performance. | Frontera Marketing / GTM-RevOps | Amarillo | `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` |
| 2026-06-21 | No mover archivos reales desde Marketing a GTM/RevOps sin PR especifico y revisado. | Migracion documental | Amarillo | `docs/MARKETING_FILE_LEVEL_MIGRATION_PLAN.md` |
| 2026-06-21 | No mover carpetas completas; separar verdad canonica, ejecucion tactica y ejecucion tecnica. | Arquitectura | Amarillo | `docs/MARKETING_FILE_LEVEL_MIGRATION_PLAN.md` |
| 2026-07-10 | Adoptar `docs/GTM_CONSUMPTION_BRIDGE.md` como contrato local obligatorio para campanas nuevas o revisadas. | Campanas y briefs | Amarillo | Global PR #88; Marketing PR #20 |
| 2026-07-10 | Toda campana debe conservar baseline canonico y aplicacion local separados. Usar ID/version o documento/seccion/version; Marketing no inventa IDs. | Trazabilidad GTM | Amarillo | `templates/CAMPAIGN_BRIEF_GTM.md` |
| 2026-07-10 | Aplicar el contrato primero a Excel presencial V3 sin modificar la campana real. `BP-001` queda primario y `BP-002` secundario como lectura documental. | Piloto | Verde/Amarillo | `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md` |
| 2026-07-10 | Para pruebas futuras, separar mensajes de productividad y empleabilidad cuando se quiera medir respuesta por buyer persona. | Diseno experimental | Amarillo | Hallazgo del piloto GTM V1 |
| 2026-07-10 | Mantener cuatro briefs operativos separados para `BP-001` a `BP-004`; `BP-000` es control y no audiencia de campana. | Arquitectura de campanas | Amarillo | Issue #21; carpeta `briefs/` |
| 2026-07-10 | Ejecutar un buyer persona primario y una hipotesis por prueba. No mezclar B2C y B2B en campana, landing o medicion comun. | Experimentacion | Amarillo | `briefs/README.md` |
| 2026-07-10 | Priorizar `BP-001` y `BP-002` para creatividad B2C inmediata; `BP-003` y `BP-004` requieren oferta, landing, formulario y ruta comercial B2B verificadas. | Secuencia operativa | Amarillo | Briefs individuales v1.0.0 |
| 2026-07-11 | Completar diagnostico de datos antes de modificar campanas o landings. El plan vigente exige terminos, destinos, competencia, tracking y reconciliacion comercial. | Google Ads y CRO | Amarillo | PR #29; Edge #27; `TASK_STATUS.md` |
| 2026-07-11 | Tratar conversiones, CVR y CPA actuales como provisionales hasta auditar GTM/Google tag y reconciliar formularios con Zoho. Gasto, clics, CPC, terminos y senales de subasta siguen siendo utilizables. | Medicion y atribucion | Amarillo | Edge #27; baseline Google Ads |
| 2026-07-11 | Auction Insights nominal se obtiene manualmente y permanece privado; la API se usa para senales propias y agregadas. | Competencia | Amarillo | PR #29; limitacion tecnica validada |
| 2026-07-11 | No crear seis landings por existencia de clusters. Una landing distinta requiere intencion, volumen, promesa, CTA, medicion y prueba controlada suficientes. | Arquitectura de landing | Amarillo | `docs/google-ads/GOOGLE_ADS_COMPETITION_AND_LANDING_DIAGNOSIS_V01.md` |
| 2026-07-11 | Separar documentacion Google Ads de metodologia SEO/GEO. PR #29 queda Ads; PR #31 contiene SEO, Local SEO y visibilidad IA. | Alcance de PR | Verde | PR #29 y PR #31 |
| 2026-07-11 | Los conceptos descubiertos permanecen locales hasta demostrar estabilidad y reutilizacion. Global #101 evalua candidatos; no cambia canonicos todavia. | Mejora continua | Amarillo | Global issue #101 |
| 2026-07-12 | Todo analisis recurrente de estatus de Google Ads debe combinar un export fresco read-only por PowerShell/API con la hoja de Drive `Historial_Rendimiento_GoogleAds`. Si falta una fuente, el informe debe declararse provisional e indicar explicitamente el acceso faltante. | Reporting, trazabilidad y dashboard | Amarillo | `docs/google-ads/GOOGLE_ADS_STATUS_ANALYSIS_PROCEDURE_V01.md` |
| 2026-07-28 | Preparar tres landings B2C pagadas de Excel como piloto documental minimo: A Basico-Intermedio `BP-001`, B Desde cero `BP-002`, C Clases presenciales con profesor `BP-001`; todas `noindex,follow`, fuera de sitemap y sin reemplazar la pagina organica. | Landings pagadas B2C Excel | Amarillo | `docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md` |
| 2026-07-28 | Consumir XFER Edge v05 como `CONSUMED_WITH_CHANGES` y responder a Capacita Edge con XFER Marketing v02. La respuesta no autoriza publicacion, tracking real, Zoho, GTM, PageSense, Turnstile, Cloudflare ni Google Ads. | XFER Marketing ↔ Edge | Amarillo | `docs/xfer/XFER__MARKETING__CAPACITA_EDGE__EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE__20260728-174500__v02__READY__MARKETING_REVIEW.md`; `docs/BITACORA_XFER.md` |
| 2026-07-28 | Aceptar PageSense como fuente complementaria CRO, no como fuente de leads o matriculas. Goals de clic (`enviar Pre`, `inicio`, `Enviar Empresa-Excel`) quedan reclasificados como interaccion secundaria hasta validar submit confirmado. | PageSense / CRO | Amarillo | `docs/pagesense/PAGESENSE_CRO_REPORTING_BASELINE_V01.md`; `docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md` |
| 2026-07-28 | Detectar como riesgo rojo que nombre y correo viajan en la URL de redireccion B2C. Marketing no lo corrige; debe enrutarse a Edge/Zoho con autorizacion especifica. | Privacidad / formularios | Rojo | `docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md` |
| 2026-07-28 | Normalizar el XFER comercial de Learning Games `GAME-EXCEL-BASICO-BLOCKS-001` desde una rama limpia sobre `main`; PR #41 queda como antecedente draft y no como PR a mergear. | XFER Marketing -> Learning Games | Verde/Amarillo | `docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md`; `docs/BITACORA_XFER.md` |
| 2026-07-28 | Rescatar el estandar de produccion de assets Meta Ads de PR #8 mediante un PR limpio desde `main`: formatos 4:5, 1:1, 9:16, video 9:16 para Stories/Reels, video 4:5 para Feed, naming y bodega externa. | Meta Ads / creatividades | Verde/Amarillo | `assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md` |
| 2026-08-09 | La cuenta Meta Ads operativa que contiene V3 es la cuenta personal/standalone accesible bajo `Otros activos`, referencia sanitizada `...2327`; no pertenece actualmente a `Capacita Spa`, `Capacita` ni `Misael N. J.` como Business Portfolio. Identificarla siempre por inventario de campañas, no por nombre de portfolio. | Routing Meta Ads / continuidad | Amarillo | `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md` |
| 2026-08-09 | La referencia histórica aproximada `...9327` queda `SUPERSEDED`; no inferir bloqueos de Ads desde incidentes históricos de WhatsApp. La cuenta `...2327` no mostró restricciones publicitarias visibles en la auditoría 2026-08-09. | Routing / restricciones Meta | Amarillo | `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md` |
| 2026-08-09 | Para un futuro System User permanente, usar `Capacita Spa` solo después de compartir/asignar formalmente acceso a `...2327`, conservando la propiedad actual; no reclamar ni mover propiedad sin decisión específica. | Acceso API permanente | Rojo | `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md` |

## Reglas derivadas

- Marketing ejecuta campanas, pauta, targeting, copies, activos, performance y aprendizajes tacticos.
- GTM/RevOps mantiene la fuente canonica y su versionado.
- Las campanas historicas conservan el baseline usado; no se reescriben automaticamente.
- La evidencia de una campana no modifica GTM por si sola: debe volver mediante issue/PR con alcance e impacto.
- Una prueba de mensaje debe mantener constantes oferta, landing y otras variables relevantes cuando sea viable.
- El paquete de briefs ofrece alternativas; no autoriza activar todas simultaneamente.
- Los ciclos B2B y B2C se miden con criterios diferentes.
- Skills / AI OS mantiene procedimientos reutilizables, no la verdad del negocio.
- Capacita Edge implementa landings, tracking y SEO tecnico.
- Capacita Zoho Deluge Core implementa campos, API names y codigo CRM/Deluge.
- WhatsApp + n8n + Zoho implementa workflows, webhooks y mensajeria.
- No subir PII, secretos, `.env`, tokens, binarios, exports CRM ni metricas sensibles sin anonimizar.
- No modificar plataformas o produccion sin autorizacion humana explicita.
- No tratar goals de clic como leads ni submits confirmados.
- No usar SENCE, franquicia tributaria, gratuidad ni promesas garantizadas en B2C.
- No subir assets creativos pesados a GitHub; registrar solo documentacion, checklist, naming, indice y ruta externa.
- Para Meta Ads V3, no seleccionar cuenta por Business Portfolio: verificar primero inventario real de campañas y `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md`.
