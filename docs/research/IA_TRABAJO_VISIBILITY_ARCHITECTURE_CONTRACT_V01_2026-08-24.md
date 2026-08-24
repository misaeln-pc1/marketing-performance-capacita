# Contrato de arquitectura de visibilidad — Landing IA Aplicada al Trabajo

Fecha: 2026-08-24  
Estado: `WORKING_BASELINE / READY_FOR_FACTORY_CONSUMPTION`  
Curso: `IA-TRAB-01 — Inteligencia Artificial Aplicada al Trabajo`

## 1. Propósito y frontera de responsabilidad

Este documento define exclusivamente la **arquitectura SEO + Local SEO + AEO + GEO/AI Search** que debe quedar representada en la landing.

Marketing define:

- intención de búsqueda;
- mapa de keywords;
- metadata SEO;
- H1 y temas semánticos obligatorios;
- preguntas FAQ/AEO obligatorias;
- hechos que deben quedar expuestos para GEO/AI Search;
- requisitos de citabilidad y AI-readability;
- consistencia de entidades y datos;
- requisitos de Local SEO;
- reglas de structured data y crawler access a validar después de construir.

La Fábrica de Landing / Capacita Edge define:

- layout;
- orden visual exacto de bloques;
- hero visual;
- cards;
- componentes;
- formulario;
- CSS;
- responsive;
- imágenes;
- detalles UI/UX;
- implementación técnica dentro de sus contratos activos.

Este contrato **no rediseña la landing** y no obliga a una composición visual concreta.

---

## 2. Baseline comercial que debe ser idéntico en toda la página

```text
NAME=Inteligencia Artificial Aplicada al Trabajo
MODALITY=PRESENCIAL_SANTIAGO
DURATION_HOURS=16
PRICE_CLP=169000
LEVEL=BASICO_INTERMEDIO
PROGRAMMING_REQUIRED=NO
PRIMARY_TOOLS=ChatGPT|Gemini|Claude|Microsoft Copilot
COMPLEMENTARY_TOOLS=NotebookLM|Perplexity
PRIMARY_BP=BP-001 v1.0.0
SECONDARY_BP=BP-002 v1.0.0
```

Fuente dominante:

`misaeln-pc1/Diseno-de-Cursos/cursos/nuevos/inteligencia-artificial-aplicada-trabajo-16h/XFER__IA_TRAB_PRESENCIAL_LANDING_v03_2026-08-23.md`

No reutilizar CLP $178.000.

---

## 3. Intención principal de búsqueda

### Intención primaria

Persona que busca **un curso de Inteligencia Artificial / curso IA** y está evaluando una capacitación real para aprender a utilizar IA.

### Diferenciador de oferta

- presencial;
- Santiago;
- IA aplicada al trabajo;
- sin programación;
- práctica guiada;
- ChatGPT + Gemini + Claude + Microsoft Copilot.

### Regla

`Presencial` y `Santiago` diferencian la oferta, pero **no reemplazan** la intención head `curso inteligencia artificial` / `curso IA`.

---

## 4. Keyword architecture

### 4.1 Keywords primarias — obligatorias en cobertura semántica

- `curso inteligencia artificial`
- `curso IA`
- `curso de inteligencia artificial`

### 4.2 Keywords presencial / local — obligatorias

- `curso inteligencia artificial presencial`
- `curso de inteligencia artificial presencial`
- `curso IA presencial`
- `curso inteligencia artificial Santiago`
- `curso inteligencia artificial Chile`
- `curso IA Santiago`

### 4.3 Propuesta de valor / necesidad — obligatorias como conceptos

- `inteligencia artificial aplicada al trabajo`
- `IA para el trabajo`
- `productividad con IA`
- `inteligencia artificial para productividad`
- `automatización de tareas con IA`
- `IA para profesionales`
- `IA para tareas administrativas`
- `IA para análisis de información`

### 4.4 Herramientas / entidades — obligatorias donde correspondan

- `ChatGPT`
- `Gemini`
- `Claude`
- `Microsoft Copilot`

Complementarias, sólo cuando el contenido canónico las soporte:

- `NotebookLM`
- `Perplexity`

### 4.5 Temas semánticos obligatorios

La página debe cubrir naturalmente:

- inteligencia artificial generativa;
- prompting profesional;
- documentos y PDF;
- investigación asistida;
- análisis y verificación de información;
- IA para Office;
- IA para Excel/Sheets y datos;
- análisis de tablas/CSV;
- asistentes de IA;
- proyectos de IA;
- multimodalidad;
- flujos de trabajo;
- alucinaciones / errores de IA;
- privacidad;
- uso responsable;
- control humano.

### 4.6 Intenciones excluidas — no deben gobernar la landing

- curso IA gratis;
- diplomado inteligencia artificial;
- carrera inteligencia artificial;
- machine learning;
- programación IA;
- Python para IA;
- desarrollo de modelos;
- curso avanzado de agentes autónomos;
- automatización técnica avanzada.

### Regla editorial

No hacer keyword stuffing. No crear un bloque independiente para cada variante. La cobertura debe ser natural dentro de la arquitectura semántica.

