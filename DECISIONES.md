# DECISIONES

Registro de decisiones operativas del repo `marketing-performance-capacita`.

## Decisiones vigentes

| Fecha | Decisión | Alcance | Riesgo | Evidencia |
|---|---|---|---:|---|
| 2026-06-21 | Mantener el repo `marketing-performance-capacita` sin renombrar y adoptar el alias operativo **Marketing (Campañas & Growth)**. | Naming, documentación, control operativo | Amarillo | Frontera global; `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` |
| 2026-06-21 | GTM/RevOps es dueño de buyer persona, value persona, segmentación, journey, scoring, nurturing y touch strategy. Marketing queda como ejecución de campañas y performance. | Frontera Marketing / GTM-RevOps | Amarillo | `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` |
| 2026-06-21 | No mover archivos reales desde Marketing a GTM/RevOps sin PR específico y revisado. | Migración documental | Amarillo | `docs/MARKETING_FILE_LEVEL_MIGRATION_PLAN.md` |
| 2026-06-21 | No mover carpetas completas; separar verdad canónica, ejecución táctica y ejecución técnica. | Arquitectura | Amarillo | `docs/MARKETING_FILE_LEVEL_MIGRATION_PLAN.md` |
| 2026-07-10 | Adoptar `docs/GTM_CONSUMPTION_BRIDGE.md` como contrato local obligatorio para campañas nuevas o revisadas. | Campañas y briefs | Amarillo | Global PR #88; issue #19 |
| 2026-07-10 | Toda campaña debe conservar baseline canónico y aplicación local separados. Usar ID/versión o documento/sección/versión; Marketing no inventa IDs. | Trazabilidad GTM | Amarillo | `templates/CAMPAIGN_BRIEF_GTM.md` |
| 2026-07-10 | Aplicar el contrato primero a Excel presencial V3 sin modificar la campaña real. `BP-001` queda primario y `BP-002` secundario como lectura documental. | Piloto | Verde/Amarillo | `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md` |
| 2026-07-10 | Para pruebas futuras, separar mensajes de productividad y empleabilidad cuando se quiera medir respuesta por buyer persona. | Diseño experimental | Amarillo | Hallazgo del piloto GTM V1 |

## Reglas derivadas

- Marketing ejecuta campañas, pauta, targeting, copies, activos, performance y aprendizajes tácticos.
- GTM/RevOps mantiene la fuente canónica y su versionado.
- Las campañas históricas conservan el baseline usado; no se reescriben automáticamente.
- La evidencia de una campaña no modifica GTM por sí sola: debe volver mediante issue/PR con alcance e impacto.
- Skills / AI OS mantiene procedimientos reutilizables, no la verdad del negocio.
- Capacita Edge implementa landings y SEO técnico.
- Capacita Zoho Deluge Core implementa campos, API names y código CRM/Deluge.
- WhatsApp + n8n + Zoho implementa workflows, webhooks y mensajería.
- No subir PII, secretos, `.env`, tokens, binarios, exports CRM ni métricas sensibles sin anonimizar.
- No modificar plataformas o producción sin autorización humana explícita.