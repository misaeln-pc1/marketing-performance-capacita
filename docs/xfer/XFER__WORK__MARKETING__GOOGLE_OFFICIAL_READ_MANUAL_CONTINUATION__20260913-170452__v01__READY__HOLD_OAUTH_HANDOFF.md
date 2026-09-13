# XFER — Work → Marketing — Continuación manual Google Official READ

Estado: `READY`

Resultado: `HOLD_OAUTH_INTERACTIVE_PASSKEY`

Productor: `Work / ejecución local Codex`

Consumidor: `Marketing Performance`

Caso: `GOOGLE_OFFICIAL_READ_MANUAL_CONTINUATION`

Versión: `v01`

Fecha-hora: `20260913-170452`

Repo productor/destino: `misaeln-pc1/marketing-performance-capacita`

Issue ejecutable: `misaeln-pc1/capacita-task-hub#254`

Issue dueño: `misaeln-pc1/marketing-performance-capacita#102`

PR destino: `misaeln-pc1/marketing-performance-capacita#103`

Rama destino: `feature/marketing-google-official-permanent-read`

Commit base leído: `09ca0bd9bc85ae2a8cc8738b2c3a4047432d1a4c`

## 1. Objetivo del XFER

Permitir que Marketing continúe manualmente el OAuth único y cierre los checks vivos de Google Ads, GA4, Reporting Sheet, bridge y scheduler sin repetir el diagnóstico ya completado.

Este XFER no declara el control plane operativo. El resultado vigente sigue en `HOLD` hasta obtener todos los `PASS` vivos.

## 2. Estado ejecutivo

```text
OFFLINE_BRIDGE_TESTS=PASS
GOOGLE_ADS_API=HOLD_ACCESS_TOKEN_SCOPE_INSUFFICIENT
GA4_DATA_API=NOT_RUN
REPORTING_SHEET=HOLD_ACCESS_TOKEN_SCOPE_INSUFFICIENT
GA4_SHEET_BRIDGE=NOT_RUN
SCHEDULE=NOT_CREATED
CONTROL_PLANE_STATUS=NOT_WRITTEN
SECRETS_IN_GITHUB=0
ADS_WRITES=0
GA4_CONFIG_WRITES=0
REPORTING_SHEET_WRITES=0
OVERALL=HOLD_OAUTH_INTERACTIVE_PASSKEY
```

## 3. Trabajo completado

1. Se verificó Task Hub #254, Marketing #102 y PR #103.
2. Se creó un checkout aislado directamente en `feature/marketing-google-official-permanent-read`; no se trabajó en `main`.
3. Se verificó que PR #103 apunta al commit base indicado arriba.
4. Se localizaron el OAuth Desktop Client JSON, `google-ads.yaml` y la hoja de reporting fuera de Git.
5. Se validó `google-ads.yaml` sin imprimir valores: contiene `developer_token` y `use_application_default_credentials: true`.
6. Se confirmó que Google Cloud CLI ya estaba instalado, aunque no estaba en `PATH` del proceso inicial.
7. El setup instaló las librerías oficiales Google pinneadas.
8. El primer gate offline detectó que Windows no resolvía `America/Santiago` porque faltaba `tzdata`.
9. Se agregó `tzdata==2026.4` a `scripts/google_official_read/requirements.txt`.
10. El test objetivo terminó `5/5 PASS`.
11. Se intentó el consentimiento en Chrome controlado, Edge y Edge con sesión previa. Google devolvió en los tres casos que no pudo encontrar una llave de acceso.
12. Se probó el ADC anterior sólo con lecturas. Google Ads y Sheets devolvieron `ACCESS_TOKEN_SCOPE_INSUFFICIENT`.
13. No se llegó a seleccionar propiedad GA4, ejecutar el daily runner, escribir la hoja ni crear el scheduler.

## 4. Evidencia exacta del bloqueo

### 4.1 Primer bloqueo técnico corregido

```text
ZoneInfoNotFoundError: No time zone found with key America/Santiago
```

Corrección local:

```text
scripts/google_official_read/requirements.txt
+ tzdata==2026.4
```

Validación posterior:

```text
Ran 5 tests in 0.000s
OK
```

### 4.2 Bloqueo OAuth vigente

Mensaje visible de Google:

```text
No pudimos encontrar una llave de acceso.
Puedes volver a intentarlo o crear una llave de acceso nueva.
```

No se creó una llave nueva. No se modificaron credenciales de cuenta.

### 4.3 ADC previo insuficiente

```text
Google Ads API: 403 ACCESS_TOKEN_SCOPE_INSUFFICIENT
Google Sheets API: 403 Request had insufficient authentication scopes
```

Estas llamadas fueron de lectura. El ADC anterior no fue suficiente para cerrar el DoD.

## 5. Inventario privado sanitizado

| Elemento | Estado | Ubicación/puntero | Validación |
|---|---|---|---|
| OAuth Desktop Client JSON | `FOUND` | `C:\Users\TECH\Downloads\client_secret_*.apps.googleusercontent.com.json` | Tipo `installed`; campos requeridos presentes. |
| Google Ads config | `FOUND` | `C:\Users\TECH\OneDrive - Sociedad de Capacitación Capacita Spa\CAPACITA\Proyectos\0-Origen\google-ads.yaml` | `developer_token` presente; ADC habilitado. |
| Reporting Sheet | `FOUND / ENV_SET` | Variable de usuario `GOOGLE_MARKETING_SPREADSHEET_ID` | Hoja `Historial_Rendimiento_GoogleAds`; el ID no se incluye. |
| ADC anterior | `FOUND / INSUFFICIENT` | `%APPDATA%\gcloud\application_default_credentials.json` | No posee scopes suficientes para Ads/Sheets. |
| Google Cloud CLI | `FOUND` | `%LOCALAPPDATA%\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd` | Ejecutable disponible. |
| Scheduled task | `NOT_CREATED` | `Capacita-Marketing-Google-Read` | No existe al corte. |

Reglas:

- no abrir ni copiar los contenidos privados en chat o GitHub;
- no imprimir el ID completo de la hoja;
- no pegar URL OAuth, código de autorización, refresh token o access token fuera de la terminal local;
- no crear una nueva llave de acceso como parte de este flujo.

## 6. Continuación manual recomendada — ruta A

Ejecutar un paso por vez.

### Paso 1 — dejar Chrome fuera de depuración

En Chrome, cerrar cualquier pestaña OAuth anterior y pulsar `Cancelar` en la franja `ChatGPT empezó a depurar este navegador`.

Resultado esperado:

```text
CHROME_DEBUG_BANNER=ABSENT
```

### Paso 2 — autenticar la cuenta antes de gcloud

En Chrome normal, abrir:

```text
https://accounts.google.com/
```

Iniciar sesión con la cuenta que posee acceso a Google Ads, GA4 y `Historial_Rendimiento_GoogleAds`. Completar la verificación con un método ya existente. No crear una passkey nueva desde el error OAuth.

Resultado esperado: la página `Cuenta de Google` queda abierta y utilizable.

### Paso 3 — abrir PowerShell normal y preparar variables privadas

```powershell
$Repo = 'C:\Users\TECH\OneDrive - Sociedad de Capacitación Capacita Spa\CAPACITA\Proyectos\9_Complementos Locales\Marketing\marketing-performance-capacita-pr103'

$OAuthCandidates = @(
  Get-ChildItem 'C:\Users\TECH\Downloads' `
    -Filter 'client_secret_*.apps.googleusercontent.com.json' `
    -File
)

if ($OAuthCandidates.Count -ne 1) {
  throw "OAUTH_CLIENT_CANDIDATE_COUNT=$($OAuthCandidates.Count)"
}

$OAuthClient = $OAuthCandidates[0].FullName
$AdsConfig = 'C:\Users\TECH\OneDrive - Sociedad de Capacitación Capacita Spa\CAPACITA\Proyectos\0-Origen\google-ads.yaml'
$SheetId = [Environment]::GetEnvironmentVariable('GOOGLE_MARKETING_SPREADSHEET_ID', 'User')
$GcloudBin = 'C:\Users\TECH\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin'
$env:Path = "$GcloudBin;$env:Path"

if (-not (Test-Path -LiteralPath $OAuthClient)) { throw 'OAUTH_CLIENT_JSON_NOT_FOUND' }
if (-not (Test-Path -LiteralPath $AdsConfig)) { throw 'GOOGLE_ADS_CONFIG_NOT_FOUND' }
if ([string]::IsNullOrWhiteSpace($SheetId)) { throw 'SPREADSHEET_ID_USER_ENV_MISSING' }

Set-Location $Repo
```

