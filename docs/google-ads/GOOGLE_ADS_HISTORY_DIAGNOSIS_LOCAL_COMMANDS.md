# Google Ads History Diagnosis Local Commands

## Objetivo

Ejecutar localmente el diagnostico historico read-only para revisar gasto, clicks y conversiones sin tocar campanas reales.

## Comando seco

```powershell
cd "C:\Users\TECH\Documents\Proyectos\marketing-performance-capacita"

python scripts/google_ads_readonly/export_search_history.py `
  --config-path "C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml" `
  --customer-id REPLACE_ME_CUSTOMER_ID `
  --start-date 2026-06-01 `
  --end-date 2026-07-08
```

Debe mostrar:

- `DRY_RUN: export_search_history ready`;
- rango de fechas;
- reportes planificados.

## Comando real

```powershell
cd "C:\Users\TECH\Documents\Proyectos\marketing-performance-capacita"

python scripts/google_ads_readonly/export_search_history.py `
  --config-path "C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml" `
  --customer-id REPLACE_ME_CUSTOMER_ID `
  --start-date 2026-06-01 `
  --end-date 2026-07-08 `
  --execute
```

## Salidas esperadas

No versionar estos archivos:

- `automation/google-ads-readonly/output/google_ads_history/search_terms.csv`
- `automation/google-ads-readonly/output/google_ads_history/keywords.csv`
- `automation/google-ads-readonly/output/google_ads_history/landing_pages.csv`
- `automation/google-ads-readonly/output/google_ads_history/campaign_daily.csv`

## Reporte seguro para ChatGPT

Despues de ejecutar, entregar solo:

```text
search_terms rows: X
keywords rows: X
landing_pages rows: X
campaign_daily rows: X
```

Si hay error, pegar el error eliminando customer IDs completos, tokens o rutas sensibles.