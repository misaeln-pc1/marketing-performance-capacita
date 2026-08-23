# REVIEW_REQUEST

## Objetivo de revisión vigente

Sincronizar Marketing con el estado real del frente SEO/AEO/GEO/AI Search después de consolidar el runtime reusable y su registry en `main`.

## Rama

```text
docs/marketing-search-intelligence-sync-20260823
```

## Fuentes verificadas

- Marketing: `docs/seo-ai/MARKETING_PAGE_VISIBILITY_PROTOCOL_V01.md`.
- AI OS PR #55: `MERGED`, merge SHA `62575085c041796d67d8f49c0845c8668cc26ed3`.
- Search Intelligence Toolchain PR #2: `MERGED`, merge SHA `fb5c4a9df255953fa6bad59a8866ddf610474d1b`.
- AI OS PR #56: `MERGED`, merge SHA `901c27a77f6c1fe06c1067723267314918dfb4d3`.
- Marketing issue #65: `CLOSED / TOOL_FALSE_NEGATIVE_RESOLVED / NO_WEB_CHANGE_REQUIRED`.

## Estado reusable que debe quedar visible en Marketing

```text
SITEONE=READY
ADVERTOOLS=READY
PROMPTFOO=READY_NO_PAID_PROVIDER
SERPBEAR=CONFIG_VALIDATED/PENDING_PROVIDER_SECURITY_REVIEW
```

Las seis skills SEO/AEO/GEO/AI Search permanecen `0.1.0 draft/candidate` y pueden usarse localmente bajo el Context Gate de Marketing sin esperar `approved` global.

## Cambios de esta rama

- `TASK_STATUS.md`: actualiza fecha, prioridad, estado de skills/runtime, piloto real y secuencia inmediata; evita usar como estado vivo tablas antiguas sin revalidación.
- `docs/seo-ai/README.md`: hace descubrible el runtime técnico, sus SHAs, ownership y límites sin duplicar el registry de AI OS.
- `REVIEW_REQUEST.md`: reemplaza el objetivo de revisión anterior por este cierre de sincronización.

## Reglas críticas preservadas

- No duplicar instalación/runtime dentro de Marketing.
- SiteOne/advertools/Promptfoo pueden consumirse en modo local/read-only según el caso.
- `PROMPTFOO_SYNTHETIC_BENCHMARK != REAL_AI_SEARCH_RANKING`.
- SerpBear no se inicia hasta resolver provider, seguridad, retención, owner y costo.
- No se autorizan providers, credenciales, costos ni cambios productivos.
- No cambia el protocolo de visibilidad ni las seis skills.
- No se modifica ninguna campaña, landing, sitemap, robots, Cloudflare, WAF, CRM, GTM, PageSense ni Ads.

## Feedback scan

- Marketing no contiene `AGENT_FEEDBACK.md` en `main`.
- `CHANGELOG_AGENT.md`, `REVIEW_REQUEST.md` y `TASK_STATUS.md` fueron revisados.
- AI OS `AGENT_FEEDBACK.md` no aporta un hallazgo material nuevo para este frente.

`Feedback scan realizado: sin hallazgos relevantes`.

## Gate

```text
PR_LISTO_PARA_MERGE
REQUIERE_AUTORIZACION_MISAEL
```

No mergear sin autorización explícita.
