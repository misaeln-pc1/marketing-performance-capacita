# Estado de Tareas

Fecha de revision: 2026-07-28

## Prioridad activa

Normalizar frentes documentales pendientes antes de seguir con cambios de campana, publicacion, tracking o integracion.

Fuente vigente Excel B2C pagado:

```text
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md
```

## Estado PR / Issues principales

| Item | Estado | Accion |
|---|---|---|
| Marketing PR #46 | `MERGED / VIGENTE_EN_MAIN` | Baseline minimo de tres landings B2C pagadas consolidado. |
| Marketing PR #47 | `MERGED / VIGENTE_EN_MAIN` | PageSense/CRO consolidado; PR #34 cerrado como superseded. |
| Marketing PR #49 | `MERGED / VIGENTE_EN_MAIN` | XFER comercial Learning Games consolidado; PR #41 cerrado como superseded. |
| Marketing PR #35 | `TRANSITORIO / NO_MERGEAR_COMPLETO` | Mantener como antecedente amplio hasta extraer o cerrar lo restante. |
| Marketing issue #43 | `CIERRE_ADMINISTRATIVO_PENDIENTE` | Cerrar solo despues de que Edge confirme consumo del XFER Marketing v02. |
| Edge PR #36 | `DRAFT / NO_MERGEAR_TODAVIA / REQUIERE_CHECKS` | Esperar respuesta Edge al XFER v02 y resolver bloqueos tecnicos/comerciales. |
| PR #34 PageSense | `CLOSED_SUPERSEDED` | Contenido util rescatado por PR #47. |
| PR #28 Google Ads V02 | `CLOSED_SUPERSEDED/PARCIAL` | Residuales transferidos a issue #48 y automatizacion futura a #33. |
| Issue #48 Google Ads residual | `OPEN / MANUAL_PRIVADO` | Auction Insights, reconciliacion agregada y cluster `clases/profesor`. |
| PR #39 Office presencial | `CLOSED_BLOCKED_NOT_MERGED` | Intento bloqueado por OAuth/scope; reintento futuro en issue #50. |
| Issue #50 Office Ads | `OPEN / FUTURE_RETRY_ONLY` | Reintentar keyword research solo con OAuth `adwords`, curso y landing autorizados. |
| PR #41 Learning Games | `CLOSED_SUPERSEDED` | Contenido util rescatado por PR #49. |
| PR #8 Meta Ads Standard | `OPEN / SUPERSEDED_POR_PR_LIMPIO` | No mergear rama antigua. Rescatar estandar de creatividades via PR limpio desde `main`. |

## Baseline Excel B2C pagado vigente

Define:

- Landing A: Curso Excel Basico-Intermedio presencial, `BP-001`.
- Landing B: Excel desde cero presencial, `BP-002`.
- Landing C: clases de Excel presenciales con profesor, `BP-001`.
- Todas venden el mismo curso grupal presencial Basico-Intermedio en Santiago Centro.
- Todas parten `noindex,follow`, fuera de sitemap y fuera de navegacion organica.
- La pagina organica actual se conserva protegida.

## XFER vigente de este ciclo

Bitacora:

```text
docs/BITACORA_XFER.md
```

Respuesta Marketing -> Edge:

```text
docs/xfer/XFER__MARKETING__CAPACITA_EDGE__EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE__20260728-174500__v02__READY__MARKETING_REVIEW.md
```

Brief Marketing -> Learning Games:

```text
docs/xfer/GAME-EXCEL-BASICO-BLOCKS-001/MARKETING_BRIEF.md
```

## Meta Ads / Facebook Ads

Estandar de produccion de creatividades Meta Ads rescatado y actualizado desde PR #8 mediante rama limpia:

```text
assets/meta-ads/PRODUCTION_STANDARD_META_ADS.md
```

Reglas vigentes propuestas:

