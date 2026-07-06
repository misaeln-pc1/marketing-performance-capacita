# Google Ads Read-Only Runbook

## Proposito

Ejecutar localmente un flujo minimo de Google Ads en modo read-only sin usar MCP y sin guardar secretos en el repositorio.

## Precondiciones

- Python local disponible.
- `google-ads` Python client instalado localmente por el operador.
- Credenciales locales fuera del repo.
- Acceso autorizado a Google Ads en modo lectura.

## Rutas seguras

- Config local externa:
  - ejemplo: `C:\local-only\google-ads.yaml`
- Output local de trabajo:
  - ejemplo: `automation/google-ads-readonly/output/`

## Comandos de referencia

No fueron ejecutados en esta tarea. Quedan como guia operativa.

```powershell
python scripts/google_ads_readonly/list_accessible_customers.py --config-path C:\local-only\google-ads.yaml --execute
python scripts/google_ads_readonly/generate_keyword_ideas.py --config-path C:\local-only\google-ads.yaml --customer-id REPLACE_ME_CUSTOMER_ID --language-id 1000 --geo-target-constant 1023191 --execute
python scripts/google_ads_readonly/export_campaign_summary.py --config-path C:\local-only\google-ads.yaml --customer-id REPLACE_ME_CUSTOMER_ID
```

## Guardrails

- No pasar rutas de secretos dentro del repo.
- No editar scripts para agregar mutaciones sin revision formal.
- No versionar outputs reales con customer IDs, nombres internos o PII.
- No usar este pipeline para crear o modificar campanas, anuncios, assets, presupuestos, bids o conversiones.

## Orden recomendado

1. Validar acceso con `list_accessible_customers.py`.
2. Revisar y ajustar `keyword_seeds_presencial_santiago.csv`.
3. Generar ideas de keywords.
4. Mantener el resumen de campanas en modo scaffold hasta aprobar el contrato de reporte.

## Politica de salida

- En consola: solo datos anonimizados o agregados.
- En archivos: preferir CSV local no versionado.
- En documentos del repo: solo planes, runbooks y placeholders.
