# XFER — Marketing → Capacita Edge — Respuesta revisión landings Excel B2C pagadas

Estado: `READY`

Productor: `Marketing Performance`

Consumidor: `Capacita Edge`

Caso: `EXCEL_B2C_PAID_LANDINGS_REVIEW_RESPONSE`

Versión: `v02`

Fecha-hora: `20260728-174500`

Repo productor: `misaeln-pc1/marketing-performance-capacita`

Repo destino: `misaeln-pc1/capacita-edge`

PR destino: `#36`

Rama destino: `feature/edge-excel-b2c-paid-landings-v1`

## 1. XFER consumido

Marketing consume como versión vigente de revisión:

```text
docs/xfer/XFER__CAPACITA_EDGE__MARKETING__EXCEL_B2C_PAID_LANDINGS_REVIEW__20260727-041500__v05__READY__LANDING_REVIEW_REQUEST.md
```

No consumir versiones anteriores v01, v02, v03 o v04 para este caso salvo revisión histórica.

## 2. Resultado de consumo

```text
CONSUMED_WITH_CHANGES
```

Motivo:

- la arquitectura de tres landings A/B/C es comercialmente válida como piloto pagado `noindex,follow`;
- las tres deben mantenerse fuera de sitemap y navegación orgánica;
- la página orgánica actual debe conservarse protegida;
- Edge ya aplicó correcciones relevantes de preview;
- persisten bloqueos comerciales/técnicos antes de publicación, integración o tráfico real.

## 3. Veredicto por landing

| Landing | Veredicto Marketing | Condición |
|---|---|---|
| A — Básico–Intermedio | `CONSUMED_WITH_CHANGES` | Mantener intención, noindex y medición propia. Bloqueada para producción hasta resolver slots, checks y tracking. |
| B — Desde cero | `CONSUMED_WITH_CHANGES` | Mantener intención y buyer persona. Bloqueada para producción hasta resolver slots, checks y tracking. |
| C — Clases con profesor | `CONSUMED_WITH_CHANGES` | Mantener solo si el copy representa un curso grupal presencial y no clases particulares/domicilio/uno a uno. |

## 4. Copy y promesa obligatoria

Landing C puede usar copy compatible con intención de búsqueda:

```text
clases de Excel presenciales
clases con profesor
profesor de Excel presencial
```

pero debe mantener explícita o naturalmente esta verdad comercial:

```text
Curso grupal presencial con profesor en vivo.
No corresponde a clases particulares, atención uno a uno ni clases a domicilio.
```

No mostrar textos internos defensivos o explicaciones de control de alcance como bloque visible de cliente.

Texto visible permitido:

```text
Una alternativa estructurada a clases sueltas: curso grupal, práctico y con profesor en vivo.
```

## 5. Valores pendientes

Marketing no confirma todavía los siguientes valores finales:

| Campo | Estado | Dueño recomendado |
|---|---|---|
| `duration` | `POR_CONFIRMAR` | Misael / operación comercial |
| `download_resource_code` | `POR_CONFIRMAR` | Edge + Marketing + recurso temario |
| `course_instance_name` | `POR_CONFIRMAR` | Edge + operación comercial |

Mientras esos valores no estén confirmados, no publicar ni integrar formularios reales.

## 6. Schema y tracking

Marketing aprueba el criterio, no la implementación final.

Pendiente antes de publicación:

- consolidar `CourseInstance` directo en HTML, no solo runtime;
- sincronizar fecha, horario, duración, modalidad, sede, valor y landing code;
- mantener GTM y PageSense desactivados en preview;
- activar GTM/PageSense solo con autorización explícita;
- no tratar goals de clic como submits;
- validar submit confirmado como conversión técnica primaria;
- conservar Zoho real desactivado hasta mapping exacto y autorización.

## 7. URLs propuestas a conservar

```text
/lp/curso-excel-basico-intermedio-presencial-santiago
/lp/curso-excel-desde-cero-presencial-santiago
/lp/clases-excel-presenciales-profesor-santiago
```

Mientras sigan como piloto pagado:

```text
noindex,follow
fuera de sitemap
fuera de navegación orgánica principal
```

## 8. Bloqueos vigentes

No pasar a publicación ni integración real hasta resolver:

1. revisión visual humana final en escritorio y celular;
2. `scripts/audit-local.py`;
3. `git diff --check` desde workspace local Edge;
4. `duration`;
5. `download_resource_code`;
6. `course_instance_name`;
7. `CourseInstance` directo en HTML;
8. mappings exactos de Zoho Forms;
9. claims/sellos institucionales;
10. consentimiento de imágenes;
11. autorización explícita para GTM, PageSense, Turnstile, Zoho, endpoints internos y Google Ads.

## 9. No autorizado

Este XFER no autoriza:

- publicar rutas reales `/lp`;
- agregar a sitemap;
- quitar `noindex`;
- tocar Worker real;
- tocar Cloudflare Dashboard;
- tocar DNS;
- activar GTM real;
- activar PageSense real;
- activar Turnstile real;
- activar Zoho real;
- enviar tráfico pagado;
- modificar Google Ads;
- modificar campañas, presupuestos, pujas, anuncios, keywords, negativas, conversiones o audiencias;
- mergear Edge PR #36;
- mergear Marketing PR #35 completo.

## 10. Respuesta esperada de Edge

Edge debe responder en PR #36 y/o bitácora con:

```text
CONSUMED_PASS
CONSUMED_WITH_CHANGES
CONSUMED_FAIL
```

incluyendo:

- XFER exacto consumido;
- archivos modificados;
- estado de slots/schema/tracking;
- evidencia de revisión visual o bloqueo;
- SHA;
- merge gate.

## 11. Gate

```text
NO_MERGEAR_TODAVIA
REQUIERE_REVISION_MISAEL
REQUIERE_CHECKS
```