---

## 5. Metadata SEO — contrato

### Slug conceptual

`/curso-inteligencia-artificial-presencial-santiago`

La URL productiva final la decide Edge bajo su contrato.

### SEO title

**Curso de Inteligencia Artificial Presencial en Santiago | Capacita**

### Meta description

**Curso presencial de Inteligencia Artificial en Santiago. Aprende a usar ChatGPT, Gemini, Claude y Copilot en tareas reales de trabajo. 16 horas prácticas.**

### H1 obligatorio

**Curso de Inteligencia Artificial Presencial en Santiago: IA Aplicada al Trabajo**

### Regla de encabezados

- un único H1;
- H2/H3 deben estructurar temas reales, no repetir keywords mecánicamente;
- no usar headings sólo por densidad SEO.

---

## 6. Cobertura temática obligatoria

La Fábrica puede decidir el orden visual, pero la landing final debe contener contenido suficiente para responder estos bloques temáticos:

1. **Qué es el curso y qué problema laboral resuelve.**
2. **Qué aprenderá el participante.**
3. **Qué herramientas se utilizarán.**
4. **Para quién está dirigido.**
5. **Cómo se aplica la IA al trabajo.**
6. **Por qué la modalidad presencial aporta valor.**
7. **Temario canónico de 6 módulos / 16 horas.**
8. **Curso presencial en Santiago / señal local.**
9. **FAQ con respuestas directas.**
10. **Hechos comerciales y académicos consistentes y visibles.**

No es obligatorio que estos diez puntos sean diez secciones visuales distintas.

---

## 7. AEO — Answer Engine Optimization

### 7.1 Regla de respuesta

Cada pregunta prioritaria debe tener una respuesta:

- directa;
- comprensible fuera de contexto;
- factual;
- visible en HTML;
- consistente con el canónico;
- sin depender de una imagen o interacción;
- sin promesas no demostradas.

La primera frase debe responder la pregunta. Después puede ampliar.

### 7.2 FAQ / preguntas P0 — obligatorias

Estas preguntas deben quedar cubiertas explícitamente en la landing, idealmente dentro de FAQ visible o de una sección equivalente:

1. **¿Qué se aprende en este curso de Inteligencia Artificial?**
2. **¿Necesito saber programación para hacer el curso?**
3. **¿Qué herramientas de Inteligencia Artificial se utilizan?**
4. **¿Cómo puedo usar la Inteligencia Artificial en mi trabajo?**
5. **¿El curso es presencial?**
6. **¿Cuánto dura el curso?**
7. **¿Cuál es el valor del curso?**
8. **¿Este curso enseña ChatGPT solamente?**
9. **¿El curso sirve para principiantes?**
10. **¿Qué diferencia tiene aprender IA de forma presencial frente a hacerlo sólo con videos o contenido online?**

### 7.3 Preguntas P1 — recomendadas

11. **¿Aprenderé a crear buenos prompts?**
12. **¿Se trabaja con documentos y PDF?**
13. **¿Se puede usar IA con Excel y datos?**
14. **¿Se enseña automatización con n8n o Make?**
15. **¿Cómo se verifican las respuestas de una IA?**
16. **¿Qué debo considerar sobre privacidad y datos confidenciales?**
17. **¿Necesito una cuenta pagada de ChatGPT, Gemini, Claude o Copilot?**
18. **¿Recibiré certificado?**

La pregunta 18 sólo puede responderse con la regla institucional vigente de Edge. No inventar certificado, acreditación, SENCE o condiciones de aprobación.

### 7.4 Preguntas AEO derivadas de intención SERP/PAA

La cobertura de contenido debe permitir responder además:

- ¿Dónde aprender IA en Chile?
- ¿Qué cursos de IA hay para principiantes?
- ¿Cómo usar la inteligencia artificial en el trabajo?
- ¿Cuáles son las herramientas de IA más usadas para trabajar?
- ¿Qué curso de IA elegir si no sé programar?
- ¿Qué diferencia hay entre ChatGPT, Gemini, Claude y Copilot?

No es obligatorio convertir todas estas preguntas en FAQ literal; sí debe existir contenido que permita responderlas.

---

## 8. GEO / AI Search — contrato de hechos y citabilidad

### 8.1 Hechos obligatorios que deben quedar explícitos en HTML visible

La landing debe exponer de forma inequívoca:

- Capacita es el proveedor del curso;
- nombre: **Inteligencia Artificial Aplicada al Trabajo**;
- modalidad: **Presencial Santiago**;
- duración: **16 horas cronológicas**;
- precio: **CLP $169.000 por participante**;
- nivel: **Básico–Intermedio**;
- programación requerida: **No**;
- herramientas principales: **ChatGPT, Gemini, Claude y Microsoft Copilot**;
- enfoque: tareas laborales reales;
- ámbitos: productividad, documentos, investigación, información, datos, Office, asistentes y flujos de trabajo;
- privacidad, verificación y uso responsable como parte del enfoque;
- CTA / siguiente paso comercial.

### 8.2 Regla de extracción

