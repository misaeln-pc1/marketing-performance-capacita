# REVIEW_REQUEST

## PR objetivo

Corrección documental posterior a la clasificación Marketing / GTM-RevOps.

## Resumen

Este cambio deja el repo `marketing-performance-capacita` alineado con la frontera global aprobada entre Marketing (Campañas & Growth), GTM/RevOps, Skills/AI OS, Capacita Edge, Capacita Zoho Deluge Core y WhatsApp + n8n + Zoho.

También registra la incidencia operativa ocurrida durante la ejecución: se creó documentación directamente en `main` por error. El contenido fue reemplazado por una clasificación válida y este PR agrega la trazabilidad faltante.

## Archivos esperados

- `TASK_STATUS.md`: actualiza estado, próxima acción, bloqueos y reglas de alcance.
- `DECISIONES.md`: crea registro de decisiones del repo.
- `REVIEW_REQUEST.md`: actualiza esta solicitud de revisión.
- `docs/.gitkeep`: se elimina porque `docs/` ya contiene documentación real.

## No se toca

- No se modifican campañas reales.
- No se toca Meta Ads, Google Ads, Zoho, n8n, WhatsApp, Cloudflare ni producción.
- No se suben datos personales, credenciales, archivos de configuración sensible ni binarios.
- No se mueven archivos reales entre carpetas.
- No se renombra el repo.

## Validación esperada

- Solo cambios documentales y eliminación de `.gitkeep` redundante.
- `marketing-performance-capacita` mantiene su nombre físico.
- Marketing queda como ejecución de campañas/performance.
- GTM/RevOps queda como fuente de estrategia comercial transversal.
- Skills / AI OS queda como biblioteca de capacidades reutilizables.

## Recomendación

Mergear si el diff confirma que solo se actualizaron documentos y se eliminó el `.gitkeep` redundante.
