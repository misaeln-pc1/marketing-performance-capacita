# Estado de Tareas

Fecha de revisión: 2026-08-23

## Prioridad activa

Operacionalizar el protocolo obligatorio de visibilidad de páginas usando el runtime reusable ya consolidado y aplicarlo a las siguientes páginas/landings reales de Capacita sin reabrir la metodología desde cero.

Fuente local obligatoria:

```text
docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md
docs/seo-ai/README.md
DECISIONES.md
```

Fuentes reusables externas al repo:

```text
misaeln-pc1/capacita-ai-operating-system
misaeln-pc1/capacita-search-intelligence-toolchain
```

## Frente SEO / AEO / GEO / AI Search — estado vigente

### Skills AI OS

AI OS PR #55 quedó `MERGED / VIGENTE_EN_MAIN`, merge SHA:

`62575085c041796d67d8f49c0845c8668cc26ed3`

Skills disponibles para evaluación/uso local bajo gate de Marketing:

1. `seo-demand-serp-research-capacita`
2. `aeo-ai-readability-capacita`
3. `geo-ai-search-benchmark-capacita`
4. `ai-crawler-retrieval-access-audit-capacita`
5. `entity-authority-corroboration-capacita`
6. `marketing-page-visibility-review-capacita`

Estado de biblioteca: `0.1.0 draft/candidate`. No requieren `approved` global para uso local controlado.

### Runtime técnico reusable

Toolchain PR #2 quedó `MERGED / VIGENTE_EN_MAIN`.

- repo: `misaeln-pc1/capacita-search-intelligence-toolchain`
- head validado: `fe829a42e5348c745a8dc5fecebdbfd03dce9ee6`
- merge SHA: `fb5c4a9df255953fa6bad59a8866ddf610474d1b`

AI OS PR #56 quedó `MERGED / VIGENTE_EN_MAIN`, merge SHA:

`901c27a77f6c1fe06c1067723267314918dfb4d3`

Estado de consumo:

```text
SITEONE=READY
ADVERTOOLS=READY
PROMPTFOO=READY_NO_PAID_PROVIDER
SERPBEAR=CONFIG_VALIDATED/PENDING_PROVIDER_SECURITY_REVIEW
```

Reglas críticas:

- SiteOne: usar para crawl técnico, render opt-in, HTML/JSON/texto/Markdown y `AI_READABILITY_TEST`.
- advertools: usar para robots, sitemap multi-source, estructura URL/crawl y términos; no sustituye GSC/Keyword Planner como fuente de demanda.
- Promptfoo: usar sólo como benchmark sintético/reproducible mientras no exista provider real autorizado. `PROMPTFOO_SYNTHETIC_BENCHMARK != REAL_AI_SEARCH_RANKING`.
- SerpBear: no iniciar. Sigue bloqueado por provider + security review en `capacita-search-intelligence-toolchain#1`.
- No duplicar instalación o runtime dentro de Marketing.
- No crear credenciales, costos o providers sin autorización explícita.

## Piloto real completado

URL piloto:

`https://capacita.cl/curso-excel-intermedio-avanzado-presencial-santiago`

Resultados relevantes:

- SiteOne: PASS, HTTP 200, canonical/indexabilidad, estructura, JSON-LD y Markdown utilizable para AI-readability.
- advertools: PASS, crawl HTTP 200 y sitemap multi-source corregido.
- Sitemap WordPress: 415 URLs / target `false`.
- Sitemap estático: 6 URLs / target `true`.
- Agregado deduplicado: 416 URLs / target `true`.
- `FALSE_NEGATIVE_SITEMAP_FIXED=PASS`.
- Marketing issue #65: `CLOSED / TOOL_FALSE_NEGATIVE_RESOLVED / NO_WEB_CHANGE_REQUIRED`.
- Promptfoo: 2/2 casos sintéticos PASS, costo/tokens/credenciales = 0.
- SerpBear: configuración validada, runtime no iniciado.

La landing no requirió cambio web por el hallazgo de sitemap.

## Regla de continuidad

Antes de recomendar sobre un frente ya trabajado, leer `DECISIONES.md`, este archivo y el documento canónico específico. Aplicar primero la decisión vigente y analizar sólo evidencia nueva o delta. No reiniciar estrategia desde recomendaciones genéricas de plataforma.

## Google Ads — frente separado vigente

Fuentes principales al retomarlo:

```text
docs/landing-pages/EXCEL_B2C_PAID_LANDINGS_MINIMUM_BASELINE_2026-07-28.md
docs/google-ads/GOOGLE_ADS_NEGATIVE_KEYWORDS_INTENT_POLICY.md
```

Reglas vigentes:

- priorizar intención de asistir/comprar curso;
- preservar negativas históricas de solución puntual mientras no exista evidencia real que justifique retirarlas;
- excluir deliberadamente intención informativa puntual y empleo cuando corresponda;
- `paso a paso` no es negativa global;
- separar exclusión global de tráfico versus routing A/B/C a nivel grupo;
- no modificar listas reales sin autorización explícita.

Baseline Excel B2C pagado:

- Landing A: Curso Excel Básico-Intermedio presencial, `BP-001`.
- Landing B: Excel desde cero presencial, `BP-002`.
- Landing C: clases de Excel presenciales con profesor, `BP-001`.
- Las tres venden el mismo curso grupal presencial Básico-Intermedio en Santiago Centro.
- Parten `noindex,follow`, fuera de sitemap y navegación orgánica.
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

1. Aplicar el protocolo integral y las skills/runtime a la próxima página real que Misael priorice.
2. Reutilizar GSC, Keyword Planner, SERP y evidencia existente antes de generar nueva investigación.
3. Usar SiteOne + advertools como evidencia técnica/readability; Promptfoo sólo como benchmark sintético controlado.
4. Mantener SerpBear bloqueado hasta resolver provider, seguridad, retención, owner y costo.
5. Después de 2–3 páginas reales, devolver feedback a AI OS sobre utilidad, gaps y falsos positivos antes de promover las skills.
6. Retomar Google Ads/Meta Ads por separado cuando Misael lo indique, leyendo primero sus canónicos específicos.

## Estado de frentes históricos

Los estados detallados de PR/issues anteriores al 2026-08-23 deben revalidarse al retomar cada frente. No usar una tabla histórica como estado vivo sin readback del PR/issue correspondiente.
