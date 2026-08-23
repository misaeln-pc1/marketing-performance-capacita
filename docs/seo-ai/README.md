# SEO, Local SEO y visibilidad en IA

Esta carpeta documenta la línea de **Visibilidad Orgánica y en Motores Generativos** de Marketing.

## Entrada obligatoria

- `MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md`: protocolo obligatorio para toda página o landing nueva/revisada. Integra SEO, Local SEO cuando aplique, AEO, GEO/AI Search, AI-readability/citabilidad, demanda, intención, buyer persona, competencia, CRO, medición e impacto comercial. Debe aplicarse por defecto aunque Misael no vuelva a solicitar cada capa explícitamente.

## Runtime reusable disponible

Desde 2026-08-23 Marketing dispone de un runtime reusable consolidado fuera de este repo:

- repo técnico: `misaeln-pc1/capacita-search-intelligence-toolchain`;
- PR técnico `#2`: `MERGED / VIGENTE_EN_MAIN`;
- merge SHA: `fb5c4a9df255953fa6bad59a8866ddf610474d1b`;
- registry/handoff AI OS: PR `#56`, merge SHA `901c27a77f6c1fe06c1067723267314918dfb4d3`.

Estados de consumo local:

```text
SITEONE=READY
ADVERTOOLS=READY
PROMPTFOO=READY_NO_PAID_PROVIDER
SERPBEAR=CONFIG_VALIDATED/PENDING_PROVIDER_SECURITY_REVIEW
```

Reglas de uso:

- SiteOne puede usarse para crawl técnico, render opt-in, reportes y Markdown como entrada de `AI_READABILITY_TEST`.
- advertools puede usarse para robots, sitemap multi-source, URL/crawl y procesamiento de términos; no sustituye GSC/Keyword Planner como fuente de demanda.
- Promptfoo puede usarse para benchmarks sintéticos versionados y resúmenes sanitizados sin provider pagado; `PROMPTFOO_SYNTHETIC_BENCHMARK != REAL_AI_SEARCH_RANKING`.
- SerpBear no debe iniciarse hasta resolver provider, seguridad, retención, owner y límite de costo; issue técnico dueño: `misaeln-pc1/capacita-search-intelligence-toolchain#1`.
- No duplicar instalación ni runtime dentro de Marketing.

## Skills AI OS aplicables

Las seis skills `0.1.0 draft/candidate` están disponibles en AI OS y pueden evaluarse localmente sin esperar `approved` global:

1. `seo-demand-serp-research-capacita`
2. `aeo-ai-readability-capacita`
3. `geo-ai-search-benchmark-capacita`
4. `ai-crawler-retrieval-access-audit-capacita`
5. `entity-authority-corroboration-capacita`
6. `marketing-page-visibility-review-capacita`

Fuente reusable: `misaeln-pc1/capacita-ai-operating-system`, PR `#55` merge SHA `62575085c041796d67d8f49c0845c8668cc26ed3`.

## Documentos de soporte

- `SEO_GEO_TECHNICAL_RESEARCH_BASELINE_V01.md`: metodología y baseline técnico.
- `AI_VISIBILITY_QUERY_BENCHMARK_V01.md`: consultas repetibles para ChatGPT, Gemini y otras superficies.
- `SEO_GEO_AUDIT_HANDOFF_TO_EDGE_V01.md`: contrato de auditoría técnica para Capacita Edge.
- `SEO_GEO_MEASUREMENT_MODEL_V01.md`: métricas y diseño del dashboard futuro.

## Regla de indexabilidad

Aplicar el protocolo no obliga a indexar todas las páginas. Una landing exclusivamente pagada puede conservar `noindex,follow` cuando esa sea la decisión vigente; el protocolo debe registrar esa condición y evitar canibalización con la arquitectura orgánica.

## Frontera

Marketing define demanda, consultas, intención, benchmark, AEO/GEO/AI-readability, medición agregada e impacto comercial. `misaeln-pc1/capacita-edge` implementa robots, headers, sitemaps, canonicals, structured data, Cloudflare, frontend y eventos. `misaeln-pc1/capacita-search-intelligence-toolchain` mantiene instalación, scripts, runtime, seguridad y actualizaciones del stack técnico reusable. AI OS mantiene registry, upstream, licencia, skills y handoff.

No se autorizan cambios productivos desde estos documentos.
