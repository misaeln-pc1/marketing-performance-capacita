# MARKETING_GTM_REVOPS_CLASSIFICATION

Fecha: 2026-06-21  
Repo: `misaeln-pc1/marketing-performance-capacita`  
Estado: corrección documental mínima tras creación accidental directa en `main`.

## Objetivo

Clasificar el contenido actual del repo Marketing Performance Capacita contra la frontera global aprobada entre:

- Marketing (Campañas & Growth);
- Go-to-Market / RevOps;
- Skills / AI OS;
- Capacita Edge;
- Capacita Zoho Deluge Core;
- WhatsApp + n8n + Zoho.

Esta revisión es documental. No mueve archivos reales, no renombra el repo y no modifica campañas activas.

## Contexto global aplicado

La frontera aprobada define:

- Marketing (Campañas & Growth): ejecución táctica de campañas, pauta, copies, calendario, landings de campaña, SEO operativo, experimentos A/B y reportes/performance.
- Go-to-Market / RevOps: buyer persona, value persona, segmentación, customer journey, lifecycle, lead scoring, nurturing, touch strategy e hipótesis comerciales.
- Skills / AI OS: capacidades reutilizables, skills de auditoría, plantillas, instrucciones técnicas IA y revisión de capacidades.
- Capacita Edge: implementación técnica de sitio, landings, metatags y performance web.
- Capacita Zoho Deluge Core: código y reglas técnicas Deluge/CRM.
- WhatsApp + n8n + Zoho: workflows, webhooks y ejecución técnica de mensajería/automatización.

## Archivos leídos

| Archivo | Estado | Observación |
|---|---:|---|
| `README.md` | leído | Declara repo maestro para metodología comercial-publicitaria, campañas, buyer personas, journey, tracking y aprendizajes. |
| `PROJECT_CONTEXT.md` | leído | Define fuentes de verdad, arquitectura base, buyer personas prioritarios y reglas de alcance. |
| `TASK_STATUS.md` | leído | Estado actual centrado en Meta V3 y bloqueo Google Ads MCP. |
| `REPO_RULES.md` | leído | Define nomenclatura, no binarios, propuestas de valor y seguridad. |
| `WORKFLOW.md` | leído | Define flujo ChatGPT arquitectura / Antigravity ejecución / revisión. |
| `core/README.md` | leído | Contiene inteligencia comercial reutilizable: buyer personas, journey, propuestas de valor, mensajes estratégicos. |
| `campaigns/README.md` | leído | Contiene ejecución por campaña/canal, briefs, hipótesis, segmentaciones, mensajes y aprendizajes. |
| `automation/README.md` | leído | Contiene tracking, Zoho, n8n, WhatsApp, atribución y seguimiento. |
| `templates/README.md` | leído | Contiene plantillas, prompts, checklists y estructuras reutilizables. |
| `assets/README.md` | leído | Índice liviano de activos en Drive; no binarios. |
| `references/README.md` | leído | Referencias metodológicas: journey, buyer persona, JTBD, bibliografía y frameworks. |

## Archivos no encontrados

| Archivo | Estado |
|---|---:|
| `DECISIONES.md` | no encontrado en revisión inicial |
| `RIESGOS.md` | no encontrado en revisión inicial |
| `SKILLS_USED.md` | no encontrado en revisión inicial |
| `REVIEW_REQUEST.md` | no encontrado en revisión inicial |

## Limitaciones

- No se hizo lectura de plataformas externas: Meta Ads, Google Ads, Zoho CRM, Google Drive, Cloudflare ni n8n.
- No se revisaron archivos binarios ni activos externos.
- No se validaron métricas reales de campañas.
- No se movieron archivos existentes.
- No se reclasificaron físicamente carpetas; solo se define criterio de propiedad conceptual.

## Matriz de clasificación