No ejecutar comandos que muestren `$OAuthClient`, `$SheetId` o el contenido de los archivos.

### Paso 4 — comprobar rama y diff

```powershell
git branch --show-current
git status --short
Select-String -Path .\scripts\google_official_read\requirements.txt `
  -Pattern '^tzdata==2026\.4$'
```

Resultado esperado:

```text
feature/marketing-google-official-permanent-read
git status --short sin salida
scripts/google_official_read/requirements.txt:6:tzdata==2026.4
```

Detenerse si aparece `main`, otra rama, otro archivo modificado o cualquier credencial dentro del repo.

### Paso 5 — repetir el gate offline

```powershell
python -m unittest discover -s tests -p 'test_google_official_read.py'
```

Resultado esperado:

```text
Ran 5 tests
OK
```

### Paso 6 — ejecutar el setup completo

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
  -File .\scripts\google_official_read\setup_google_read.ps1 `
  -OAuthClientJson $OAuthClient `
  -GoogleAdsConfigPath $AdsConfig `
  -SpreadsheetId $SheetId
```

### Paso 7 — completar el consentimiento

Revisar que Google solicite únicamente:

```text
https://www.googleapis.com/auth/adwords
https://www.googleapis.com/auth/analytics.readonly
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/cloud-platform
```

El scope `spreadsheets` sólo autoriza el sink interno definido por contrato. Los scripts no ejecutan writes en Google Ads ni configuración GA4.

### Paso 8 — esperar el cierre del setup

No cerrar PowerShell. El resultado final esperado es:

```text
CAPACITA_GOOGLE_READ_SETUP=PASS
```

Si aparece `CAPACITA_GOOGLE_READ_SETUP=HOLD_*`, conservar el error sanitizado y no instalar nada manualmente fuera de la secuencia.

### Paso 9 — verificar scheduler

```powershell
Get-ScheduledTask -TaskName 'Capacita-Marketing-Google-Read' |
  Select-Object TaskName, State
```

Resultado esperado:

```text
TASK_NAME=Capacita-Marketing-Google-Read
STATE=Ready
```

### Paso 10 — verificar la hoja

Abrir `Historial_Rendimiento_GoogleAds` y revisar:

```text
Control_Plane_Status
Log_Diario_GA4_Campaigns
Log_Diario_GA4_Landing_Pages
```

Confirmar que `Control_Plane_Status` muestra PASS para Ads, GA4 y bridge, y que existe el primer snapshot rolling de tres días.

## 7. Fallback manual — ruta B

Usar sólo si la ruta A vuelve a fallar por passkey.

### Paso 11 — detener el setup anterior

En su PowerShell, usar `Ctrl+C` y cerrar las pestañas OAuth fallidas. Confirmar que no queda otra autorización pendiente.

### Paso 12 — iniciar OAuth sin lanzamiento automático

```powershell
$Scopes = @(
  'https://www.googleapis.com/auth/adwords'
  'https://www.googleapis.com/auth/analytics.readonly'
  'https://www.googleapis.com/auth/spreadsheets'
  'https://www.googleapis.com/auth/cloud-platform'
) -join ','

gcloud auth application-default login `
  --client-id-file="$OAuthClient" `
  --scopes="$Scopes" `
  --no-launch-browser
```

