# Competitive Intelligence F2 V03 — IA + B2B/Empresa

Fecha de corte: 2026-08-29  
Issue padre: `#69`  
Task Hub: `misaeln-pc1/capacita-task-hub#155`  
Modelo consumido: AI OS Competitive Intelligence V03  
Pin exacto AI OS: `4f02d14e9ffa6dda31163c18b26d87b12349bbc8`  
Estado: `F2_EXECUTED / PUBLIC_ONLY / TRANSITORIO_NO_VIGENTE_EN_MAIN`

## 1. Scope / Decision

```text
FRONT=INTELIGENCIA_ARTIFICIAL + B2B/EMPRESA
DECISION_TO_SUPPORT=qué oferta, práctica, posicionamiento, DNC/diagnóstico, packaging, contenido o enablement vale ADOPTAR/ADAPTAR/PILOTEAR en Capacita
BUYER_OR_AREA=BP-003 Coordinador B2B v1.0.0 + BP-004 Dueño o Jefatura PyME v1.0.0
COMPETITORS=Edutecno|Transversal OTEC|CIDES Corpotraining|Kibernum IT Academy
DEPTH=STANDARD
DATA_ALLOWED=PUBLIC_ONLY
TOOLS_USED=web pública + GitHub READ/FETCH + baselines Marketing + modelo V03 pinneado
PAID_API_CREDITS_USED=0
SEM_RUSH_USED=NO
KEYWORD_PLANNER_USED=NO
ADS_API_USED=NO
CRM_USED=NO
PRODUCTION_CHANGES=0
```

### Decisión que este F2 debía soportar

Determinar si la evidencia pública de los cuatro referentes justifica cambiar algo ahora en la oferta/posicionamiento IA de Capacita o, alternativamente, pilotear prácticas B2B específicas sin reabrir el curso/landing B2C ya definidos.

---

## 2. Baseline reutilizado — no se rehizo research IA

Se consumieron como baseline vigente en Marketing:

1. `docs/research/IA_TRABAJO_PRESENCIAL_SANTIAGO_MARKET_BENCHMARK_V01_2026-08-23.md` — PR #67.
2. `docs/research/IA_TRABAJO_VISIBILITY_ARCHITECTURE_CONTRACT_V01_2026-08-24.md` — PR #68.

Baseline preservado:

```text
COURSE_CODE=IA-TRAB-01
NAME=Inteligencia Artificial Aplicada al Trabajo
LEVEL=Básico-Intermedio
DURATION=16 horas cronológicas
MODALITY=Presencial Santiago
PRICE=CLP 169000
PROGRAMMING_REQUIRED=NO
PRIMARY_TOOLS=ChatGPT|Gemini|Claude|Microsoft Copilot
PRIMARY_B2C_DIFFERENTIATOR=PRESENCIAL_ACCESIBLE_SANTIAGO
PRIMARY_SEARCH_INTENT=curso inteligencia artificial
```

Regla aplicada: el F2 **no** reabrió demanda, SEO/AEO/GEO, precio, duración, modalidad ni temario de la oferta presencial. El análisis se concentró en el delta B2B/empresa.

Buyer personas B2B canónicos consumidos desde GTM/RevOps:

- `BP-003 v1.0.0 — Coordinador B2B`: coordina capacitación para terceros; valora baja fricción, trazabilidad, fechas, modalidad, factura/reportes y SENCE cuando aplique.
- `BP-004 v1.0.0 — Dueño o Jefatura PyME`: decide por impacto operacional; valora rapidez, utilidad, adopción del equipo, claridad comercial y baja fricción.

No se redefinieron buyer personas.

---

## 3. SOURCE_MANIFEST

Todas las fuentes siguientes son públicas. No se usaron zonas autenticadas ni datos personales.