| Archivo / carpeta / contenido | Ubicación actual | Tipo de contenido | Dueño canónico recomendado | Acción recomendada | Riesgo | Observación |
|---|---|---|---|---|---:|---|
| `README.md` | raíz | Descripción general y alcance histórico | Marketing (Campañas & Growth) + referencia a GTM/RevOps | revisar después | Amarillo | Contiene conceptos que ahora deben interpretarse con frontera nueva: campaña en Marketing, estrategia transversal en GTM/RevOps. |
| `PROJECT_CONTEXT.md` | raíz | Contexto del proyecto, fuentes de verdad, arquitectura base y buyer personas | Marketing (Campañas & Growth) con referencias a GTM/RevOps | revisar después | Amarillo | Buyer personas y estrategia comercial deben quedar referenciadas a GTM/RevOps; campañas y performance siguen aquí. |
| `TASK_STATUS.md` | raíz | Estado operativo del repo | Marketing (Campañas & Growth) | se queda en Marketing | Verde | Debe registrar próxima acción de clasificación y no mover contenido real. |
| `REPO_RULES.md` | raíz | Reglas operativas y seguridad | Marketing (Campañas & Growth) | se queda en Marketing | Verde | Alineado con no binarios, no PII, no secretos. |
| `WORKFLOW.md` | raíz | Flujo ChatGPT/Antigravity | Marketing (Campañas & Growth) | se queda en Marketing | Verde | Se mantiene útil para ejecución documental. |
| `core/` | carpeta | Inteligencia comercial reutilizable | GTM/RevOps para buyer/journey/criterio; Marketing para mensajes aplicados | migrar conceptualmente a GTM/RevOps | Amarillo | No mover físicamente todavía. Crear referencias o extracción futura archivo por archivo. |
| `campaigns/` | carpeta | Ejecución por campaña/canal/curso | Marketing (Campañas & Growth) | se queda en Marketing | Verde | Es el corazón táctico del repo. |
| Briefs de campaña | `campaigns/` | Ejecución táctica | Marketing (Campañas & Growth) | se queda en Marketing | Verde | Pueden referenciar buyer/journey desde GTM/RevOps. |
| Hipótesis publicitarias por campaña | `campaigns/` | Experimentos tácticos | Marketing (Campañas & Growth) | se queda en Marketing | Verde | Si se vuelven hipótesis comerciales transversales, referenciar a GTM/RevOps. |
| Segmentaciones por campaña | `campaigns/` | Aplicación táctica de públicos | Marketing (Campañas & Growth), con fuente GTM/RevOps | referenciar a GTM/RevOps | Amarillo | Segmentación canónica vive en GTM/RevOps; targeting específico queda aquí. |
| Aprendizajes por campaña | `campaigns/` | Performance y aprendizaje táctico | Marketing (Campañas & Growth) | se queda en Marketing | Verde | Puede alimentar a GTM/RevOps como evidencia. |
| `automation/` | carpeta | Tracking, CRM, n8n, WhatsApp, atribución | Marketing para documentación de tracking; Zoho/WhatsApp repos para implementación | referenciar a Zoho Deluge Core / WhatsApp+n8n | Amarillo | No debe contener código productivo ni secretos. Debe referenciar repos ejecutores. |
| Tracking y UTM | `automation/` | Trazabilidad campaña-funnel | Marketing (Campañas & Growth) + Skills / AI OS | referenciar a Skills / AI OS | Verde | Skills puede auditar nomenclatura/eventos; no reemplaza estrategia. |
| Zoho CRM / seguimiento | `automation/` | Relación comercial/CRM | Capacita Zoho Deluge Core para implementación; GTM/RevOps para lógica | referenciar a Zoho Deluge Core | Amarillo | No duplicar Zoho CRM ni código Deluge. |
| n8n / WhatsApp | `automation/` | Automatización/mensajería | WhatsApp + n8n + Zoho | referenciar a WhatsApp + n8n + Zoho | Amarillo | Marketing define necesidad de campaña; repo técnico ejecuta. |
| `templates/` | carpeta | Plantillas reutilizables | Marketing (Campañas & Growth), Skills / AI OS si son prompts/skills reutilizables | revisar después | Verde | Plantillas operativas se quedan; skills reutilizables deberían referenciar AI OS. |
| Prompts operativos | `templates/` | Instrucciones reutilizables | Skills / AI OS si son generales; Marketing si son específicas | referenciar a Skills / AI OS | Amarillo | No convertir cada prompt puntual en skill. Solo patrones estables. |
| `assets/` | carpeta | Índice de archivos pesados en Drive | Marketing (Campañas & Growth) | se queda en Marketing | Verde | Correcto: repo no guarda binarios. |
| Creatividades reales / videos / imágenes | fuera del repo | Activos pesados | Google Drive/local respaldado | se queda fuera del repo | Verde | Mantener solo índice, no binarios. |
| `references/` | carpeta | Referencias metodológicas, journey, buyer persona, JTBD | GTM/RevOps para contenido estratégico; Marketing para referencias aplicadas | migrar conceptualmente a GTM/RevOps | Amarillo | Puede quedar como referencia, pero la verdad de negocio debe vivir en GTM/RevOps. |
| Buyer persona | `core/`, `references/`, `PROJECT_CONTEXT.md` | Estrategia comercial | GTM/RevOps | migrar conceptualmente a GTM/RevOps | Amarillo | Mantener referencias en Marketing, no duplicar versiones. |
| Value persona / propuesta de valor | `core/`, `PROJECT_CONTEXT.md`, posibles briefs | Estrategia comercial | GTM/RevOps | migrar conceptualmente a GTM/RevOps | Amarillo | Marketing aplica; GTM gobierna. |
| Customer journey / lifecycle | `core/`, `references/` | Estrategia comercial | GTM/RevOps | migrar conceptualmente a GTM/RevOps | Amarillo | Evitar versiones divergentes. |
| Lead scoring / nurturing / touch strategy | `automation/`, posibles docs de campañas | Reglas comerciales | GTM/RevOps | migrar conceptualmente a GTM/RevOps | Amarillo | Ejecución técnica debe vivir en Zoho/WhatsApp repos. |
| Performance Ads: CPL, CPA, ROI | `campaigns/`, docs/audits si existen | Reporte táctico | Marketing (Campañas & Growth) | se queda en Marketing | Verde | Alimenta GTM/RevOps con evidencia agregada. |
| Implementación técnica SEO / landings | referencias a landing / Edge | Código web/performance | Capacita Edge | referenciar a Capacita Edge | Amarillo | Marketing no debe tocar producción web directa desde este repo. |

