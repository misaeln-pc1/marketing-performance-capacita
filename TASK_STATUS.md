# Estado de Tareas

Fecha de revision: 2026-08-14

## Prioridad activa

Potenciar el frente **Excel B2C presencial Santiago** con análisis conversacional conectado, preservando las decisiones Google Ads/Meta Ads/landings ya canonizadas y sin reemplazar rutas read-only actuales hasta demostrar ganancia material.

Fuentes vigentes principales:

```text
docs/analytics/CONNECTED_MARKETING_ANALYTICS_PILOT_2026-08-14.md
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md
docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md
docs/google-ads/GOOGLE_ADS_STATUS_ANALYSIS_PROCEDURE_V01.md
docs/meta-ads/META_ADS_ACCOUNT_ROUTING.md
```

## Regla de continuidad

Antes de recomendar sobre un frente ya trabajado, leer `DECISIONES.md`, este archivo y el documento canónico específico. Aplicar primero la decisión vigente y analizar sólo evidencia nueva o delta. No reiniciar estrategia desde recomendaciones genéricas de plataforma.

## Estado PR / Issues principales

| Item | Estado | Accion |
|---|---|---|
| Marketing PR #59 | `MERGED / VIGENTE_EN_MAIN` | Memoria operativa sincronizada; main actual parte de ese merge. |
| Global PR #134 | `MERGED` | V3 fue versionada en Global y copiada manualmente por Misael. |
| Marketing issue #60 | `OPEN / BOOTSTRAP_PASS_DELTA_PENDING` | Este ciclo aporta Bootstrap PASS; ejecutar una prueba Delta separada después. No cerrar todavía. |
| Marketing PR #58 | `MERGED / VIGENTE_EN_MAIN` | Política canónica de negativas por intención. |
| Marketing PR #54 / #55 | `MERGED / VIGENTE_EN_MAIN` | Routing Meta Ads corregido y canónico. |
| Marketing PR #52 | `OPEN / REVISION_TECNICA_PENDIENTE` | Ruta Meta API read-only; conservar separada del piloto de conector oficial. |
| Marketing issue #48 | `OPEN / MANUAL_PRIVADO` | Auction Insights, reconciliación agregada y cluster `clases/profesor`. |
| Marketing issue #50 | `OPEN / FUTURE_RETRY_ONLY` | Office Ads; no ejecutar ahora. |
| Marketing issue #53 | `BACKLOG / NO_EJECUTAR_AHORA` | Google Ads B2B separado del piloto B2C. |

## Connected Analytics — estado 2026-08-14

### Skills P0

```text
Google account performance diagnostics = ADAPTAR_MINIMO
Anthropic performance-report = ADAPTAR_MINIMO
Anthropic competitive-brief = ADAPTAR_MINIMO
```

No cambia lifecycle AI OS ni se declara `approved`.

### Google Ads

- API/PowerShell actual = `METHOD_A` y fallback.
- Google Ads MCP oficial = `METHOD_B`, sólo para micro-piloto comparativo.
- Diseño de paridad 12 tareas = `PASS`.
- Histórico Drive localizado y leído hasta `2026-08-13`.
- Estado actual sigue **provisional** hasta combinar histórico con una lectura API/MCP fresca equivalente.
- Keyword crítica `curso excel básico e intermedio` sigue concentrando gasto con eficiencia de plataforma inferior al promedio reciente; no autoriza cambios de negativas o concordancia.

### GA4

Requisitos read-only definidos para propiedades, sesiones/usuarios, source-medium-campaign, landing, key events, funnels/drop-off, realtime cuando corresponda, custom dimensions/metrics y Google Ads links.

`GA4 downstream actual = DATA_GAP` hasta que System Integration confirme conexión/auth existente y lecturas disponibles.

### Meta Ads

- API `ads_read` + account routing canónico = fallback vigente.
- Conector/agente oficial Meta = sólo piloto read-only si ya está disponible/autenticado.
- No habilitar WRITE ni migrar por existencia del conector.
- Métrica por creative en este run = `DATA_GAP`.

### Atribución

Capas separadas obligatorias:

```text
conversion de plataforma
!= GA4 key event
!= Lead/Contact
!= Deal
!= CursoAlumno
!= venta real
```

Mapping de API names CRM para atribución = `DATA_GAP`; no inferir nombres desde documentación histórica ausente.

### Competitive brief

Primer piloto: Excel B2C presencial Santiago.

- amenaza directa observada: Activa Latam por combinación de Santiago Centro + propuesta práctica + precio público bajo;
- EFTEC, INACAP y Pro-Active quedan como comparables complementarios;
- reviews, Ads Library validada por identidad y SEO traffic = `DATA_GAP` cuando no exista evidencia robusta.

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
- Parten `noindex,follow`, fuera de sitemap y navegación orgánica.
- La página orgánica actual se conserva protegida.
- No declarar A/B/C ganador sin downstream confiable.

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

- PageSense es fuente complementaria de CRO, no fuente de leads ni matrículas.
- Goals de clic no equivalen a submits confirmados.
- Zoho CRM sigue siendo fuente de verdad comercial.
- Nombre/correo en URL de redirección B2C sigue siendo riesgo rojo de privacidad y debe resolverse fuera de Marketing con autorización específica.

## Archivos pesados

- GitHub conserva Markdown, manifests, hashes, síntesis y trazabilidad liviana.
- Bodega definitiva: SharePoint/OneDrive Empresa.
- `external-files/marketing-performance-capacita` es staging local operativo.
- Google Drive o Cloudflare R2 sólo se usan como capas específicas cuando exista decisión documentada; no son la bóveda canónica general.

## Reglas operativas vigentes

- No trabajar directo en `main`.
- No modificar campañas, presupuesto, pujas, anuncios, keywords, negativas, conversiones, landings productivas, GTM, PageSense, Turnstile, Zoho, Cloudflare, Worker, DNS ni sitemap sin autorización explícita.
- No subir PII, secretos, IDs completos, exports crudos, capturas sensibles ni binarios.
- No inventar métricas, claims, IDs, eventos ni API names.
- Mantener un buyer persona primario y una hipótesis por prueba.
- Separar B2C y B2B en campaña, landing y medición.
- No usar SENCE, franquicia, beneficio tributario, gratuidad ni promesas garantizadas en B2C.

## Secuencia inmediata

1. Revisar el PR de este piloto documental; no mergear todavía sin Misael.
2. System Integration consume `CONNECTED_ANALYTICS_READ_PILOT` v01 y devuelve evidencia read-only.
3. Marketing ejecuta **Delta** sobre ese retorno: paridad Google, GA4, Meta y mapping CRM.
4. Completar el funnel Ads → landing → GA4 → Lead/Contact → Deal → CursoAlumno/venta sólo donde exista evidencia.
5. Retomar optimización Google Ads B2C A/B/C aplicando primero la política canónica de negativas.
