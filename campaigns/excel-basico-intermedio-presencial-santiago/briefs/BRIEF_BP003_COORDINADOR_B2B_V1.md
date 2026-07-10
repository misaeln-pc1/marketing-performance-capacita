# Brief BP-003 — Coordinador B2B

Fecha: 2026-07-10  
Versión del brief: 1.0.0  
Estado: listo documentalmente; activación condicionada a oferta y ruta B2B  
Campaign ID recomendado: `B2B_LEAD_EXCEL_EQUIPOS_BP003_V1`

## 1. Baseline canónico

```yaml
canonical_baseline:
  buyer_persona:
    id: BP-003
    name: Coordinador B2B
    version: 1.0.0
    role: primary
    evidence_maturity: hypothesis
  value_propositions:
    - document: VALUE_PROPOSITIONS.md
      section: A) Capacitación práctica y guiada
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

Captar solicitudes de información o cotización de personas que coordinan capacitación para equipos y necesitan comparar proveedores, reunir antecedentes, resolver logística y presentar una alternativa internamente.

Objetivo de negocio: solicitud B2B identificada con empresa, cantidad aproximada de participantes, necesidad, modalidad y horizonte de fecha.

## 3. Problema concreto

- Debe cotizar y comparar alternativas con información incompleta.
- Necesita temario, duración, modalidad, valores y condiciones claras.
- Debe coordinar fechas, participantes, asistencia y comunicaciones.
- Requiere evidencia para justificar la compra o reportar resultados.
- Puede influir en la decisión, pero no necesariamente autorizar presupuesto.

No asumir autoridad final de compra por cargo, dominio de correo o canal de contacto.

## 4. Hipótesis táctica

Si la campaña ofrece una ruta de cotización clara y reduce la carga administrativa del coordinador, aumentarán las solicitudes B2B completas y disminuirán los intercambios necesarios para obtener información básica.

Variable principal del test: baja fricción para coordinar y justificar una capacitación de equipo.

## 5. Promesa táctica

**Coordina una capacitación práctica de Excel para tu equipo con información clara, opciones de modalidad y una propuesta formal según la necesidad de la empresa.**

No prometer reportes, SENCE, evaluaciones o personalización que no estén confirmados para la oferta específica.

## 6. Arquitectura de mensaje

### Dolor principal

“Necesitas presentar una alternativa de capacitación, pero reunir temario, fechas, costos y condiciones te toma demasiado tiempo.”

### Transformación esperada

Pasar de una búsqueda dispersa a una conversación B2B estructurada con antecedentes suficientes para evaluar y coordinar.

### Soporte de credibilidad

- propuesta formal;
- temario y duración;
- modalidad presencial, sincrónica o alternativa aplicable;
- coordinación de fechas;
- asistencia, evaluaciones o informes únicamente cuando estén incluidos;
- experiencia OTEC y procesos aplicables, sin exagerar acreditaciones.

### CTA principal

`Solicitar cotización para mi equipo`

### CTA secundario

`Revisar alternativas para empresas`

## 7. Rutas creativas iniciales

### Ruta A — Cotización completa

**Hook:** ¿Necesitas cotizar un curso de Excel para tu equipo y presentar una propuesta interna?

**Texto base:** Cuéntanos cuántas personas participan, qué necesitan aprender y en qué fecha. Preparamos una alternativa con modalidad, temario y condiciones aplicables.

**Título:** Capacitación de Excel para equipos

### Ruta B — Coordinación simple

**Hook:** Menos correos para coordinar una capacitación.

**Texto base:** Centraliza programa, fechas, participantes y requerimientos en una sola solicitud de cotización para empresas.

**Título:** Coordina tu curso de empresa

### Ruta C — Evidencia y seguimiento

**Hook:** Capacitar no termina cuando finaliza la clase.

**Texto base:** Consulta por las alternativas de evaluación, asistencia y seguimiento disponibles para tu programa de Excel.

**Título:** Capacitación con trazabilidad

La Ruta C solo puede publicarse si los entregables están definidos y operativos.

## 8. Público y targeting táctico

| Dimensión | Decisión inicial | Estado |
|---|---|---|
| Alcance | B2B comprador/coordinador para terceros | Definido |
| Rol declarado | RRHH, capacitación, administración, operaciones, coordinación | Señal, no targeting rígido |
| Tamaño de grupo | 2-5 / 6-15 / 16+ / no definido | Preguntar en formulario |
| Necesidad | Productividad, estandarización, errores, adopción tecnológica | Preguntar |
| Canal | Google Search, LinkedIn o campañas B2B separadas | Hipótesis; evaluar costo |
| Exclusión conceptual | Compra individual | Derivar a `BP-001` o `BP-002` |
| Atributos sensibles | No usar | Prohibido |

Un correo corporativo por sí solo no clasifica a una persona como B2B.

## 9. Formulario y destino B2B

El destino debe estar separado de la landing B2C o mostrar una ruta empresarial inequívoca.

Campos mínimos recomendados:

- nombre;
- empresa;
- correo y teléfono;
- cantidad aproximada de participantes;
- curso/área;
- modalidad preferida;
- fecha objetivo;
- problema que busca resolver;
- rol en la decisión;
- consentimiento para contacto.

No solicitar RUT, datos sensibles o antecedentes innecesarios en la etapa inicial.

## 10. Claims

| Claim | Estado |
|---|---|
| Cotización para equipos | Permitido si existe proceso de respuesta. |
| Modalidad adaptable | Confirmar opciones reales. |
| Temario personalizado | Solo si existe capacidad y alcance definidos. |
| Control de asistencia | Confirmar entregable. |
| Evaluación inicial/final o seguimiento | Confirmar por programa. |
| Uso SENCE | Confirmar curso, condiciones y proceso antes de mencionar. |
| Mejora garantizada de productividad | Prohibido. |
| Cumplimiento total o ROI asegurado | Prohibido. |

## 11. Medición

| Etapa | Métrica prioritaria | Fuente |
|---|---|---|
| Exposición | impresiones/clics B2B | Ads |
| Acción | formulario B2B completo | Landing / formulario |
| Calidad | empresa, grupo, necesidad y fecha identificados | CRM / ventas |
| Avance | reunión, propuesta o cotización emitida | CRM |
| Resultado | deal ganado / orden de compra / matrícula grupal | CRM / operación |

No comparar CPL B2B directamente con CPL B2C sin considerar valor potencial y ciclo de venta.

## 12. Datos pendientes antes de activar

- landing o ruta B2B definitiva;
- SLA de respuesta comercial;
- modalidades y tamaños de grupo atendibles;
- esquema de precios/cotización;
- entregables de asistencia/evaluación;
- condiciones SENCE, si aplica;
- campos CRM y propietario del lead;
- UTM y trazabilidad de deal.

## 13. Definition of Done

- [x] Buyer persona, hipótesis y baseline registrados.
- [x] Mensaje, CTA y rutas creativas preparados.
- [x] Formulario mínimo propuesto.
- [x] Medición B2B separada de B2C.
- [ ] Oferta grupal validada.
- [ ] Landing/formulario B2B verificados.
- [ ] SLA y ruta CRM definidos.
- [ ] Creatividad revisada.
- [ ] Autorización de activación real.

## 14. Aprendizaje hacia GTM

Como `BP-003` está en madurez `hypothesis`, registrar especialmente:

- rol real de quienes consultan;
- información que necesitan para avanzar;
- tamaño de grupo;
- objeciones internas;
- tiempo hasta cotización;
- tasa de respuesta a propuestas;
- diferencias entre coordinador e influenciador sin poder de decisión.

La evidencia agregada debe volver a Global antes de promover la madurez del perfil.
