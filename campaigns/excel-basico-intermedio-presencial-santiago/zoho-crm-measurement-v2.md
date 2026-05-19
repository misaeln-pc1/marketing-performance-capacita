# Zoho CRM Measurement v2 — Meta Excel Presencial

## Objetivo

Definir la medición mínima para comparar calidad comercial entre Lead Form filtrado y WhatsApp, sin convertir el CRM en una copia de Meta Ads.

## Principio

Meta Ads debe seguir siendo la fuente de métricas publicitarias agregadas. Zoho CRM debe registrar atribución básica, calidad del lead y resultado comercial.

No conviene intentar cargar automáticamente todas las métricas de Meta en cada lead. CPC, CTR, impresiones y gasto son métricas de campaña/anuncio, no propiedades naturales de cada lead individual.

## Campos recomendados en Leads

| Campo | Tipo sugerido | Uso |
|---|---|---|
| `Marketing_Campaign_Key` | Texto o picklist | Identificador interno de campaña |
| `Marketing_Test_Variant` | Picklist | `FORM` / `WHATSAPP` |
| `Meta_Campaign_Name` | Texto | Nombre de campaña Meta |
| `Meta_Adset_Name` | Texto | Nombre del conjunto |
| `Meta_Ad_Name` | Texto | Nombre del anuncio |
| `Meta_Form_Name` | Texto | Nombre del formulario si aplica |
| `Dolor_Inferido` | Picklist | Reportes / Planillas / Guía / CV |
| `Buyer_Persona_Inferida` | Picklist | Desbordado Operativo / Reinserción Laboral / Acompañamiento |
| `Respuesta_Formulario` | Texto o picklist | Respuesta principal del formulario |
| `Intencion_Comercial` | Picklist | Alta / Media / Baja / No calza |
| `Lead_Contactado` | Checkbox | Lead contactado por ventas |
| `Lead_Respondio` | Checkbox | Lead respondió efectivamente |
| `Canal_Primer_Contacto` | Picklist | WhatsApp / Llamada / Email |
| `Fecha_Primer_Contacto` | DateTime | Control de velocidad comercial |
| `Fecha_Primera_Respuesta` | DateTime | Control de respuesta |
| `Resultado_Comercial` | Picklist | Matriculado / Cotizando / No responde / No calza / Perdido |

## Campos mínimos si se quiere partir liviano

Si no se quieren crear demasiados campos, partir con estos:

- `Marketing_Test_Variant`.
- `Meta_Ad_Name`.
- `Dolor_Inferido`.
- `Buyer_Persona_Inferida`.
- `Intencion_Comercial`.
- `Lead_Respondio`.
- `Resultado_Comercial`.

## Atribución por anuncio

La atribución debe basarse en el nombre del anuncio si Zoho Social lo entrega.

Nombres canónicos:

| Anuncio | Dolor inferido | Buyer persona inferida |
|---|---|---|
| `AD01_DESBORDADO_REPORTE` | Reportes | Desbordado Operativo |
| `AD02_DESBORDADO_PLANILLAS` | Planillas | Desbordado Operativo |
| `AD03_PRESENCIAL_GUIADO` | Guía presencial | Acompañamiento |
| `AD04_REINSERCION_CV` | CV / nuevo trabajo | Reinserción Laboral |

Regla sugerida:

| `Meta_Ad_Name` contiene | `Dolor_Inferido` | `Buyer_Persona_Inferida` |
|---|---|---|
| `REPORTE` | Reportes | Desbordado Operativo |
| `PLANILLAS` | Planillas | Desbordado Operativo |
| `GUIA` | Guía presencial | Acompañamiento |
| `CV` o `REINSERCION` | CV / nuevo trabajo | Reinserción Laboral |

Si Zoho Social no entrega nombre de anuncio, usar formularios separados por dolor o nombres de formulario diferenciados.

## Atribución por WhatsApp

Para WhatsApp, si no hay integración automática, el mensaje prellenado debe contener el dolor principal para facilitar clasificación manual o futura automatización.

Ejemplo:

> Hola, quiero información del curso Excel presencial para mejorar reportes en mi trabajo.

## Automatización mínima recomendada

Cuando ingrese un lead desde Zoho Social:

1. Identificar campaña o formulario.
2. Identificar anuncio si el dato está disponible.
3. Asignar `Dolor_Inferido`.
4. Asignar `Buyer_Persona_Inferida`.
5. Asignar `Marketing_Test_Variant`.
6. Definir `Intencion_Comercial` según respuesta del formulario.
7. Marcar seguimiento comercial pendiente.

## Reglas de intención

| Señal | Intención sugerida |
|---|---|
| Inscribirme en curso presencial | Alta |
| Mejorar trabajo actual | Media/Alta |
| Reportes y planillas | Media/Alta |
| CV o nuevo trabajo | Media |
| Solo cotizando valores | Baja |
| Prefiere online o no calza presencial | No calza o derivar |

## Reporte manual mínimo semanal

Comparar por variante:

| Variante | Leads | Respondieron | Matriculados | Costo total | Costo por lead | Costo por respondido | Costo por matrícula |
|---|---:|---:|---:|---:|---:|---:|---:|
| FORM | — | — | — | — | — | — | — |
| WHATSAPP | — | — | — | — | — | — | — |

## Pendiente técnico

Validar en Zoho Social qué campos llegan desde Meta Lead Ads:

- campaña;
- conjunto de anuncios;
- anuncio;
- formulario;
- plataforma;
- respuesta de pregunta;
- fecha/hora.

No crear automatizaciones complejas hasta confirmar qué datos llegan efectivamente.
