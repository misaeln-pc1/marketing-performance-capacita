# Benchmark SENCE de ejecución — Inteligencia Artificial aplicada al trabajo

Fecha de corte: 2026-08-23  
Estado: `WORKING_BASELINE / RESEARCH_V01`

## Objetivo

Añadir al benchmark comercial una señal de **demanda revelada**: cursos de Inteligencia Artificial registrados en el ecosistema SENCE, organismo ejecutor, modalidad, duración, precio observado y cantidad de veces impartido.

## Regla de evidencia

- SENCE/Elige Mejor es la fuente institucional para búsqueda de cursos por nombre/código y OTEC.
- SENCE declara que el catálogo permite filtrar por costo, duración, evaluaciones y cantidad de veces impartido.
- Para el detalle indexable de curso/código/veces impartido/precio se usa el directorio público `cursosdelsence.cl`, que referencia cursos con código SENCE y enlaza a Elige Mejor.
- La modalidad se debe confirmar desde el descriptor/metodología del curso o desde la fuente institucional del proveedor cuando esté disponible; no basta con asumirla por ciudad, OTEC o precio.
- No se interpretan las veces impartido como ventas B2C ni como matrículas individuales.
- No se infieren ingresos, alumnos totales ni margen.

## Corrección metodológica obligatoria — modalidad

Precio, horas y cantidad de ejecuciones **no deben compararse sin modalidad**. Un curso e-learning asincrónico, e-learning sincrónico, mixto y presencial tienen estructuras de costo y experiencia distintas.

Cuando una etiqueta agregada como `Mixta` entra en conflicto con la metodología descrita, prevalece para el análisis comercial la descripción concreta de cómo se ejecuta el curso y se conserva la etiqueta agregada sólo como referencia del registro.

## Hallazgos iniciales relevantes

