# Estado de Tareas

Fecha de revisión: 2026-07-28

## Prioridad activa

Normalizar el frente **Excel B2C pagado**, medición y XFER pendientes antes de seguir con cambios de campaña, publicación, tracking o integración.

Fuente ya vigente en `main`:

```text
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md
```

## Estado PR / Issues principales

| Ítem | Estado | Acción |
|---|---|---|
| Marketing PR #46 | `MERGED / VIGENTE_EN_MAIN` | Baseline mínimo de tres landings B2C pagadas consolidado. |
| Marketing PR #47 | `MERGED / VIGENTE_EN_MAIN` | PageSense/CRO consolidado; PR #34 cerrado como superseded. |
| Marketing PR #35 | `TRANSITORIO / NO_MERGEAR_COMPLETO` | Mantener como antecedente amplio hasta extraer o cerrar lo restante. |
| Marketing issue #43 | `CIERRE_ADMINISTRATIVO_PENDIENTE` | Cerrar solo después de que Edge confirme consumo del XFER Marketing v02. |
| Edge PR #36 | `DRAFT / NO_MERGEAR_TODAVIA / REQUIERE_CHECKS` | Esperar respuesta Edge al XFER v02 y resolver bloqueos técnicos/comerciales. |
| PR #34 PageSense | `CLOSED_SUPERSEDED` | Contenido útil rescatado por PR #47. |
| PR #28 Google Ads V02 | `CLOSED_SUPERSEDED/PARCIAL` | Residuales transferidos a issue #48 y automatización futura a #33. |
| Issue #48 Google Ads residual | `OPEN / MANUAL_PRIVADO` | Auction Insights, reconciliación agregada y cluster `clases/profesor`. |
| PR #39 Office presencial | `BLOQUEADO_POR_ACCESO` | Requiere decisión de Misael sobre OAuth `adwords` o cierre como intento bloqueado. |
| PR #41 Learning Games | `DRAFT / SUPERSEDED_POR_PR_LIMPIO` | No mergear. Rescatar brief vía rama limpia desde `main`. |

## Baseline Excel B2C pagado vigente

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

Brief Marketing → Learning Games:

```text
docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md
```

## PageSense / CRO

Vigente en `main` por PR #47:

```text
docs/pagesense/PAGESENSE_CRO_REPORTING_BASELINE_V01.md
docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md
```

Regla vigente:

- PageSense es fuente complementaria de CRO, no fuente de leads ni matrículas.
- Goals de clic no equivalen a submits confirmados.
- `enviar Pre`, `inicio` y `Enviar Empresa-Excel` son métricas secundarias de interacción mientras no se validen como éxito real.
- Submit confirmado debe basarse en una página de agradecimiento o evento posterior a aceptación real del formulario.
- Zoho CRM sigue siendo fuente de verdad para lead, contactabilidad, cotización y matrícula.

Bloqueo crítico detectado:

```text
Nombre y correo en URL de redirección B2C = riesgo rojo de privacidad.
```

No corregir desde Marketing. Debe enrutarse a Capacita Edge / Zoho con autorización específica.

## Google Ads

Estado documental vigente:

- Basic Access aprobado.
- Procedimiento recurrente de estatus exige doble fuente: export fresco PowerShell/API + `Historial_Rendimiento_GoogleAds`.
- Diagnóstico 90 días quedó documentado en `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md`.
- PR #28 e issue #27 quedaron cerrados como superseded/parcial.
- Issue #48 conserva residuales manuales: Auction Insights nominal, reconciliación agregada y cluster `clases/profesor`.
- Issue #33 conserva automatización futura por API/Drive, sin ejecución hasta nueva autorización.
- No se autoriza crear grupos, negativas, anuncios, destinos, presupuesto, pujas ni pausas desde estos cierres.

## Learning Games XFER

Se normaliza el XFER comercial para `GAME-EXCEL-BASICO-BLOCKS-001` desde una rama limpia creada sobre `main`.

- Output esperado: `docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md`.
- PR #41 queda como antecedente draft, no como PR a mergear.
- Learning Games #6 ya tenía estado `READY_FOR_LEARNING_GAMES_SYNTHESIS`, pero con referencia a PR draft; después del merge del PR limpio debe actualizarse callback hacia versión vigente en main.

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
11. corrección de URL de agradecimiento B2C sin PII;
12. autorización explícita para GTM, PageSense, Turnstile, Zoho, endpoints internos y Google Ads.

## Reglas operativas vigentes

- No trabajar directo en `main`.
- No modificar campañas, presupuesto, pujas, anuncios, keywords, negativas, conversiones, landings productivas, GTM, PageSense, Turnstile, Zoho, Cloudflare, Worker, DNS ni sitemap sin autorización explícita.
- No subir PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios.
- No inventar métricas, claims, IDs, eventos ni API names.
- Mantener un buyer persona primario y una hipótesis por prueba.
- Separar B2C y B2B en campaña, landing y medición.
- No usar SENCE, franquicia, beneficio tributario, gratuidad ni promesas garantizadas en B2C.

## Secuencia inmediata recomendada

1. Revisar y mergear el PR limpio Learning Games XFER si sigue documental.
2. Cerrar PR #41 como `SUPERSEDED` después de mergear el nuevo PR.
3. Actualizar Marketing #40 y Learning Games #6 con callback nuevo desde `main`.
4. Mantener issue #43 abierto hasta que Edge confirme consumo del XFER Marketing v02.
5. Luego decidir PR #39 Office presencial y el cierre administrativo de PR #35.
