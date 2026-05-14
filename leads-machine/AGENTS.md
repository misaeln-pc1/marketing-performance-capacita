# AGENTS.md — Leads Machine Capacita

## Propósito

Este directorio contiene la documentación estratégica y los datos estructurados para construir una mini app interactiva de la Máquina de Leads Capacita + Zoho One.

El objetivo es captar volumen, filtrar intención automáticamente, aplicar scoring y derivar a venta humana solo cuando exista señal suficiente.

## Alcance permitido

Puedes crear o modificar archivos solo dentro de:

```text
/leads-machine/
```

## Archivos principales

- `PROJECT_CONTEXT.md`: visión estratégica y reglas del proyecto.
- `LEADS_MACHINE_MAP.md`: mapa maestro operativo.
- `LEADS_MACHINE_STATUS.md`: estado de avance, pendientes y bloqueos.
- `src/data/phases.json`: fases clicables del mapa.
- `src/data/scoring.json`: matriz de scoring y umbrales.
- `src/data/journeys.json`: journeys mínimos.
- `src/data/zohoStack.json`: rol de cada aplicación Zoho.

## Mapas de relación e impacto

Estos documentos expanden la visión del proyecto para analizar dependencias y riesgos operativos.

- `RELACIONES_PROYECTOS.md`: mapa visual de cómo interactúan los proyectos y la infraestructura.
- `INFRAESTRUCTURA_COMPARTIDA.md`: tabla de activos tecnológicos compartidos y su impacto.
- `MATRIZ_IMPACTO.md`: guía para entender las consecuencias de realizar cambios en el sistema.
- `FICHAS_PROYECTOS.md`: fichas detalladas por cada proyecto o sistema involucrado.

## Reglas duras

1. No modificar archivos fuera de `/leads-machine/` sin autorización explícita.
2. No crear integraciones reales con Zoho todavía.
3. No incluir credenciales, tokens, datos personales reales ni endpoints privados.
4. No tocar `main` directamente.
5. No implementar automatizaciones productivas.
6. No mezclar este mapa con licitaciones, TrainerCentral u otros proyectos.
7. Mantener textos editables en Markdown o JSON; evitar hardcodear contenido estratégico en componentes.
8. Priorizar claridad y mantenibilidad sobre diseño complejo.
9. Evitar sobreingeniería.
10. Toda implementación visual debe leer datos desde `src/data/` cuando sea razonable.

## Criterio de revisión

Prioridad:

1. Coherencia estratégica.
2. Separación B2C/B2B.
3. CRM como fuente única de verdad.
4. Scoring y estados claros.
5. Mantenibilidad.
6. UI simple y clicable.

## Definition of Done inicial

- Existe estructura documental base.
- Existen JSON válidos para fases, scoring, journeys y stack Zoho.
- El mapa puede transformarse en app clicable sin reescribir la estrategia.
- No se tocó ningún archivo fuera de `/leads-machine/`.
