# Estado de Tareas

Fecha de revisión: 2026-07-28

## Prioridad activa

Normalizar el frente **Excel B2C pagado** antes de seguir con cambios de campaña, publicación, tracking o integración.

La prioridad inmediata es dejar una fuente mínima en `main` para:

1. tres landings pagadas B2C `noindex,follow`;
2. respuesta XFER de Marketing a Capacita Edge;
3. bloqueo explícito de publicación, tracking, Zoho, PageSense, Turnstile, Cloudflare y Google Ads;
4. reducción de dependencia de PR #35 completo y archivos ubicados solo en ramas.

## Estado PR / Issues principales

| Ítem | Estado | Acción |
|---|---|---|
| Marketing PR #35 | `TRANSITORIO_NO_VIGENTE_EN_MAIN` | No mergear completo. Usar solo como antecedente amplio. |
| Marketing issue #43 | `CIERRE_ADMINISTRATIVO_PENDIENTE` | Cerrar solo después de que el XFER Marketing→Edge quede en main y Edge confirme consumo. |
| Edge PR #36 | `DRAFT / NO_MERGEAR_TODAVIA / REQUIERE_CHECKS` | Esperar respuesta Edge al XFER v02 y resolver bloqueos técnicos/comerciales. |
| Edge XFER v05 | `READY / CONSUMED_WITH_CHANGES` | Consumido por Marketing; versiones anteriores quedan históricas. |
| Marketing XFER v02 | `READY` | Respuesta consolidada en esta rama; queda vigente solo si se mergea el PR. |
| PR #34 PageSense | `RECUPERABLE` | Revisar después de consolidar baseline mínimo para evitar duplicidad. |
| PR #28 Google Ads V02 | `SUPERSEDED/PARCIAL` | No mergear como está. Separar residuales en issues/tareas. |
| PR #39 Office presencial | `BLOQUEADO_POR_ACCESO` | Requiere decisión de Misael sobre OAuth `adwords` o cierre como intento bloqueado. |
| PR #41 Learning Games | `DRAFT / READY COMO XFER` | Revisar como frente separado. |

## Baseline mínimo propuesto

Archivo dueño en esta rama:

```text
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md
```

Define:

- Landing A: Curso Excel Básico–Intermedio presencial, `BP-001`.
- Landing B: Excel desde cero presencial, `BP-002`.
- Landing C: clases de Excel presenciales con profesor, `BP-001`.
- Todas venden el mismo curso grupal presencial Básico–Intermedio en Santiago Centro.
- Todas parten `noindex,follow`, fuera de sitemap y fuera de navegación orgánica.
- La página orgánica actual se conserva protegida.

## XFER vigente de este ciclo

Bitácora:

```text
docs/BITACORA_XFER.md
```

Respuesta Marketing → Edge:

```text
docs/xfer/XFER__MARKETING__CAPACITA_EDGE__EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE__20260728-174500__v02__READY__MARKETING_REVIEW.md
```

Estado:

```text
CONSUMED_WITH_CHANGES
```

## Bloqueos antes de publicar o integrar

No publicar ni integrar las landings hasta resolver:

1. revisión visual humana final en escritorio y celular;
2. `scripts/audit-local.py` en Edge;
3. `git diff --check` en workspace local Edge;
4. `duration`;
5. `download_resource_code`;
6. `course_instance_name`;
7. `CourseInstance` directo en HTML;
8. mapping exacto de Zoho Forms;
9. claims/sellos institucionales;
10. consentimiento de imágenes;
11. autorización explícita para GTM, PageSense, Turnstile, Zoho, endpoints internos y Google Ads.

## Google Ads

Estado documental vigente:

- Basic Access aprobado.
- Procedimiento recurrente de estatus exige doble fuente: export fresco PowerShell/API + `Historial_Rendimiento_GoogleAds`.
- Diagnóstico 90 días quedó documentado en `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md`.
- No se autoriza crear grupos, negativas, anuncios, destinos, presupuesto, pujas ni pausas desde este PR.

## PageSense / CRO

Regla vigente:

- goals de clic no equivalen a leads ni submits confirmados;
- PageSense es complemento de Ads, GA4/GTM y Zoho;
- submit confirmado debe ser la conversión técnica primaria antes de evaluar pauta.

PR #34 queda como candidato recuperable para revisión posterior.

## Reglas operativas vigentes

- No trabajar directo en `main`.
- No modificar campañas, presupuesto, pujas, anuncios, keywords, negativas, conversiones, landings productivas, GTM, PageSense, Turnstile, Zoho, Cloudflare, Worker, DNS ni sitemap sin autorización explícita.
- No subir PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios.
- No inventar métricas, claims, IDs, eventos ni API names.
- Mantener un buyer persona primario y una hipótesis por prueba.
- Separar B2C y B2B en campaña, landing y medición.
- No usar SENCE, franquicia, beneficio tributario, gratuidad ni promesas garantizadas en B2C.

## Secuencia inmediata recomendada

1. Revisar este PR de baseline mínimo.
2. Si está correcto, mergear solo con autorización expresa de Misael.
3. Después, comentar/cerrar Marketing #43 con evidencia del XFER y PR mergeado.
4. Pedir a Edge consumir XFER v02 y reportar estado.
5. Recién después decidir qué hacer con PR #35, PR #34, PR #28 y PR #39.
