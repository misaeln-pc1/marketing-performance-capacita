# MARKETING_FILE_LEVEL_MIGRATION_PLAN

Fecha: 2026-06-21  
Repo: `misaeln-pc1/marketing-performance-capacita`  
Rama: `docs/marketing-file-level-migration-plan-2026-06-21`  
Estado: propuesta aprobada, fase 1 documental, sin movimientos físicos.

## Objetivo

Definir una propuesta concreta de redistribución conceptual y futura migración controlada entre:

- Marketing (Campañas & Growth);
- Go-to-Market / RevOps;
- Skills / AI OS;
- Capacita Edge;
- Capacita Zoho Deluge Core;
- WhatsApp + n8n + Zoho.

Esta fase **no mueve archivos reales**. Solo define qué debería quedarse, referenciarse o migrarse en PRs posteriores.

## Criterio aprobado

Marketing conserva campañas, ejecución táctica, copies, assets, performance y aprendizajes.

GTM/RevOps conserva la verdad canónica de buyer persona, value persona, segmentación, journey, nurturing, scoring y touch strategy.

La implementación técnica vive en repos técnicos.

No se mueven carpetas completas; se migran archivos o se crean referencias caso a caso.

## Evidencia de base leída

| Fuente | Evidencia aplicada |
|---|---|
| `README.md` | El repo mezcla estrategia, campañas, buyer personas, journey, tracking, formularios, nurturing y aprendizajes comerciales. |
| `PROJECT_CONTEXT.md` | Define fuentes de verdad externas: Zoho CRM, Google Drive y plataformas Ads; no debe reemplazarlas. |
| `TASK_STATUS.md` | Ordena revisar `core/`, `references/` y `automation/` archivo por archivo antes de mover. |
| `DECISIONES.md` | Ya define que Marketing no se renombra y que GTM/RevOps es dueño de la lógica comercial transversal. |
| `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` | Clasifica carpetas y contenidos por dueño recomendado. |
| `core/README.md` | Declara buyer personas, journey, propuestas de valor, mensajes estratégicos y criterios comerciales reutilizables. |
| `campaigns/README.md` | Declara ejecución específica por campaña/canal/curso/objetivo. |
| `automation/README.md` | Declara tracking, Zoho CRM, n8n, WhatsApp, atribución y seguimiento. |
| `references/README.md` | Declara customer journey, buyer persona, JTBD, bibliografía, frameworks y notas comparativas. |
| `REVIEW_REQUEST.md` | Confirma que no deben tocarse campañas, producción, datos personales ni binarios. |
| `CHANGELOG_AGENT.md` | Registra auditorías previas de Meta/Google Ads y bloqueo Google Ads MCP. |

## Propuesta de destino canónico

| Bloque actual | Qué contiene | Acción recomendada | Destino canónico futuro | Qué queda en Marketing |
|---|---|---|---|---|
| `core/` | Inteligencia comercial reutilizable | Dividir por tipo de verdad | GTM/RevOps para estrategia transversal | Índice y referencias a canónicos |
| `core/buyer-personas/` o equivalente | Buyer personas | Migrar conceptualmente; mover archivo solo si existe y es estable | `capacita-global-control/docs/gtm-revops/BUYER_PERSONAS.md` | Resumen aplicado por campaña |
| `core/value-propositions/` o equivalente | Propuesta de valor reusable | Migrar conceptualmente | `capacita-global-control/docs/gtm-revops/VALUE_PROPOSITIONS.md` | Uso táctico en briefs/copies |
| `core/customer-journey/` o equivalente | Journey/lifecycle | Migrar conceptualmente | `capacita-global-control/docs/gtm-revops/CUSTOMER_JOURNEY.md` | Referencia aplicada a campaña |
| `core/messages/` o equivalente | Mensajes estratégicos | Dividir | GTM/RevOps para arquitectura de mensaje; Marketing para copies finales | Copies, titulares y variantes |
| `core/commercial-criteria/` o equivalente | Criterios comerciales | Migrar conceptualmente | `capacita-global-control/docs/gtm-revops/COMMERCIAL_CRITERIA.md` | Checklist de aplicación |
| `campaigns/` | Briefs, hipótesis, segmentación táctica, mensajes por canal y aprendizajes | Se queda | Marketing (Campañas & Growth) | Todo el bloque |
| `campaigns/*/brief*` | Brief de campaña | Se queda | Marketing (Campañas & Growth) | Documento completo |
| `campaigns/*/copy*` o equivalentes | Copies y anuncios | Se queda | Marketing (Campañas & Growth) | Documento completo |
| `campaigns/*/learning*` o equivalentes | Aprendizajes por campaña | Se queda y alimenta GTM | Marketing; referencia hacia GTM/RevOps | Documento completo |
| `campaigns/*/segmentation*` | Targeting táctico | Referenciar a GTM/RevOps | GTM/RevOps define la segmentación canónica | Segmentación aplicada a plataforma/campaña |
| `automation/utm*` o tracking | UTM, eventos, trazabilidad | Se queda parcialmente; referenciar Skills si es patrón reutilizable | Marketing + Skills / AI OS | Nomenclatura táctica y checklist |
| `automation/zoho*` | CRM, seguimiento, posible Deluge | Referenciar o migrar a repo técnico | `Capacita-Zoho-Deluge-Core/docs/` | Necesidad comercial y enlace al repo técnico |
| `automation/touch*`, `scoring*`, `nurturing*` | Reglas comerciales | Migrar conceptualmente | `capacita-global-control/docs/gtm-revops/TOUCH_STRATEGY.md`, `LEAD_SCORING_RULES.md`, `NURTURING_RULES.md` | Aplicación por campaña |
| `automation/n8n*`, `whatsapp*` | Workflows/mensajería | Referenciar o migrar diseño técnico | `whatsapp-n8n-zoho-capacita/docs/` | Necesidad comercial y enlace al flujo |
| `templates/` | Plantillas, prompts, checklists | Revisar caso a caso | Marketing o Skills / AI OS | Plantillas específicas de campaña |
| `templates/prompts*` | Prompts reutilizables | Solo migrar si son estables y generalizables | `capacita-ai-operating-system` como skill o prompt base | Prompts específicos de campaña |
| `assets/` | Índice a Drive/local | Se queda | Marketing + Drive externo | Todo el bloque, sin binarios |
| `references/` | Bibliografía, journey, buyer persona, JTBD, frameworks | Dividir | GTM/RevOps para estrategia; Knowledge/Playbooks si es referencia general | Índice y notas aplicadas |
| `references/jtbd*` | Jobs To Be Done | Migrar conceptualmente | GTM/RevOps o Knowledge/Playbooks | Aplicación a campaña |
| `references/frameworks*` | Frameworks | Revisar | Knowledge/Playbooks si es general; GTM si define regla de negocio | Índice y enlace |
| `docs/audits/*` | Auditorías de campañas/performance | Se queda | Marketing (Campañas & Growth) | Todo el bloque |
| `docs/google-ads/*` | Auditoría/estado Google Ads | Se queda | Marketing (Campañas & Growth) | Todo el bloque |
| Landings productivas mencionadas | Implementación web | Referenciar | `capacita-edge` | Hipótesis comercial y medición |