Estos hechos pueden estar distribuidos en varios componentes, pero al menos una parte de la página debe permitir reconstruir la oferta sin ambigüedad.

No dejar hechos críticos sólo en:

- imágenes;
- sliders;
- tooltips;
- texto cargado únicamente después de interacción;
- JSON-LD sin paridad visible;
- atributos inaccesibles al contenido principal.

### 8.3 Entidades

Nombrar con consistencia:

- `Capacita`;
- `Inteligencia Artificial Aplicada al Trabajo`;
- `ChatGPT`;
- `Google Gemini` o `Gemini`;
- `Claude`;
- `Microsoft Copilot`;
- `Santiago`.

No alternar nombres que parezcan productos distintos.

### 8.4 Citabilidad

Los bloques importantes deben ser:

- autocontenidos;
- factuales;
- breves cuando sea posible;
- con sujeto explícito;
- sin pronombres ambiguos;
- sin marketing exagerado;
- con limitaciones cuando corresponda.

Ejemplo de patrón válido:

> Capacita ofrece un curso presencial de Inteligencia Artificial Aplicada al Trabajo en Santiago, de 16 horas cronológicas y nivel Básico–Intermedio. No requiere programación y trabaja con ChatGPT, Gemini, Claude y Microsoft Copilot.

No es obligatorio usar exactamente este texto; sí conservar estos hechos y su claridad.

---

## 9. Local SEO — contrato

La landing debe conectar de forma natural:

`curso inteligencia artificial` + `presencial` + `Santiago`.

### Obligatorio

- `Santiago` visible en title/H1 o equivalente definido arriba;
- modalidad presencial inequívoca;
- ubicación/sede exacta sólo desde fuente operativa confirmada;
- coherencia entre página, schema y datos institucionales;
- evitar crear páginas locales duplicadas sin contenido diferenciador.

### Cuando la sede exacta esté confirmada

Edge deberá verificar si corresponde mostrar:

- Santiago Centro;
- dirección;
- referencia de acceso;
- mapa o información de ubicación;
- datos institucionales consistentes con el sitio.

Marketing no inventa estos datos.

---

## 10. Structured data — contrato

- usar sólo tipos y propiedades válidos/soportados por la implementación vigente de Edge;
- mantener paridad entre structured data y contenido visible;
- no crear schema especial para AEO/GEO/AI Search;
- no inventar rating, reviews, fechas, disponibilidad, SENCE, cupos o certificaciones;
- FAQ structured data sólo si Edge lo mantiene conforme a su contrato y existe paridad con FAQ visible; no asumir rich result.

---

## 11. Crawler / AI retrieval — validación post-build

Después de construir la landing, Marketing debe revisar:

- Googlebot;
- Bingbot;
- OAI-SearchBot;
- PerplexityBot / Perplexity-User cuando corresponda;
- Claude-SearchBot / Claude-User cuando corresponda.

Separar búsqueda/retrieval de crawlers de entrenamiento/desarrollo.

No inferir acceso sólo leyendo `robots.txt`; revisar también HTTP status, CDN/WAF/challenge y contenido entregado cuando aplique.

---

## 12. DO_NOT_CHANGE

La Fábrica no debe modificar por razones SEO/AEO/GEO:

- 16 horas;
- CLP $169.000;
- modalidad Presencial Santiago;
- nivel Básico–Intermedio;
- no requiere programación;
- temario canónico de 6 módulos;
- herramientas principales;
- buyer personas canónicos;
- exclusión de Python, machine learning y automatización técnica avanzada.

---

## 13. Definition of Done para la Fábrica

Antes de devolver la landing a Marketing, verificar:

```text
PRIMARY_INTENT_COVERED=PASS
PRIMARY_KEYWORD_COVERED=PASS
PRESENTIAL_SANTIAGO_SIGNAL=PASS
SEO_TITLE=PASS
META_DESCRIPTION=PASS
SINGLE_H1=PASS
SEMANTIC_TOPICS=PASS
FAQ_P0=PASS
AEO_DIRECT_ANSWERS=PASS
GEO_FACTS_VISIBLE=PASS
ENTITY_CONSISTENCY=PASS
LOCAL_SEO=PASS
STRUCTURED_DATA_PARITY=PASS|PENDING_POST_BUILD
CRAWLER_ACCESS=PENDING_MARKETING_POST_BUILD
PRICE_169000_PARITY=PASS
DURATION_16H_PARITY=PASS
PROGRAMMING_REQUIRED_NO=PASS
```

---

## 14. Handoff de vuelta a Marketing

Cuando HTML/Edge termine el preview, devolver a Marketing:

- URL de preview;
- HTML/render accesible;
- metadata;
- JSON-LD/structured data;
- robots/indexability del preview;
- cualquier decisión de Factory que afecte headings, FAQ, contenido visible o datos locales.

Marketing entonces ejecutará el protocolo integral:

`SEO → Local SEO → AEO → GEO/AI Search → AI-readability → demanda/intención → buyer persona → CRO → medición → impacto comercial`.

La revisión post-build es donde se harán los ajustes finos. Esta fase sólo define la arquitectura que la Fábrica debe poder construir.