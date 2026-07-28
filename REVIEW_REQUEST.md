# REVIEW_REQUEST

## Objetivo de revisión vigente

Revisar el PR documental que consolida el baseline mínimo de las tres landings Excel B2C pagadas y la respuesta XFER de Marketing a Capacita Edge.

Este reemplaza la solicitud histórica centrada en PR #29/#30/#31, ya mergeados según `TASK_STATUS.md` y `CHANGELOG_AGENT.md`.

## PR en revisión

- Rama: `docs/marketing-excel-b2c-min-baseline-20260728`.
- Alcance:
  - baseline mínimo de tres landings B2C pagadas;
  - XFER Marketing → Edge v02;
  - bitácora XFER;
  - actualización de estado, decisiones y changelog.

## Archivos esperados

```text
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md
docs/xfer/XFER__MARKETING__CAPACITA_EDGE__EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE__20260728-174500__v02__READY__MARKETING_REVIEW.md
docs/BITACORA_XFER.md
TASK_STATUS.md
DECISIONES.md
CHANGELOG_AGENT.md
REVIEW_REQUEST.md
```

## Decisión que debe validar Misael

Validar si este PR corto debe ser la fuente mínima en `main` para:

1. tres landings B2C pagadas `noindex,follow`;
2. protección de la página orgánica actual;
3. consumo de Edge XFER v05 como `CONSUMED_WITH_CHANGES`;
4. respuesta formal de Marketing a Edge;
5. no mergear PR #35 completo por ahora.

## Validación solicitada

Confirmar que el PR:

1. no activa ni autoriza campañas;
2. no modifica Google Ads, Meta Ads, Edge, Cloudflare, Worker, DNS, sitemap, GTM, PageSense, Turnstile, Zoho ni producción;
3. no ejecuta API, scripts ni exports;
4. no contiene PII, secretos, IDs completos, CSV crudos, capturas sensibles ni binarios;
5. no trata goals de clic como leads ni submits confirmados;
6. conserva `noindex,follow` y fuera de sitemap para las tres landings;
7. protege la página orgánica actual;
8. mantiene Landing C como curso grupal presencial con profesor, no clases particulares ni domicilio;
9. deja bloqueos claros antes de publicar, integrar tracking o enviar tráfico;
10. deja PR #35 como antecedente amplio, no como paquete a mergear completo.

## Gates

```text
REQUIERE_REVISION_MISAEL
NO_MERGEAR_TODAVIA
```

Si el diff es correcto y sigue siendo documental, el siguiente paso será pedir autorización de merge con la frase acordada.

## No hacer desde esta revisión

- No cerrar PR #35 todavía.
- No cerrar issue #43 todavía.
- No comentar Edge PR #36 todavía.
- No mergear sin autorización expresa.
- No crear tareas Task Hub en esta misma pasada.
- No tocar producción ni plataformas.