- cada creatividad debe tener set por placement, no una sola pieza reutilizada para todo;
- imagenes minimas: 4:5, 1:1 y 9:16;
- videos minimos por placement: 9:16 para Stories/Reels y 4:5 para Feed si se activa Feed;
- no usar video 9:16 como unico video para todos los placements;
- no subir JPG/PNG/WEBP/MP4/MOV/PSD/AI/Canva/fuentes ni previews sensibles a GitHub;
- archivos reales van en `external-files/marketing-performance-capacita/meta-ads/...` o bodega SharePoint/OneDrive documentada;
- el routing de cuenta Meta Ads sigue en `docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md`.

Este estandar no autoriza publicar anuncios ni modificar Meta Ads Manager.

## PageSense / CRO

Vigente en `main` por PR #47:

```text
docs/pagesense/PAGESENSE_CRO_REPORTING_BASELINE_V01.md
docs/pagesense/PAGESENSE_GOAL_CONFIGURATION_AUDIT_2026-07-12.md
```

Regla vigente:

- PageSense es fuente complementaria de CRO, no fuente de leads ni matriculas.
- Goals de clic no equivalen a submits confirmados.
- `enviar Pre`, `inicio` y `Enviar Empresa-Excel` son metricas secundarias de interaccion mientras no se validen como exito real.
- Submit confirmado debe basarse en una pagina de agradecimiento o evento posterior a aceptacion real del formulario.
- Zoho CRM sigue siendo fuente de verdad para lead, contactabilidad, cotizacion y matricula.

Bloqueo critico detectado:

```text
Nombre y correo en URL de redireccion B2C = riesgo rojo de privacidad.
```

No corregir desde Marketing. Debe enrutarse a Capacita Edge / Zoho con autorizacion especifica.

## Google Ads

Estado documental vigente:

- Basic Access aprobado.
- Procedimiento recurrente de estatus exige doble fuente: export fresco PowerShell/API + `Historial_Rendimiento_GoogleAds`.
- Diagnostico 90 dias quedo documentado en `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_BASELINE_2026-07-11.md`.
- PR #28 e issue #27 quedaron cerrados como superseded/parcial.
- Issue #48 conserva residuales manuales: Auction Insights nominal, reconciliacion agregada y cluster `clases/profesor`.
- Issue #33 conserva automatizacion futura por API/Drive, sin ejecucion hasta nueva autorizacion.
- Issue #50 conserva reintento futuro Office Ads con OAuth `adwords`, sin ejecucion hasta nueva autorizacion.
- No se autoriza crear grupos, negativas, anuncios, destinos, presupuesto, pujas ni pausas desde estos cierres.

## Bloqueos antes de publicar o integrar

No publicar ni integrar las landings hasta resolver:

1. revision visual humana final en escritorio y celular;
2. `scripts/audit-local.py` en Edge;
3. `git diff --check` en workspace local Edge;
4. `duration`;
5. `download_resource_code`;
6. `course_instance_name`;
7. `CourseInstance` directo en HTML;
8. mapping exacto de Zoho Forms;
9. claims/sellos institucionales;
10. consentimiento de imagenes;
11. correccion de URL de agradecimiento B2C sin PII;
12. autorizacion explicita para GTM, PageSense, Turnstile, Zoho, endpoints internos y Google Ads.

## Reglas operativas vigentes

- No trabajar directo en `main`.
- No modificar campanas, presupuesto, pujas, anuncios, keywords, negativas, conversiones, landings productivas, GTM, PageSense, Turnstile, Zoho, Cloudflare, Worker, DNS ni sitemap sin autorizacion explicita.
- No subir PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios.
- No inventar metricas, claims, IDs, eventos ni API names.
- Mantener un buyer persona primario y una hipotesis por prueba.
- Separar B2C y B2B en campana, landing y medicion.
- No usar SENCE, franquicia, beneficio tributario, gratuidad ni promesas garantizadas en B2C.

## Secuencia inmediata recomendada

1. Revisar y mergear el PR limpio Meta Ads production standard si sigue documental.
2. Cerrar PR #8 como `SUPERSEDED` despues de mergear el nuevo PR.
3. Mantener issue #43 abierto hasta que Edge confirme consumo del XFER Marketing v02.
4. Luego decidir cierre administrativo de PR #35.