## Estructura propuesta para GTM/RevOps en Global

No crear repo nuevo. Crear o completar en `capacita-global-control`:

```text
capacita-global-control/
  docs/
    gtm-revops/
      README.md
      BUYER_PERSONAS.md
      VALUE_PERSONAS.md
      VALUE_PROPOSITIONS.md
      CUSTOMER_JOURNEY.md
      SEGMENTATION_RULES.md
      LEAD_SCORING_RULES.md
      NURTURING_RULES.md
      TOUCH_STRATEGY.md
      COMMERCIAL_CRITERIA.md
      GTM_REFERENCES_INDEX.md
```

## Fases de migración

### Fase 1 — Inventario documental

Estado: este PR.

Acción:

- Documentar qué se queda, qué se referencia y qué se propone mover después.
- No mover archivos reales.
- No crear GTM/RevOps como repo nuevo.

### Fase 2 — Crear canónicos GTM/RevOps en Global

Acción:

- Crear documentos canónicos vacíos o sintetizados en `capacita-global-control/docs/gtm-revops/`.
- No copiar bruto desde Marketing.
- Sintetizar la verdad de negocio estable.
- Dejar referencias desde Marketing.

### Fase 3 — PRs de extracción por bloque

Acción:

- PR 1: buyer personas.
- PR 2: value propositions / propuesta de valor.
- PR 3: customer journey / lifecycle.
- PR 4: scoring, nurturing y touch strategy.
- PR 5: automation technical references.

Cada PR debe tener:

- archivo origen;
- archivo destino;
- motivo;
- evidencia;
- referencia de reemplazo en Marketing;
- validación de que no se movieron datos sensibles.

### Fase 4 — Limpieza física controlada

Acción:

- Solo mover archivos cuando ya exista destino canónico aprobado.
- Dejar `README.md` o `INDEX.md` en la carpeta de origen si ayuda a continuidad.
- Evitar romper rutas usadas por campañas activas.

## Criterios de decisión para mover o no mover

| Pregunta | Si la respuesta es sí | Acción |
|---|---|---|
| ¿Define verdad comercial transversal? | Sí | GTM/RevOps |
| ¿Es un copy, brief o aprendizaje de campaña? | Sí | Marketing |
| ¿Es código, función o regla técnica Deluge? | Sí | Zoho Deluge Core |
| ¿Es workflow, webhook o mensajería ejecutable? | Sí | WhatsApp + n8n + Zoho |
| ¿Es landing, metatag, SEO técnico o performance web? | Sí | Capacita Edge |
| ¿Es una capacidad reutilizable IA? | Sí | Skills / AI OS |
| ¿Es binario, export o dato sensible? | Sí | No subir ni mover por GitHub |

## Riesgos y controles

| Riesgo | Semáforo | Control mínimo |
|---|---:|---|
| Duplicar buyer persona en Marketing y GTM/RevOps | Amarillo | GTM/RevOps debe ser fuente canónica; Marketing solo referencia. |
| Romper campañas activas por mover carpetas completas | Amarillo | No mover carpetas completas; migración archivo por archivo. |
| Mezclar reglas comerciales con código técnico | Amarillo | GTM define lógica; repos técnicos ejecutan. |
| Subir datos personales o métricas sensibles | Amarillo | Solo agregados anonimizados; no PII, no exports, no capturas sensibles. |
| Convertir prompts puntuales en skills prematuramente | Verde/Amarillo | Skill solo si es estable, repetible, generalizable y útil. |

## Qué no se toca en esta fase

- No se mueven archivos reales.
- No se renombran carpetas.
- No se modifica `main` directo.
- No se tocan campañas reales.
- No se toca Meta Ads, Google Ads, Zoho, n8n, WhatsApp, Cloudflare ni producción.
- No se suben binarios, PII, métricas sensibles, secretos ni credenciales.

## Recomendación

Aprobar este plan como mapa de migración. Después abrir PR en `capacita-global-control` para crear la carpeta `docs/gtm-revops/` y los documentos canónicos iniciales.
