# Plantilla de brief de campaña con baseline GTM

Estado: plantilla operativa v1.1.0 propuesta  
Referencias:

- `docs/GTM_CONSUMPTION_BRIDGE.md`;
- `docs/analytics/MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md`;
- `docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md` cuando exista landing/página.

## 0. Decisión y Opportunity Scan

| Campo | Valor |
|---|---|
| Decisión que debe habilitar |  |
| Resultado comercial esperado |  |
| Ventana/baseline |  |
| Restricciones vigentes |  |
| `DO_NOT_CHANGE` |  |
| `NEXT_BEST_ACTION` |  |

### Fuentes consultadas

| Fuente | Ventana/cobertura | Estado | Evidencia o data gap |
|---|---|---|---|
| Google Ads / Keyword Planner |  | PASS / PARTIAL / N/A / NO_ACCESS |  |
| Meta Ads |  | PASS / PARTIAL / N/A / NO_ACCESS |  |
| GSC |  | PASS / PARTIAL / N/A / NO_ACCESS |  |
| GA4 / PageSense |  | PASS / PARTIAL / N/A / NO_ACCESS |  |
| SERP / competencia / Semrush-HYPD |  | PASS / PARTIAL / N/A / NO_ACCESS |  |
| CRM / venta agregada |  | PASS / PARTIAL / N/A / NO_ACCESS |  |
| Canonical Capacita |  | PASS / PARTIAL |  |

No completar esta tabla por ritual. Consultar sólo fuentes pertinentes, pero justificar cualquier fuente material omitida. Preferir lectura conectada autorizada sobre copia/pega manual.

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
- Un clic o una respuesta aislada puede ser señal, no confirmación definitiva del buyer persona.

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


### Oportunidad detectada proactivamente


## 4. Público, intención y targeting táctico

| Dimensión | Decisión de campaña | Fuente o hipótesis |
|---|---|---|
| Ubicación |  |  |
| Curso/interés |  |  |
| Modalidad |  |  |
| Intención |  |  |
| Pain signal principal |  |  |
| Exclusiones / negativas |  |  |
| Plataforma/audiencia |  |  |

No convertir targeting de plataforma en nueva segmentación corporativa. En Google Ads, aplicar la política canónica de negativas por intención antes de excluir términos. En orgánico, distinguir intención no objetivo y canibalización de una negativa de campaña.

## 5. Propuesta, copy y CTA

### Propuestas canónicas seleccionadas


### Adaptación táctica


### CTA principal


### CTA secundario


### Mapa dolor/señal → mensaje → CTA

| `pain_signal` | Evidencia/hipótesis | Mensaje | CTA | Buyer persona compatible como hipótesis |
|---|---|---|---|---|
|  |  |  |  |  |

Mantener idealmente tres a cinco pain signals estables por oferta/familia. No crear etiquetas libres por cada página.

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

## 6. Landing, diferenciación y journey

| Campo | Definición |
|---|---|
| Etapa inicial |  |
| Conversión esperada |  |
| Destino |  |
| Siguiente acción |  |
| Repo técnico involucrado |  |
| Página hermana comparada |  |

### Diferenciación controlada

| Dimensión | Decisión | Justificación |
|---|---|---|
| Hero/imagen propia |  |  |
| Acento visual dentro de marca |  |  |
| Ejemplo aplicado |  |  |
| Dolor/señal visible |  |  |
| Prueba/confianza específica |  |  |
| CTA/microcopy |  |  |
| Elemento distintivo adicional |  |  |

Regla: `MISMA_MARCA != MISMA_PAGINA`. No rediseñar por variedad estética ni clonar una landing cambiando sólo el nombre del curso.

## 7. Tracking y atribución

### Contrato de evento recomendado

```yaml
tracking:
  course:
  modality:
  audience:
  pain_signal:
  bp_hypothesis:
  cta_action:
  cta_location:
  page_variant:
```