## Acciones recomendadas

### Mantener en Marketing (Campañas & Growth)

- `campaigns/`.
- Briefs, copies, creatividades documentales, calendario editorial, hipótesis tácticas y aprendizajes por campaña.
- Reportes de performance agregados: CPL, CPA, ROI, tasa de contacto, tasa de matrícula.
- `assets/` como índice de ubicación externa, sin binarios.
- `TASK_STATUS.md`, `REPO_RULES.md`, `WORKFLOW.md`.

### Referenciar a GTM/RevOps

- Buyer persona.
- Value persona / propuesta de valor transversal.
- Segmentación canónica.
- Customer journey / lifecycle.
- Lead scoring, nurturing y touch strategy.
- Hipótesis comerciales que excedan una campaña puntual.

### Referenciar a Skills / AI OS

- Skills de Google Ads, Meta Ads, performance bridge, taxonomía UTM/eventos y buyer-persona-signal.
- Prompts o checklists que se vuelvan estables, repetibles y reutilizables.

### Referenciar a Capacita Edge

- Landings productivas.
- Implementación técnica SEO.
- Metatags, performance web, redirecciones y formularios en sitio.

### Referenciar a Capacita Zoho Deluge Core

- Código de CRM.
- Reglas técnicas Deluge.
- Automatización de touch/scoring en Zoho.

### Referenciar a WhatsApp + n8n + Zoho

- Workflows n8n.
- Webhooks.
- Mensajería WhatsApp.
- Ejecución técnica de nurturing multicanal.

## Riesgos

| Riesgo | Semáforo | Mitigación |
|---|---:|---|
| Duplicar buyer persona entre Marketing y GTM/RevOps | Amarillo | Mantener Marketing como consumidor; GTM/RevOps como fuente canónica. |
| Mezclar ejecución de campañas con estrategia transversal | Amarillo | Usar alias Marketing (Campañas & Growth) y referencias a GTM/RevOps. |
| Que `automation/` acumule implementación técnica real | Amarillo | Documentar solo criterio/tracking; código y workflows en repos técnicos. |
| Subir assets, PII o métricas sensibles | Amarillo | Mantener reglas de no binarios, no PII, no secretos, solo agregados anonimizados. |
| Crear migración física prematura | Amarillo | No mover archivos hasta PR específico con diff revisado. |

## Decisión de esta fase

No se mueven archivos reales. La clasificación queda como mapa para revisión humana y futura migración controlada archivo por archivo.

## Siguiente paso

Revisar `core/`, `references/` y `automation/` archivo por archivo cuando el árbol completo esté disponible en VS Code o conector, y decidir qué queda como referencia en Marketing y qué se transforma en fuente canónica de GTM/RevOps dentro de Global.
