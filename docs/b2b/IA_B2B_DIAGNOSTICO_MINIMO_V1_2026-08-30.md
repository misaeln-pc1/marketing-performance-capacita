# IA B2B — Diagnóstico mínimo V1

Fecha: 2026-08-30  
Issue: `#73`  
Task Hub: `misaeln-pc1/capacita-task-hub#162`  
Estado: `DRAFT_NO_VIGENTE / PILOT_READY_DOCUMENTAL`

## 1. Objetivo

Crear un levantamiento breve previo a cotización para empresas interesadas en capacitación de Inteligencia Artificial, reutilizando el patrón detectado en F2 sin copiar DNC, tests ni formularios de competidores.

El diagnóstico no es una auditoría de madurez, consultoría de procesos ni evaluación técnica exhaustiva. Su función es reducir fricción comercial y evitar ofrecer un curso genérico cuando la necesidad declarada requiere otro alcance.

## 2. Buyer canónico

Consumir, sin redefinir:

- `BP-003 v1.0.0 — Coordinador B2B`;
- `BP-004 v1.0.0 — Dueño o Jefatura PyME`.

## 3. Baseline IA que no se modifica

```text
COURSE_CODE=IA-TRAB-01
NAME=Inteligencia Artificial Aplicada al Trabajo
DURATION=16 horas cronológicas
ACTIVE_MODALITY=PRESENCIAL_SANTIAGO
PRICE_CURRENT_OPEN_COURSE=CLP169000 por participante
LEVEL=BASICO_INTERMEDIO
PROGRAMMING_REQUIRED=NO
TOOLS=ChatGPT|Gemini|Claude|Microsoft Copilot
```

Este diagnóstico no cambia precio, currículo, modalidad ni duración. Sólo determina si la necesidad B2B encaja con el curso actual o requiere revisión separada.

## 4. Regla de uso

Aplicar antes de preparar una propuesta B2B de IA cuando la empresa no llega con un requerimiento completamente especificado.

Duración objetivo del levantamiento: 5–10 minutos mediante formulario o conversación comercial breve.

No pedir RUT, PII innecesaria, información confidencial de procesos, bases de clientes, prompts internos, documentos privados ni secretos comerciales.

## 5. Preguntas mínimas

### Q1 — Rol en la decisión

¿Cuál describe mejor tu participación?

- coordino capacitación / RRHH / administración;
- lidero un equipo o área;
- decido o apruebo la capacitación;
- estoy explorando alternativas;
- otro / no definido.

**Uso:** orientar conversación `BP-003` vs `BP-004`; no clasificar automáticamente a una persona real sin incertidumbre.

### Q2 — Problema que quieren resolver

¿Cuál es hoy la principal necesidad del equipo?

- ahorrar tiempo en tareas repetitivas;
- trabajar mejor con documentos e información;
- apoyar análisis de datos/Office;
- mejorar uso de ChatGPT/Gemini/Claude/Copilot;
- estandarizar criterios de uso de IA;
- aprender buenas prácticas, privacidad y verificación;
- identificar casos de uso por área;
- otro.

### Q3 — Tareas concretas

¿Qué 2–3 tareas laborales quieren mejorar con IA?

Respuesta breve, sin adjuntar información confidencial.

**Uso:** distinguir capacitación aplicable de consultoría o automatización técnica.

### Q4 — Participantes

¿Cuántas personas aproximadamente participarían?

- 2–5;
- 6–15;
- 16+;
- todavía no definido.

**Regla:** el número se usa para cotización/logística; no asumir capacidad de sala o tarifa grupal hasta confirmar.

### Q5 — Nivel actual

¿Cómo describirías el nivel del equipo?

- nunca ha usado IA generativa;
- usa IA ocasionalmente;
- usa IA con frecuencia, pero sin método común;
- ya tiene usos avanzados/automatizaciones;
- niveles mezclados;
- no sabemos.

### Q6 — Modalidad / operación

¿Qué modalidad sería más viable?

- presencial en Santiago;
- in-company;
- online en vivo;
- híbrida;
- asincrónica;
- no definida.

**Regla:** esta respuesta expresa preferencia, no disponibilidad confirmada para IA. La oferta debe pasar por `IA_B2B_OFFER_REVIEW_V1`.

### Q7 — Herramientas y licencias

¿Qué herramientas utiliza o tiene autorizadas la empresa?

- ChatGPT;
- Gemini;
- Claude;
- Microsoft Copilot;
- otras;
- ninguna definida.

No pedir credenciales, claves, cuentas ni accesos.

### Q8 — Privacidad / restricciones

¿Existen restricciones internas relevantes para usar IA?

- política corporativa de IA;
- información confidencial;
- datos personales;
- herramientas aprobadas/restringidas;
- todavía no existe política;
- no sabemos.

**Uso:** ajustar ejemplos y límites; no emitir asesoría legal/compliance.

### Q9 — Horizonte

¿Cuándo esperan ejecutar la capacitación?

- dentro de 30 días;
- 1–3 meses;
- 3+ meses;
- exploratorio.

### Q10 — Requisitos administrativos / evidencia

¿Qué necesitan para gestionar internamente la capacitación?

