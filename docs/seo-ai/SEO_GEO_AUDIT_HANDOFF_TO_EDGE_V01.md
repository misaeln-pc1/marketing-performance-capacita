# Handoff a Capacita Edge — auditoría SEO/GEO técnica V01

## Repo dueño

`misaeln-pc1/capacita-edge`

## Problema

Capacita no aparece de forma consistente en consultas como `15 instituciones que ofrecen cursos de Excel presencial en Santiago`, ejecutadas en ChatGPT o Gemini. El ecosistema web combina WordPress, Cloudflare Pages y subdominios, por lo que deben verificarse rastreo, indexación, canonicalización, políticas de bots y consistencia de entidad.

## Frontera

Marketing define consultas, intención, benchmark, impacto comercial y evidencia agregada. Edge audita e implementa SEO técnico, robots, headers, sitemaps, canonicals, Cloudflare, frontend y eventos.

## Trabajo solicitado a Edge

1. inventario de dominios, subdominios y tecnologías;
2. inventario de URLs de Excel presencial, básico, intermedio y básico–intermedio;
3. auditoría de `robots.txt`, meta robots y `X-Robots-Tag`;
4. prueba de acceso para Googlebot, Bingbot y OAI-SearchBot;
5. revisión de Cloudflare WAF, Bot Fight Mode, AI Crawl Control y Verified Bots;
6. auditoría de sitemap, indexación, canonicals, redirects y páginas históricas;
7. validación de `Organization`, `LocalBusiness`, breadcrumbs y structured data aplicable;
8. revisión de contenido visible, fechas, títulos, enlaces internos y duplicidad;
9. revisión de logs de crawler por hostname, path, status y regla aplicada;
10. plan reversible de corrección con validación y rollback.

## Hallazgos preliminares a validar

- la home pública es rastreable por un crawler general;
- existe una landing específica para Excel presencial en Santiago;
- existen páginas WordPress históricas con fechas/slugs de enero de 2026 y contenido muy similar;
- la página general de cursos mezcla niveles, modalidades y públicos;
- no existe evidencia todavía para afirmar bloqueo de OAI-SearchBot o Googlebot;
- la ausencia en respuestas IA puede combinar problemas técnicos, semánticos, de entidad y de autoridad externa.

## Evidencia requerida

- mapa URL → tecnología → canonical → indexación → sitemap;
- matriz bot → robots → WAF → status → contenido recibido;
- resultados sanitizados de Search Console/URL Inspection;
- resultados sanitizados de Rich Results Test;
- structured data antes/después;
- lista de páginas vigentes, históricas, duplicadas y candidatas a redirect/noindex;
- diff, SHA, PR y validación;
- sin credenciales, IDs completos, PII, logs crudos ni capturas sensibles.

## DoD

- bots de Search autorizados reciben contenido 200 sin desafío cuando la política lo permite;
- páginas prioritarias están indexables, canónicas y enlazadas;
- páginas históricas no compiten sin una decisión explícita;
- sitemaps reflejan URLs vigentes;
- entidad local y oferta están expresadas consistentemente;
- no se rompe WordPress, Cloudflare Pages, formularios ni tracking;
- existe baseline previo y validación posterior.

## Relación

- Marketing PR #31: metodología SEO/GEO y benchmark;
- Edge issue #28: auditoría técnica dueña;
- Edge issue #27: GTM/atribución;
- benchmark `docs/seo-ai/AI_VISIBILITY_QUERY_BENCHMARK_V01.md`.

Este handoff no reemplaza el issue técnico ni autoriza cambios productivos.