# Meta Ads Quality Test v2 — Excel Presencial Santiago

## Objetivo

Comparar calidad comercial entre dos rutas de conversión para la campaña Excel Básico–Intermedio Presencial Santiago Centro:

1. Lead Form filtrado.
2. Click a WhatsApp.

El objetivo no es maximizar leads brutos, sino identificar qué ruta genera más leads respondidos y matrículas.

## Estructura recomendada

Campaña:

`META_EXCEL_PRESENCIAL_B2C_CALIDAD_V2`

Conjuntos:

| Conjunto | Objetivo | Destino |
|---|---|---|
| `AS01_FORM_CALIDAD_SANTIAGO` | Captura estructurada | Formulario instantáneo |
| `AS02_WHATSAPP_CALIDAD_SANTIAGO` | Conversación con intención | WhatsApp |

Recomendación: usar presupuesto por conjunto para que Meta no concentre automáticamente el gasto en el resultado más barato sin comparar calidad.

## Anuncios por dolor

Mantener la lógica de cuatro dolores:

- `AD01_DESBORDADO_REPORTE`.
- `AD02_DESBORDADO_PLANILLAS`.
- `AD03_PRESENCIAL_GUIADO`.
- `AD04_REINSERCION_CV`.

Si el presupuesto diario es bajo, reducir la prueba inicial a dos dolores:

- `AD01_DESBORDADO_REPORTE`.
- `AD04_REINSERCION_CV`.

## Filtro visual obligatorio

Agregar en las creatividades una señal visible de pago y modalidad.

Frase base recomendada:

> Curso Excel presencial  
> Pagado · sin matrícula · Santiago Centro

Variantes para probar:

1. Curso Excel presencial / Curso pagado · sin matrícula · Santiago Centro.
2. Excel presencial / Pago único del curso · sin matrícula.
3. Aprende Excel con profesor / Curso pagado · Santiago Centro.
4. Excel para el trabajo / Curso presencial pagado · sin matrícula.
5. Fortalece tu CV con Excel / Curso presencial pagado.
6. Excel básico–intermedio / Curso pagado · práctica guiada · sin matrícula.
7. Aprende Excel paso a paso / Con profesor · presencial.
8. Excel presencial en Santiago Centro / Pago único · sin matrícula.

No usar lenguaje que sugiera gratuidad. La frase "sin matrícula" no debe usarse aislada: siempre debe ir acompañada de "curso pagado", "pagado" o una señal equivalente de pago.

## Lead Form v2

Usar una sola pregunta fuerte, preferentemente selección única:

> ¿Qué estás buscando principalmente?

Opciones:

- Inscribirme en un curso presencial de Excel.
- Mejorar Excel para mi trabajo actual.
- Aprender reportes y planillas.
- Mejorar mi CV o buscar nuevo trabajo.
- Solo estoy cotizando valores.

Regla:

- Si la respuesta es inscripción, alta prioridad.
- Si la respuesta es trabajo/reportes/CV, prioridad media o alta según contacto.
- Si la respuesta es solo cotizando, baja prioridad.

## WhatsApp v2

Usar mensajes prellenados por dolor:

| Anuncio | Mensaje sugerido |
|---|---|
| `AD01_DESBORDADO_REPORTE` | Hola, quiero información del curso Excel presencial para mejorar reportes en mi trabajo. |
| `AD02_DESBORDADO_PLANILLAS` | Hola, quiero información del curso Excel presencial para ordenar planillas. |
| `AD03_PRESENCIAL_GUIADO` | Hola, quiero información del curso Excel presencial con profesor. |
| `AD04_REINSERCION_CV` | Hola, quiero información del curso Excel presencial para fortalecer mi CV. |

Primera respuesta sugerida:

> Perfecto. Para orientarte rápido: ¿buscas inscribirte en la próxima fecha o solo estás cotizando valores?

## Configuraciones a revisar

### Anuncios multianunciante

Para esta prueba, desactivar si la plataforma lo permite.

Motivo: se busca medir creatividad, dolor y canal con el mayor control posible. Los formatos multianunciante pueden mostrar el anuncio junto a otros anuncios y dificultar la lectura limpia del experimento.

### Advantage+ / automatismos creativos

Evitar que Meta altere demasiado textos o creatividades en esta etapa. La prioridad es aprender qué mensaje filtra mejor, no maximizar variaciones automáticas.

### Ubicaciones

Revisar placements y evitar ubicaciones de baja calidad cuando sea posible. El objetivo no es solo volumen, sino contactabilidad.

## Métricas de decisión

| Métrica | Fuente principal |
|---|---|
| Impresiones | Meta Ads |
| Clics | Meta Ads |
| CTR | Meta Ads |
| CPC | Meta Ads |
| Leads brutos | Meta Ads / Zoho CRM |
| CPL bruto | Meta Ads |
| Leads contactados | Zoho CRM |
| Leads respondidos | Zoho CRM |
| Matrículas | Zoho CRM |
| Costo por lead respondido | Meta Ads + Zoho CRM |
| Costo por matrícula | Meta Ads + Zoho CRM |

## Criterios de decisión

Mantener una ruta si:

- genera leads respondidos a costo razonable;
- permite identificar dolor/persona;
- produce conversaciones comerciales reales;
- no depende solo de CPL bajo.

Pausar o corregir si:

- genera muchos leads sin respuesta;
- atrae interesados que creen que el curso es gratuito;
- no permite atribuir anuncio/dolor;
- baja el CPL pero no mejora matrículas.

## Pendientes antes de publicar

- Activar medio de pago en Meta.
- Confirmar precio, fecha y duración vigentes.
- Confirmar política de privacidad usada en formularios.
- Confirmar cómo Zoho Social traspasa campaña, conjunto, anuncio y formulario a Zoho CRM.
- Confirmar si WhatsApp quedará manual o integrado.
