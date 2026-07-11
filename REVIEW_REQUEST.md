# REVIEW_REQUEST

## PR objetivo

Habilitar un exportador histórico Google Ads read-only para diagnosticar gasto, clics, términos de búsqueda, calidad de keywords, landing pages, dispositivos, anuncios y acciones de conversión.

## Contexto

El radar anterior basado en Keyword Ideas confirmó demanda, pero no explica el deterioro post-click reportado. El caso observado incluye gasto diario aproximado de CLP $20.000, 16–18 clics y 0–2 leads. Se requiere historial real antes de cambiar campañas o crear múltiples landings.

## Rama

`feature/marketing-google-ads-history-v01`

## Cambios

### Modifica

- `scripts/google_ads_readonly/export_campaign_summary.py`
  - reemplaza el scaffold bloqueado por un exportador GAQL read-only;
  - exige configuración y output fuera del repo;
  - genera reportes separados para evitar distorsión por segmentación;
  - omite customer IDs de los outputs;
  - redacta emails y secuencias numéricas largas detectables en búsquedas o URLs;
  - continúa con reportes restantes si una consulta falla y registra el error.

### Crea

- `docs/google-ads/GOOGLE_ADS_HISTORICAL_DIAGNOSIS_RUNBOOK_V01.md`
  - documenta alcance, datos incluidos, limitaciones y PowerShell;
  - define dry run y ejecución read-only;
  - mantiene ZIP/CSV fuera del repo.

## Reportes locales previstos

1. contexto de cuenta sin ID;
2. configuración de campañas Search;
3. performance diaria de campañas;
4. dispositivo y red;
5. search terms reales;
6. keywords y Quality Score;
7. landing pages efectivas;
8. acciones de conversión;
9. anuncios y Ad Strength;
10. resumen comparativo 7/30/90 días;
11. manifest de ejecución.

## No se toca

- No se ejecuta la API desde este PR.
- No se crean, editan, pausan o activan campañas.
- No se modifican presupuestos, pujas, anuncios, keywords, conversiones o cuentas.
- No se suben YAML, tokens, OAuth JSON, customer IDs completos, TSV/CSV/ZIP reales ni PII.
- No se modifica landing, CRM, Cloudflare, WhatsApp o n8n.
- No se usa MCP.

## Validación esperada

- `python -m py_compile scripts/google_ads_readonly/export_campaign_summary.py`.
- Dry run local sin `--execute`.
- `git diff --check` sin errores.
- Ausencia de PII, secretos, IDs completos y binarios.
- Revisión de consultas GAQL contra Google Ads API v24.
- Ejecución real solo después del merge y autorización de Misael.

## Riesgo

**Amarillo:** consulta datos reales de Ads y costos, aunque solo en modo lectura. Los outputs se mantienen locales y no se versionan.

## Siguiente paso después del merge

Ejecutar primero el dry run. Después, con autorización explícita, ejecutar 90 días, comprimir el directorio local y entregar el ZIP en el chat para análisis agregado.

## Decisión solicitada

- [ ] APROBADO PARA PR
- [ ] CORREGIR ANTES DE PR
