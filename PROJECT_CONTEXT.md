# Project Context: Marketing Performance Capacita

## Visión

Repositorio operativo y liviano de **Marketing (Campañas & Growth)** para ejecutar y aprender de campañas comerciales-publicitarias de Capacita.

## Fuentes de verdad

- **GTM / RevOps en Global:** buyer personas, propuestas de valor, segmentación transversal, customer journey, scoring, nurturing, touch strategy y criterios comerciales.
- **Este repositorio:** campañas, hipótesis tácticas, targeting, copies, activos documentales, medición y aprendizajes agregados.
- **Zoho CRM:** leads, contactos, deals, seguimiento comercial y resultados reales.
- **Google Drive:** fotos, videos, creatividades finales, exports pesados y archivos multimedia.
- **Meta Ads / Google Ads / LinkedIn Ads:** campañas activas, públicos, anuncios, presupuestos y métricas operativas.
- **Capacita Edge:** landings, formularios, SEO técnico y eventos frontend.

Este repositorio no reemplaza ninguna de esas fuentes.

## Contrato de consumo

Toda campaña nueva o revisada debe aplicar:

- `docs/GTM_CONSUMPTION_BRIDGE.md`;
- `templates/CAMPAIGN_BRIEF_GTM.md`.

Debe registrar:

- buyer persona e versión;
- propuesta de valor y etapa del journey;
- hipótesis táctica diferenciada;
- CTA, destino y medición;
- aprendizaje que podría volver a GTM.

## Arquitectura base

- `campaigns/`: ejecución específica por campaña y canal.
- `docs/`: auditorías, metodología local y puentes.
- `automation/`: requerimientos de tracking y automatización; no implementación productiva.
- `templates/`: plantillas específicas de Marketing.
- `assets/`: índice a recursos externos.
- `core/`: índice de consumo y aplicación local.
- `references/`: bibliografía y notas metodológicas aplicadas.

## Campaña inicial

- Curso: Excel Básico–Intermedio Presencial en Santiago Centro.
- Canales documentados: Meta Ads y radar Google Ads read-only.
- Buyer personas canónicos:
  - `BP-001 — Desbordado Operativo`, v1.0.0;
  - `BP-002 — Reinserción Laboral`, v1.0.0.
- Propuestas aplicadas: capacitación práctica y guiada; experiencia presencial céntrica; productividad; empleabilidad; reducción de fricción logística.
- Journey inicial: visitante/audiencia fría hacia lead identificado.

Los detalles de precio, fechas, cupos, dirección, medios de pago y materiales exactos son datos tácticos que deben confirmarse antes de publicar.

## Reglas de alcance

- No redefinir en Marketing los canónicos GTM/RevOps.
- No copiar evidencia privada de Global o CRM al repo público.
- No subir datos personales, credenciales, tokens, fotos, videos o archivos pesados.
- No modificar landing o campañas de producción sin hipótesis documentada y autorización.
- No crear archivos sin utilidad práctica.
- Priorizar estructura simple, reutilizable y mantenible.

## Roles

- **GTM / RevOps:** dueño del modelo comercial corporativo.
- **Marketing:** dueño de la aplicación táctica y el aprendizaje de campañas.
- **ChatGPT / Atlas:** auditor de arquitectura, límites, trazabilidad y riesgos.
- **Agente ejecutor:** modifica archivos acotados en rama/PR sin redefinir estrategia ni tocar producción.