| ID | Tipo | Organización | Fuente | Observado | Uso en F2 |
|---|---|---|---|---|---|
| K1 | Primaria | Kibernum | https://www.kibernum.com/ | 2026-08-29 | Portafolio IA actual: Hello AI, AI Adoption, AI Fusion Squads, AI EDGE Talent, AI Fast Scope; posicionamiento empresa/IA. |
| K2 | Primaria | Kibernum | https://www.kibernum.com/kibernum-presento-su-portafolio-2026-en-encuentro-con-triadas-y-equipos/ | 2026-08-29 | Confirma portafolio 2026 y `AI Fast Scope` con diagnóstico consultivo + ejecución acotada. |
| K3 | Primaria | Kibernum | https://www.kibernum.com/summit-agro-chile-finalizo-el-programa-hello-ai-junto-a-it-academy/ | 2026-08-29 | Caso público: charla + 12 h de talleres para adopción práctica de IA en una empresa. |
| K4 | Primaria histórica | Kibernum | https://www.kibernum.com/kibernum-y-cenia-celebran-el-dia-de-la-inteligencia-artificial-ai-in-action-y-firman-un-nuevo-acuerdo-de-colaboracion/ | 2026-08-29 | Antecedente del patrón adopción: entrenamiento -> benchmark/use cases -> oportunidades KPI -> POC/MVP. Se usa como corroboración histórica, no como oferta 2026 por sí sola. |
| E1 | Primaria | Edutecno | https://edutecno.cl/ | 2026-08-29 | Posicionamiento B2B, co-creación, trayectoria y prueba social declarada por proveedor. |
| E2 | Primaria | Edutecno | https://edutecno.cl/tde/ | 2026-08-29 | Ruta formativa de 6 cursos + test de madurez digital + CTA demo. |
| E3 | Primaria | Edutecno | https://edutecno.cl/cursos/ | 2026-08-29 | Programas de capacitación, desarrollos a medida, categorías empresariales. |
| E4 | Primaria | Edutecno | https://lms.educampus.cl/?lang=es | 2026-08-29 | Campus público con `Herramientas de la Inteligencia Artificial`, Excel+Copilot y otros cursos laborales. |
| T1 | Primaria | Transversal OTEC | https://www.transversal-otec.cl/servicios/ | 2026-08-29 | Divisiones Mercado Privado, programas anuales, DNC/evaluación de desempeño y autoinstrucción. |
| T2 | Primaria | Transversal OTEC | https://www.transversal-otec.cl/equipo/ | 2026-08-29 | Evidencia pública de empresas capacitadas / prueba social corporativa. |
| T3 | Secundaria | Transversal OTEC | https://redcapacitacion.cl/v3.ver-requerimiento.php?rid=373862 | 2026-08-29 | Señal de respuesta a demanda: requerimiento IA 7 personas; Transversal y Kibernum entre interesados. |
| T4 | Secundaria | Transversal OTEC | https://redcapacitacion.cl/v3.ver-requerimiento.php?rid=385532 | 2026-08-29 | Señal de respuesta a demanda: Artificial Intelligence Expert 12 personas; Transversal entre interesados. |
| T5 | Secundaria | Transversal OTEC | https://redcapacitacion.cl/v3.ver-requerimiento.php?rid=385844 | 2026-08-29 | Señal de respuesta a demanda: IA + Google Workspace para 25+25 personas; Transversal entre interesados. |
| T6 | Secundaria | Transversal OTEC | https://redcapacitacion.cl/v3.ver-requerimiento.php?rid=385347 | 2026-08-29 | Señal de respuesta a demanda: Microsoft 365 Copilot; Transversal entre interesados. |
| C1 | Primaria | CIDES | https://cides.com/curso-asincronico/?id=01B04C01 | 2026-08-29 | `Inteligencia Artificial en la Pyme`, 70 h asincrónico, SENCE a solicitud de empresa, foco aplicación empresarial. |
| C2 | Primaria | CIDES | https://cides.com/curso/ventas-con-inteligencia-artificial-y-emocional/ | 2026-08-29 | IA verticalizada a ventas, 16 h, online/presencial e in-company. |
| C3 | Primaria | CIDES | https://cides.com/curso/ia-asistente-mantenimiento/ | 2026-08-29 | IA verticalizada a mantenimiento, 16 h, online/presencial e in-company. |
| C4 | Primaria | CIDES | https://cides.com/curso/excel-gestion-bases-de-datos-con-ia-y-automatizacion/ | 2026-08-29 | Cruce Excel + IA + automatización en oferta programada/in-company. |
| C5 | Primaria | CIDES | https://cides.com/cursos-de-capacitacion-online-asincronicos/ | 2026-08-29 | Catálogo asincrónico con IA PyME y transformación digital. |

### Regla de confianza