- No incluir PII en parámetros de eventos.
- Marketing define nomenclatura y significado.
- Edge implementa frontend/tracking.
- Analytics registra comportamiento.
- CRM conserva atribución o resultado sólo mediante diseño autorizado.

### Capas de resultado

| Capa | Métrica | Fuente | Criterio inicial |
|---|---|---|---|
| Ads | alcance, impresiones, clics, gasto, conversiones de plataforma | Plataforma Ads |  |
| Web | sesiones, landing, evento/submit, drop-off | GA4 / PageSense / Edge |  |
| Lead | lead/contacto y contactabilidad | CRM |  |
| Pipeline | Deal creado/ganado/perdido | CRM |  |
| Operación | CursoAlumno vinculado | sistema dueño |  |
| Comercial | matrícula/venta/valor confirmado | fuente autoritativa |  |

No declarar éxito por clics o conversiones de plataforma cuando el objetivo real es lead, cotización, matrícula o venta.

## 8. Diseño experimental

| Campo | Definición |
|---|---|
| Hipótesis única |  |
| Control |  |
| Variante |  |
| Variable principal |  |
| Ventana |  |
| Métrica primaria |  |
| Guardrail |  |
| Criterio de éxito |  |
| Criterio de detención |  |

Mantener una hipótesis y un buyer persona primario por prueba. Separar B2C y B2B cuando intención, oferta o ciclo comercial difieran.

## 9. Diagnóstico y prioridad

| Hallazgo | Evidencia | Prioridad | Impacto | Esfuerzo | Confianza | Riesgo | Acción exacta | Dueño | Validación |
|---|---|---:|---:|---:|---:|---:|---|---|---|
|  |  | P0/P1/P2 | alto/medio/bajo | alto/medio/bajo | alta/media/baja | verde/amarillo/rojo |  |  |  |

### Qué mantener


### Qué corregir


### Qué probar después


### Qué no tocar todavía


## 10. Riesgos y límites

- No datos personales en GitHub.
- No campañas, presupuesto ni plataforma real sin autorización.
- No modificación de landing productiva desde Marketing.
- No claims sin evidencia.
- No mezclar B2C y B2B sin decisión explícita.
- No usar atributos sensibles para clasificación.
- No inferir dolor o buyer persona como hecho a partir de un clic.
- No colapsar Ads, web, CRM, Deal, CursoAlumno y venta.
- No abrir OAuth/scope, instalar herramientas ni generar costos por inferencia.

## 11. Aprendizaje y retroalimentación

### Evidencia obtenida


### Hipótesis confirmada, rechazada o pendiente


### Posible impacto en el canónico GTM

- ID o documento afectado:
- versión:
- evidencia agregada:
- cambio propuesto:
- issue Global, si aplica:

### Posible patrón reusable para AI OS

- capacidad/patrón:
- evidencia de recurrencia:
- decisión `ADOPTAR / ADAPTAR_MINIMO / MIX / REFERENCIA / NO_APLICA`:

## 12. Definition of Done

- [ ] Decisión de negocio y `NEXT_BEST_ACTION` explícitas.
- [ ] Fuentes pertinentes consultadas o data gaps justificados.
- [ ] Baseline canónico y versiones registrados.
- [ ] Hipótesis táctica separada del canónico.
- [ ] Público, intención, pain signal, copy, CTA y destino definidos.
- [ ] Diferenciación frente a página/campaña hermana revisada.
- [ ] Claims verificables.
- [ ] Tracking y capas de atribución separados.
- [ ] Métricas conectadas al objetivo de negocio.
- [ ] P0/P1/P2, acción exacta, dueño y validación definidos.
- [ ] Riesgos y datos pendientes visibles.
- [ ] Ruta de aprendizaje hacia GTM/AI OS definida cuando aplique.
- [ ] Sin cambios reales de plataforma o producción dentro de este brief.
