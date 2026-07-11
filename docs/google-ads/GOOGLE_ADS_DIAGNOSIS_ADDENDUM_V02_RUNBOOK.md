# Google Ads Diagnosis Addendum V02 Runbook

## Estado

- Issue dueño: `#27`.
- Rama: `fix/marketing-google-ads-history-v02`.
- Riesgo: amarillo, por uso read-only de Google Ads API y análisis que puede condicionar campañas, tracking y landings.
- No modifica campañas, presupuestos, pujas, anuncios, keywords, conversiones ni cuentas.

## Objetivo

Completar el diagnóstico histórico iniciado por PR #26 y obtener evidencia suficiente antes de decidir negativas, grupos de anuncios, campañas o múltiples landing pages.

El primer ZIP de 90 días generó siete reportes correctos, pero fallaron:

1. `05_search_terms_daily.csv` por incompatibilidad de `segments.search_term_targeting_status` con `search_term_view`.
2. `07_landing_pages_daily.csv` porque `campaign.advertising_channel_type` se usó como filtro sin incluirlo en `SELECT`.

## Qué agrega V02

### Addendum de campaña

`scripts/google_ads_readonly/export_diagnosis_addendum_v02.py` genera localmente:

- `11_search_terms_daily_v02.csv`:
  - término real buscado;
  - keyword activadora;
  - concordancia;
  - campaña y grupo;
  - dispositivo y red;
  - clics, costo y conversiones.
- `12_landing_pages_daily_v02.csv`:
  - URL efectiva;
  - campaña y grupo;
  - dispositivo;
  - clics, costo y conversiones.
- `13_hour_day_device_daily.csv`:
  - día de semana;
  - hora;
  - dispositivo y red;
  - gasto y conversiones.
- `14_customer_search_term_insights.csv`:
  - categoría y subcategoría de búsqueda;
  - término;
  - clics, impresiones y conversiones;
  - se trata como reporte opcional: si la cuenta o versión no lo soporta, el error queda en el manifest y los demás reportes continúan.
- `manifest_addendum_v02.json`.

### Histórico de mercado

`scripts/google_ads_readonly/generate_keyword_market_history_v02.py` usa `GenerateKeywordHistoricalMetrics` y genera:

- `15_keyword_market_summary.csv`:
  - promedio de búsquedas mensuales;
  - variantes cercanas;
  - competencia;
  - índice competitivo 0–100;
  - rango bajo y alto de puja superior.
- `16_keyword_monthly_volume.csv`:
  - volumen aproximado por mes para los últimos doce meses disponibles.
- `manifest_keyword_market_v02.json`.

El set inicial incluye intención básica, intermedia, presencial, clases particulares, profesor a domicilio y online. Puede reemplazarse por un archivo local externo con columna `keyword`.

## Qué no entrega la API

El histórico de keywords permite observar presión de mercado agregada, pero no identifica directamente dominios rivales.

Para confirmar si Superprof u otros anunciantes coinciden con nuestras subastas se requiere exportar **Auction Insights** desde la interfaz de Google Ads. Ese informe permite comparar:

- impression share;
- overlap rate;
- outranking share;
- position above rate;
- top of page rate;
- absolute top of page rate.

No confundir:

- `competition` e índice 0–100 de Keyword Planner: presión agregada sobre una keyword;
- Auction Insights: anunciantes que participaron en las mismas subastas;
- CPC real y Quality Score: resultado operativo propio.

## Preflight

Confirmar fuera del repo:

- `C:\Users\TECH\Documents\Proyectos\0-Origen\google-ads.yaml`;
- `C:\Users\TECH\Documents\Proyectos\0-Origen\run-google-ads-keywords.ps1`;
- Python con `google-ads` instalado;
- customer ID disponible localmente y no pegado en chat o GitHub.

## PowerShell — dry run

Este bloque no llama Google Ads:

```powershell
$ErrorActionPreference = "Stop"

$repo = "C:\Users\TECH\Documents\Proyectos\marketing-performance-capacita"
$localBase = "C:\Users\TECH\Documents\Proyectos\0-Origen"
$configPath = Join-Path $localBase "google-ads.yaml"
$runnerPath = Join-Path $localBase "run-google-ads-keywords.ps1"
$out = Join-Path $localBase "google-ads-diagnosis\v02-dry-run"

$runnerContent = Get-Content $runnerPath -Raw
$match = [regex]::Match($runnerContent, '\$cid\s*=\s*"(?<id>\d{10})"')
if (-not $match.Success) { throw "No se encontró el customer ID en el runner local." }
$cid = $match.Groups["id"].Value

python "$repo\scripts\google_ads_readonly\export_diagnosis_addendum_v02.py" `
  --config-path $configPath `
  --customer-id $cid `
  --days 90 `
  --output-dir $out

if ($LASTEXITCODE -ne 0) { throw "Falló dry run del addendum." }

python "$repo\scripts\google_ads_readonly\generate_keyword_market_history_v02.py" `
  --config-path $configPath `
  --customer-id $cid `
  --output-dir $out