- Fuentes primarias: se usan para afirmar lo que cada proveedor publica sobre su propia oferta.
- REDCAPACITACION: se usa sólo como señal secundaria de actividad/respuesta a demanda; **no prueba adjudicación, venta, revenue ni ejecución**.
- Claims/autoevaluaciones de proveedor se tratan como claims públicos, no como evidencia independiente de resultado.

---

## 4. COMPETITOR_PROFILE — Kibernum IT Academy / Kibernum

### FACT

- El sitio 2026 presenta un portafolio de cinco productos IA: `Hello AI`, `AI Adoption`, `AI Fusion Squads`, `AI EDGE Talent` y `AI Fast Scope`.
- `Hello AI` combina capacitación y acompañamiento para incorporar IA al trabajo diario.
- `AI Adoption` declara un motor de hábitos y métricas para impulsar adopción y eficiencia.
- `AI Fast Scope` se presenta como solución de IA con diagnóstico consultivo y ejecución acotada.
- El caso público Summit Agro describe una charla inicial y 12 horas de talleres prácticos para adopción de IA en distintas áreas.
- Kibernum publica alianzas/capacidades tecnológicas y una propuesta B2B de mayor alcance que una academia de cursos aislados.

### INFERENCE

Kibernum está compitiendo por una categoría más amplia: **adopción de IA en organizaciones**, donde la capacitación es una capa de una solución que puede continuar hacia diagnóstico, hábitos, métricas y proyectos.

### VERIFY

```text
CONFIDENCE=HIGH
CORROBORATION=K1+K2+K3; K4 histórico
MATERIALITY=HIGH
```

### WHY_IT_MATTERS

Para `BP-003`, un diagnóstico reduce la incertidumbre de “qué capacitar y para quién”. Para `BP-004`, conecta capacitación con problemas operacionales y casos de uso. Esto resuelve una fricción distinta de la landing B2C presencial.

### DECISION

```text
DECISION_CLASS=ACT
ACTION_TYPE=PILOT
ACTION=Adaptar el patrón diagnóstico/oportunidades IA como entrada B2B de bajo riesgo, sin copiar el servicio ni la tecnología de Kibernum.
OWNER=Marketing
DEPENDENCY=GTM/RevOps valida buyer/propuesta; Diseño de Cursos sólo si el piloto implicara cambios curriculares posteriores.
VALIDATION=probar en una oportunidad B2B autorizada un diagnóstico breve que termine en recomendación de ruta/caso de uso y medir si mejora claridad de la cotización; métricas comerciales requieren gate posterior.
ROLLBACK_OR_STOP=detener si agrega fricción sin mejorar la definición de necesidad o si exige consultoría técnica fuera de capacidades Capacita.
```

---

## 5. COMPETITOR_PROFILE — Edutecno

### FACT

- La home se posiciona hacia crecimiento empresarial y co-creación de experiencias de capacitación.
- Su programa `Transformación Digital Empresarial` agrupa seis cursos en una ruta 100% e-learning.
- Antes de la demo, invita a responder un test de madurez digital de la organización.
- Publica programas de capacitación, desarrollos a medida y tecnologías de aprendizaje.
- Su campus público expone cursos de IA laboral, IA para PYMEs y Excel con Copilot, entre otras líneas.
- Publica métricas de recomendación/mejora laboral como claims propios; no fueron corroborados de forma independiente en este F2.

### INFERENCE

El valor principal para Capacita no está en copiar su catálogo, sino en **funnel B2B + assessment + ruta formativa + demo + prueba social**. La evidencia pública actual es más fuerte para esa arquitectura comercial/formativa que para una oferta integral de adopción IA comparable a Kibernum.

### VERIFY

```text
CONFIDENCE=HIGH para arquitectura B2B; MEDIUM para alcance específico de servicios IA
CORROBORATION=E1+E2+E3+E4
MATERIALITY=HIGH
```

### DECISION

```text
DECISION_CLASS=ACT
ACTION_TYPE=ADAPT_PRACTICE
ACTION=Usar como benchmark el patrón assessment -> ruta/programa -> demo/cotización y el uso disciplinado de prueba social, sin copiar su malla, claims ni web.
OWNER=Marketing
VALIDATION=incorporar el patrón al diseño del piloto B2B IA y verificar que cada paso reduzca una fricción real de BP-003/BP-004.
ROLLBACK_OR_STOP=no publicar métricas/proof que Capacita no pueda demostrar; no crear una ruta multcurso sólo para parecerse al referente.
```

