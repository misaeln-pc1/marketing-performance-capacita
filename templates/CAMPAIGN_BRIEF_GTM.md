# Plantilla de brief de campaña con baseline GTM

Estado: plantilla operativa v1.0.0  
Referencia: `docs/GTM_CONSUMPTION_BRIDGE.md`

## 1. Identificación

| Campo | Valor |
|---|---|
| Campaign ID |  |
| Nombre |  |
| Curso/oferta |  |
| Canal |  |
| Responsable |  |
| Estado | draft / approved / active / paused / closed |
| Fecha del brief |  |

## 2. Baseline canónico

```yaml
canonical_baseline:
  buyer_personas:
    - id: BP-000
      version: 1.0.0
      role: primary
  value_propositions:
    - document: VALUE_PROPOSITIONS.md
      section: SECCION_EXACTA
      version: 0.2.1
  journey_stage:
    document: CUSTOMER_JOURNEY.md
    section: SECCION_EXACTA
    version: 0.2
  segmentation:
    document: SEGMENTATION_RULES.md
    section: SECCION_EXACTA
    version: 0.1
  source_date: AAAA-MM-DD
```

Reglas:

- Usar ID y versión cuando existan.
- Si no existe ID, registrar documento, sección y versión.
- No inventar IDs ni redefinir el contenido canónico.
- Explicar por qué se selecciona cada buyer persona.

## 3. Aplicación local de Marketing

```yaml
local_application:
  objective: 
  audience_scope: B2C | B2B | MIXTO_APROBADO
  channel: 
  tactical_hypothesis: 
  primary_cta: 
  landing_or_destination: 
  owner_repo: misaeln-pc1/marketing-performance-capacita
```

### Problema concreto


### Mensaje o promesa táctica


### Diferencia respecto de campañas anteriores


## 4. Público y targeting táctico

| Dimensión | Decisión de campaña | Fuente o hipótesis |
|---|---|---|
| Ubicación |  |  |
| Curso/interés |  |  |
| Modalidad |  |  |
| Intención |  |  |
| Exclusiones |  |  |
| Plataforma/audiencia |  |  |

No convertir targeting de plataforma en nueva segmentación corporativa.

## 5. Propuesta, copy y CTA

### Propuestas canónicas seleccionadas


### Adaptación táctica


### CTA principal


### CTA secundario


### Claims permitidos y evidencia

| Claim | Evidencia | Estado |
|---|---|---|
|  |  | verificado / por confirmar / prohibido |

### Datos tácticos por confirmar

- precio;
- fechas;
- cupos;
- modalidad;
- dirección;
- medios de pago;
- condiciones comerciales.

## 6. Journey y destino

| Campo | Definición |
|---|---|
| Etapa inicial |  |
| Conversión esperada |  |
| Destino |  |
| Siguiente acción |  |
| Repo técnico involucrado |  |

## 7. Medición

| Métrica | Fuente | Criterio inicial |
|---|---|---|
| Alcance/impresiones | Plataforma Ads |  |
| Clic o visita | Plataforma/analítica |  |
| Lead | Landing/CRM |  |
| Lead contactable | CRM |  |
| Respuesta | CRM/ventas |  |
| Cotización/inscripción | CRM |  |
| Matrícula | CRM/operación |  |

No declarar éxito por clics si el objetivo real es lead, cotización o matrícula.

## 8. Riesgos y límites

- No datos personales en GitHub.
- No campañas, presupuesto ni plataforma real sin autorización.
- No modificación de landing productiva desde Marketing.
- No claims sin evidencia.
- No mezclar B2C y B2B sin decisión explícita.
- No usar atributos sensibles para clasificación.

## 9. Aprendizaje y retroalimentación

### Evidencia obtenida


### Hipótesis confirmada, rechazada o pendiente


### Posible impacto en el canónico GTM

- ID o documento afectado:
- versión:
- evidencia agregada:
- cambio propuesto:
- issue Global, si aplica:

## 10. Definition of Done

- [ ] Baseline canónico y versiones registrados.
- [ ] Hipótesis táctica separada del canónico.
- [ ] Público, copy, CTA y destino definidos.
- [ ] Claims verificables.
- [ ] Métricas conectadas al objetivo de negocio.
- [ ] Riesgos y datos pendientes visibles.
- [ ] Ruta de aprendizaje hacia GTM definida.
- [ ] Sin cambios reales de plataforma o producción dentro de este brief.