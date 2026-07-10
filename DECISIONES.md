# DECISIONES

Registro de decisiones operativas del repo `marketing-performance-capacita`.

## Decisiones vigentes

| Fecha | Decisión | Alcance | Riesgo | Evidencia |
|---|---|---|---:|---|
| 2026-06-21 | Mantener el repo `marketing-performance-capacita` sin renombrar y adoptar el alias operativo **Marketing (Campañas & Growth)**. | Naming, documentación, control operativo | Amarillo | Frontera global; `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` |
| 2026-06-21 | GTM/RevOps es dueño de buyer persona, value persona, segmentación, journey, scoring, nurturing y touch strategy. Marketing queda como ejecución de campañas y performance. | Frontera Marketing / GTM-RevOps | Amarillo | `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` |
| 2026-06-21 | No mover archivos reales desde Marketing a GTM/RevOps sin PR específico y revisado. | Migración documental | Amarillo | `docs/MARKETING_FILE_LEVEL_MIGRATION_PLAN.md` |
| 2026-06-21 | No mover carpetas completas; separar verdad canónica, ejecución táctica y ejecución técnica. | Arquitectura | Amarillo | `docs/MARKETING_FILE_LEVEL_MIGRATION_PLAN.md` |
| 2026-07-10 | Adoptar `docs/GTM_CONSUMPTION_BRIDGE.md` como contrato local obligatorio para campañas nuevas o revisadas. | Campañas y briefs | Amarillo | Global PR #88; Marketing PR #20 |
| 2026-07-10 | Toda campaña debe conservar baseline canónico y aplicación local separados. Usar ID/versión o documento/sección/versión; Marketing no inventa IDs. | Trazabilidad GTM | Amarillo | `templates/CAMPAIGN_BRIEF_GTM.md` |
| 2026-07-10 | Aplicar el contrato primero a Excel presencial V3 sin modificar la campaña real. `BP-001` queda primario y `BP-002` secundario como lectura documental. | Piloto | Verde/Amarillo | `campaigns/excel-basico-intermedio-presencial-santiago/gtm-baseline-v1.md` |
| 2026-07-10 | Para pruebas futuras, separar mensajes de productividad y empleabilidad cuando se quiera medir respuesta por buyer persona. | Diseño experimental | Amarillo | Hallazgo del piloto GTM V1 |
| 2026-07-10 | Mantener cuatro briefs operativos separados para `BP-001` a `BP-004`; `BP-000` es control y no audiencia de campaña. | Arquitectura de campañas | Amarillo | Issue #21; carpeta `briefs/` |
| 2026-07-10 | Ejecutar un buyer persona primario y una hipótesis por prueba. No mezclar B2C y B2B en campaña, landing o medición común. | Experimentación | Amarillo | `briefs/README.md` |
| 2026-07-10 | Priorizar `BP-001` y `BP-002` para creatividad B2C inmediata; `BP-003` y `BP-004` requieren oferta, landing, formulario y ruta comercial B2B verificadas. | Secuencia operativa | Amarillo | Briefs individuales v1.0.0 |

## Reglas derivadas

- Marketing ejecuta campañas, pauta, targeting, copies, activos, performance y aprendizajes tácticos.
- GTM/RevOps mantiene la fuente canónica y su versionado.
- Las campañas históricas conservan el baseline usado; no se reescriben automáticamente.
- La evidencia de una campaña no modifica GTM por sí sola: debe volver mediante issue/PR con alcance e impacto.
- Una prueba de mensaje debe mantener constantes oferta, landing y otras variables relevantes cuando sea viable.
- El paquete de briefs ofrece alternativas; no autoriza activar todas simultáneamente.
- Los ciclos B2B y B2C se miden con criterios diferentes.
- Skills / AI OS mantiene procedimientos reutilizables, no la verdad del negocio.
- Capacita Edge implementa landings y SEO técnico.
- Capacita Zoho Deluge Core implementa campos, API names y código CRM/Deluge.
- WhatsApp + n8n + Zoho implementa workflows, webhooks y mensajería.
- No subir PII, secretos, `.env`, tokens, binarios, exports CRM ni métricas sensibles sin anonimizar.
- No modificar plataformas o producción sin autorización humana explícita.
