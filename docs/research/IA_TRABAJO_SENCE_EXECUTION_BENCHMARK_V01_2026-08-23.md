# Benchmark SENCE de ejecución — Inteligencia Artificial aplicada al trabajo

Fecha de corte: 2026-08-23  
Estado: `WORKING_BASELINE / RESEARCH_V01`

## Objetivo

Añadir al benchmark comercial una señal de **demanda revelada**: cursos de Inteligencia Artificial registrados en el ecosistema SENCE, organismo ejecutor, duración, precio observado y cantidad de veces impartido.

## Regla de evidencia

- SENCE/Elige Mejor es la fuente institucional para búsqueda de cursos por nombre/código y OTEC.
- SENCE declara que el catálogo permite filtrar por costo, duración, evaluaciones y cantidad de veces impartido.
- Para el detalle indexable de curso/código/veces impartido/precio se usa el directorio público `cursosdelsence.cl`, que referencia cursos con código SENCE y enlaza a Elige Mejor.
- No se interpretan las veces impartido como ventas B2C ni como matrículas individuales.
- No se infieren ingresos, alumnos totales ni margen.

## Hallazgos iniciales relevantes

| Curso | Organismo | Código SENCE | Horas | Precio observado | Veces impartido | Afinidad con IA laboral |
|---|---|---|---:|---:|---:|---|
| Competencias Digitales de Inteligencia Artificial | Instituto Madicap | 1238082128 | 9 | $1.659.726 | 42 | Alta: asistentes administrativos, automatización, análisis de datos |
| Descubriendo la Inteligencia Artificial | Universidad Adolfo Ibáñez | 1238064367 | 96 | $572.000 | 34 | Media: innovación/TI, vida cotidiana y organizaciones |
| Inteligencia Artificial en los Negocios | Pontificia Universidad Católica de Chile | 1238054007 | 75 | $475.000 | 31 | Alta B2B: toma de decisiones y estrategia |
| Herramientas Aplicadas de IA para el Trabajo | eClass | 1238082385 | 60 | $564.481 | 23 | Muy alta: productividad, Copilot, Gemini, Google Workspace, agentes |
| Optimización de la Productividad Empresarial con IA y ChatGPT | Talent Solutions Capacitación | 1238081262 | 115 | $1.380.000 | 21 | Muy alta: productividad, automatización y gestión empresarial |
| Inteligencia Artificial Aplicada en el Ámbito Laboral | World Trade Center Santiago | 1238060238 | 16 | $130.000 | 14 | Muy alta y comparable: IA en ámbito laboral |
| ChatGPT para Mejorar la Productividad Laboral | Universidad Gabriela Mistral | 1238085773 | 100 | $1.200.000 | 9 | Muy alta: tareas administrativas y productivas |
| Introducción a la Inteligencia Artificial | Capacitación Funcional | 1238083941 | 100 | $550.000 | 6 | Media-alta: optimización de procesos y tareas laborales |
| Técnicas en Inteligencia Artificial | BP Capacitación | 1238071678 | 16 | $241.417 | 5 | Media: foco más técnico |
| Optimización de la Productividad Empresarial con Inteligencia Artificial | Consoportec OTEC | 1238089635 | 40 | $480.000 | 5 | Muy alta: productividad y automatización |
| Uso de IA para Maximizar la Eficiencia en el Trabajo | VIS Training OTEC | 1238089858 | 9 | $2.300.000 | 4 | Muy alta: eficiencia laboral |
| Inteligencia Artificial en el Ámbito Laboral | Centro de Capacitación y Producción Empresarial | 1238084818 | 120 | $9.445.068 | 4 | Muy alta: gestión administrativa/documental |
| Uso de Herramientas IA Generativa y ChatGPT | Universidad del Desarrollo | 1238056492 | 8 | $562.667 | 3 | Muy alta: presencial, productividad, ChatGPT |
| Herramientas de IA para la Productividad Profesional | Universidad de Chile | 1238082191 | 16 | $174.360 | 3 | Muy alta y comparable: 16 h, productividad profesional |
| IA, uso de herramientas para habilidades del siglo XXI | Actualeduc | 1238072976 | 16 | $132.168 | 2 | Baja para B2C laboral: foco educación |
| Herramientas de Inteligencia Artificial | Sociedad de Capacitación Desarrollo Nacional | 1238077119 | 100 | $2.300.000 | 2 | Media: desarrollo organizacional |
| Introducción a la Inteligencia Artificial | Educademia | 1238090051 | 60 | $360.000 | 1 | Media: fundamentos y aplicaciones |
| Inteligencia Artificial | BIT Capacitaciones | 1238090180 | 200 | $368.000 | 1 | Alta: administrativos, ventas, logística y apoyo comercial |
| IA generativa para gestión del tiempo y productividad laboral | Tecnipro | 1238091977 | 45 | $250.000 | 1 | Muy alta: RRHH, ventas, marketing, finanzas, operaciones |
| IA para productividad y bienestar laboral | Lifebox | 1238091900 | 49 | $396.136 | 1 | Muy alta: perfiles administrativos/comerciales |

## Lectura inicial

1. Existe evidencia de **ejecución real repetida** en el cluster IA aplicada al trabajo/productividad.
2. `Herramientas Aplicadas de IA para el Trabajo` de eClass alcanza 23 ejecuciones y es uno de los referentes directos más fuertes.
3. `Inteligencia Artificial Aplicada en el Ámbito Laboral` de World Trade Center Santiago tiene **16 horas**, $130.000 y 14 ejecuciones; es especialmente comparable con Capacita.
4. Universidad de Chile tiene un curso de **16 horas / $174.360 / 3 ejecuciones**, prácticamente en el mismo rango de duración y precio del baseline Capacita ($178.000), aunque su público/propuesta puede diferir.
5. UDD confirma **8 horas / $562.667 / 3 ejecuciones** en modalidad presencial.
6. Las muchas ejecuciones de cursos largos o corporate no deben usarse directamente para fijar precio B2C, pero sí confirman demanda empresarial.

## Implicación para Capacita

La comparación futura debe separar:

- `DIRECTO_B2C_PRESENCIAL`: modalidad y propuesta cercanas a Capacita.
- `DIRECTO_IA_LABORAL`: misma necesidad, aunque modalidad/duración difieran.
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

Hacer un barrido más amplio de `inteligencia artificial`, `IA generativa`, `ChatGPT`, `productividad`, `ámbito laboral`, `trabajo`, `Copilot` y `automatización`, deduplicar por código SENCE y clasificar por afinidad competitiva antes de tomar decisiones de precio/duración.