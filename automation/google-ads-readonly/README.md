# Google Ads Read-Only Automation

Carpeta minima para documentar y preparar un pipeline local read-only basado en Google Ads API Python client.

## Incluye

- runbook de ejecucion local;
- CSV de semillas iniciales para cursos presenciales Santiago Centro;
- carpeta `output/` vacia para salidas locales no versionadas de prueba;
- scripts Python esqueleto bajo `scripts/google_ads_readonly/`.

## No incluye

- secretos;
- `.env`;
- `google-ads.yaml` real;
- OAuth JSON;
- customer IDs reales;
- exports reales;
- mutaciones.

## Regla operativa

Todo secreto debe vivir fuera del repo. Si un script recibe una ruta de configuracion dentro del repo, debe abortar.
