# Brief BP-004 — Dueño o Jefatura PyME

Fecha: 2026-07-10  
Versión del brief: 1.0.0  
Estado: listo documentalmente; activación condicionada a oferta y ruta B2B  
Campaign ID recomendado: `B2B_LEAD_EXCEL_PYME_BP004_V1`

## 1. Baseline canónico

```yaml
canonical_baseline:
  buyer_persona:
    id: BP-004
    name: Dueño o Jefatura PyME
    version: 1.0.0
    role: primary
    evidence_maturity: hypothesis
  value_propositions:
    - document: VALUE_PROPOSITIONS.md
      section: C) Productividad laboral y seguridad operativa
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: F) Medición de aprendizaje en tres fases
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: G) Propuesta B2B: Capacitación para equipos
      version: 0.2.1
  journey_stage:
    document: CUSTOMER_JOURNEY.md
    section: 1. Visitante / audiencia fría
    version: 0.2
  expected_transition:
    document: CUSTOMER_JOURNEY.md
    section: 3. Lead identificado
    version: 0.2
  source_date: 2026-07-10
```

## 2. Objetivo

Captar conversaciones comerciales con dueños, gerentes o jefaturas de pequeñas y medianas empresas que buscan resolver problemas concretos de productividad, errores, dependencia de pocas personas o uso insuficiente de Excel en sus equipos.

Objetivo de negocio: lead B2B decisor o patrocinador con problema operativo, cantidad aproximada de participantes, urgencia y disposición a evaluar una solución.

## 3. Problema concreto

- El equipo pierde tiempo en tareas manuales y reportes repetitivos.
- Hay errores o criterios distintos entre personas.
- El conocimiento está concentrado en uno o dos colaboradores.
- Se compran herramientas, pero no siempre se usan correctamente.
- Necesita una solución práctica y justificable, no capacitación genérica.

No asumir presupuesto, tamaño de empresa o autoridad final por cargo declarado.

## 4. Hipótesis táctica

Si el mensaje presenta la capacitación como una intervención práctica sobre problemas operativos concretos, en vez de una actividad formativa genérica, aumentarán las conversaciones con decisores que buscan impacto y tienen capacidad de impulsar una compra.

Variable principal del test: impacto operativo y reducción de dependencia o errores.

## 5. Promesa táctica

**Fortalece el uso de Excel en tu equipo con una capacitación práctica orientada a los procesos y tareas que hoy consumen tiempo o generan errores.**

No garantizar porcentajes de ahorro, ROI, reducción de errores o resultados financieros.

## 6. Arquitectura de mensaje

### Dolor principal

“Tu empresa depende de planillas críticas, pero el equipo trabaja con métodos distintos, tareas manuales y conocimiento concentrado.”

### Transformación esperada

Pasar de una necesidad difusa de “capacitar en Excel” a una propuesta alineada con tareas, nivel del equipo y objetivos operativos.

### Soporte de credibilidad

- levantamiento inicial de necesidad, si se ofrece;
- nivel y temario definidos;
- práctica aplicada;
- alternativas de modalidad;
- evaluación y seguimiento, solo cuando correspondan;
- propuesta formal con alcance y condiciones.

### CTA principal

`Evaluar capacitación para mi equipo`

### CTA secundario

`Solicitar una propuesta`

## 7. Rutas creativas iniciales

### Ruta A — Tiempo operativo

**Hook:** ¿Cuántas horas pierde tu equipo cada mes repitiendo tareas manuales en Excel?

**Texto base:** Evalúa una capacitación práctica para fortalecer reportes, bases de datos y tareas frecuentes de tu equipo. Cuéntanos el problema y preparamos una alternativa.

**Título:** Mejora el uso de Excel en tu empresa

El hook es una pregunta, no una afirmación cuantificada.

### Ruta B — Dependencia

**Hook:** Si solo una persona domina las planillas críticas, existe un riesgo operativo.

**Texto base:** Estandariza conocimientos y fortalece la autonomía del equipo con una capacitación de Excel ajustada al nivel y necesidad de la empresa.

**Título:** Reduce la dependencia de pocas personas

### Ruta C — Errores y estandarización

**Hook:** Distintas formas de trabajar pueden producir reportes distintos con los mismos datos.