`gcloud` mostrará una URL y pedirá un código. Abrir la URL en un navegador o dispositivo de confianza con una sesión Google normal. Pegar el código final exclusivamente en el mismo PowerShell.

Nunca pegar URL, código o token en chat, GitHub, XFER o archivos del repo.

### Paso 13 — seleccionar GA4 y persistir punteros

```powershell
$GA4PropertyId = (& python .\scripts\google_official_read\select_ga4_property.py).Trim()
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($GA4PropertyId)) {
  throw 'GA4_PROPERTY_SELECTION_FAILED'
}

[Environment]::SetEnvironmentVariable('GOOGLE_ADS_CONFIGURATION_FILE_PATH', $AdsConfig, 'User')
[Environment]::SetEnvironmentVariable('GA4_PROPERTY_ID', $GA4PropertyId, 'User')
[Environment]::SetEnvironmentVariable('GOOGLE_MARKETING_SPREADSHEET_ID', $SheetId, 'User')
[Environment]::SetEnvironmentVariable('GA4_REFRESH_LOOKBACK_DAYS', '3', 'User')

$env:GOOGLE_ADS_CONFIGURATION_FILE_PATH = $AdsConfig
$env:GA4_PROPERTY_ID = $GA4PropertyId
$env:GOOGLE_MARKETING_SPREADSHEET_ID = $SheetId
$env:GA4_REFRESH_LOOKBACK_DAYS = '3'
```

Si aparecen varias propiedades GA4, seleccionar por nombre visible de cuenta/propiedad. No adivinar un ID.

### Paso 14 — ejecutar el primer daily runner

```powershell
python .\scripts\google_official_read\run_daily_google_read.py
```

Resultado esperado:

```text
GOOGLE_ADS=PASS
GA4=PASS
REPORTING_SHEET=PASS
GA4_SHEET_BRIDGE=PASS
```

### Paso 15 — instalar scheduler sólo después del PASS vivo

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass `
  -File .\scripts\google_official_read\install_google_read_task.ps1 `
  -DailyAt '05:30'
```

Resultado esperado:

```text
GOOGLE_READ_SCHEDULE=PASS
```

## 8. Cierre técnico y PR

Este XFER, el registro de bitácora y la corrección `tzdata==2026.4` se entregan versionados en PR #103.

Después de obtener todos los `PASS` vivos, revisar y versionar únicamente la evidencia sanitizada nueva que corresponda:

```powershell
git diff --check
git status --short
```

No volver a agregar los tres archivos ya entregados si no tuvieron cambios posteriores. No versionar ADC, OAuth client JSON, `google-ads.yaml`, IDs, tokens, URLs OAuth, códigos ni payloads.

Registrar evidencia sanitizada en Marketing #102, PR #103 y Task Hub #254. No incluir IDs completos, tokens, URLs OAuth, códigos, payloads ni contenido de credenciales.

## 9. Evidencia final requerida

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

## 10. No autorizado

Este XFER no autoriza:

- modificar campañas, presupuestos, pujas, anuncios, keywords, negativas, conversiones o audiencias en Google Ads;
- modificar configuración, eventos, propiedades, streams, audiences o conversiones GA4;
- escribir fuera de las pestañas internas de reporting ya contratadas;
- crear nuevas credenciales, OAuth clients o passkeys;
- pegar secretos o IDs completos en GitHub o chat;
- trabajar en `main`;
- mergear PR #103.

## 11. Respuesta esperada de Marketing

Marketing debe registrar el consumo con uno de estos resultados:

```text
CONSUMED_PASS
CONSUMED_WITH_CHANGES
CONSUMED_FAIL
```

La respuesta debe incluir:

- nombre exacto de este XFER;
- ruta A o B utilizada;
- nueve checks finales;
- scheduler observable;
- confirmación de 0 writes en Ads y configuración GA4;
- archivos modificados y commit/PR si aplica;
- merge gate explícito.

## 12. Gate

```text
XFER_STATUS=READY
LIVE_CONTROL_PLANE=HOLD
NEXT_OWNER=MARKETING_PERFORMANCE
NO_MERGEAR_PR_103
```