---

## 6. COMPETITOR_PROFILE — Transversal OTEC

### FACT

- Su página de servicios separa mercado privado, licitaciones/grandes compras, desarrollo organizacional, mercado público y autoinstrucción.
- Declara explícitamente `Detección de necesidades de capacitación [DNC] y Evaluaciones de desempeño`.
- Publica empresas capacitadas como prueba social.
- En 2026 aparece repetidamente como interesado en requerimientos corporativos públicos de IA, IA Expert, Copilot y un paquete IA + Google Workspace.
- La participación en esos requerimientos sólo prueba intención comercial/actividad, no venta ni adjudicación.

### INFERENCE

Transversal parece operar con una lógica de **captura rápida de demanda + DNC + programas cerrados/anuales**. Su valor de benchmark es la disciplina comercial y la amplitud de respuesta, no una superioridad demostrada del producto IA.

### VERIFY

```text
CONFIDENCE=HIGH para DNC/arquitectura de servicios; MEDIUM para interpretación de intensidad comercial
CORROBORATION=T1+T2+T3+T4+T5+T6
MATERIALITY=HIGH
```

### DECISION

```text
DECISION_CLASS=ACT
ACTION_TYPE=ADAPT_PRACTICE
ACTION=Incorporar DNC/levantamiento breve como componente del piloto B2B IA y mantener un radar de requerimientos públicos como señal de mercado, sin inferir ventas de competidores.
OWNER=Marketing
VALIDATION=el DNC debe producir una decisión accionable de capacitación/oferta; si no cambia la propuesta, simplificarlo.
ROLLBACK_OR_STOP=no construir una burocracia DNC extensa ni responder automáticamente a toda señal de mercado.
```

---

## 7. COMPETITOR_PROFILE — CIDES Corpotraining

### FACT

- CIDES publica `Inteligencia Artificial en la Pyme` (70 h asincrónico) con foco explícito en aplicación empresarial.
- Publica `Ventas con Inteligencia Artificial y Emocional` (16 h), disponible online/presencial e in-company.
- Publica `Uso de IA como Asistente de Mantenimiento` (16 h), también orientado a aplicación funcional.
- Publica cruces como Excel + IA + automatización.
- Su arquitectura de cursos permite cotización in-company y mantiene un catálogo amplio por áreas/modalidades.

### INFERENCE

CIDES está **verticalizando IA por función/problema** en vez de depender sólo de un curso general. Ese patrón puede aumentar relevancia B2B, pero no demuestra que Capacita deba crear múltiples cursos ahora.

### VERIFY

```text
CONFIDENCE=HIGH
CORROBORATION=C1+C2+C3+C4+C5
MATERIALITY=HIGH
```

### DECISION

```text
DECISION_CLASS=ACT
ACTION_TYPE=PORTFOLIO_REVIEW
ACTION=Revisar si el curso IA existente puede presentarse B2B mediante énfasis/casos de uso por rol o área, sin crear cursos separados ni alterar el currículo canónico en esta fase.
OWNER=Marketing
DEPENDENCY=GTM/RevOps para buyer/propuesta; Diseño de Cursos si una futura variante curricular se justifica.
VALIDATION=identificar 2–3 casos de uso recurrentes de BP-003/BP-004 y comprobar demanda/capacidad antes de cualquier nueva variante.
ROLLBACK_OR_STOP=NO crear catálogo de IA por función sin evidencia suficiente y ownership curricular.
```

---

## 8. Matriz común IA/B2B

