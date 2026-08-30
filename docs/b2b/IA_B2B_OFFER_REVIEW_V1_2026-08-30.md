# IA B2B — Offer Review V1

Fecha: 2026-08-30  
Issue: `#73`  
Task Hub: `misaeln-pc1/capacita-task-hub#162`  
Estado: `DRAFT_NO_VIGENTE / REVIEW_READY`

## 1. Objetivo

Separar con trazabilidad qué puede ofrecer Capacita hoy a una empresa interesada en IA, qué requiere confirmación previa y qué no debe prometerse todavía.

La matriz evita heredar automáticamente al curso IA capacidades institucionales genéricas publicadas para otras líneas.

Estados:

- `AVAILABLE`: existe evidencia suficiente para usarlo dentro del alcance indicado.
- `NEEDS_CONFIRMATION`: existe señal institucional o hipótesis, pero falta confirmación específica para IA/propuesta concreta.
- `NOT_AVAILABLE`: el canónico actual lo excluye o no está preparado.
- `PILOT_READY`: patrón documental diseñado, aún no validado como servicio operativo.

## 2. Baseline IA vigente

Fuente dominante: Diseño de Cursos `IA-TRAB-01`.

```text
NAME=Inteligencia Artificial Aplicada al Trabajo
DURATION=16 horas cronológicas
ACTIVE_MODALITY=PRESENCIAL_SANTIAGO
PRICE_OPEN_COURSE=CLP169000 por participante
LEVEL=BASICO_INTERMEDIO
PROGRAMMING_REQUIRED=NO
TOOLS=ChatGPT|Gemini|Claude|Microsoft Copilot
SENCE=NO_PREPARADO
ZOHO=ALTA_OPERATIVA_PENDIENTE
```

Exclusiones explícitas: Python, APIs, VBA, n8n/Make hands-on, agentes autónomos avanzados, automatización técnica avanzada, programación de IA y machine learning.

## 3. Matriz de oferta IA B2B

