# Google Ads Read-Only Runbook

## Proposito

Ejecutar localmente un flujo minimo de Google Ads en modo read-only sin usar MCP y sin guardar secretos en el repositorio.

## Precondiciones

- Python local disponible.
- `google-ads` Python client instalado localmente por el operador.
- Credenciales locales fuera del repo.
- Acceso autorizado a Google Ads en modo lectura.
- Basic Access aprobado para Google Ads API.

## Rutas seguras

- Config local externa:
  - ejemplo usado localmente: `C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml`
  - alternativa recomendada: `C:\local-only\google-ads.yaml`
- Output local de trabajo:
  - `automation/google-ads-readonly/output/`

## Comandos de referencia

No versionar outputs reales ni pegar customer IDs completos en documentos del repo.

```powershell
python scripts/google_ads_readonly/list_accessible_customers.py --config-path "C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml" --execute

python scripts/google_ads_readonly/generate_keyword_ideas.py --config-path "C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml" --customer-id REPLACE_ME_CUSTOMER_ID --language-id 1003 --geo-target-constant 1023191 --execute
```

## Diagnostico historico read-only

Usar solo despues de validar el contrato documental `docs/google-ads/GOOGLE_ADS_HISTORY_DIAGNOSIS_CONTRACT_V01.md`.

Exporta datos historicos locales para diagnosticar gasto/clicks/leads:

- terminos reales de busqueda;
- keywords compradas;
- landing/final URLs;
- resumen diario por campana.

```powershell
python scripts/google_ads_readonly/export_search_history.py `
  --config-path "C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml" `
  --customer-id REPLACE_ME_CUSTOMER_ID `
  --start-date 2026-06-01 `
  --end-date 2026-07-08 `
  --execute
```

Salidas locales esperadas, no versionar:

- `automation/google-ads-readonly/output/google_ads_history/search_terms.csv`
- `automation/google-ads-readonly/output/google_ads_history/keywords.csv`
- `automation/google-ads-readonly/output/google_ads_history/landing_pages.csv`
- `automation/google-ads-readonly/output/google_ads_history/campaign_daily.csv`

## Guardrails

- No pasar rutas de secretos dentro del repo.
- No editar scripts para agregar mutaciones sin revision formal.
- No versionar outputs reales con customer IDs, nombres internos, URLs sensibles o PII.
- No usar este pipeline para crear o modificar campanas, anuncios, assets, presupuestos, bids o conversiones.
- No ejecutar `export_campaign_summary.py` hasta aprobar su contrato especifico.

## Orden recomendado

1. Validar acceso con `list_accessible_customers.py`.
2. Generar ideas de keywords cuando se necesite radar de demanda.
3. Exportar historial real con `export_search_history.py` para diagnostico de gasto/clicks/conversiones.
4. Construir resumen agregado y anonimo.
5. Recién despues proponer negativas, separacion de landing o estructura Search.

## Politica de salida

- En consola: solo conteos o datos anonimizados/agregados.
- En archivos: CSV local no versionado.
- En documentos del repo: solo planes, contratos, runbooks, resumenes sanitizados y decisiones.