| Dimensión | Kibernum | Edutecno | Transversal | CIDES | Lectura para Capacita |
|---|---|---|---|---|---|
| Entrada B2B | Conversación/diagnóstico y adopción IA | Test madurez + demo | DNC + divisiones comerciales | Curso/cotización in-company | **Gap visible:** Capacita necesita una entrada B2B explícita distinta de la landing B2C. |
| Forma de oferta IA | Portfolio adopción + capacitación + proyectos | Cursos/rutas + transformación digital | Respuesta amplia a demanda + DNC | Cursos IA verticalizados | No copiar amplitud; pilotear una arquitectura mínima. |
| Personalización | Alta | Alta/desarrollos a medida | Alta/DNC/programas | Alta/in-company | B2B requiere personalización proporcional, no curso genérico como única entrada. |
| Prueba social | Casos, partners, clientes | Clientes + claims propios | Empresas capacitadas | Certificaciones, facilitadores, testimonios/ejecuciones | Capacita debe usar sólo proof verificable propio. |
| Enfoque buyer | Empresa/adopción | Empresa/desarrollo capital humano | Empresa/mercado público-privado | Profesionales + empresas por función | BP-003/BP-004 requieren mensajes y CTA propios. |
| SENCE/operación | Academy/corporativo | OTEC/capacitación empresarial | SENCE explícito | SENCE/in-company explícito | SENCE sólo si corresponde y está confirmado; no usar como claim B2C. |
| Señal diferencial reusable | Adoption journey | Assessment + ruta | DNC + market responsiveness | Verticalización por función | Componer las cuatro señales, no elegir un competidor para copiar. |

---

## 9. Señales repetidas / interpretación V03

### Señal R1 — diagnóstico antes de capacitación

Se observa en:

- Kibernum: `AI Fast Scope` con diagnóstico consultivo;
- Edutecno: test de madurez digital;
- Transversal: DNC formal.

```text
EVENT=REPEATED_TREND_ACROSS_COMPETITORS
FACT=3 de 4 core publican algún mecanismo explícito de diagnóstico/assessment/DNC antes o alrededor de la solución empresarial.
INFERENCE=la venta B2B madura compite en definición del problema, no sólo en horas/temario.
CONFIDENCE=HIGH
MATERIALITY=HIGH
DECISION_CLASS=ACT
ACTION_TYPE=PILOT
```

### Señal R2 — IA contextualizada al trabajo/función

- Kibernum: productividad/adopción/casos de uso.
- CIDES: PyME, ventas, mantenimiento, Excel+IA.
- Requerimientos públicos 2026: IA general, Copilot y combinaciones IA + herramientas de productividad.

```text
EVENT=REPEATED_TREND_ACROSS_COMPETITORS
INFERENCE=crece el valor de empaquetar IA por problema/rol/herramienta, pero no hay evidencia para multiplicar cursos de inmediato.
DECISION_CLASS=ACT
ACTION_TYPE=PORTFOLIO_REVIEW
```

### Señal R3 — evidencia de empresa y reducción de riesgo

Los cuatro core publican, en distintos grados, clientes, casos, certificaciones, partners, modalidad in-company o prueba social.

```text
DECISION_CLASS=ACT
ACTION_TYPE=UPDATE_SALES_ENABLEMENT
ACTION=preparar un inventario de proof B2B verificable de Capacita y, sólo con evidencia existente, usarlo en una futura pieza corporativa.
STOP=no inventar logos, resultados, métricas ni certificaciones.
```

---

## 10. Decisiones `ACT / NO_ACTION`

### ACT-01 — Pilotear un diagnóstico B2B IA mínimo

**Decisión:** `ACT / PILOT`.

Patrón propuesto, no producto definitivo:

```text
NECESIDAD/ROL
-> tareas y fricciones
-> nivel/adopción actual
-> 2-3 casos de uso prioritarios
-> riesgos/datos/privacidad
-> recomendación de modalidad/ruta
-> cotización/propuesta
```

No debe transformarse en consultoría técnica profunda. Su objetivo es mejorar la definición de la capacitación y la propuesta comercial.

### ACT-02 — Ejecutar `OFFER_REVIEW` B2B del curso IA existente

**Decisión:** `ACT / ADAPT_PRACTICE`.

Revisar qué componentes ya puede prometer Capacita de forma verificable para empresa:

- formato cerrado/in-company;
- modalidad y fechas;
- número de participantes;
- adaptación de ejemplos/casos;
- asistencia/evaluación/reportes;
- SENCE cuando corresponda y esté confirmado;
- contacto/cotización;
- proof/casos verificables.

Este F2 **no afirma** que todos estos componentes existan hoy. El offer review debe separar `AVAILABLE / NEEDS_CONFIRMATION / NOT_AVAILABLE` antes de publicar.

### ACT-03 — Portfolio review de verticalización ligera

**Decisión:** `ACT / PORTFOLIO_REVIEW`.

Evaluar si B2B puede comunicar el mismo curso IA con casos de uso/énfasis por área —por ejemplo administración/productividad, liderazgo/gestión o datos/Office— antes de crear nuevas variantes curriculares.

