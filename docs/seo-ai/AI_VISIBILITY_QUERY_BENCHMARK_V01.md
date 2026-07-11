# Benchmark de visibilidad en motores generativos V01

## Propósito

Medir de forma repetible si Capacita aparece, es citado correctamente y mantiene presencia estable en respuestas de motores generativos. Este benchmark no es un ranking oficial ni una garantía de visibilidad.

## Motores iniciales

- ChatGPT con búsqueda web cuando esté disponible;
- Gemini;
- Google Search con AI Overviews o AI Mode cuando aplique;
- Bing/Copilot como referencia secundaria cuando esté disponible.

## Condiciones de prueba

Registrar en cada ejecución:

- fecha y hora;
- motor y versión/superficie visible;
- país e idioma;
- sesión nueva o incógnito;
- búsqueda web/fuentes activadas o no;
- texto exacto de la consulta;
- respuesta completa conservada fuera del repo si contiene datos sensibles;
- fuentes y URLs citadas;
- presencia o ausencia de Capacita;
- competidores repetidos.

No mezclar resultados de sesiones personalizadas con sesiones neutrales.

## Consultas B2C locales

1. `Lista 15 instituciones que ofrecen cursos de Excel presencial en Santiago de Chile.`
2. `¿Dónde puedo hacer un curso de Excel básico presencial en Santiago Centro?`
3. `Recomienda cursos de Excel básico e intermedio presenciales cerca del Metro La Moneda.`
4. `¿Qué instituciones ofrecen Excel presencial para principiantes en Santiago?`
5. `Compara opciones de cursos de Excel presencial en Santiago por ubicación, modalidad y nivel.`
6. `¿Dónde estudiar Excel desde cero de forma presencial en Santiago de Chile?`
7. `Cursos de Excel con profesor en vivo y computador para cada alumno en Santiago Centro.`

## Consultas por intención separada

### Básico

- `Curso de Excel básico presencial en Santiago.`
- `Aprender Excel desde cero presencial en Santiago Centro.`

### Intermedio

- `Curso de Excel intermedio presencial en Santiago.`
- `Curso de tablas dinámicas y BUSCARV presencial en Santiago.`

### Básico–intermedio

- `Curso de Excel básico e intermedio presencial en Santiago.`

### Clases particulares

- `Profesor particular de Excel presencial en Santiago.`
- `Clases particulares de Excel a domicilio en Santiago.`

### B2B

- `Capacitación Excel presencial para empresas en Santiago.`
- `OTEC para capacitar equipos en Excel en Chile.`

## Campos de evaluación

| Campo | Criterio |
|---|---|
| Presencia | Capacita aparece o no aparece. |
| Posición aproximada | Orden de aparición cuando existe lista explícita. |
| Citación | Se incluye una URL o fuente atribuible. |
| URL | Página citada: home, landing, artículo, directorio u otra. |
| Exactitud | Modalidad, ubicación, nivel y oferta son correctos. |
| Relevancia | La recomendación responde a la intención consultada. |
| Persistencia | Presencia repetida en varias formulaciones y fechas. |
| Competidores | Dominios o marcas que aparecen recurrentemente. |
| Fuente externa | Directorios, medios, reseñas o terceros que sustentan la respuesta. |

## Métricas agregadas

- cobertura de presencia = consultas donde aparece / consultas ejecutadas;
- cobertura de citación = consultas con URL de Capacita / consultas ejecutadas;
- exactitud = respuestas correctas / respuestas que mencionan Capacita;
- persistencia = consultas donde aparece en al menos dos ejecuciones independientes;
- diversidad de URLs citadas;
- share of voice del conjunto observado;
- frecuencia de competidores por intención.

## Cadencia

- baseline inicial: tres ejecuciones por consulta en días diferentes;
- seguimiento: mensual;
- revisión extraordinaria: después de cambios relevantes de robots, canonicals, contenido, structured data o arquitectura.

## Guardrails

- no usar prompts manipulados para forzar la marca;
- no concluir por una sola respuesta;
- no declarar causalidad sin cambio controlado;
- no publicar respuestas completas que contengan datos sensibles;
- no automatizar consultas masivas contra servicios sin revisar términos, límites y costos;
- no mezclar B2C, B2B y clases particulares en una única métrica.

## Salida esperada

Una tabla agregada y sanitizada por fecha, motor, consulta, intención, presencia, URL citada, competidores, exactitud y observaciones. La evidencia privada puede vivir fuera del repo; GitHub conserva solo metodología y síntesis.