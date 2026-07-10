# Brief BP-001 — Desbordado Operativo

Fecha: 2026-07-10  
Versión del brief: 1.0.0  
Estado: listo para desarrollo creativo; activación pendiente de validaciones tácticas  
Campaign ID recomendado: `META_TRAFFIC_EXCEL_PRESENCIAL_BP001_V1`

## 1. Baseline canónico

```yaml
canonical_baseline:
  buyer_persona:
    id: BP-001
    name: Desbordado Operativo
    version: 1.0.0
    role: primary
  value_propositions:
    - document: VALUE_PROPOSITIONS.md
      section: A) Capacitación práctica y guiada
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: C) Productividad laboral y seguridad operativa
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: E) Recursos incluidos y cero fricción logística
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

Captar consultas y cotizaciones de personas que usan Excel en su trabajo actual y necesitan reducir lentitud, errores, tareas repetitivas o inseguridad al preparar reportes y planillas.

Objetivo de negocio: lead contactable con intención de revisar fecha, valor o inscripción.

## 3. Problema concreto

- Pierde demasiado tiempo ordenando planillas o repitiendo tareas.
- Teme cometer errores en fórmulas, reportes o bases de datos.
- Depende de compañeros para resolver operaciones frecuentes.
- Ha aprendido de forma fragmentada y necesita práctica guiada.
- No busca teoría extensa: busca aplicar Excel en situaciones laborales.

No asumir cargo, empresa, edad o nivel técnico por la sola interacción con un anuncio.

## 4. Hipótesis táctica

Si el mensaje conecta Excel con problemas cotidianos de productividad y muestra una experiencia presencial práctica, el público con necesidad inmediata tendrá mayor probabilidad de visitar la landing, solicitar información y responder al seguimiento comercial.

Variable principal del test: mensaje de productividad y reducción de errores.

## 5. Promesa táctica

**Aprende Excel de forma práctica para trabajar con más orden, rapidez y seguridad en tus planillas.**

La promesa no garantiza una cantidad específica de horas ahorradas ni ausencia total de errores.

## 6. Arquitectura de mensaje

### Dolor principal

“Excel te está haciendo perder tiempo y depender de otros para terminar tu trabajo.”

### Transformación esperada

Pasar de resolver planillas por ensayo y error a utilizar herramientas y métodos aplicables al trabajo cotidiano.

### Soporte de credibilidad

- profesor en vivo, cuando corresponda a la oferta vigente;
- ejercicios prácticos guiados;
- modalidad presencial en Santiago Centro;
- equipamiento y materiales, solo cuando estén confirmados;
- temario y nivel claramente informados.

### CTA principal

`Revisar fechas y valor`

### CTA comercial alternativo

`Cotizar mi cupo`

No utilizar simultáneamente varios CTA principales en la misma pieza.

## 7. Rutas creativas iniciales

### Ruta A — Tiempo perdido

**Hook:** ¿Cuánto tiempo pierdes cada semana ordenando planillas que deberían ser simples?

**Texto base:** Aprende Excel con práctica guiada y herramientas aplicables a tu trabajo. Revisa el programa, las fechas y el valor del curso presencial en Santiago Centro.

**Título:** Trabaja mejor con Excel

### Ruta B — Errores e inseguridad

**Hook:** Una fórmula mal aplicada puede convertir un reporte simple en horas de revisión.

**Texto base:** Fortalece tu manejo de Excel con ejercicios prácticos, acompañamiento en vivo y una ruta clara de aprendizaje.

**Título:** Más seguridad en tus planillas

### Ruta C — Dependencia

**Hook:** ¿Todavía necesitas pedir ayuda para terminar tus reportes en Excel?

**Texto base:** Aprende a resolver tareas frecuentes con mayor autonomía en un curso presencial y práctico.

**Título:** Gana autonomía con Excel

Estas rutas son borradores para creatividad. Deben pasar por revisión de oferta, claims y formato antes de publicación.

## 8. Público y targeting táctico

| Dimensión | Decisión inicial | Estado |
|---|---|---|
| Alcance | B2C y usuarios de empresa que compran individualmente | Hipótesis operativa |
| Geografía | Santiago / Región Metropolitana para modalidad presencial | Confirmar radio y cobertura |
| Interés | Excel, productividad, administración, reportes, análisis de datos básico | Hipótesis de plataforma |
| Intención | Aprender para trabajo actual, resolver problemas y actualizar manejo | Señal preferida |
| Exclusión conceptual | Consultas de capacitación para equipos | Derivar a `BP-003` o `BP-004` |
| Atributos sensibles | No usar edad, género, situación familiar u otros | Prohibido |

El targeting de plataforma no redefine la segmentación corporativa.

## 9. Destino y requisitos de landing

Destino esperado: landing de Excel presencial Santiago.

La landing debe confirmar antes del contacto:

- para quién es el curso;
- nivel y temario;
- modalidad presencial;
- ubicación;
- fechas;
- valor y pago;
- equipamiento/materiales aplicables;
- formulario o CTA funcionando.

La campaña no debe prometer elementos que la landing no respalde.

## 10. Claims

| Claim | Estado |
|---|---|
| Curso práctico y guiado | Permitido si corresponde a la metodología vigente. |
| Profesor en vivo | Confirmar para la edición ofertada. |
| Santiago Centro | Confirmar dirección y disponibilidad. |
| Computador individual | Confirmar antes de publicar. |
| Trabajar con más orden, rapidez y seguridad | Permitido como beneficio esperado, no como garantía cuantificada. |
| Ahorrar X horas por semana | Prohibido sin evidencia específica. |
| Eliminar todos los errores | Prohibido. |
| Ascenso o mejora salarial garantizada | Prohibido. |

## 11. Medición

| Etapa | Métrica prioritaria | Fuente |
|---|---|---|
| Exposición | alcance, frecuencia | Ads |
| Interés | visita a landing | Ads / analítica |
| Acción | CTA, formulario o WhatsApp iniciado | Edge / formulario |
| Calidad | lead contactable, respuesta | Zoho CRM / ventas |
| Resultado | cotización, inscripción, matrícula | CRM / operación |

Criterio inicial de aprendizaje: comparar calidad comercial, no únicamente CTR o CPC.

## 12. Datos pendientes antes de activar

- fecha exacta;
- precio y cuotas;
- cupos;
- temario/nivel ofertado;
- equipamiento y materiales incluidos;
- URL final y UTM;
- evento de formulario/WhatsApp;
- ruta de ingreso a Zoho.

## 13. Definition of Done

- [x] Buyer persona y versiones registrados.
- [x] Una hipótesis principal definida.
- [x] Promesa, CTA y rutas creativas preparadas.
- [x] Claims y prohibiciones visibles.
- [x] Métricas conectadas con calidad comercial.
- [ ] Datos tácticos confirmados.
- [ ] Creatividad producida y revisada.
- [ ] Landing y tracking validados.
- [ ] Autorización de activación real.

## 14. Aprendizaje hacia GTM

Registrar de forma agregada:

- dolor que generó más leads contactables;
- objeciones repetidas;
- tasa de respuesta;
- cotizaciones y matrículas;
- porcentaje que terminó clasificado como `BP-000` o `BP-002`;
- posibles señales nuevas que se repitan en más de una campaña.

No modificar `BP-001` desde Marketing. Proponer cambios mediante issue en Global con evidencia agregada.