### ACT-04 — Sales enablement B2B basado en evidencia

**Decisión:** `ACT / UPDATE_SALES_ENABLEMENT`.

Después del offer review, preparar una pieza interna de venta/cotización que responda a BP-003/BP-004: problema, solución, modalidad, coordinación, evidencia, next step. No publicar hasta validar cada claim.

### NO_ACTION-01 — No cambiar el curso B2C/presencial IA por este benchmark

```text
NO_ACTION=mantener 16 h, CLP 169000, Presencial Santiago, Básico-Intermedio, sin programación y herramientas principales ya definidas.
RATIONALE=el F2 estudia B2B; no apareció evidencia que invalide el baseline de PR #67/#68.
```

### NO_ACTION-02 — No ampliar por reflejo a agentes, RAG, ML, Python, n8n/Make o consultoría de implementación

Los competidores con servicios más amplios tienen capacidades/ownership distintos. Capacita no debe convertir un benchmark B2B en expansión curricular o técnica sin Diseño de Cursos + evidencia + capacidad operativa.

### NO_ACTION-03 — No copiar precios ni usar precio competidor como target

No se hizo benchmark de precio profundo porque el modelo V03 exige comparar inclusiones, buyer, valor y economía interna antes de modificar oferta. `PRICE_CHANGE=NO_ACTION`.

### NO_ACTION-04 — No crear hoy un catálogo de múltiples cursos IA por función

CIDES aporta una señal válida de verticalización, pero una sola señal de oferta no justifica deuda de portafolio. Primero `PORTFOLIO_REVIEW` y evidencia.

---

## 11. OPPORTUNITY_BACKLOG

| Prioridad | Oportunidad | Acción V03 | Owner | Dependencias / Gate | Validación futura |
|---|---|---|---|---|---|
| P0 | Diagnóstico B2B IA mínimo / mapa de oportunidades | `PILOT` | Marketing | GTM/RevOps para buyer/VP; oportunidad B2B autorizada para prueba real | ¿Mejora definición de necesidad y calidad de propuesta sin fricción excesiva? |
| P0 | Offer review empresa del curso IA vigente | `ADAPT_PRACTICE` | Marketing | Confirmación operación/SENCE/reportes antes de claims | Matriz `AVAILABLE/NEEDS_CONFIRMATION/NOT_AVAILABLE`. |
| P1 | Casos de uso por rol/área sin nueva malla | `PORTFOLIO_REVIEW` | Marketing | GTM + Diseño de Cursos sólo si deriva en variante | Evidencia de recurrencia en demanda y capacidad. |
| P1 | Pieza interna de sales enablement IA empresa | `UPDATE_SALES_ENABLEMENT` | Marketing | Offer review + proof verificable | Uso en cotización/pipeline bajo gate posterior. |
| P1 | Radar de requerimientos públicos IA/Copilot/productividad | `WATCH` | Marketing | Automatización/scheduling fuera de este F2 | Señales útiles vs ruido; no inferir venta. |
| P2 | Partnerships/certificaciones IA | `PARTNERSHIP_REVIEW` | Marketing/Portfolio | costo, contrato, ownership externo | Sólo si aporta diferenciación/credibilidad verificable. |

---

## 12. EXPERIMENT_CARD — diagnóstico B2B IA mínimo

Estado: `PROPOSED / NOT_EXECUTED`.

```text
HYPOTHESIS=Un diagnóstico breve previo a cotizar IA para empresa mejora el encaje entre necesidad, buyer, modalidad y propuesta sin convertir Capacita en consultora tecnológica.
PRIMARY_BUYER=BP-003 v1.0.0
SECONDARY_BUYER=BP-004 v1.0.0
CHANGE=usar un cuestionario/guion breve en una oportunidad B2B autorizada antes de cotizar.
CONTROL=flujo actual de cotización sin diagnóstico estructurado, si existe evidencia comparable.
SUCCESS_SIGNAL=mejor definición de casos de uso/participantes/modalidad y menor retrabajo comercial; métricas de conversión sólo con datos autorizados posteriores.
GUARDRAIL=no prometer implementación IA; no recolectar datos sensibles innecesarios; no copiar assessment de competidor.
STOP=si el diagnóstico alarga el ciclo sin cambiar la propuesta o genera expectativas de consultoría fuera de alcance.
```

