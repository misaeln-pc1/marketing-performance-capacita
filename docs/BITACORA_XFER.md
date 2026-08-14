# BITACORA_XFER — Marketing Performance

Registro liviano de XFER producidos o consumidos por `misaeln-pc1/marketing-performance-capacita`.

## Estado vigente

| Fecha-hora | Productor | Consumidor | Caso | Versión | Estado | Archivo | Resultado |
|---|---|---|---|---|---|---|---|
| 20260814-163000 | Marketing Performance | System Integration | `CONNECTED_ANALYTICS_READ_PILOT` | v01 | `READY` | `docs/xfer/XFER__MARKETING__SYSTEM_INTEGRATION__CONNECTED_ANALYTICS_READ_PILOT__20260814__v01__READY.md` | Solicita paridad Google API/PowerShell vs MCP, requisitos GA4, delta Meta read-only y mapping CRM; sin OAuth nuevo ni writes. |
| 20260728-182000 | Marketing Performance | Capacita Learning Games | `GAME-EXCEL-BASICO-BLOCKS-001` | v02 | `READY` | `docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md` | Brief comercial normalizado desde `main`; reemplaza PR #41 draft tras merge. |
| 20260728-174500 | Marketing Performance | Capacita Edge | `EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE` | v02 | `READY` | `docs/xfer/XFER__MARKETING__CAPACITA_EDGE__EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE__20260728-174500__v02__READY__MARKETING_REVIEW.md` | `CONSUMED_WITH_CHANGES` para XFER Edge v05; requiere respuesta Edge. |

## XFER externo consumido en este ciclo

| Fecha-hora | Productor | Consumidor | Caso | Versión | Estado | Archivo | Resultado |
|---|---|---|---|---|---|---|---|
| 20260727-041500 | Capacita Edge | Marketing Performance | `EXCEL_B2C_PAID_LANDINGS_REVIEW` | v05 | `READY` | `docs/xfer/XFER__CAPACITA_EDGE__MARKETING__EXCEL_B2C_PAID_LANDINGS_REVIEW__20260727-041500__v05__READY__LANDING_REVIEW_REQUEST.md` | Consumido por Marketing como `CONSUMED_WITH_CHANGES`; versiones v01-v04 no deben usarse salvo revisión histórica. |

## Reglas

- Los XFER `READY` se consumen por mayor versión y luego fecha más reciente.
- No mezclar casos, productores ni versiones.
- GitHub guarda Markdown/bitácora; no guarda binarios, exports crudos, PII ni secretos.
- Todo XFER que implique producción, campañas, formularios, API, tracking, Zoho, Cloudflare o costos mantiene gate de autorización humana.