| Curso | Organismo | Código SENCE | Modalidad confirmada / observada | Horas | Precio observado | Veces impartido | Afinidad con IA laboral |
|---|---|---|---|---:|---:|---:|---|
| Competencias Digitales de Inteligencia Artificial | Instituto Madicap | 1238082128 | **Presencial** en metodología; directorio agrega `Mixta` | 9 | $1.659.726 | 42 | Alta: asistentes administrativos, automatización, análisis de datos |
| Descubriendo la Inteligencia Artificial | Universidad Adolfo Ibáñez | 1238064367 | **Mixta** según registro público; detalle operativo pendiente | 96 | $572.000 | 34 | Media: innovación/TI, vida cotidiana y organizaciones |
| Inteligencia Artificial en los Negocios | Pontificia Universidad Católica de Chile | 1238054007 / oferta vigente relacionada 1238085428 | **Online mixta**: e-learning asincrónico + clases en vivo | 75 | $475.000 en registro histórico / oferta vigente distinta | 31 en registro histórico | Alta B2B: toma de decisiones y estrategia |
| Herramientas Aplicadas de IA para el Trabajo | eClass | 1238082385 | **Online / e-learning predominantemente asincrónico**, con plataforma, módulos, foros y tutoría; oferta comercial actual online | 60 SENCE | $564.481 SENCE; oferta retail online actual distinta | 23 | Muy alta: productividad, Copilot, Gemini, Google Workspace, agentes |
| Optimización de la Productividad Empresarial con IA y ChatGPT | Talent Solutions Capacitación | 1238081262 | **E-learning asincrónico** | 115 | $1.380.000 | 21 | Muy alta: productividad, automatización y gestión empresarial |
| Inteligencia Artificial Aplicada en el Ámbito Laboral | World Trade Center Santiago | 1238060238 | **E-learning sincrónico** | 16 | $130.000 | 14 | Muy alta por contenido; **no es competidor presencial directo** |
| ChatGPT para Mejorar la Productividad Laboral | Universidad Gabriela Mistral | 1238085773 | Modalidad exacta **pendiente de confirmar** antes de usar precio como comparable | 100 | $1.200.000 | 9 | Muy alta: tareas administrativas y productivas |
| Introducción a la Inteligencia Artificial | Capacitación Funcional | 1238083941 | **E-learning / plataforma Moodle, autoavance** | 100 | $550.000 | 6 | Media-alta: optimización de procesos y tareas laborales |
| Técnicas en Inteligencia Artificial | BP Capacitación | 1238071678 | Modalidad exacta **pendiente de confirmar** | 16 | $241.417 | 5 | Media: foco más técnico |
| Optimización de la Productividad Empresarial con Inteligencia Artificial | Consoportec OTEC | 1238089635 | **E-learning asincrónico** | 40 | $480.000 | 5 | Muy alta: productividad y automatización |
| Uso de IA para Maximizar la Eficiencia en el Trabajo | VIS Training OTEC | 1238089858 | Registro agregado `Mixta`; metodología observada basada en videos, ejercicios y plataforma; **no clasificar como presencial sin mayor confirmación** | 9 | $2.300.000 | 4 | Muy alta: eficiencia laboral |
| Inteligencia Artificial en el Ámbito Laboral | Centro de Capacitación y Producción Empresarial | 1238084818 | Modalidad exacta **pendiente de confirmar** | 120 | $9.445.068 | 4 | Muy alta: gestión administrativa/documental |
| Uso de Herramientas IA Generativa y ChatGPT | Universidad del Desarrollo | 1238056492 | **Presencial** | 8 | $562.667 | 3 | Muy alta: productividad, ChatGPT |
| Herramientas de IA para la Productividad Profesional | Universidad de Chile | 1238082191 | **Presencial** | 16 | $174.360 | 3 | Muy alta y comparable: 16 h, productividad profesional |
| IA, uso de herramientas para habilidades del siglo XXI | Actualeduc | 1238072976 | Modalidad exacta **pendiente de confirmar** | 16 | $132.168 | 2 | Baja para B2C laboral: foco educación |
| Herramientas de Inteligencia Artificial | Sociedad de Capacitación Desarrollo Nacional | 1238077119 | Modalidad exacta **pendiente de confirmar** | 100 | $2.300.000 | 2 | Media: desarrollo organizacional |
| Introducción a la Inteligencia Artificial | Educademia | 1238090051 | Modalidad exacta **pendiente de confirmar** | 60 | $360.000 | 1 | Media: fundamentos y aplicaciones |
| Inteligencia Artificial | BIT Capacitaciones | 1238090180 | Modalidad exacta **pendiente de confirmar** | 200 | $368.000 | 1 | Alta: administrativos, ventas, logística y apoyo comercial |
| IA generativa para gestión del tiempo y productividad laboral | Tecnipro | 1238091977 | Modalidad exacta **pendiente de confirmar** | 45 | $250.000 | 1 | Muy alta: RRHH, ventas, marketing, finanzas, operaciones |
| IA para productividad y bienestar laboral | Lifebox | 1238091900 | Modalidad exacta **pendiente de confirmar** | 49 | $396.136 | 1 | Muy alta: perfiles administrativos/comerciales |

## Comparables presenciales confirmados

Para decisiones de precio/duración de Capacita, este subconjunto tiene mayor peso que la tabla general:

| Curso | Organismo | Modalidad | Horas | Precio observado | Veces impartido | Lectura |
|---|---|---|---:|---:|---:|---|
| Competencias Digitales de Inteligencia Artificial | Instituto Madicap | Presencial | 9 | $1.659.726 | 42 | Mucha ejecución, pero público/precontrato y precio atípico; no usar como ancla B2C |
| Uso de Herramientas IA Generativa y ChatGPT | UDD | Presencial | 8 | $562.667 | 3 | Comparable por modalidad; más corto y mucho más caro |
| Herramientas de IA para la Productividad Profesional | Universidad de Chile | Presencial | 16 | $174.360 | 3 | **Comparable directo fuerte por modalidad, horas y precio** |
| Capacita — baseline | Capacita | Presencial Santiago | 16 | $178.000 | N/A nuevo curso | Prácticamente mismo precio/hora que UChile; propuesta B2C y cuatro plataformas |