---

## 13. Measure — estado de esta primera pasada

```text
FOUR_CORE_REVIEWED=4/4
MATERIAL_REPEATED_SIGNALS=3
PAID_API_COST=0
PRIVATE_DATA_USED=NO
FALSE_POSITIVE_RATE=NOT_APPLICABLE_NO_AUTOMATED_WATCHER
WIN_LOSS_EVIDENCE=NOT_USED_NOT_AUTHORIZED
REVENUE_CAUSALITY_CLAIMED=NO
```

La efectividad comercial de las acciones propuestas **no** puede medirse en este F2 documental. Requiere pilotos y datos autorizados posteriores.

---

## 14. Feedback reusable para AI OS

### FDBK-01 — V03 funcionó sin mega-suite

`APLICAR`: el flujo `BASELINE -> SENSE -> VERIFY -> INTERPRET -> DECIDE -> ACT` fue suficiente para convertir evidencia pública en decisiones sin ejecutar toda la suite ni usar APIs pagadas. `CREAR_INTERNA=NO` sigue siendo correcto.

### FDBK-02 — agregar wrapper simple `ACT/NO_ACTION`

`PROPONER`: mantener la taxonomía rica (`PILOT`, `WATCH`, etc.), pero sumar dos campos de cierre:

```text
DECISION_CLASS=ACT|NO_ACTION
ACTION_TYPE=<taxonomía V03>
```

Esto hace más evidente el gate ejecutivo sin perder detalle.

### FDBK-03 — distinguir fuente primaria de señal de mercado secundaria

`PROPONER`: agregar en `VERIFY`:

```text
SOURCE_TYPE=PRIMARY|SECONDARY|INTERNAL_AUTHORIZED
SOURCE_ROLE=OFFER_EVIDENCE|DEMAND_SIGNAL|PROOF|CORROBORATION
```

En este F2, REDCAPACITACION fue útil como `DEMAND_SIGNAL`, pero no debe interpretarse como venta/adjudicación.

### FDBK-04 — dimensión específica para servicios B2B

`PROPONER`: en empresas de capacitación/servicios, incorporar al perfil cuando aplique:

`ENTRY_MECHANISM | DNC/ASSESSMENT | CUSTOMIZATION | IN_COMPANY | DELIVERY_EVIDENCE | REPORTING | SENCE/COMPLIANCE | PROOF`.

Estos campos resultaron más decisivos que una matriz SaaS de features.

### FDBK-05 — regla de repetición aumenta materialidad, no autoriza acción automática

`PROPONER`: cuando una práctica aparece en `2+` core, o en un core + una fuente independiente de demanda, elevar `MATERIALITY` para revisión. La repetición **no** debe disparar `PILOT` automáticamente; todavía exige buyer fit, capacidad y diferenciación.

---

## 15. DoD / cierre F2

```text
FOUR_CORE_COMPARED=YES
EXISTING_IA_BASELINE_REUSED=YES
FACT_INFERENCE_SEPARATED=YES
DECISION_SUPPORTED=YES
ACTION_OR_NO_ACTION_EXPLICIT=YES
OWNER_EVIDENCE_PRESENT=YES
NO_PRIVATE_METRICS_INVENTED=YES
NO_COPYING_PROPRIETARY_ASSETS=YES
SOURCE_MANIFEST=YES
OPPORTUNITY_BACKLOG=YES
FEEDBACK_PREPARED=YES
SEM_RUSH_USED=NO
KEYWORD_PLANNER_USED=NO
ADS_API_USED=NO
CRM_USED=NO
PRODUCTION_CHANGES=0
```

## 16. Conclusión ejecutiva

El F2 **no justifica cambiar la oferta IA presencial vigente**. Sí justifica una línea B2B distinta y reversible: **pilotear un diagnóstico/levantamiento breve antes de cotizar**, revisar el packaging empresa del curso actual y evaluar verticalización ligera por casos de uso antes de crear nuevos cursos.

La evidencia más fuerte no es “un competidor tiene un curso que debemos copiar”, sino un patrón común: los referentes B2B maduros reducen incertidumbre antes de vender, personalizan la solución y muestran proof/operación empresarial. Capacita puede adaptar ese patrón con menor complejidad y sin abandonar su diferenciador actual de capacitación práctica y accesible.
