# PROJECT_CONTEXT.md — Máquina de Leads Capacita + Zoho One

## Propósito

Construir una arquitectura de captación, calificación automática, nurturing y derivación comercial para Capacita usando Zoho One como entorno principal.

El proyecto busca atraer más leads, aceptar que muchos serán de baja calidad, y filtrar automáticamente para que venta humana intervenga solo cuando exista intención real.

## Principio rector

No perseguir todos los leads. Clasificarlos antes.

## Arquitectura base

```text
Captación → Captura → CRM SSOT → Scoring → Segmentación → Journeys → Venta humana → Medición → Optimización
```

## Stack considerado

- Meta Ads: volumen y dolores laborales.
- Google Ads: intención directa.
- Web/SEO: demanda orgánica.
- Zoho CRM: fuente única de verdad.
- Zoho Marketing Automation: journeys, scoring conductual y tracking web.
- Zoho Campaigns: email a bases con permiso o relación previa.
- Zoho SalesIQ: intención web, chatbot y handoff humano.
- Zoho Forms / Survey: captura, diagnóstico y perfilamiento.
- Zoho PageSense: A/B testing, heatmaps y optimización.

## Curso piloto recomendado

Excel básico–intermedio presencial en Santiago Centro.

## Supuestos operativos

1. No se compran listas de correos.
2. No se usa Zoho Campaigns para spam o cold email masivo.
3. Primero se documenta y estructura; después se implementa.
4. El CRM debe quedar como fuente única de verdad.
5. B2C y B2B deben separarse desde la captura o el scoring.
6. WhatsApp humano se reserva para señales claras de intención.

## Límites actuales

- No crear integraciones reales con Zoho en esta fase.
- No usar credenciales ni tokens.
- No modificar archivos fuera de `/leads-machine/`.
- No tocar `main` directamente.
- No implementar automatizaciones productivas.

## Roles de trabajo

- ChatGPT: definición estratégica, criterio, revisión crítica y coherencia del sistema.
- Codex: ejecución técnica cuando pueda trabajar sobre el repo y abrir PR.
- GitHub: memoria versionada del proyecto.

## Riesgos principales

- Medir solo CPL y no calidad comercial.
- Mezclar particulares con empresas.
- Crear automatizaciones sin campos CRM claros.
- Duplicar lógica entre CRM, Campaigns y Marketing Automation.
- Sobrecargar formularios.
- No registrar fuente, campaña, anuncio y landing.

## Definition of Done del scaffold

- Documentación base creada.
- Datos estratégicos en JSON editable.
- Fases clicables definidas.
- Scoring y journeys iniciales definidos.
- No hay cambios fuera de `/leads-machine/`.