- propuesta formal;
- temario/duración;
- modalidad y fechas;
- asistencia;
- evaluación;
- informe/seguimiento;
- SENCE;
- certificación;
- todavía no definido.

**Regla:** registrar necesidad. No prometer asistencia, evaluación, informes, SENCE, certificación o seguimiento hasta validar el Offer Review.

## 6. Clasificación de salida

### `FIT_CURRENT_COURSE`

Usar cuando:

- necesidad = productividad/documentos/datos/Office/uso responsable;
- nivel = inicial o intermedio;
- no exige programación avanzada;
- la modalidad viable puede confirmarse;
- el alcance cabe razonablemente dentro del baseline IA-TRAB-01.

**Salida:** preparar propuesta B2B sólo después de confirmar condiciones en Offer Review.

### `FIT_WITH_CONTEXTUALIZATION`

Usar cuando el curso base encaja, pero la empresa necesita énfasis por función/área, ejemplos o nivel.

**Salida:** `OFFER_REVIEW / DESIGN_REVIEW`; no prometer personalización total ni alterar currículo desde Marketing.

### `NEEDS_DEEPER_SCOPING`

Usar cuando:

- necesidad no está clara;
- niveles muy heterogéneos;
- exige múltiples áreas/procesos;
- solicita diagnóstico cuantitativo de madurez;
- requiere una ruta de varios cursos.

**Salida:** reunión de levantamiento; no cotizar un curso estándar por reflejo.

### `OUT_OF_SCOPE_CURRENT_IA`

Usar cuando el requerimiento principal sea:

- desarrollo de software/IA;
- Python/API/VBA;
- agentes autónomos avanzados;
- RAG;
- machine learning;
- n8n/Make hands-on como competencia central;
- implementación técnica productiva;
- consultoría de procesos o gobernanza IA completa.

**Salida:** `NO_ACTION` sobre el curso actual; evaluar portfolio/partner por separado si existe interés comercial.

## 7. Resumen de salida recomendado

```text
EMPRESA=<nombre sólo si lo entrega para cotización>
BUYER_OR_ROLE=<declarado>
PARTICIPANTS_RANGE=
PRIMARY_PROBLEM=
TOP_TASKS=
CURRENT_LEVEL=
PREFERRED_MODALITY=
TOOLS_AVAILABLE=
PRIVACY_CONSTRAINTS=
TARGET_DATE=
ADMIN_REQUIREMENTS=
FIT=FIT_CURRENT_COURSE|FIT_WITH_CONTEXTUALIZATION|NEEDS_DEEPER_SCOPING|OUT_OF_SCOPE_CURRENT_IA
NEXT_ACTION=
CONFIRMATIONS_REQUIRED=
```

No guardar respuestas en GitHub. GitHub conserva sólo esta metodología y evidencia agregada/sanitizada futura.

## 8. Decisiones ACT / NO_ACTION

### ACT

1. `PILOT`: usar este diagnóstico en un número acotado de conversaciones B2B antes de convertirlo en formulario público.
2. `MEASURE`: registrar de forma agregada qué preguntas cambian realmente la propuesta.
3. `LEARN`: devolver a GTM/RevOps patrones repetidos de buyer/problema; no modificar buyer personas desde Marketing.

### NO_ACTION

1. No crear un score 0–100 de madurez sin evidencia.
2. No calcular ROI/productividad ahorrada a partir de respuestas declaradas.
3. No pedir información confidencial para “personalizar”.
4. No convertir cada rol/área en un curso nuevo.
5. No publicar el diagnóstico como servicio de consultoría hasta validar alcance y operación.

## 9. Validación del piloto posterior

Medir:

- % conversaciones donde el diagnóstico cambia la propuesta;
- minutos adicionales de levantamiento;
- preguntas que generan confusión;
- proporción `FIT_CURRENT_COURSE / CONTEXTUALIZATION / DEEPER / OUT_OF_SCOPE`;
- requisitos B2B recurrentes no confirmados;
- utilidad para BP-003 vs BP-004.

## 10. Stop / rollback

Detener o simplificar si:

- agrega fricción sin cambiar decisiones;
- empieza a capturar PII/datos sensibles innecesarios;
- Ventas lo usa como promesa de consultoría;
- se vuelve un cuestionario largo sin impacto en la propuesta.

Rollback: volver a levantamiento comercial breve de `problema + participantes + modalidad + fecha`.

## 11. Fuentes

- Marketing F2 V03 vigente: `docs/research/COMPETITIVE_INTELLIGENCE_F2_IA_B2B_V03_2026-08-29.md`.
- GTM/RevOps: `BUYER_PERSONAS.md`, BP-003/BP-004 v1.0.0.
- Marketing: `BRIEF_BP003_COORDINADOR_B2B_V1.md` y `BRIEF_BP004_JEFATURA_PYME_V1.md`.
- Diseño de Cursos: `CURRENT.md` y `FICHA_CURSO.md` de `IA-TRAB-01`.

## Estado

`PILOT_READY_DOCUMENTAL / NO_PUBLICAR_NO_AUTOMATIZAR_SIN_GATE`.
