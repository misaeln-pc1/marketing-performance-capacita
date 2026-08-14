# Estado de Tareas

Fecha de revision: 2026-08-13

## Prioridad activa

Continuar el frente Google Ads B2C Excel presencial A/B/C sin reabrir decisiones ya canonizadas y mantener sincronizada la memoria operativa del repo.

Fuente vigente Excel B2C pagado:

```text
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md
```

Política canónica de negativas:

```text
docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md
```

## Regla de continuidad

Antes de recomendar sobre un frente ya trabajado, leer `DECISIONES.md`, este archivo y el documento canónico específico. Aplicar primero la decisión vigente y analizar solo evidencia nueva o delta. No reiniciar estrategia desde recomendaciones genéricas de plataforma.

## Estado PR / Issues principales

| Item | Estado | Accion |
|---|---|---|
| Marketing PR #58 | `MERGED / VIGENTE_EN_MAIN` | Política canónica de negativas Google Ads por intención. |
| Marketing issue #56 | `CLOSED_COMPLETED` | Regla de negativas consolidada en PR #58. |
| Marketing issue #57 | `CLOSED_DUPLICATE` | Duplicado de #56; no usar como fuente paralela. |
| Marketing PR #54 / #55 | `MERGED / VIGENTE_EN_MAIN` | Routing Meta Ads corregido y marcado canónico. |
| Marketing PR #51 | `MERGED / VIGENTE_EN_MAIN` | Estándar de producción Meta Ads vigente. |
| Marketing PR #8 | `CLOSED_SUPERSEDED` | Sustituido por PR #51; no usar como pendiente activo. |
| Marketing PR #46 | `MERGED / VIGENTE_EN_MAIN` | Baseline mínimo de tres landings B2C pagadas consolidado. |
| Marketing PR #47 | `MERGED / VIGENTE_EN_MAIN` | PageSense/CRO consolidado; PR #34 superseded. |
| Marketing PR #49 | `MERGED / VIGENTE_EN_MAIN` | XFER comercial Learning Games consolidado; PR #41 superseded. |
| Marketing PR #35 | `HISTORICO / NO_GOBIERNA_CONTEXTO_ACTUAL` | Material parcialmente absorbido por PR #46 y issues posteriores; no mergear completo sin auditoría residual específica. |
| Marketing PR #45 | `HISTORICO / AUDITORIA_SUPERADA` | Auditoría previa al PR #46; no usar como review vigente. |
| Marketing PR #52 | `OPEN / REVISION_TECNICA_PENDIENTE` | Procedimiento/script Meta Ads read-only; conservar separado hasta revisión específica. |
| Marketing issue #43 | `OPEN / XFER_EDGE` | Revisar estado solo al retomar handoff Edge; no mezclar con Google Ads negativas. |
| Issue #48 Google Ads residual | `OPEN / MANUAL_PRIVADO` | Auction Insights, reconciliación agregada y cluster `clases/profesor`. |
| Issue #50 Office Ads | `OPEN / FUTURE_RETRY_ONLY` | Reintentar keyword research solo con OAuth `adwords`, curso y landing autorizados. |
| Issue #53 Google Ads B2B | `BACKLOG / NO_EJECUTAR_AHORA` | Frente separado posterior al B2C A/B/C. |
| Issue #23 instrucciones | `OPEN / DESACTUALIZADO_PENDIENTE_GLOBAL` | V1 ya no representa literalmente las instrucciones actuales del Proyecto ChatGPT; requiere sincronización en Global. |

## Google Ads — regla vigente de negativas

PR #58 consolidó:

- priorizar intención de asistir/comprar curso;
- preservar negativas históricas de solución puntual mientras no exista evidencia que justifique retirarlas;
- excluir deliberadamente intención informativa puntual y empleo cuando corresponda;
- `paso a paso` no es negativa global;
- separar exclusión global de tráfico versus routing A/B/C a nivel grupo;
- no modificar listas reales sin autorización explícita.

## Baseline Excel B2C pagado vigente

- Landing A: Curso Excel Básico-Intermedio presencial, `BP-001`.
- Landing B: Excel desde cero presencial, `BP-002`.
- Landing C: clases de Excel presenciales con profesor, `BP-001`.
- Las tres venden el mismo curso grupal presencial Básico-Intermedio en Santiago Centro.
- Parten `noindex,follow`, fuera de sitemap y fuera de navegación orgánica.
- La página orgánica actual se conserva protegida.

## Meta Ads / Facebook Ads

Fuentes vigentes:

```text
assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md
docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md
```

Reglas críticas:

- cuenta operativa V3: cuenta personal/standalone bajo `Otros activos`, referencia sanitizada `...2327`;
- no identificar la cuenta por Business Portfolio;
- no propagar restricciones históricas entre activos sin evidencia;
- creatividades como set por placement; video 9:16 para Stories/Reels y 4:5 para Feed cuando aplique;
- no subir assets pesados a GitHub.

## PageSense / CRO

Fuentes vigentes:

```text
docs/pagesense/PAGESENSE_CRO_REPORTING_BASELINE_V01.md
docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md
```

- PageSense es fuente complementaria de CRO, no fuente de leads ni matrículas.
- Goals de clic no equivalen a submits confirmados.
- Zoho CRM sigue siendo fuente de verdad comercial.
- Nombre/correo en URL de redirección B2C sigue siendo riesgo rojo de privacidad y debe resolverse fuera de Marketing con autorización específica.

## Archivos pesados

- GitHub conserva Markdown, manifests, hashes, síntesis y trazabilidad liviana.
- Bodega definitiva del proyecto: SharePoint/OneDrive Empresa, con staging local en `external-files/marketing-performance-capacita` cuando corresponda.
- No tratar Google Drive ni Cloudflare R2 como bóveda canónica general de Marketing salvo caso específico documentado y aprobado.

## Reglas operativas vigentes

- No trabajar directo en `main`.
- No modificar campañas, presupuesto, pujas, anuncios, keywords, negativas, conversiones, landings productivas, GTM, PageSense, Turnstile, Zoho, Cloudflare, Worker, DNS ni sitemap sin autorización explícita.
- No subir PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios.
- No inventar métricas, claims, IDs, eventos ni API names.
- Mantener un buyer persona primario y una hipótesis por prueba.
- Separar B2C y B2B en campaña, landing y medición.
- No usar SENCE, franquicia, beneficio tributario, gratuidad ni promesas garantizadas en B2C.

## Secuencia inmediata

1. Mergear primero este saneamiento documental cuando sea aprobado.
2. Sincronizar en Global las instrucciones realmente activas del Proyecto Marketing y preparar la versión corregida con regla anti-reinicio.
3. Retomar Google Ads B2C A/B/C leyendo la política canónica de negativas antes de recomendar cambios.
4. Revisar PR #52 por separado si se necesita reactivar la ruta técnica Meta Ads read-only.
