# DECISIONES

Registro de decisiones operativas del repo `marketing-performance-capacita`.

## Decisiones vigentes

| Fecha | Decisión | Alcance | Riesgo | Evidencia |
|---|---|---|---:|---|
| 2026-06-21 | Mantener el repo `marketing-performance-capacita` sin renombrar y adoptar el alias operativo **Marketing (Campañas & Growth)**. | Naming, documentación, control operativo | Amarillo | Frontera global aprobada en `capacita-global-control` PR #27; `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` |
| 2026-06-21 | GTM/RevOps es dueño de buyer persona, value persona, segmentación, journey, scoring, nurturing y touch strategy. Marketing queda como ejecución de campañas y performance. | Frontera Marketing / GTM-RevOps | Amarillo | `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` |
| 2026-06-21 | No mover archivos reales desde Marketing a GTM/RevOps en esta fase. Cualquier migración física debe hacerse por PR posterior específico y revisado. | Migración documental | Amarillo | `docs/MARKETING_GTM_REVOPS_CLASSIFICATION.md` |
| 2026-06-21 | Registrar como incidencia la creación accidental directa en `main` de archivos documentales durante la clasificación, y corregir mediante rama/PR correctivo. | Gobernanza GitHub | Amarillo | Rama `docs/fix-marketing-gtm-classification-followup-2026-06-21` |

## Reglas derivadas

- Marketing (Campañas & Growth) ejecuta campañas, pauta, copies, assets documentales, performance y aprendizajes tácticos.
- GTM/RevOps define estrategia comercial transversal y debe ser fuente canónica cuando haya riesgo de duplicidad.
- Skills / AI OS mantiene capacidades reutilizables, no la verdad del negocio.
- Capacita Edge implementa landings y SEO técnico.
- Capacita Zoho Deluge Core implementa código CRM/Deluge.
- WhatsApp + n8n + Zoho implementa workflows, webhooks y mensajería.
- No subir PII, secretos, `.env`, tokens, binarios, exportaciones CRM ni métricas sensibles sin anonimizar.