**Texto base:** Consulta por una capacitación práctica orientada a criterios comunes, orden de información y uso más seguro de Excel.

**Título:** Estandariza el trabajo con Excel

Las rutas deben validarse contra el alcance real del curso y no prometer consultoría de procesos si solo se vende capacitación.

## 8. Público y targeting táctico

| Dimensión | Decisión inicial | Estado |
|---|---|---|
| Alcance | B2B decisor, patrocinador o jefatura | Definido |
| Problema | Productividad, errores, dependencia, estandarización | Señal principal |
| Tamaño de grupo | Grupo pequeño o mediano, por confirmar | Preguntar |
| Urgencia | Necesidad concreta y horizonte de implementación | Preguntar |
| Canal | Google Search, LinkedIn, remarketing B2B o contacto comercial | Hipótesis |
| Exclusión conceptual | Coordinador que solo reúne antecedentes | Puede derivar a `BP-003` |
| Atributos sensibles | No usar | Prohibido |

No usar facturación, cargo aparente o dominio de correo como inferencia automática de presupuesto.

## 9. Destino y conversación comercial

El destino debe invitar a describir el problema, no solo a descargar un temario genérico.

Campos mínimos:

- nombre y empresa;
- correo y teléfono;
- rol en la decisión;
- cantidad aproximada de participantes;
- tareas o problemas que busca mejorar;
- nivel estimado del equipo;
- modalidad y fecha objetivo;
- consentimiento para contacto.

Siguiente acción recomendada: contacto comercial breve para validar necesidad antes de emitir propuesta.

## 10. Claims

| Claim | Estado |
|---|---|
| Capacitación práctica para equipos | Permitido si existe oferta B2B. |
| Orientación a tareas frecuentes | Permitido si el temario puede alinearse. |
| Estandarización de conocimientos | Permitido como objetivo, no como resultado garantizado. |
| Evaluación inicial/final | Confirmar por propuesta. |
| Seguimiento posterior | Confirmar alcance. |
| Ahorro o ROI específico | Prohibido sin estudio y evidencia. |
| Eliminar errores | Prohibido. |
| Consultoría de procesos incluida | Prohibido salvo contratación explícita. |
| Capacitación totalmente personalizada | Confirmar capacidad, horas y precio. |

## 11. Medición

| Etapa | Métrica prioritaria | Fuente |
|---|---|---|
| Exposición | impresiones y clics B2B | Ads |
| Acción | solicitud con problema descrito | Landing / formulario |
| Calidad | decisor/patrocinador, grupo y urgencia identificados | CRM / ventas |
| Avance | reunión diagnóstica y propuesta emitida | CRM |
| Resultado | deal ganado, OC o matrícula grupal | CRM / operación |

Medir valor potencial, tasa de propuesta y cierre; no optimizar solamente por formularios baratos.

## 12. Datos pendientes antes de activar

- alcance real de personalización;
- oferta para grupos y modalidades;
- precio o método de cotización;
- capacidad de diagnóstico inicial;
- entregables de evaluación y seguimiento;
- landing y formulario B2B;
- SLA de contacto;
- pipeline y etapas de Zoho;
- UTM y atribución hacia deal.

## 13. Definition of Done

- [x] Buyer persona, hipótesis y baseline registrados.
- [x] Mensaje de impacto operativo separado del coordinador B2B.
- [x] CTA, rutas creativas y formulario propuestos.
- [x] Claims y límites visibles.
- [x] Medición orientada a oportunidad/deal.
- [ ] Oferta B2B y personalización confirmadas.
- [ ] Landing/formulario verificados.
- [ ] Ruta CRM y responsable comercial definidos.
- [ ] Creatividad revisada.
- [ ] Autorización de activación real.

## 14. Aprendizaje hacia GTM

Como `BP-004` está en madurez `hypothesis`, registrar:

- problema operativo declarado;
- rol y autoridad real;
- tamaño del equipo;
- urgencia y criterios de decisión;
- objeciones de costo/tiempo;
- tasa de reunión, propuesta y cierre;
- diferencias observadas respecto de `BP-003`.

La evidencia repetida debe volver a Global antes de cambiar el perfil corporativo.
