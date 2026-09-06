# Handoff Marketing → Capacita Edge para slots, landings y campañas — V01

Estado de vigencia: `VIGENTE_EN_MAIN` cuando esta versión está en `main`; en cualquier rama/PR se interpreta `DRAFT_NO_VIGENTE`.  
Issue: `#87`.  
Issue técnico padre: `misaeln-pc1/capacita-edge#293`.  
Última alineación: `2026-09-06`.

## 1. Propósito

Este documento define cómo Marketing entrega a Capacita Edge un cambio de fecha, horario, precio, disponibilidad, modalidad o sede sin duplicar datos ni pedir modificaciones técnicas archivo por archivo.

No copia los contratos de Edge. Los referencia como fuente canónica.

## 2. Cuándo es obligatorio

Aplicar antes de:

- crear una landing que será destino de campaña;
- cambiar fecha, horario, precio o disponibilidad;
- abrir, cerrar, ocultar o cancelar una convocatoria;
- relanzar una campaña hacia una landing existente;
- cambiar modalidad o sede;
- declarar una página lista para campaña;
- solicitar actualización de sitemap o reindexación.

## 3. Fuentes canónicas en Capacita Edge

Leer desde `main`:

```text
misaeln-pc1/capacita-edge/docs/LANDING_CAPA18_BOOTSTRAP_CURRENT.md
misaeln-pc1/capacita-edge/docs/MARKETING_LANDING_SLOT_CHANGE_RUNBOOK.md
misaeln-pc1/capacita-edge/docs/templates/MARKETING_SLOT_CHANGE_REQUEST.md
misaeln-pc1/capacita-edge/docs/LANDING_SLOT_PUBLICATION_AND_SITEMAP_STANDARD.md
```

Fuentes técnicas relacionadas, administradas por Edge:

```text
misaeln-pc1/capacita-edge/data/corporate-site/canonical-entity-venue.json
misaeln-pc1/capacita-edge/data/seo/landing-slot-publication-contract.json
misaeln-pc1/capacita-edge/data/seo/organic-sitemap-lastmod.json
```

Si estas fuentes no pueden leerse, Marketing no debe reconstruirlas de memoria. Debe declarar `EDGE_HANDOFF_SOURCE_BLOCKED`.

## 4. Fórmula de landing que Marketing debe respetar

```text
17 BLOQUES VISUALES OBLIGATORIOS
+ CAPA TÉCNICA 18 OBLIGATORIA Y NO VISUAL
+ FOOTER LEGAL OBLIGATORIO FUERA DEL CONTEO
```

Marketing define intención, demanda, buyer persona, propuesta de valor, contenido, CRO y prioridad. Edge implementa estructura, frontend, slots, schema, canonical, sitemap/`lastmod`, seguridad, tracking técnico y publicación.

## 5. Solicitud única

Marketing completa una sola solicitud usando:

```text
misaeln-pc1/capacita-edge/docs/templates/MARKETING_SLOT_CHANGE_REQUEST.md
```

Debe incluir, como mínimo:

- curso y URL canónica;
- modalidad;
- acción solicitada;
- slot;
- fecha;
- días y horario;
- precio y moneda;
- disponibilidad/etiqueta;
- canal y fecha objetivo de campaña;
- fuente operativa;
- aprobador;
- evidencia;
- anuncios y superficies afectadas.

Un dato no confirmado se marca `UNKNOWN`; no se estima ni inventa.

## 6. Regla de sede

Para la sede habitual:

```text
VENUE_ID=https://capacita.cl/#sede-santiago-centro
VENUE_CHANGE=NO
```

Marketing no repite la dirección. Edge la deriva desde su fuente institucional canónica.

Sólo un cambio real de sede usa:

```text
VENUE_CHANGE=YES
```

con fuente, evidencia y aprobación separada.

Para una modalidad online, la sede física de impartición es `NOT_APPLICABLE`. La sede institucional puede respaldar a Capacita sin convertir el curso en presencial.

## 7. Qué no hace Marketing

Marketing no edita ni instruye ediciones manuales separadas de:

- HTML;
- hero/tarjetas;
- JSON-LD;
- `CourseInstance` u `Offer`;
- sitemap;
- `lastmod`;
- `main`;
- Worker/DNS/Cloudflare;
- fuente institucional de Organization/Place.

Tampoco activa una campaña sólo porque exista un preview o un PR abierto.

## 8. Qué debe devolver Edge

```text
PUBLIC_URL=
COURSE=
SLOT_ID=
PUBLISHED_START_DATE=
PUBLISHED_DAYS=
PUBLISHED_SCHEDULE=
PUBLISHED_PRICE=
PUBLISHED_AVAILABILITY=
SITEMAP_STATUS=PASS|NOT_APPLICABLE
MERGE_SHA=
DEPLOY_STATUS=
PUBLIC_READBACK=
CAMPAIGN_DESTINATION_MATCH=PASS|FAIL
CAMPAIGN_LAUNCH_ALLOWED=YES|NO
```

## 9. Gate de campaña

Marketing activa o actualiza la campaña únicamente cuando recibe:

```text
CAMPAIGN_LAUNCH_ALLOWED=YES
```

Esto exige que Edge haya verificado, según aplique:

- datos aprobados;
- slot válido;
- HTML inicial;
- paridad JSON-LD;
- superficies dependientes;
- manifest y sitemap;
- merge/deploy;
- readback de URL pública;
- coincidencia anuncio ↔ landing.

Si falta un control aplicable:

```text
CAMPAIGN_LAUNCH_ALLOWED=NO
```

## 10. Cambio urgente con campaña activa

Usar:

```text
PRIORITY=URGENT_ACTIVE_CAMPAIGN
```

Marketing pausa o corrige el anuncio si la landing pública aún no coincide. La urgencia permite reducir alcance, no omitir fuente, validación, sitemap o readback.

## 11. Estado actual

```text
EDGE_EXCEL_PILOT=PASS
EDGE_HOME_AND_EXCEL_ENTITY_SOURCE=UNIFIED
EDGE_CAPA_18=VIGENTE_EN_MAIN
EDGE_ALL_LANDINGS_ROLLOUT=PENDING
EDGE_ZOHO_SLOT_AUTOMATION=PENDING_ISSUE_24
```

Hasta completar el rollout, Marketing debe comprobar qué landing ya está migrada y cuál requiere corrección en Edge.

## 12. Declaración obligatoria en trabajos de Marketing

Cuando exista una landing o campaña con datos variables, cerrar con:

```text
MARKETING_EDGE_SLOT_HANDOFF=APPLIED|NOT_APPLICABLE|BLOCKED
EDGE_REQUEST_TEMPLATE_USED=YES|NO|NOT_APPLICABLE
SOURCE_FACTS_APPROVED=YES|NO
VENUE_ID_MODEL=APPLIED|NOT_APPLICABLE
CAMPAIGN_DESTINATION_MATCH=PASS|FAIL|PENDING
CAMPAIGN_LAUNCH_ALLOWED=YES|NO|PENDING
```

## 13. No duplicación

Este archivo no reemplaza ni versiona localmente los contratos técnicos de Edge. Ante cambios en esos contratos, Marketing consume la versión vigente en `main` de `misaeln-pc1/capacita-edge`.

```text
MARKETING_OWNS=DEMAND_INTENT_CONTENT_CRO_CAMPAIGN_PRIORITY
EDGE_OWNS=IMPLEMENTATION_SLOTS_SCHEMA_SITEMAP_PUBLICATION_READBACK
```

No crear una segunda plantilla local de cambio de slots.