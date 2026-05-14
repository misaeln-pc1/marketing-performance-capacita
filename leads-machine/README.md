# Leads Machine

Este subproyecto contiene la base visual y editable para la Maquina de Leads Capacita + Zoho One. Su objetivo es ordenar captacion, captura, CRM, scoring, segmentacion, journeys, venta humana, medicion y optimizacion sin crear todavia una app ni integraciones reales.

## Como abrir el mapa mental

Abre `MAPA_MENTAL.md` en VS Code y usa la extension Markmap (`gera2ld.markmap-vscode`) para ver la estructura como mapa visual. El archivo esta escrito en Markdown para que se pueda editar rapido y versionar sin herramientas especiales.

## Como ver el flujo maestro

Abre `FLUJO_MAESTRO.md` en VS Code con una extension compatible con Mermaid, como `bierner.markdown-mermaid`. El diagrama muestra el flujo principal y rutas separadas para B2C, B2B, exalumnos y leads frios/no respuesta.

## Archivos

- `MAPA_MENTAL.md`: mapa jerarquico compatible con Markmap.
- `FLUJO_MAESTRO.md`: flujo principal en Mermaid.
- `PLAN_ACCION.md`: fases de trabajo con tareas, entregables y Definition of Done.
- `DECISIONES.md`: registro de decisiones del subproyecto.
- `CHECKLIST.md`: checklist operativo para revision local, commit y push.
- `PROJECT_CONTEXT.md`: contexto estrategico existente.
- `AGENTS.md`: reglas locales existentes para asistentes tecnicos.

## Reglas de trabajo

- Trabajar solo dentro de `/leads-machine/`, salvo `.vscode/extensions.json` si se necesita recomendar extensiones.
- Mantener documentos simples, visuales y editables.
- Usar Zoho CRM como fuente unica de verdad conceptual.
- Separar rutas B2C, B2B, exalumnos y leads frios.
- Medir calidad comercial, no solo volumen.

## Que no se debe hacer todavia

- No crear app React.
- No crear `package.json`.
- No instalar dependencias.
- No crear `src/`.
- No crear integraciones Zoho.
- No usar credenciales, tokens ni datos personales reales.
- No tocar campanas, core, assets, automation, templates, references ni documentos raiz del repo.
