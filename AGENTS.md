# AGENTS

## Lectura obligatoria y Gate de Vigencia

Antes de modificar documentación, prompts, estructuras, protocolos, campañas, criterios de medición, fuentes oficiales o decisiones que deban afectar futuros chats, leer:

```text
misaeln-pc1/capacita-global-control/docs/LECTURA_OBLIGATORIA_GLOBAL.md
misaeln-pc1/capacita-global-control/docs/CONTROL_CAMBIOS_PLAN_ACORDADO.md
misaeln-pc1/capacita-global-control/docs/DICCIONARIO_OPERATIVO_CAPACITA.md
misaeln-pc1/capacita-global-control/docs/ESTANDAR_GLOBAL_PROYECTOS.md
misaeln-pc1/capacita-global-control/docs/ISSUE_TASK_ROUTING_STANDARD.md
```

Regla de vigencia:

- Una definición aprobada por Misael debe cerrar como `VIGENTE_EN_MAIN`, `PR_LISTO_PARA_MERGE`, `TRANSITORIO_NO_VIGENTE_EN_MAIN`, `DRAFT_NO_VIGENTE` o `SUPERSEDED` / `HISTORICO`.
- Si el PR documental queda listo, pedir autorización con: `PR #X listo para merge. ¿Autorizas que yo haga el merge?`.
- Si hay dos documentos/protocolos que parecen vigentes y se contradicen, detenerse y preparar consolidación.

## Sistema de Tareas Atlas

Regla vigente:

```text
El problema vive en el repo.
La tarea ejecutable vive en Task Hub.
La evidencia tecnica vive en el repo.
```

- Ideas, investigaciones, decisiones, riesgos, bloqueos, epicas e incidentes: issue en este repo.
- Tareas ejecutables, personales, administrativas y seguimientos accionables: issue en `misaeln-pc1/capacita-task-hub`.
- Si una tarea deriva de un issue local, registrar `Issue padre` y `Repo dueno`.
- Referencia: `misaeln-pc1/capacita-global-control/docs/ISSUE_TASK_ROUTING_STANDARD.md`.

## Reglas duras

- No trabajar directo en `main`.
- No ejecutar Google Ads API, scripts, workflows, integraciones ni automatizaciones sin autorización.
- No subir tokens, credenciales, `.env`, IDs sensibles ni datos crudos no sanitizados.
- No modificar campañas reales, presupuestos, conversiones, etiquetas, GTM, PageSense, formularios ni producción sin autorización explícita.
- Los cambios documentales reversibles deben ir en rama `docs/marketing-[objetivo]` o equivalente.
