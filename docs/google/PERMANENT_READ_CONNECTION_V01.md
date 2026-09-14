# Permanent Google READ Connection V01

Issue: `#102`
PR: `#103`
Branch: `feature/marketing-google-official-permanent-read`
Estado: `IMPLEMENTED_PENDING_LIVE_OAUTH`

## Objetivo

Establecer una conexión oficial, reutilizable y sin dependencia de trials para que Marketing pueda consultar Google Ads + GA4 de forma consistente desde ChatGPT.

## Decisión de arquitectura

```text
Google Ads API oficial (READ)
+ GA4 Data API oficial (READ)
+ Google Sheets API (write limitado al reporting sink)
→ Historial_Rendimiento_GoogleAds
→ ChatGPT / Marketing READ
```

```text
PRIMARY_AUTH=Google OAuth / Application Default Credentials (ADC)
THIRD_PARTY_TRIALS=OPTIONAL_ONLY
ADS_WRITES=0
GA4_CONFIG_WRITES=0
SECRETS_IN_GITHUB=0
PII_QUERY_STRING_CAPTURED=0
```

Se reutiliza el fast path existente de `#85/#86`; este frente no crea otro control plane.

## Cambio oficial de Google — septiembre 2026

Google retiró los developer tokens para Google Ads API el 2026-09-09. El acceso se asocia ahora al Google Cloud project que posee el OAuth client o service account. Headers `developer-token` legacy pueden seguir presentes en código antiguo, pero el servidor los ignora.

Consecuencia: **no crear un Google Cloud project/OAuth client en un proyecto nuevo por reflejo**. Debe reutilizarse el proyecto que conserva el acceso de Google Ads API, salvo verificación explícita de otro proyecto autorizado.

## Autenticación elegida

Para el entorno Windows/local existente se conserva `single-user OAuth + ADC` porque:

- el fast path ya consume ADC;
- el bloqueo observado fue `ACCESS_TOKEN_SCOPE_INSUFFICIENT`, no ausencia de infraestructura;
- evita service-account delegation, claves JSON permanentes y una migración innecesaria.

Scopes del consentimiento único:

```text
https://www.googleapis.com/auth/adwords
https://www.googleapis.com/auth/analytics.readonly
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/cloud-platform
```

`spreadsheets` no habilita writes en Ads ni GA4; se usa únicamente para mantener el bridge de reporting ya conectado a ChatGPT.

ADC se guarda por `gcloud` fuera del repo. OAuth client JSON, refresh token y `google-ads.yaml` nunca se versionan.

> `PERMANENTE` significa infraestructura propia y reutilizable con refresh automático de access tokens. Google puede revocar un refresh token por seguridad o por revocación explícita del usuario.

## Bridge existente y delta mínimo

La hoja `Historial_Rendimiento_GoogleAds` ya es la fuente histórica operativa de Google Ads y mostró datos diarios recientes en la revisión 2026-09-13. No se reemplazan sus pestañas Ads.

Se agregaron únicamente:

```text
Log_Diario_GA4_Campaigns
Log_Diario_GA4_Landing_Pages
Control_Plane_Status
```

GA4 se restringe a sesiones pagadas `google / cpc` para reconciliación Ads → web.

### Privacidad

Se usa la dimensión GA4 `landingPage`, no `landingPagePlusQueryString`.

```text
PII_QUERY_STRING_CAPTURED=0
```

Esto evita replicar parámetros de URL potencialmente sensibles al histórico de reporting.

## Implementación

Ruta:

```text
scripts/google_official_read/
```

Componentes:

- `requirements.txt`: versiones oficiales Google pinneadas.
- `setup_google_read.ps1`: instalación/consentimiento/validación/scheduler en una sola ejecución.
- `select_ga4_property.py`: descubre la propiedad GA4 accesible; si hay varias, permite seleccionar una vez.
- `check_google_read.py`: health check vivo Google Ads + propiedad GA4 + Sheet.
- `publish_ga4_to_sheet.py`: rolling upsert idempotente de 3 días.
- `run_daily_google_read.py`: orquestación diaria y actualización de estado.
- `run_daily_google_read.ps1`: wrapper con log local fuera de GitHub.
- `install_google_read_task.ps1`: Windows Scheduled Task reversible.

## Observabilidad

`Control_Plane_Status` mantiene estado separado para:

```text
Google Ads API
GA4 Data API
GA4 → Reporting Sheet
```

Regla:

```text
NO_DATA != CONNECTION_FAILED
```

Una fecha sin delivery no se interpreta como falla si el health check está `PASS`.

## Scheduling

Default preparado:

```text
TASK=Capacita-Marketing-Google-Read
DAILY_AT=05:30
START_WHEN_AVAILABLE=YES
LOGON=INTERACTIVE_USER
```

La hora es modificable sin rehacer OAuth. `StartWhenAvailable` reduce pérdidas si el PC no estaba disponible exactamente a la hora programada. Con `Interactive` no se almacena contraseña de Windows; el job corre cuando la sesión del usuario está disponible.

## Guardrails

```text
NO_NEW_TRIAL_AS_BASELINE
NO_ADS_MUTATIONS
NO_GA4_CONFIG_MUTATIONS
NO_GTM_MUTATIONS
NO_CREDENTIALS_IN_GITHUB
NO_RAW_QUERY_STRING_STORAGE
SHEET_WRITE_SCOPE=REPORTING_ONLY_BY_CONTRACT
```

## Validación pendiente

Todo lo estructural está preparado, pero no declarar conexión terminada sin ejecución en el PC que contiene las credenciales privadas.

DoD vivo:

```text
OFFLINE_BRIDGE_TESTS=PASS
GOOGLE_ADS_API=PASS
GA4_DATA_API=PASS
REPORTING_SHEET=PASS
GA4_SHEET_BRIDGE=PASS
SCHEDULE=PASS
CONTROL_PLANE_STATUS=PASS
SECRETS_IN_GITHUB=0
ADS_WRITES=0
GA4_CONFIG_WRITES=0
```

## Cierre

Hasta evidencia viva:

```text
NO_MERGEAR_TODAVIA
REQUIERE_CHECKS
```
