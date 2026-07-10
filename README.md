# Marketing Performance Capacita

## Propósito

Repositorio operativo de **Marketing (Campañas & Growth)** para diseñar, documentar y aprender de campañas, pauta, targeting táctico, copies, activos, medición y performance de Capacita.

No es la fuente canónica de buyer personas, propuesta de valor, segmentación transversal, customer journey, scoring, nurturing o touch strategy.

## Fuente comercial transversal

Las definiciones corporativas vigentes viven en:

`misaeln-pc1/capacita-global-control/docs/gtm-revops/`

Toda campaña debe aplicar `docs/GTM_CONSUMPTION_BRIDGE.md` y registrar IDs/versiones o, cuando aún no existan IDs, documento/sección/versión.

## Qué contiene

- briefs e hipótesis de campaña;
- públicos y targeting táctico por plataforma;
- copies, anuncios y criterios de activos;
- planes de medición y auditorías;
- resultados agregados y aprendizajes;
- referencias hacia GTM/RevOps y repos técnicos.

## Qué no contiene

- definiciones corporativas paralelas;
- código complejo o landings de producción;
- workflows productivos de Zoho, n8n o WhatsApp;
- datos personales, exports CRM, secretos, tokens o archivos pesados.

## Campaña inicial

Excel Básico–Intermedio Presencial en Santiago Centro.

Baseline vigente para el piloto:

- `BP-001 — Desbordado Operativo`;
- `BP-002 — Reinserción Laboral`;
- propuestas de valor y journey referenciados desde GTM/RevOps.

## Estructura

- `campaigns/`: ejecución específica por campaña y canal.
- `docs/`: auditorías, contratos locales y puentes de consumo.
- `automation/`: necesidades de tracking y automatización; la lógica transversal viene de GTM y la implementación vive en repos técnicos.
- `templates/`: plantillas específicas de Marketing.
- `assets/`: índices a activos externos; no binarios.
- `core/`: índice de aplicación local y referencias, no fuente canónica.
- `references/`: bibliografía y notas aplicadas, no definiciones corporativas duplicadas.

## Reglas críticas

- No trabajar directo en `main`.
- No modificar campañas, presupuesto, landing, CRM o producción sin autorización explícita.
- No subir PII, credenciales, secretos, exports, capturas sensibles ni binarios.
- No inventar métricas ni claims.
- No redefinir GTM dentro de un brief; proponer cambios mediante evidencia, issue y PR.