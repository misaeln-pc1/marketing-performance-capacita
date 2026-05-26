# Meta Ads Campaign Audit V1

## 1. Campaña Revisada

| Campo | Registro |
| --- | --- |
| Nombre o identificador disponible | `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3` |
| Campaña base referenciada | `META_LEADS_EXCEL_PRESENCIAL_SANTIAGO_B2C_V1` |
| Periodo | Mayo 2026 como contexto comercial; test V3 documentado para 24-48 horas, sin resultados cargados. |
| Curso/oferta | Excel Basico-Intermedio Presencial en Santiago Centro. |
| Objetivo de campaña | V3: Trafico a landing. V1: Lead Ads/formulario instantaneo. |
| Fuente de datos | Documentos del repo: `PROJECT_CONTEXT.md`, `TASK_STATUS.md`, `campaigns/`, `references/zoho-crm/MAPEO_LEADS_META_ADS.md`. |
| Limitaciones | No hay CSV de resultados, exportacion Meta Ads, datos Zoho agregados ni metricas reales versionadas. No se consulto Meta Business Manager ni API. |

## 2. Estructura

| Nivel | Estado documentado |
| --- | --- |
| Campaña | V3: `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`. V1 observada: `META_LEADS_EXCEL_PRESENCIAL_SANTIAGO_B2C_V1`. |
| Conjunto de anuncios | V3: `AS01_LANDING_PAGADO_EXCEL_PRESENCIAL`. V1 observada: `AS01_B2C_SANTIAGO_PRESENCIAL`. |
| Anuncios | V3 inicial: `AD01_REEL_9X16_LANDING_PAGADO`. V1 observados: `AD01_DESBORDADO_REPORTE`, `AD02_DESBORDADO_PLANILLAS`, `AD03_PRESENCIAL_GUIADO`, `AD04_REINSERCION_CV`. |
| Placement | V3 prioriza video movil 9:16 para Reels, Stories y Feed. No usar inicialmente 1:1 ni 16:9. |
| Audiencia | Santiago y comunas con posibilidad razonable de asistir presencialmente. Personas administrativas, profesionales y en busqueda activa de empleo. |
| Formulario o landing | V1 uso formulario instantaneo. V3 usa landing: `https://capacita.cl/curso-de-excel-presencial-en-santiago`. |
| Creativos disponibles | Copys documentados para desbordado operativo, reinsercion laboral, presencial guiado e infraestructura. No hay assets binarios versionados. |

## 3. Métricas

No hay metricas reales versionadas para gasto, entrega, leads, contacto, calificacion o matriculas. La siguiente tabla registra disponibilidad, no resultados.

| Metrica | Valor disponible | Fuente |
| --- | --- | --- |
| Gasto | No documentado | Pendiente exportacion agregada |
| Impresiones | No documentado | Pendiente exportacion agregada |
| Alcance | No documentado | Pendiente exportacion agregada |
| Frecuencia | No documentado | Pendiente exportacion agregada |
| Clicks | No documentado | Pendiente exportacion agregada |
| CTR | No documentado | Pendiente exportacion agregada |
| CPC | No documentado | Pendiente exportacion agregada |
| Leads | No documentado | Pendiente exportacion agregada |
| CPL | No documentado | Pendiente exportacion agregada |
| Leads contactados | No documentado | Pendiente Zoho CRM agregado |
| Leads calificados | No documentado | Pendiente Zoho CRM agregado |
| CPQL | No documentado | Requiere gasto y leads calificados |
| Matriculas | No documentado | Pendiente Zoho CRM agregado |
| CPA | No documentado | Requiere gasto y matriculas |
| Tasa de contacto | No documentado | Requiere leads y contactados |
| Tasa de matricula | No documentado | Requiere leads o contactados y matriculas |

## 4. Diagnóstico

### Calidad de lead

La documentacion indica que V1/V2 generaron volumen, pero baja respuesta comercial. El problema principal identificado no es la atraccion inicial, sino la baja intencion generada por formularios instantaneos con poca friccion.

### Fricción del formulario

El formulario V1 categoriza motivacion y nivel, pero no filtra con suficiente fuerza intencion de compra. V2 recomienda filtro visual explicito: curso presencial, pagado, Santiago Centro y sin lenguaje que sugiera gratuidad.

### Coherencia anuncio -> formulario/landing

V3 mejora la coherencia al enviar a una landing con precio, fechas, modalidad presencial, ubicacion y alternativas de pago antes del contacto. La promesa debe seguir evitando nivel avanzado, empleo garantizado o mensajes de gratuidad.

### Tracking/UTMs

V3 documenta una URL con `utm_source=meta`, `utm_medium=paid_social`, `utm_campaign=excel_presencial_v3` y `utm_content=ad01_reel_9x16_landing_pagado`. Falta confirmar captura completa de UTMs desde landing hacia Zoho CRM.

### Conexión con Zoho CRM

Existe referencia de campos Zoho relevantes: `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`, `f_ads_fbclid`, `landing_url`, `landing_page`, `capture_time` y otros. El documento no demuestra que esos campos esten poblados para la campana reciente.

### Riesgos de atribución

- Evaluar por CPL bruto puede favorecer volumen de baja calidad.
- V1/V2 y V3 tienen objetivos y destinos distintos; no deben compararse solo por costo de resultado.
- Sin UTMs en CRM no se puede cerrar campaña -> contacto -> matricula.
- Sin datos agregados de Zoho no se puede calcular CPQL, CPA ni tasa de matricula.

### Datos faltantes

- Exportacion agregada Meta Ads por campaña/conjunto/anuncio.
- Leads agregados por fuente/campaña en Zoho CRM.
- Estados de contacto, lead calificado y matricula.
- Clics internos en WhatsApp/formulario dentro de landing.
- Confirmacion de precio, fecha y cupos vigentes del curso.

## 5. Recomendaciones

### Acciones inmediatas

- Mantener separadas V1/V2 Lead Ads y V3 Trafico a landing.
- Evaluar V3 por calidad posterior, no solo por clicks o CPL.
- Confirmar que la landing muestra precio, fechas, modalidad presencial, Santiago Centro y alternativas de pago.
- Confirmar que UTMs viajan hasta Zoho CRM antes de decidir escalamiento.

### Datos que faltan

- CSV/exportacion agregada Meta Ads sin PII.
- Exportacion agregada Zoho CRM sin PII con estados de contacto, calificacion y matricula.
- Definicion operacional de lead calificado.
- Registro de clics internos en WhatsApp/formulario.

### Hipótesis a validar

- La landing reduce volumen pero mejora intencion.
- El filtro de curso pagado/presencial reduce leads que no responden.
- `AD01_REEL_9X16_LANDING_PAGADO` puede atraer trafico movil suficiente sin activar 1:1 o 16:9.
- La calidad mejora si la fuente CRM conserva campaña, anuncio y UTM.

### Qué NO cambiar todavía

- No activar automaticamente 1:1, 16:9 o mas anuncios antes del primer aprendizaje V3.
- No volver a optimizar solo por CPL bruto.
- No mezclar V3 con la campana anterior de Lead Ads.
- No modificar campañas reales, landing productiva ni Zoho CRM desde este repo.
