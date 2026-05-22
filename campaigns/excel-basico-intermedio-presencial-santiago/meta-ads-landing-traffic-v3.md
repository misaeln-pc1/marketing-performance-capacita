# Meta Ads Landing Traffic v3 - Excel Presencial Santiago

## Estado

Decision operativa documentada. No representa una campana creada o modificada directamente en Meta Ads.

## Decision

Crear una campana nueva V3:

`META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`

La V3 no debe mezclarse con la campana anterior de Lead Ads/formulario instantaneo.

## Motivo

- Separar V3 de campanas anteriores basadas en Lead Ads/formulario instantaneo.
- Evitar conflicto de optimizacion entre conjuntos de anuncios con destinos distintos.
- Evitar repetir la generacion de leads sucios o de baja respuesta.
- Probar la landing como filtro comercial antes de WhatsApp o formulario.

## Contexto comercial

Curso Excel presencial pagado en Santiago Centro.

Landing:

`https://capacita.cl/curso-de-excel-presencial-en-santiago`

La campana anterior produjo volumen, pero baja respuesta comercial. La V3 prioriza intencion sobre volumen: la landing debe exponer precio, fechas, modalidad presencial, ubicacion y alternativas de pago antes del contacto comercial.

## Configuracion Meta Ads V3

| Nivel | Configuracion |
|---|---|
| Objetivo de campana | Trafico |
| Tipo | Campana manual de trafico |
| Campana | `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3` |
| Conjunto de anuncios | `AS01_LANDING_PAGADO_EXCEL_PRESENCIAL` |
| Ubicacion de conversion | Sitio web |
| Objetivo de rendimiento | Maximizar visitas a la pagina de destino |
| Destino | `https://capacita.cl/curso-de-excel-presencial-en-santiago?utm_source=meta&utm_medium=paid_social&utm_campaign=excel_presencial_v3&utm_content=ad01_reel_9x16_landing_pagado` |
| Enlace visible | `capacita.cl` |
| CTA | Cotizar |
| Presupuesto test | CLP $5.000 a $8.000 diarios durante 24-48 horas |

El test debe medir calidad, no solo volumen.

## Anuncio inicial V3

Anuncio:

`AD01_REEL_9X16_LANDING_PAGADO`

Formato inicial:

- Solo video 9:16.
- Resolucion: 1080x1920.
- No usar inicialmente 1:1 ni 16:9 aunque esten listos.

Motivo:

- Aislar variable creativa.
- Evitar mezcla de placements, recortes y errores.
- Mantener el aprendizaje inicial concentrado en video movil vertical.

Backlog:

- `AD02_FEED_1X1_LANDING_PAGADO`: posible prueba posterior para feed 1:1.
- `AD03_HORIZONTAL_16X9_LANDING_PAGADO`: posible prueba posterior si se testea video horizontal o in-stream.

## Copy inicial

Texto principal:

> Curso de Excel presencial pagado en Santiago Centro. Aprende con profesor en vivo, practica guiada y computador individual. Revisa fechas, valor y alternativas de pago antes de cotizar.

Titulo:

> Excel presencial en Santiago

Descripcion:

> Curso pagado - Cupos limitados

## Elementos desactivados en V3

No usar en esta version inicial:

- Formulario instantaneo.
- WhatsApp como complemento del navegador.
- Llamada telefonica.
- Experiencia instantanea.
- Evento de Facebook como destino.
- Traduccion Advantage+.
- Mejoras automaticas de texto.
- Retoques automaticos de video.
- Sticker/CTA generado por IA.
- Imagen de marca automatica.
- Enlaces al sitio automaticos.
- "Lo mas destacado del sitio web".
- Imagen solo para columna derecha de Facebook.

Si aparece una advertencia de columna derecha y no bloquea la publicacion, ignorarla en esta prueba. El foco operativo es video movil para Reels, Stories y Feed, no columna derecha.

## Landing como filtro

La landing HTML en Cloudflare Pages es el filtro principal de V3.

Debe mostrar antes del contacto:

- Precio.
- Fechas.
- Modalidad presencial.
- Santiago Centro.
- Alternativas de pago.

WhatsApp y formulario deben quedar dentro de la landing, no como destino directo del anuncio.

El objetivo real de negocio sigue siendo lead o inscripcion. La optimizacion inicial de Meta, sin embargo, queda orientada a visita a landing para filtrar intencion antes del contacto.

## Hipotesis V3

V1/V2 con formulario instantaneo produjo volumen, pero baja respuesta.

V3 prioriza friccion comercial:

- Decir explicitamente "pagado".
- Usar landing con precio y fechas.
- Usar CTA "Cotizar".
- Separar trafico a landing de capturas instantaneas.

Hipotesis:

Menos volumen, mayor intencion.

La V3 no debe evaluarse por clics solamente. Debe evaluarse por calidad comercial posterior: consultas reales, clics internos relevantes, formularios enviados, conversaciones respondidas e inscritos.

## Restricciones de repositorio

- No subir videos, imagenes, exports, masters, Canva, PSD ni fuentes.
- No subir datos personales de leads o clientes.
- No subir secretos, tokens, credenciales ni `.env`.
- No documentar resultados no medidos.
- No modificar landing de produccion desde este repositorio.
- No modificar campanas reales de Meta Ads desde este repositorio.