if ($LASTEXITCODE -ne 0) { throw "Falló dry run de histórico de mercado." }
```

## PowerShell — ejecución read-only

Ejecutar solo después de revisión, merge y autorización explícita:

```powershell
$ErrorActionPreference = "Stop"

$repo = "C:\Users\TECH\Documents\Proyectos\marketing-performance-capacita"
$localBase = "C:\Users\TECH\Documents\Proyectos\0-Origen"
$configPath = Join-Path $localBase "google-ads.yaml"
$runnerPath = Join-Path $localBase "run-google-ads-keywords.ps1"

$runnerContent = Get-Content $runnerPath -Raw
$match = [regex]::Match($runnerContent, '\$cid\s*=\s*"(?<id>\d{10})"')
if (-not $match.Success) { throw "No se encontró el customer ID en el runner local." }
$cid = $match.Groups["id"].Value

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$out = Join-Path $localBase "google-ads-diagnosis\$stamp-v02"
New-Item -ItemType Directory -Force $out | Out-Null

python "$repo\scripts\google_ads_readonly\export_diagnosis_addendum_v02.py" `
  --config-path $configPath `
  --customer-id $cid `
  --days 90 `
  --output-dir $out `
  --execute

$addendumExit = $LASTEXITCODE

python "$repo\scripts\google_ads_readonly\generate_keyword_market_history_v02.py" `
  --config-path $configPath `
  --customer-id $cid `
  --output-dir $out `
  --execute

$marketExit = $LASTEXITCODE

Get-ChildItem $out | Select-Object Name, Length | Format-Table -AutoSize

$zip = "$out.zip"
Compress-Archive -Path "$out\*" -DestinationPath $zip -Force

Write-Host "ADDENDUM_EXIT_CODE: $addendumExit"
Write-Host "MARKET_EXIT_CODE: $marketExit"
Write-Host "DIAGNOSTIC_ZIP: $zip"
```

Un código `2` del addendum significa que un reporte opcional falló, pero el script conservó los demás archivos y registró el error.

## Auction Insights — export manual

Realizar dos exports, sin subirlos al repo:

### Campaña presencial

1. Abrir Google Ads.
2. Entrar a `EXCEL-PRE-STGO`.
3. Seleccionar un rango de 90 días y luego otro de 30 días.
4. Ir a Campañas, Grupos de anuncios o Palabras clave de búsqueda.
5. Seleccionar la campaña, grupo o keywords relevantes.
6. Abrir `Estadísticas de subasta` / `Auction insights`.
7. Descargar CSV.

### Clústeres prioritarios

Intentar export separado, cuando exista volumen suficiente, para:

- `curso excel básico e intermedio`;
- keywords presenciales;
- clases de Excel / clases particulares / profesor de Excel.

Auction Insights puede no aparecer cuando el elemento no cumple el umbral mínimo de actividad.

## Entrega para análisis

Compartir en chat:

- ZIP V02 generado por PowerShell;
- CSV de Auction Insights de 90 días;
- CSV de Auction Insights de 30 días;
- opcionalmente exports por clúster si Google los permite.

No compartir:

- YAML;
- tokens;
- runner local;
- customer ID;
- OAuth JSON;
- datos personales.

## Decisiones que quedan bloqueadas hasta analizar V02

- cantidad final de landing pages;
- pausar o aislar `curso excel básico e intermedio`;
- crear oferta separada de clases particulares o profesor a domicilio;
- negativas definitivas;
- separación por campaña, grupo, keyword o dispositivo;
- ajuste de pujas o presupuesto.

## Hipótesis, no conclusión

La evidencia preliminar sugiere al menos tres intenciones diferentes:

1. curso presencial local;
2. nivel básico/intermedio;
3. clases particulares o profesor a domicilio.

No se fija todavía una arquitectura de seis páginas. El número de destinos debe resultar de search terms, volumen, costo, conversión, Auction Insights y capacidad real de mantener contenido y tracking separados.

## Guardrails

- Solo lectura.
- Outputs fuera del repo.
- Sin PII, secretos, IDs completos ni binarios.
- Sin cambios en Google Ads.
- Sin creación de landings desde esta tarea.
- Sin declarar competencia o presión de mercado sin datos del período y geografía analizados.
