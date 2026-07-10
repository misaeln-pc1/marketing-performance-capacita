# REVIEW_REQUEST

## PR objetivo

Crear un paquete de briefs operativos para los cuatro buyer personas activos de GTM/RevOps, aplicado a Excel presencial Santiago.

## Issue

[#21 — Crear briefs operativos para los buyer personas activos](https://github.com/misaeln-pc1/marketing-performance-capacita/issues/21)

## Contexto

Global PR #88 dejó buyer personas versionados y Marketing PR #20 dejó el contrato de consumo. Faltaba transformar ese baseline en documentos concretos para comenzar trabajo creativo y campañas sin mezclar perfiles ni redefinir GTM.

## Cambios

Crea:

- `campaigns/excel-basico-intermedio-presencial-santiago/briefs/README.md`;
- `BRIEF_BP001_DESBORDADO_OPERATIVO_V1.md`;
- `BRIEF_BP002_REINSERCION_LABORAL_V1.md`;
- `BRIEF_BP003_COORDINADOR_B2B_V1.md`;
- `BRIEF_BP004_JEFATURA_PYME_V1.md`.

Actualiza:

- `campaigns/README.md`;
- `TASK_STATUS.md`;
- `DECISIONES.md`;
- `CHANGELOG_AGENT.md`;
- `REVIEW_REQUEST.md`.

## Criterio aplicado

- Existen cuatro buyer personas activos: `BP-001` a `BP-004`.
- `BP-000` es control para evidencia insuficiente y no una audiencia.
- Cada brief tiene un buyer persona primario, una hipótesis, una promesa, CTA, rutas creativas, targeting táctico, claims, destino, métricas y pendientes.
- `BP-001` y `BP-002` se preparan para creatividad B2C inmediata.
- `BP-003` y `BP-004` quedan condicionados a oferta, landing, formulario y ruta CRM B2B.
- No se mezclan B2C y B2B en campaña o medición común.

## Orden recomendado

1. `BP-001 — Desbordado Operativo`.
2. `BP-002 — Reinserción Laboral`.
3. `BP-003 — Coordinador B2B`.
4. `BP-004 — Dueño o Jefatura PyME`.

El orden no cambia el estado canónico de los perfiles. Es una decisión operativa basada en la preparación actual de oferta y landing.

## No se toca

- No se crean ni modifican campañas reales.
- No se modifican presupuestos, pujas, anuncios, públicos o plataformas Ads.
- No se modifica landing, Cloudflare, Zoho, n8n, WhatsApp o formularios reales.
- No se suben datos personales, exports, credenciales, tokens, IDs completos o binarios.
- No se inventan métricas o resultados.
- No se garantizan empleo, productividad, ahorro o ROI.

## Validación esperada

- Cambios Markdown solamente.
- Rama basada en `main` después del merge de PR #20.
- Sin borrados ni renombres.
- Cuatro briefs independientes y un índice.
- Referencias GTM versionadas.
- Claims y datos pendientes visibles.
- Estado y decisiones actualizados.

## Riesgo

**Amarillo metodológico:** los briefs condicionan futuras campañas. Se mitiga con un perfil por prueba, separación B2C/B2B, versionado, claims limitados y autorización previa a producción.

## Siguiente paso después del merge

Confirmar los datos tácticos del curso y comenzar desarrollo creativo con `BP-001`, sin activar campañas hasta validar landing, tracking y autorización.

## Decisión solicitada

- [ ] APROBADO PARA MERGE
- [ ] CORREGIR ANTES DE MERGE
