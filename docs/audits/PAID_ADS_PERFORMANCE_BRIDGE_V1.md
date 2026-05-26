# Paid Ads Performance Bridge V1

## Objetivo

Preparar una lectura transversal de performance para conectar Meta Ads con landing/formulario, Zoho CRM, contacto comercial y matricula, sin usar APIs ni datos personales.

## Matriz campaña -> formulario/landing -> CRM -> contacto -> matrícula

| Etapa | Estado documentado | Evidencia | Brecha |
| --- | --- | --- | --- |
| Campaña | V3: `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`; V1: `META_LEADS_EXCEL_PRESENCIAL_SANTIAGO_B2C_V1` | `meta-ads-landing-traffic-v3.md`, `lead-quality-learnings-v1.md` | No hay resultados agregados por campaña. |
| Anuncio | V3: `AD01_REEL_9X16_LANDING_PAGADO`; V1: cuatro anuncios por dolor | `meta-ads-v3-measurement-checklist.md`, `lead-quality-learnings-v1.md` | No hay gasto, entrega ni clicks por anuncio. |
| Landing/formulario | V3: landing; V1: formulario instantaneo | `meta-ads-landing-traffic-v3.md`, `lead-form-v1.md` | No hay medicion de clics internos ni formularios enviados desde landing. |
| CRM | Zoho CRM tiene campos UTM/click IDs identificados | `references/zoho-crm/MAPEO_LEADS_META_ADS.md` | No hay exportacion agregada que confirme poblacion real de campos. |
| Contacto | Debe medir contactados/respondidos | `lead-quality-learnings-v1.md`, `meta-ads-quality-test-v2.md` | No hay conteo agregado de contactados/respondidos. |
| Matricula | Resultado comercial esperado | `campaign-brief.md`, `meta-ads-v3-measurement-checklist.md` | No hay matriculas agregadas por campaña. |

## Brechas de trazabilidad

- Falta evidencia de que `utm_campaign`, `utm_content` y `f_ads_fbclid` se capturan en Zoho CRM.
- Falta exportacion agregada por estado comercial: lead bruto, contactado, respondido, calificado, matricula.
- Falta dato de clicks internos en WhatsApp/formulario dentro de la landing V3.
- Falta criterio unico para lead calificado y CPQL.
- Falta asociar cada matricula a campaña/conjunto/anuncio sin datos personales.

## Métricas normalizadas

| Metrica | Definicion sugerida | Estado |
| --- | --- | --- |
| Gasto | Inversion Meta Ads por campaña/conjunto/anuncio | Faltante |
| Impresiones | Entregas registradas por Meta | Faltante |
| Clicks | Clicks en enlace o visita a landing, segun objetivo | Faltante |
| CTR | Clicks / impresiones | Faltante |
| CPC | Gasto / clicks | Faltante |
| Leads | Formularios o contactos creados | Faltante |
| CPL | Gasto / leads | Faltante |
| Lead calificado | Lead que cumple criterio comercial definido | Faltante |
| CPQL | Gasto / leads calificados | Faltante |
| Matriculas | Inscripciones confirmadas | Faltante |
| CPA | Gasto / matriculas | Faltante |
| Tasa de contacto | Contactados / leads | Faltante |
| Tasa de matricula | Matriculas / leads o matriculas / contactados | Faltante |

## Campos mínimos para próximo CSV/exportación

### Meta Ads agregado

- `date_start`
- `date_stop`
- `campaign_name`
- `adset_name`
- `ad_name`
- `objective`
- `placement` si esta disponible
- `spend`
- `impressions`
- `reach`
- `frequency`
- `inline_link_clicks` o clicks equivalente
- `landing_page_views` si aplica
- `ctr`
- `cpc`
- `leads`
- `cpl`

### Landing/formulario agregado

- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_content`
- `landing_url`
- `landing_page`
- `whatsapp_clicks`
- `form_submissions`
- `capture_date`

### Zoho CRM agregado y sin PII

- `lead_source`
- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_content`
- `f_ads_fbclid_present`
- `landing_url_present`
- `lead_status`
- `contacted_count`
- `responded_count`
- `qualified_count`
- `enrolled_count`
- `lost_reason_group`

## Recomendación para siguiente ciclo

Preparar una exportacion agregada y anonima que permita unir Meta -> landing/formulario -> Zoho CRM por `utm_campaign` y `utm_content`. No tomar decisiones por CPL mientras falten CPQL, CPA, tasa de contacto y tasa de matricula.

## Límites

- No usar Meta API.
- No tocar Business Manager.
- No descargar leads con PII.
- No modificar Zoho CRM.
- No inventar metricas faltantes.
