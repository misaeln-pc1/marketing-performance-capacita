# REVIEW_REQUEST

## Objetivo de revisión vigente

Revisar el PR documental limpio que rescata PageSense/CRO desde `main` y reemplaza al PR #34 antiguo.

Este PR no activa PageSense, GTM, Zoho, Google Ads ni producción. Solo consolida síntesis agregada y reglas de medición.

## PR en revisión

- Rama: `docs/marketing-pagesense-cro-baseline-clean-20260728`.
- Alcance:
  - baseline PageSense/CRO;
  - auditoría de configuración de goals PageSense;
  - actualización de estado, decisiones y changelog;
  - clasificación de PR #34 como superseded por PR limpio.

## Archivos esperados

```text
docs/pagesense/PAGESENSE_CRO_REPORTING_BASELINE_V01.md
docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md
TASK_STATUS.md
DECISIONES.md
CHANGELOG_AGENT.md
REVIEW_REQUEST.md
```

## Validación solicitada

Confirmar que el PR:

1. no ejecuta PageSense, Google Ads, GTM, Zoho, Edge ni APIs;
2. no modifica campañas, landings productivas, tracking, formularios ni producción;
3. no contiene CSV crudos, capturas, grabaciones, PII, secretos, IDs completos ni binarios;
4. trata PageSense como fuente complementaria de CRO, no como fuente de leads ni matrículas;
5. reclasifica `enviar Pre`, `inicio` y `Enviar Empresa-Excel` como interacción secundaria mientras no exista submit confirmado;
6. registra que el submit confirmado debe medirse después de aceptación real del formulario;
7. registra riesgo rojo por nombre/correo en URL de redirección B2C;
8. no corrige ese riesgo desde Marketing y lo deja para Edge/Zoho con autorización específica;
9. deja PR #34 como antecedente histórico/superseded, no como PR a mergear;
10. no autoriza A/B, Split URL ni cambios productivos hasta corregir goals y privacidad.

## Gates

```text
REQUIERE_REVISION_MISAEL
NO_MERGEAR_TODAVIA
```

Si el diff es correcto y sigue siendo documental, el siguiente paso será pedir autorización de merge con la frase acordada.

## No hacer desde esta revisión

- No cerrar issue #43 todavía.
- No cerrar PR #35 todavía.
- No modificar Edge, Zoho, PageSense, GTM ni Ads.
- No mergear sin autorización expresa.
- No crear tareas Task Hub en esta misma pasada.
- No tocar producción ni plataformas.
