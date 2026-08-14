# REVIEW_REQUEST

## Objetivo de revisión vigente

Validar el saneamiento de memoria operativa de Marketing para evitar que futuros chats/agentes reinicien decisiones ya resueltas o usen archivos puente obsoletos.

## Rama

```text
docs/marketing-context-memory-sync-20260813
```

## Hallazgos corregidos

1. `TASK_STATUS.md` estaba fechado 2026-07-28 y no incluía PR #58, issue #56 ni la corrección Meta Ads de agosto.
2. `DECISIONES.md` no registraba la política canónica de negativas ni la regla de continuidad anti-reinicio.
3. `CHANGELOG_AGENT.md` no registraba el trabajo del 13-ago.
4. `REVIEW_REQUEST.md` seguía apuntando al routing Meta ya mergeado.
5. `docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md` seguía marcado `PROPUESTO_PARA_MAIN` después del merge.
6. `PROJECT_CONTEXT.md` trataba Google Drive como bodega general de pesados, contradiciendo la regla actual del proyecto.
7. `AGENTS.md` no obligaba a recuperar el documento canónico específico antes de dar recomendaciones genéricas.
8. PR #35 y PR #45 seguían abiertos pese a estar superados, contaminando el estado visible para futuros Bootstrap.

## Regla crítica nueva

Antes de recomendar sobre un frente ya trabajado:

- leer `TASK_STATUS.md` y `DECISIONES.md`;
- buscar el documento canónico específico;
- usar issues/PR solo para delta no consolidado;
- aplicar primero la decisión vigente;
- no pedir de nuevo a Misael justificaciones ya documentadas salvo contradicción o evidencia nueva.

Para Google Ads negativas de Excel B2C presencial, la fuente obligatoria es:

```text
docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md
```

## Archivos modificados

```text
AGENTS.md
TASK_STATUS.md
DECISIONES.md
CHANGELOG_AGENT.md
REVIEW_REQUEST.md
PROJECT_CONTEXT.md
docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md
```

## Clasificación de antecedentes

- PR #35: `CLOSED_SUPERSEDED / HISTORICO`; cerrado sin merge.
- PR #45: `CLOSED_SUPERSEDED / HISTORICO`; cerrado sin merge.
- PR #52: `OPEN / REVISION_TECNICA_PENDIENTE`; no se cierra en este saneamiento.
- PR #8: `CLOSED_SUPERSEDED` por PR #51.
- Issue #23: `CLOSED / HISTORICO`; validación V1 finalizada.
- Issue #60: `OPEN / V3_CANDIDATA_NO_ACTIVA`; nuevo ciclo de validación.

## Relación con Global

- Global PR #134 captura las instrucciones realmente activas como V2 snapshot y prepara V3 candidata.
- V3 no se activa hasta merge, copia manual por Misael y Bootstrap documentado en issue #60.

## Incidente operativo durante esta revisión

Se creó accidentalmente el archivo inocuo `__noop__` en `main` mediante una llamada errónea del conector y fue revertido inmediatamente.

Evidencia de reversión:

```text
commit de limpieza en main: 9e4e7683040fa4c6854d7d526e8d72f2c1aa1ae6
```

El archivo ya no existe y no contenía datos, secretos ni lógica. Archivos de prueba creados accidentalmente solo en la rama también fueron revertidos y no forman parte del diff final.

## No se toca

- Google Ads / Meta Ads productivos;
- campañas, presupuestos, pujas, anuncios, públicos, keywords o negativas reales;
- APIs, scripts o workflows;
- Zoho, GTM, PageSense, Edge, Cloudflare o producción;
- PII, secretos, exports crudos o archivos pesados.

## Validación esperada

- Solo Markdown en la rama.
- Documento de negativas marcado `VIGENTE_EN_MAIN` con PR #58 y merge SHA correctos.
- `TASK_STATUS.md` fechado 2026-08-13 y sin PR obsoletos como pendientes activos.
- `DECISIONES.md` contiene la política de negativas y la regla anti-reinicio.
- `PROJECT_CONTEXT.md` usa SharePoint/OneDrive Empresa como bodega definitiva del proyecto.
- `AGENTS.md` contiene lectura contextual específica por frente.
- PR #35/#45 cerrados sin merge; PR #52 preservado.
- Sin PII, secretos ni binarios.

## Gate

```text
LISTO_PARA_MERGE
REQUIERE_REVISION_MISAEL
```

No mergear sin autorización explícita.