## Comparables online/sincrónicos confirmados

| Curso | Organismo | Modalidad | Horas | Precio observado | Veces impartido | Lectura |
|---|---|---|---:|---:|---:|---|
| Inteligencia Artificial Aplicada en el Ámbito Laboral | World Trade Center Santiago | E-learning sincrónico | 16 | $130.000 | 14 | Fuerte evidencia de demanda laboral, pero **no debe usarse como precio presencial directo** |
| Herramientas Aplicadas de IA para el Trabajo | eClass | Online/e-learning | 60 SENCE | $564.481 SENCE | 23 | Alta ejecución; estructura y duración distintas |
| Optimización de la Productividad Empresarial con IA y ChatGPT | Talent Solutions | E-learning asincrónico | 115 | $1.380.000 | 21 | Corporate y largo; señal de demanda, no ancla de precio presencial |
| Introducción a la Inteligencia Artificial | Capacitación Funcional | E-learning / autoavance | 100 | $550.000 | 6 | No comparable en experiencia ni duración |
| Optimización de la Productividad Empresarial con Inteligencia Artificial | Consoportec | E-learning asincrónico | 40 | $480.000 | 5 | Señal B2B/productividad |

## Lectura corregida

1. Existe evidencia de **ejecución real repetida** en el cluster IA aplicada al trabajo/productividad.
2. `Herramientas Aplicadas de IA para el Trabajo` de eClass alcanza 23 ejecuciones, pero es una oferta online/e-learning de 60 horas; sirve como señal de demanda, no como ancla directa de precio presencial.
3. `Inteligencia Artificial Aplicada en el Ámbito Laboral` de World Trade Center Santiago tiene **16 horas, $130.000 y 14 ejecuciones**, pero es **e-learning sincrónico**, por lo que no debe compararse uno-a-uno con Capacita presencial.
4. Universidad de Chile tiene un curso **presencial de 16 horas / $174.360 / 3 ejecuciones**, prácticamente idéntico al baseline Capacita de 16 h / $178.000 en duración y precio. Este es uno de los comparables más importantes encontrados hasta ahora.
5. UDD confirma **presencial / 8 horas / $562.667 / 3 ejecuciones**.
6. Instituto Madicap registra una metodología presencial de 9 horas y 42 ejecuciones, pero su contexto de precontrato SENCE y precio observado lo convierten en evidencia de ejecución, no en una referencia B2C directa.
7. Las muchas ejecuciones de cursos largos, online o corporate no deben usarse directamente para fijar precio presencial B2C, pero sí confirman demanda empresarial.

## Implicación para Capacita

La comparación futura debe separar:

- `DIRECTO_B2C_PRESENCIAL`: modalidad y propuesta cercanas a Capacita.
- `DIRECTO_PRESENCIAL_SENCE`: presencial y contenido comparable, aunque sea corporate.
- `DIRECTO_IA_LABORAL_ONLINE`: misma necesidad pero modalidad distinta.
- `B2B_CORPORATE`: señal de demanda empresarial, no precio comparable.
- `TECNICO`: IA más técnica/programación/ML.
- `SUSTITUTO_ONLINE`: e-learning/sincrónico/gratuito.

## Baseline a contrastar

```text
CAPACITA_HOURS=16
CAPACITA_PRICE_CLP=178000
CAPACITA_MODALITY=PRESENCIAL_SANTIAGO
CAPACITA_POSITIONING=IA_APLICADA_AL_TRABAJO
CAPACITA_PROGRAMMING_REQUIRED=NO
```

## Siguiente paso

Hacer un barrido más amplio de `inteligencia artificial`, `IA generativa`, `ChatGPT`, `productividad`, `ámbito laboral`, `trabajo`, `Copilot` y `automatización`, deduplicar por código SENCE y clasificar por modalidad y afinidad competitiva antes de tomar decisiones de precio/duración.