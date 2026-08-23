# Corrección benchmark SENCE — modalidad y semántica de precio

Fecha de corte: 2026-08-23
Estado: `WORKING_BASELINE / CORRECTION_V01`

## Regla de lectura

Para comparar cursos SENCE, la modalidad es obligatoria. Si una etiqueta resumen como `Mixta` entra en conflicto con la metodología detallada, prevalece la metodología específica del curso y se documenta la discrepancia.

El `precio observado` en las fichas consultadas está expresado como **precio total por persona/participante para el curso asociado al código SENCE**. No corresponde al precio total de un grupo ni al valor por hora. La franquicia tributaria puede cubrir parte de ese monto según el tramo aplicable; eso no cambia que el valor publicado base sea por participante.

## Modalidad verificada de cursos relevantes

| Curso | Organismo | Código SENCE | Modalidad verificada | Horas | Precio por persona | Veces impartido | Evidencia de modalidad |
|---|---|---|---|---:|---:|---:|---|
| Competencias Digitales de Inteligencia Artificial | Instituto Madicap | 1238082128 | Presencial | 9 | $1.659.726 | 42 | Metodología explícita: `Modalidad: Presencial (sala móvil)`; algunos listados resumen lo etiquetan `Mixta` |
| Descubriendo la Inteligencia Artificial | Universidad Adolfo Ibáñez | 1238064367 | Online mixta: e-learning + instancias sincrónicas | 96 | $572.000 | 34 | Plataforma UAI Online, módulos e-learning y dos clases sincrónicas |
| Inteligencia Artificial en los Negocios | Pontificia Universidad Católica de Chile | 1238054007 | Online mixta: e-learning + sincrónico | 75 | $475.000 | 31 | Seis sesiones e-learning y dos clases sincrónicas |
| Herramientas Aplicadas de IA para el Trabajo | eClass | 1238082385 | E-learning online, principalmente asincrónico | 60 | $564.481 | 23 | Material online, foros asincrónicos, actividades y controles en línea |
| Optimización de la Productividad Empresarial con IA y ChatGPT | Talent Solutions Capacitación | 1238081262 | E-learning asincrónico | 115 | $1.380.000 | 21 | Metodología declara explícitamente modalidad asincrónica en plataforma e-learning |
| Inteligencia Artificial Aplicada en el Ámbito Laboral | World Trade Center Santiago | 1238060238 | E-learning sincrónico | 16 | $130.000 | 14 | Metodología declara sesión e-learning sincrónica/streaming en aula virtual Moodle |
| ChatGPT para Mejorar la Productividad Laboral | Universidad Gabriela Mistral | 1238085773 | E-learning asincrónico | 100 | $1.200.000 | 9 | Metodología declara modalidad asincrónica en plataforma e-learning |
| Introducción a la Inteligencia Artificial | Capacitación Funcional | 1238083941 | E-learning/autoinstruccional en plataforma | 100 | $550.000 | 6 | Desarrollo mediante Moodle, contenidos HTML5 y evaluaciones interactivas en línea |
| Técnicas en Inteligencia Artificial | BP Capacitación | 1238071678 | Mixta según ficha; metodología con actividades presenciales/no remotas descritas | 16 | $241.417 | 5 | La ficha resumen indica `Mixta`; la metodología usa clases expositivas, data show, plenarios y supervisión directa. No reclasificar como presencial puro sin evidencia adicional |
| Optimización de la Productividad Empresarial con Inteligencia Artificial | Consoportec OTEC | 1238089635 | E-learning asincrónico | 40 | $480.000 | 5 | Metodología declara modalidad asincrónica en plataforma e-learning |
| Uso de IA para Maximizar la Eficiencia en el Trabajo | VIS Training OTEC | 1238089858 | Mixta según ficha; componente e-learning/autónomo evidente | 9 | $2.300.000 | 4 | Ficha resumen `Mixta`; metodología describe videos, autoevaluaciones y tareas en plataforma |
| Uso de Herramientas IA Generativa y ChatGPT | Universidad del Desarrollo | 1238056492 | Presencial | 8 | $562.667 | 3 | Metodología declara explícitamente `modalidad presencial` |
| Herramientas de IA para la Productividad Profesional | Universidad de Chile | 1238082191 | Presencial | 16 | $174.360 | 3 | Metodología declara explícitamente modalidad presencial y clases expositivas presenciales |

## Implicación

No comparar precios SENCE sin separar al menos:

- `PRESENCIAL`
- `E_LEARNING_SINCRONICO`
- `E_LEARNING_ASINCRONICO`
- `ONLINE_MIXTO`
- `MIXTA_NO_RESUELTA`

Para el benchmark de Capacita, los comparables más directos de la tabla anterior son principalmente Universidad de Chile (16 h presencial), UDD (8 h presencial), Instituto Madicap (9 h presencial, aunque con contexto de precontrato) y eventualmente BP Capacitación sólo después de resolver su mezcla modal.
