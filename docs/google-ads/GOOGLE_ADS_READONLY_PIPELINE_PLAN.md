# Google Ads Read-Only Pipeline Plan

## Objetivo

Disenar una alternativa local, simple y read-only al Google Ads MCP para alimentar el radar comercial de cursos presenciales en Santiago Centro sin depender de tools MCP invocables en Codex.

## Alcance V0.1

Este plan cubre solo:

- listado de cuentas accesibles;
- generacion de ideas de keywords a partir de semillas locales;
- preparacion de un resumen agregado de campanas como esqueleto bloqueado hasta aprobar su contrato read-only.

Este plan no cubre:

- mutaciones;
- creacion o edicion de campanas;
- presupuestos, bids, anuncios, assets o conversiones;
- carga de secretos al repo;
- customer IDs reales;
- exports reales o PII.

## Principios

- Read-only por defecto.
- Secretos fuera del repositorio.
- Datos agregados y anonimizados solamente.
- Fallo seguro: si falta configuracion o se detecta una ruta sensible dentro del repo, el script debe abortar.
- Nada de MCP.

## Arquitectura propuesta

```text
keyword_seeds_presencial_santiago.csv
    -> generate_keyword_ideas.py
    -> output local anonimizado

env vars / ruta local externa de config
    -> list_accessible_customers.py
    -> customer IDs enmascarados

env vars / ruta local externa de config
    -> export_campaign_summary.py
    -> scaffold bloqueado hasta aprobar reporte agregado
```

## Estructura acordada

- `docs/google-ads/GOOGLE_ADS_READONLY_PIPELINE_PLAN.md`
- `automation/google-ads-readonly/README.md`
- `automation/google-ads-readonly/GOOGLE_ADS_READONLY_RUNBOOK.md`
- `automation/google-ads-readonly/keyword_seeds_presencial_santiago.csv`
- `automation/google-ads-readonly/output/.gitkeep`
- `scripts/google_ads_readonly/list_accessible_customers.py`
- `scripts/google_ads_readonly/generate_keyword_ideas.py`
- `scripts/google_ads_readonly/export_campaign_summary.py`

## Configuracion permitida

Solo se permite una de estas dos opciones:

1. Variables de entorno locales, fuera del repo.
2. Archivo `google-ads.yaml` o equivalente fuera del repo, pasado por ruta absoluta local externa.

Variables sugeridas:

- `GOOGLE_ADS_DEVELOPER_TOKEN`
- `GOOGLE_ADS_CLIENT_ID`
- `GOOGLE_ADS_CLIENT_SECRET`
- `GOOGLE_ADS_REFRESH_TOKEN`
- `GOOGLE_ADS_LOGIN_CUSTOMER_ID`
- `GOOGLE_ADS_USE_PROTO_PLUS`

Guardrail:

- si `--config-path` apunta a una ruta dentro del repo, el script debe fallar;
- nunca imprimir secretos;
- nunca versionar `.env`, `google-ads.yaml` real ni OAuth JSON.

## Flujo operativo

1. Preparar credenciales localmente fuera del repo.
2. Ejecutar `list_accessible_customers.py` para validar acceso read-only.
3. Ajustar el CSV de semillas segun oferta real de cursos presenciales.
4. Ejecutar `generate_keyword_ideas.py` y guardar output local o agregado.
5. Mantener `export_campaign_summary.py` en modo scaffold hasta aprobar el contrato de reporte read-only.

## Contrato minimo de salida

### Cuentas accesibles

- cantidad total de cuentas;
- customer IDs enmascarados, por ejemplo `123-***-7890`.

### Ideas de keywords

- keyword semilla;
- idea sugerida;
- idioma objetivo;
- geografia objetivo;
- observaciones de uso comercial.

### Resumen de campanas

- solo agregado;
- sin nombres sensibles si el area comercial no los quiere versionar;
- sin customer IDs reales;
- sin estados operativos que impliquen accion automatica.

## Riesgos conocidos

- La API Python client permite operaciones de mutacion; por eso los scripts deben exponer solo funciones read-only y rechazar argumentos no esperados.
- El resumen de campanas por API puede terminar requiriendo GAQL; por eso el scaffold queda bloqueado hasta revision explicita de ese contrato.
- Sin CRM agregado y sin trazabilidad comercial no se puede calcular CPQL real.

## Fases sugeridas

### Fase 1

- validar acceso a cuentas;
- generar keyword ideas desde semillas locales;
- no exportar campanas todavia.

### Fase 2

- definir contrato de resumen agregado;
- revisar si se acepta GAQL read-only o si el resumen se resuelve por export UI fuera del repo;
- documentar anonimizado de salida.

## Criterios de aceptacion de esta V0.1

- pipeline documentado;
- scripts esqueleto con guardas read-only;
- semillas iniciales creadas;
- sin secretos ni IDs reales;
- sin ejecucion de Google Ads API desde esta tarea;
- sin uso de MCP.