| Capacidad / claim | Estado IA | Evidencia | Regla comercial |
|---|---|---|---|
| Curso `IA-TRAB-01` práctico y laboral | `AVAILABLE` | Diseño `CURRENT.md` / `FICHA_CURSO.md` | Puede presentarse como base de una conversación B2B. |
| 16 horas cronológicas | `AVAILABLE` | Canónico Diseño | No modificar desde Marketing. |
| Nivel Básico–Intermedio | `AVAILABLE` | Canónico Diseño | No vender como avanzado. |
| Sin programación | `AVAILABLE` | Canónico Diseño | Diferenciador válido. |
| ChatGPT + Gemini + Claude + Microsoft Copilot | `AVAILABLE` | Canónico Diseño | Mantener consistencia de marcas y alcance. |
| Productividad, documentos, investigación, Office/datos, asistentes y flujos de trabajo | `AVAILABLE` | Canónico Diseño | No convertir “flujos” en promesa de automatización técnica productiva. |
| Privacidad, verificación y uso responsable como contenidos | `AVAILABLE` | Canónico Diseño | No presentar como consultoría legal/compliance IA. |
| Presencial Santiago | `AVAILABLE` | Canónico Diseño | Modalidad comercial activa del curso. |
| Precio CLP 169.000 | `AVAILABLE_ONLY_OPEN_COURSE` | Canónico Diseño | Es precio por participante de la salida actual; **no** usar como tarifa grupal/in-company automática. |
| Cotización/propuesta para empresas | `AVAILABLE_INSTITUTIONAL` | Sitio público empresas + briefs B2B | Se puede recibir y estructurar solicitud; precio/condiciones IA deben definirse caso a caso. |
| Diagnóstico B2B IA mínimo previo | `PILOT_READY` | F2 + `IA_B2B_DIAGNOSTICO_MINIMO_V1` | Usar primero como levantamiento preventa; no vender como assessment cuantitativo de madurez. |
| In-company | `NEEDS_CONFIRMATION` | Capacidad institucional pública; no existe variante IA canónica específica | Confirmar lugar, relator, equipos, participantes, condiciones y precio antes de ofrecer. |
| Presencial en regiones | `NEEDS_CONFIRMATION` | Capacidad institucional pública; IA no tiene variante específica | No prometer cobertura IA nacional por reflejo. |
| Online en vivo | `NEEDS_CONFIRMATION / REQUIRES_VARIANT` | Institucionalmente disponible; variante IA sincrónica histórica está superseded | Diseño de Cursos debe reactivar/definir variante antes de venta. |
| Híbrida | `NEEDS_CONFIRMATION / REQUIRES_VARIANT` | Institucionalmente publicada; no definida para IA | Requiere definición de Diseño/operación. |
| E-learning asincrónico | `NOT_AVAILABLE_FOR_CURRENT_IA` | Moodle fuera de alcance; no hay variante IA activa | No vender como modalidad IA actual. |
| Personalización de ejemplos/casos | `NEEDS_CONFIRMATION` | Patrón B2B vigente; canónico IA no define alcance de personalización | Aceptar necesidad, no prometer adaptación total. |
| Temario totalmente personalizado | `NEEDS_CONFIRMATION / DESIGN_OWNER` | No definido | Requiere Diseño de Cursos, alcance/horas/precio. |
| Grupo/tamaño máximo | `NEEDS_CONFIRMATION` | No definido para IA | No heredar automáticamente capacidades de sala de otros cursos. |
| Diagnóstico de nivel formal | `PILOT_READY / NOT_YET_PRODUCTIZED` | Diagnóstico mínimo diseñado; evaluación formal fuera de alcance del curso | No publicar score o certificado diagnóstico. |
| Evaluación inicial/final | `NEEDS_CONFIRMATION` | Evaluaciones fuera del alcance de la ficha IA | Definir por propuesta antes de prometer. |
| Control de asistencia / informe a empresa | `NEEDS_CONFIRMATION` | Brief BP-003 exige confirmarlo por programa | No publicar claim genérico sin entregable operativo. |
| Seguimiento posterior | `NEEDS_CONFIRMATION` | No definido en IA | Acordar explícitamente si se incorpora. |
| Certificación | `NEEDS_CONFIRMATION` | Ficha IA no la define | No inventar certificado/condiciones. |
| Franquicia / código SENCE para IA | `NOT_AVAILABLE_CURRENTLY` | `CURRENT.md`: `SENCE=NO_PREPARADO` | **No mencionar SENCE para IA** hasta preparación/validación específica. |
| Gestión administrativa SENCE institucional | `AVAILABLE_INSTITUTIONAL_BUT_NOT_IA` | Sitio público de Capacita | No convierte automáticamente IA-TRAB-01 en curso SENCE. |
| Consultoría de procesos | `NOT_INCLUDED` | Baseline B2B y Diseño | Sólo capacitación salvo contratación/diseño separado. |
| Implementación técnica de IA | `NOT_AVAILABLE` | Exclusiones canónicas | No vender desarrollo/automatización productiva. |
| Python/APIs/RAG/agentes/ML/n8n/Make hands-on | `NOT_AVAILABLE` | Exclusiones canónicas | Derivar a portfolio review, no ampliar el curso actual. |
| ROI/mejora porcentual garantizada | `NOT_ALLOWED_WITHOUT_EVIDENCE` | Reglas B2B/F2 | No prometer ahorro, productividad, reducción de errores ni retorno garantizado. |

## 4. Capacidad institucional pública observada — no heredar sin validación IA

Fuentes públicas revisadas 2026-08-30:

- `https://capacita.cl/cursos-para-empresas`
- `https://capacita.cl/servicios-de-capacitacion/`
- `https://capacita.cl/curso-empresa-excel`

El sitio institucional publica, entre otras capacidades:

- presencial Santiago y regiones;
- online en vivo, e-learning e híbrido;
- in-company;
- DNC/diagnósticos;
- orientación/gestión SENCE;
- propuestas para empresas.

**Regla:** estas señales prueban capacidad institucional general, no automáticamente disponibilidad para `IA-TRAB-01`. La matriz de la sección 3 prevalece para la oferta IA.

## 5. Hallazgo de consistencia pública — requiere validación antes de sales enablement

La página pública `cursos-para-empresas` muestra actualmente claims cuantitativos de impacto (por ejemplo cobertura diagnóstica, mejora promedio y retención) y lenguaje de “retorno real de inversión”.

Este Offer Review **no encontró evidencia interna canónica** que permita reutilizar esos porcentajes como proof para IA.

Decisión:

```text
ACTION=DEEP_DIVE / VERIFY_PUBLIC_PROOF
OWNER=Marketing + dueño operativo de medición
STATUS=NEEDS_CONFIRMATION
USE_IN_IA_SALES_ENABLEMENT=NO_UNTIL_VERIFIED
```

No se modifica la página en esta rama. Si esos claims carecen de fuente verificable, corresponde issue/PR separado antes de promoverlos en campañas o ventas.

## 6. Propuesta mínima B2B IA que sí puede estructurarse hoy

Sin publicar nuevos claims, Marketing puede trabajar documentalmente con este flujo:

```text
SOLICITUD EMPRESA
-> DIAGNOSTICO B2B IA MINIMO
-> CLASIFICAR FIT
-> CONFIRMAR MODALIDAD / PARTICIPANTES / FECHA / REQUISITOS
-> CONFIRMAR AVAILABLE vs NEEDS_CONFIRMATION
-> PROPUESTA FORMAL
-> SI HAY CAMBIO CURRICULAR: DISEÑO DE CURSOS
-> SI HAY SENCE: GATE SENCE ESPECIFICO
-> CAPACITACION
-> EVIDENCIA/SEGUIMIENTO SOLO SI FUE DEFINIDO EN PROPUESTA
```

## 7. Offer skeleton permitido para conversación comercial

Puede decirse, sujeto a confirmar logística/precio empresa:

> Capacita dispone de un curso base de Inteligencia Artificial Aplicada al Trabajo de 16 horas, nivel Básico–Intermedio y sin programación, enfocado en el uso práctico de ChatGPT, Gemini, Claude y Microsoft Copilot en tareas laborales. Para una empresa, primero levantamos la necesidad del equipo y confirmamos modalidad, participantes, fechas y condiciones antes de preparar la propuesta.

No añadir automáticamente:

- “con código SENCE”;
- “100% personalizado”;
- “incluye informe de impacto”;
- “ROI medido”;
- “seguimiento incluido”;
- “online/híbrido disponible”;
- “en todo Chile”;
- “certificación incluida”;

sin confirmación específica.

## 8. Decisiones ACT / NO_ACTION

### ACT

1. `PILOT`: probar el diagnóstico mínimo en conversaciones B2B.
2. `OFFER_REVIEW`: usar esta matriz antes de cualquier cotización IA empresa.
3. `CONFIRM`: definir las primeras capacidades IA B2B que merecen pasar de `NEEDS_CONFIRMATION` a `AVAILABLE`.
4. `UPDATE_SALES_ENABLEMENT`: sólo después de confirmar proof, modalidad, entregables y claims.
5. `VERIFY_PUBLIC_PROOF`: revisar por separado los porcentajes/ROI publicados en la página empresas antes de reutilizarlos.

### NO_ACTION

1. No modificar `IA-TRAB-01` B2C/presencial por este offer review.
2. No activar SENCE para IA desde Marketing.
3. No reactivar online/híbrido desde Marketing.
4. No definir tarifa grupal extrapolando CLP 169.000.
5. No convertir el diagnóstico en consultoría de madurez sin piloto.
6. No prometer personalización, reporting o seguimiento no confirmados.

## 9. Próximas confirmaciones recomendadas — orden mínimo

Estas son confirmaciones operativas, no preguntas para Misael en esta fase documental:

1. `IA_IN_COMPANY`: ¿se ejecutará realmente y bajo qué condiciones?
2. `IA_GROUP_SIZE`: rango operativo por modalidad.
3. `IA_B2B_PRICING_METHOD`: cómo cotizar grupos sin reutilizar precio individual por reflejo.
4. `IA_CUSTOMIZATION`: qué puede adaptarse sin cambiar competencia/duración.
5. `IA_ATTENDANCE_EVALUATION_REPORTING`: entregables disponibles.
6. `IA_CERTIFICATION`: regla institucional aplicable.
7. `IA_SENCE`: mantener NO hasta que Diseño/SENCE lo prepare.
8. `IA_ONLINE_OR_HYBRID`: sólo si se decide crear/reactivar variante.

## 10. Fuentes

### Internas

- `docs/research/COMPETITIVE_INTELLIGENCE_F2_IA_B2B_V03_2026-08-29.md`.
- GTM/RevOps `BUYER_PERSONAS.md`, BP-003/BP-004 v1.0.0.
- Marketing `BRIEF_BP003_COORDINADOR_B2B_V1.md`.
- Marketing `BRIEF_BP004_JEFATURA_PYME_V1.md`.
- Diseño de Cursos `CURRENT.md` / `FICHA_CURSO.md` de `IA-TRAB-01`.

### Públicas

- `https://capacita.cl/cursos-para-empresas`
- `https://capacita.cl/servicios-de-capacitacion/`
- `https://capacita.cl/curso-empresa-excel`

## 11. Estado / gate

```text
OFFER_REVIEW_DOCUMENTAL=PASS
IA_BASELINE_CHANGED=NO
SENCE_IA=NOT_AVAILABLE_CURRENTLY
B2B_DIAGNOSTIC=PILOT_READY
PRODUCTION_CHANGES=0
PUBLIC_CLAIMS_CHANGED=0
NEXT_GATE=REVIEW_AND_CONFIRM_MINIMUM_B2B_CAPABILITIES
```

Estado: `REVIEW_READY / NO_PUBLICAR_NO_ACTIVAR_SIN_GATE`.
