# REVIEW_REQUEST

## Objetivo de revisión vigente

Revisar el PR documental limpio que normaliza el XFER comercial de Learning Games `GAME-EXCEL-BASICO-BLOCKS-001` desde `main` y reemplaza al PR #41 draft.

Este PR no activa tracking, Zoho, Edge, Supabase, Ads, workflows ni producción. Solo consolida un brief comercial documental y la bitácora XFER.

## PR en revisión

- Rama: `docs/marketing-xfer-game-excel-basico-blocks-clean-20260728`.
- Alcance:
  - brief comercial Marketing → Learning Games;
  - registro en `docs/BITACORA_XFER.md`;
  - actualización de estado, decisiones y changelog;
  - clasificación de PR #41 como draft/superseded por PR limpio.

## Archivos esperados

```text
docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md
docs/BITACORA_XFER.md
TASK_STATUS.md
DECISIONES.md
CHANGELOG_AGENT.md
REVIEW_REQUEST.md
```

## Validación solicitada

Confirmar que el PR:

1. no toca campañas, Ads, Edge, Zoho, Supabase, tracking, workflows ni producción;
2. no contiene PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios;
3. conserva `BP-001` como buyer persona primario y `BP-002` como secundario;
4. no redefine canónicos GTM/RevOps;
5. no envía respuestas crudas del juego a Zoho;
6. deja eventos y señales como conceptuales, no implementados;
7. recomienda captura de datos solo al final y con opt-in;
8. mantiene el piloto como B2C salvo decisión separada;
9. deja PR #41 como antecedente draft, no como PR a mergear;
10. deja pendiente callback final a Marketing #40 y Learning Games #6 después del merge.

## Gates

```text
REQUIERE_REVISION_MISAEL
NO_MERGEAR_TODAVIA
```

Si el diff es correcto y sigue siendo documental, el siguiente paso será pedir autorización de merge con la frase acordada.

## No hacer desde esta revisión

- No cerrar issue #40 todavía.
- No cerrar PR #41 todavía.
- No comentar Learning Games #6 todavía.
- No modificar Edge, Zoho, Supabase, PageSense, GTM ni Ads.
- No mergear sin autorización expresa.
- No crear tareas Task Hub en esta misma pasada.
- No tocar producción ni plataformas.
