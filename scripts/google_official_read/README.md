# Google Official READ — conexión permanente

Issue: `#102`
PR: `#103`
Estado: `IMPLEMENTED_PENDING_LIVE_OAUTH`

## Objetivo

Conexión estable y oficial para Marketing Performance, sin depender de HYPD, Adspirer, Semrush u otros trials:

```text
Google Ads API oficial (READ)
+ GA4 Data API oficial (READ)
+ Google Sheets API (sólo reporting sink)
→ Historial_Rendimiento_GoogleAds
→ ChatGPT / Marketing analiza
```

## Qué ya existe

La hoja `Historial_Rendimiento_GoogleAds` continúa como bridge histórico de Google Ads. Este frente agrega:

- `Log_Diario_GA4_Campaigns`;
- `Log_Diario_GA4_Landing_Pages`;
- `Control_Plane_Status`.

No se reemplazan ni reescriben las pestañas históricas Ads.

## Prerrequisitos privados — nunca GitHub

1. OAuth Desktop Client JSON del **mismo Google Cloud project que conserva el acceso Google Ads API**.
2. `google-ads.yaml` actual fuera del repo, con `use_application_default_credentials: true`.
3. ID de la hoja de reporting. No se versiona.

GA4 se descubre interactivamente durante el setup; si sólo existe una propiedad accesible, se selecciona automáticamente.

## Ejecución única

Desde la raíz local del repo y estando en la rama del PR #103:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\google_official_read\setup_google_read.ps1 `
  -OAuthClientJson "C:\RUTA_PRIVADA\oauth-client.json" `
  -GoogleAdsConfigPath "C:\RUTA_PRIVADA\google-ads.yaml" `
  -SpreadsheetId "ID_PRIVADO_DE_LA_HOJA"
```

Opcional:

```powershell
-DailyAt "05:30"
```

El setup realiza una sola autorización ADC con scopes:

```text
https://www.googleapis.com/auth/adwords
https://www.googleapis.com/auth/analytics.readonly
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/cloud-platform
```

Después:

1. persiste sólo punteros/config no secreta en variables de usuario;
2. valida Google Ads API;
3. valida GA4 Data API sobre la propiedad seleccionada;
4. valida acceso a la hoja;
5. publica el primer snapshot GA4 pagado (`google / cpc`), rolling 3 días;
6. instala `Capacita-Marketing-Google-Read` en Windows Task Scheduler;
7. la tarea se ejecuta a diario y usa `StartWhenAvailable`.

## Privacidad

GA4 usa `landingPage`, **no** `landingPagePlusQueryString`. Así no se replica nombre/correo u otros parámetros que pudieran viajar en query strings.

```text
PII_QUERY_STRING_CAPTURED=0
```

## Observabilidad

`Control_Plane_Status` registra:

- salud de Google Ads API;
- salud de GA4 Data API;
- salud del bridge GA4 → Sheet;
- timestamp del último check.

Esto separa:

```text
NO_DATA != CONNECTION_FAILED
```

## Archivos

- `check_google_read.py`: health check de Ads + GA4 + Sheet.
- `select_ga4_property.py`: selección local de propiedad GA4.
- `publish_ga4_to_sheet.py`: upsert idempotente rolling 3 días.
- `run_daily_google_read.py`: orquestación diaria + status.
- `run_daily_google_read.ps1`: wrapper/log local.
- `install_google_read_task.ps1`: scheduled task reversible.
- `setup_google_read.ps1`: setup inicial completo.
- `requirements.txt`: versiones oficiales Google pinneadas.

## Guardrails

```text
ADS_WRITES=0
GA4_CONFIG_WRITES=0
SECRETS_IN_GITHUB=0
PII_QUERY_STRING_CAPTURED=0
THIRD_PARTY_TRIAL_DEPENDENCY=NO
```

La única escritura externa de este módulo es la hoja de reporting de Marketing.

## DoD

No declarar completo ni mergear hasta obtener evidencia viva:

```text
GOOGLE_ADS_API=PASS
GA4_DATA_API=PASS
REPORTING_SHEET=PASS
GA4_SHEET_BRIDGE=PASS
SCHEDULE=PASS
CONTROL_PLANE_STATUS=PASS
```
