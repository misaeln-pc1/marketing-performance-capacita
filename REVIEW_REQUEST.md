# REVIEW_REQUEST

## PR objetivo

Completar el diagnóstico histórico Google Ads V02 después del primer ZIP de 90 días, recuperando search terms, landing pages, horario/dispositivo, categorías de búsqueda e histórico competitivo de keywords antes de decidir negativas, campañas o múltiples landings.

## Issue dueño

[#27 — Completar diagnóstico Google Ads V02: search terms, landings y competencia](https://github.com/misaeln-pc1/marketing-performance-capacita/issues/27)

## Contexto

PR #26 habilitó y validó el export histórico read-only V01. La primera ejecución real generó siete reportes correctos y dos errores:

- `05_search_terms_daily.csv`: incompatibilidad de `segments.search_term_targeting_status` con `search_term_view`;
- `07_landing_pages_daily.csv`: campo de canal usado en filtro sin incluirlo en `SELECT`.

La evidencia preliminar mostró deterioro post-click y costo alto en `curso excel básico e intermedio`, pero todavía no justifica fijar seis landing pages ni una arquitectura definitiva. Faltan términos reales, URLs efectivas, histórico mensual de mercado y Auction Insights.

## Rama

`fix/marketing-google-ads-history-v02`

## Cambios

### Crea

- `scripts/google_ads_readonly/export_diagnosis_addendum_v02.py`
  - corrige search terms y landing pages;
  - agrega día, hora, dispositivo y red;
  - intenta categorías de Search Term Insights;
  - registra errores por reporte sin cancelar los demás;
  - mantiene configuración y outputs fuera del repo.

- `scripts/google_ads_readonly/generate_keyword_market_history_v02.py`
  - usa `GenerateKeywordHistoricalMetrics`;
  - obtiene promedio y volumen mensual;
  - competencia e índice 0–100;
  - rangos bajo/alto de puja superior;
  - incluye clústeres básico, intermedio, presencial, clases particulares, profesor a domicilio y online.

- `docs/google-ads/GOOGLE_ADS_DIAGNOSIS_ADDENDUM_V02_RUNBOOK.md`
  - documenta dry run y ejecución read-only;
  - diferencia competencia de Keyword Planner, CPC propio y Auction Insights;
  - define export manual de Auction Insights para identificar dominios competidores;
  - bloquea decisiones de landings hasta disponer de evidencia.

### Actualiza

- `REVIEW_REQUEST.md` para reflejar V02 e issue #27.

## Resultados locales previstos

1. `11_search_terms_daily_v02.csv`.
2. `12_landing_pages_daily_v02.csv`.
3. `13_hour_day_device_daily.csv`.
4. `14_customer_search_term_insights.csv`, opcional según compatibilidad/volumen.
5. `15_keyword_market_summary.csv`.
6. `16_keyword_monthly_volume.csv`.
7. manifests separados.
8. Auction Insights descargado manualmente desde Google Ads UI.

## Hipótesis que se evaluarán

- La keyword `curso excel básico e intermedio` mezcla intención general y de nivel.
- Las búsquedas `clases de excel`, `clases particulares`, `profesor de excel` y `a domicilio` pertenecen a una intención/oferta distinta y pueden coincidir con Superprof.
- El aumento de CPC puede provenir de presión competitiva, mezcla de búsquedas, Ad Rank o menor relevancia post-click.
- Puede justificarse separar grupos, campañas o landings, pero no se fija todavía una cantidad de destinos.

## No se toca

- No se crean, editan, pausan o activan campañas.
- No se modifican presupuestos, pujas, anuncios, keywords, negativas, conversiones o cuentas.
- No se ejecuta la API desde el PR.
- No se crean landings ni se modifica Capacita Edge.
- No se suben YAML, tokens, OAuth JSON, customer IDs completos, ZIP/CSV reales, PII o binarios.
- No se usa MCP.

## Validación realizada

- `python -m py_compile` correcto para ambos scripts en preparación local.
- `--help` correcto en ambos scripts.
- Dry run local correcto con configuración ficticia y output externo:
  - addendum: cuatro reportes preparados;
  - histórico de mercado: dieciocho keywords preparadas.

## Validación pendiente

- `git diff --check` en clon local o agente ejecutor.
- ausencia final de secretos, IDs completos y binarios;
- dry run con paths reales;
- ejecución real solo después de merge y autorización explícita;
- análisis del ZIP V02 y Auction Insights.

## Riesgo

**Amarillo:** consulta métricas reales de Ads y mercado, aunque solo en modo lectura. Los outputs permanecen locales y no se versionan.

## Siguiente paso después del merge

1. ejecutar dry run;
2. ejecutar addendum e histórico de mercado de forma read-only;
3. exportar Auction Insights para 90 y 30 días;
4. compartir ZIP/CSV en chat;
5. decidir, con evidencia, negativas, estructura y cantidad mínima de landing pages.

## Decisión solicitada

- [ ] APROBADO PARA MERGE
- [ ] CORREGIR ANTES DE MERGE
