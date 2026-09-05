# Project Context: Marketing Performance Capacita

## Visión

Repositorio operativo y liviano de **Marketing, Growth, Performance y Market Intelligence** para convertir demanda, campañas, comportamiento web y resultados comerciales agregados en decisiones, experimentos y mejoras trazables para Capacita.

Marketing no es sólo auditor ni receptor de solicitudes. Debe detectar oportunidades, priorizar la siguiente mejor acción y producir especificaciones ejecutables para los repos o agentes que implementan.

## Objetivo operativo

Para cada frente material:

```text
MEDIR
→ DIAGNOSTICAR
→ PRIORIZAR
→ ESPECIFICAR
→ DERIVAR/IMPLEMENTAR CON AUTORIZACION
→ VALIDAR
→ APRENDER
```

No optimizar métricas aisladas perjudicando adquisición, conversión, calidad del lead, venta, marca o mantenibilidad.

## Fuentes de verdad

- **GTM / RevOps en Global:** buyer personas, propuestas de valor, segmentación transversal, customer journey, scoring, nurturing, touch strategy y criterios comerciales.
- **Este repositorio:** campañas, hipótesis tácticas, targeting, copies, criterios visuales, medición, análisis, oportunidades y aprendizajes agregados.
- **Zoho CRM:** leads, contactos, deals, seguimiento comercial y resultados reales, sólo mediante acceso autorizado y evidencia agregada.
- **SharePoint Site:** fuente canónica de fotos, videos, creatividades finales, exports pesados y archivos multimedia en `Documentos/CAPACITA/Proyectos/external-files/marketing-performance-capacita`.
- **OneDrive `Sitio de comunicación - external-files`:** acceso local sincronizado a SharePoint, no segunda bodega.
- **Meta Ads / Google Ads / LinkedIn Ads:** campañas activas, públicos, anuncios, presupuestos y métricas operativas.
- **GSC / GA4 / PageSense:** consultas, páginas, sesiones, eventos y comportamiento web según su cobertura real.
- **Capacita Edge:** landings, formularios, SEO técnico y eventos frontend.
- **AI OS:** capacidades y patrones reutilizables; no fuente de verdad comercial.

Google Drive, Cloudflare R2 u otras capas sólo se usan cuando existe una decisión específica documentada. Este repositorio no reemplaza ninguna fuente operativa.

## Contrato de consumo

Toda campaña nueva o revisada debe aplicar:

- `docs/GTM_CONSUMPTION_BRIDGE.md`;
- `templates/CAMPAIGN_BRIEF_GTM.md`;
- `docs/analytics/MARKETING_PROACTIVE_OPPORTUNITY_SCAN_V01.md`;
- `docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md` cuando exista página o landing.

Debe registrar:

- decisión de negocio;
- buyer persona y versión;
- propuesta de valor y etapa del journey;
- hipótesis táctica diferenciada;
- fuentes consultadas y data gaps;
- CTA, destino, pain signals y medición;
- acción priorizada, dueño y validación;
- aprendizaje que podría volver a GTM o AI OS.

## Continuidad operativa

Antes de recomendar sobre un frente ya trabajado, consultar `TASK_STATUS.md`, `DECISIONES.md`, el documento canónico específico y sólo los PR/issues recientes que aporten estado no consolidado. No reconstruir estrategia desde cero; analizar evidencia nueva o delta.

## Proactividad y herramientas

Cuando una fuente conectada READ pueda reducir copia manual, errores o latencia, Marketing debe usarla sin esperar una petición granular. La recomendación debe apoyarse en evidencia real o declarar `DATA_GAP`.

Las herramientas de lectura no autorizan escrituras. Nuevos OAuth/scopes, instalaciones, costos, PII, campañas reales, presupuestos, CRM, producción o automatización conservan sus gates.

## Arquitectura base

- `campaigns/`: ejecución específica por campaña y canal.
- `docs/analytics/`: contratos de análisis, oportunidad y atribución.
- `docs/seo-ai/`: visibilidad, SEO/AEO/GEO y protocolos de páginas.
- `docs/google-ads/`, `docs/meta-ads/`, `docs/pagesense/`: canónicos por plataforma.
- `docs/xfer/`: handoffs trazables entre proyectos.
- `automation/`: requerimientos de tracking/automatización; no implementación productiva.
- `templates/`: plantillas específicas de Marketing.
- `assets/`: índices y criterios de recursos externos, no binarios.
- `core/`: índice de consumo y aplicación local.
- `references/`: bibliografía y notas metodológicas aplicadas.

No crear carpetas paralelas si un frente ya tiene dueño.

## Campaña inicial

- Curso: Excel Básico–Intermedio Presencial en Santiago Centro.
- Canales documentados: Meta Ads y Google Ads read-only.
- Buyer personas canónicos:
  - `BP-001 — Desbordado Operativo`, v1.0.0;
  - `BP-002 — Reinserción Laboral`, v1.0.0.
- Propuestas aplicadas: capacitación práctica y guiada; experiencia presencial céntrica; productividad; empleabilidad; reducción de fricción logística.
- Journey inicial: visitante/audiencia fría hacia lead identificado.

Precio, fechas, cupos, dirección, medios de pago y materiales exactos deben confirmarse antes de publicar.

## Reglas de alcance

- No redefinir en Marketing los canónicos GTM/RevOps.
- No copiar evidencia privada de Global, plataformas o CRM al repo público.
- No subir datos personales, credenciales, tokens, fotos, videos o archivos pesados.
- No modificar landing, campañas o tracking de producción sin hipótesis documentada y autorización.
- No confundir conversiones de plataforma con leads, deals, CursoAlumno o ventas.
- No crear archivos sin utilidad práctica.
- Priorizar estructura simple, reutilizable y mantenible.

## Roles

- **GTM / RevOps:** dueño del modelo comercial corporativo y de sus canónicos.
- **Marketing:** dueño de adquisición táctica, análisis de performance, demanda/intención, aplicación de buyer persona, criterios de creatividad/landing, CRO, hipótesis, medición y aprendizaje.
- **ChatGPT / Atlas:** lead analítico y controlador de Growth; consulta fuentes, descubre oportunidades, prioriza, especifica y audita sin ejecutar writes no autorizados.
- **Capacita Edge:** dueño de implementación web, SEO técnico y tracking frontend.
- **Agente ejecutor:** modifica archivos acotados en rama/PR según un handoff, sin redefinir estrategia ni tocar producción fuera del permiso.
- **Misael:** aprueba cambios de campaña, presupuesto, producción, permisos, merge/main y decisiones materiales de inversión.
