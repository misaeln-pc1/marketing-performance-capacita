# Baseline GTM — Excel Presencial Santiago V3

Fecha: 2026-07-10  
Versión del baseline local: 1.0.0  
Campaña asociada: `META_TRAFFIC_EXCEL_PRESENCIAL_SANTIAGO_B2C_V3`  
Documento operativo: `meta-ads-landing-traffic-v3.md`  
Estado: aplicación documental; no modifica Meta Ads ni producción

## Baseline canónico

```yaml
canonical_baseline:
  buyer_personas:
    - id: BP-001
      version: 1.0.0
      role: primary
    - id: BP-002
      version: 1.0.0
      role: secondary
  value_propositions:
    - document: VALUE_PROPOSITIONS.md
      section: A) Capacitación práctica y guiada
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: B) Experiencia presencial confiable en ubicación céntrica
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: E) Recursos incluidos y cero fricción logística
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: C) Productividad laboral y seguridad operativa
      version: 0.2.1
    - document: VALUE_PROPOSITIONS.md
      section: D) Empleabilidad / reinserción laboral
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

Fuentes: `misaeln-pc1/capacita-global-control/docs/gtm-revops/`.

## Aplicación local

```yaml
local_application:
  objective: filtrar tráfico pagado y aumentar la intención comercial posterior
  audience_scope: B2C
  channel: Meta Ads hacia landing
  tactical_hypothesis: informar que el curso es pagado y mostrar precio/fechas antes del contacto reducirá volumen pero aumentará calidad
  primary_cta: Cotizar
  landing_or_destination: curso de Excel presencial en Santiago
  owner_repo: misaeln-pc1/marketing-performance-capacita
```

## Lectura por buyer persona

### `BP-001 — Desbordado Operativo`

Dolor aplicable:

- lentitud y errores en el trabajo;
- necesidad de práctica inmediata;
- búsqueda de acompañamiento presencial y resolución de dudas.

Propuestas más relevantes:

- A) capacitación práctica y guiada;
- C) productividad laboral y seguridad operativa;
- E) recursos incluidos y menor fricción logística.

### `BP-002 — Reinserción Laboral`

Dolor aplicable:

- necesidad de actualizar competencias;
- inseguridad respecto del nivel;
- búsqueda de certificado y ruta de aprendizaje confiable.

Propuestas más relevantes:

- A) capacitación práctica y guiada;
- B) experiencia presencial confiable;
- D) empleabilidad / reinserción laboral.

## Hallazgo del piloto documental

La pieza V3 existente combina ambos perfiles con un copy general sobre experiencia presencial, fechas y valor. Esto permite una campaña amplia, pero dificulta saber qué dolor genera la conversión.

Para próximos tests:

- mantener la campaña V3 como antecedente histórico;
- crear variantes diferenciadas, sin reescribir resultados anteriores:
  - variante productividad para `BP-001`;
  - variante empleabilidad para `BP-002`;
- conservar la misma oferta y landing cuando se quiera aislar el efecto del mensaje;
- no declarar una variante ganadora sin datos de calidad comercial posterior.

## Claims y datos tácticos

| Elemento | Estado |
|---|---|
| Curso presencial pagado | Debe confirmarse en oferta vigente antes de publicar. |
| Santiago Centro | Verificar dirección/ruta vigente en landing. |
| Profesor en vivo y práctica guiada | Permitido si corresponde al curso ofertado. |
| Computador individual | Confirmar disponibilidad y condiciones vigentes. |
| Materiales, diploma y evaluaciones | Confirmar qué aplica exactamente al curso. |
| Fechas, valor, cupos y pago | Datos tácticos; no pertenecen al canónico permanente. |
| Empleabilidad garantizada | Prohibido. |
| Resultado laboral o salarial garantizado | Prohibido. |

## Medición mínima

| Etapa | Métrica | Fuente esperada |
|---|---|---|
| Exposición | alcance, impresiones, frecuencia | Meta Ads |
| Interés | clic y visita a landing | Meta Ads / analítica web |
| Acción | clic interno, formulario o WhatsApp iniciado | Edge / analítica |
| Calidad | lead contactable y respuesta | Zoho CRM / ventas |
| Conversión | cotización, inscripción y matrícula | Zoho CRM / operación |

La V3 no debe evaluarse solo por clics. La hipótesis exige observar calidad, respuesta y conversión posterior.

## Aprendizaje hacia GTM

Todavía no existe evidencia suficiente para cambiar `BP-001` o `BP-002`.

Evidencia futura útil:

- tasa de lead contactable por variante;
- respuesta comercial por perfil/mensaje;
- costo por lead calificado;
- cotización y matrícula;
- objeciones repetidas;
- porcentaje de leads que no encajan y deberían quedar en `BP-000`.

Cualquier propuesta de cambio al canónico debe indicar ID, versión, evidencia agregada e issue en Global.

## Límites

- No cambia Meta Ads, presupuesto, anuncios o targeting real.
- No modifica landing, Cloudflare, Zoho, formularios o automatizaciones.
- No contiene datos personales ni métricas reales no verificadas.
- No redefine buyer personas; documenta una aplicación local.