# REVIEW_REQUEST

## Objetivo de revisión vigente

Revisar el resultado de Marketing para el batch editorial V01 de Content Factory y validar el XFER consolidado antes de que Factory aplique los deltas.

```text
MARKETING_ISSUE=71
BATCH_ID=CONTENT_PRE_MARKETING_V01_2026-08-29
ARTICLES=45
FACTORY_ISSUE=capacita-content-factory#16
FACTORY_PR=capacita-content-factory#17
FACTORY_HEAD=641213040cd9fe86b28885ba15ea6322808a6f4c
MARKETING_STATUS=XFER_READY_PENDING_FACTORY_READBACK
PUBLICATION=NO
EDGE=NO
MAIN_MERGE=NO
```

## Rama Marketing

`docs/marketing-content-batch-v01-review-20260829`

## Documento principal

`docs/xfer/XFER__MARKETING__CONTENT_FACTORY__CONTENT_PRE_MARKETING_V01_REVIEW__20260829-213400__v01__READY__MARKETING_REVIEW.md`

## Fuentes de control

- `TASK_STATUS.md`
- `DECISIONES.md`
- `PROJECT_CONTEXT.md`
- `AGENTS.md`
- `docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md`
- GTM/RevOps `docs/gtm-revops/BUYER_PERSONAS.md` v1.0.0
- Factory PR #17 / commit fijado `641213040cd9fe86b28885ba15ea6322808a6f4c`

## Evidencia usada

- lectura material de 45/45 artículos;
- HYPD Keyword Research Chile/español;
- SERP real Google Chile por clusters materiales;
- contenido existente de `capacita.cl` para canibalización;
- documentación oficial vigente cuando el producto cambia;
- GSC intentado, pero `DATA_GAP_PAYMENT_REQUIRED` por suscripción inactiva en esta sesión.

## Hallazgos principales

```text
BATCH_45_READ=YES
TOP_10_SELECTED=YES
E01=MERGE_WITH_EXISTING_BUSCARV_URL
PROJECT_10_NEW_URLS=HOLD_PENDING_ARCHITECTURE
PBI06=DASHBOARD_VS_REPORT_DELTA_REQUIRED
NEW_SKILL_REQUIRED=NO
FACTORY_READBACK_REQUIRED=YES
```

Top 10 de trabajo editorial priorizado:

1. E02 — Power Query Excel.
2. IA03 — prompts ChatGPT.
3. IA05 — agentes IA.
4. PBI06 — dashboard Power BI, con corrección técnica.
5. PBI04 — DAX Power BI.
6. IA06 — ChatGPT Work, fast-track coyuntural.
7. IA07 — Deep Research.
8. E03 — Copilot en Excel.
9. PBI03 — Power Query Power BI.
10. IA01 — IA para el trabajo, pillar.

Acción adicional P0: actualizar `https://capacita.cl/funcion-buscarv-excel/` con el material E01; no crear URL duplicada.

## Qué se revisa ahora

- coherencia del XFER con issue #71;
- trazabilidad 45/45;
- prioridades y deltas;
- canibalización;
- buyer persona/GTM aplicado sin forzar perfiles;
- ausencia de publicación, Ads, Edge o `main`.

## Qué NO se revisa todavía

- HTML/productivo;
- robots/canonical/sitemap/structured data de páginas inexistentes;
- assets finales;
- cambios Ads;
- merge a `main`.

## Siguiente condición

Content Factory consume el XFER y devuelve:

```text
CONSUMED_PASS|CONSUMED_WITH_GAPS
commit
changed CONTENT_IDs
diff/QA
open gaps
```

Marketing revisa ese readback en issue #71. Recién después se decide cierre del ciclo y eventual merge documental.

## Gate

```text
NO_MERGEAR_TODAVIA
PENDING_FACTORY_READBACK
```
