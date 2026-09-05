<#
.SYNOPSIS
  Exporta informacion de Meta Ads por Marketing API en modo read-only.

.DESCRIPTION
  Ruta A validada para Capacita: User Access Token + ads_read + cuenta publicitaria visible bajo Otros activos.
  No modifica campanas, anuncios, presupuestos, audiencias, formularios ni produccion.
  Los outputs crudos quedan fuera del repo, en META_EXPORT_ROOT.

.PARAMETER EnvPath
  Ruta del archivo .env privado. No versionar.

.PARAMETER DatePreset
  Preset de fecha de Meta Ads: today, yesterday, last_7d, last_14d, last_30d, this_month, last_month, maximum.

.PARAMETER TimeIncrement
  1 para diario; omitir o 0 para agregado.

.EXAMPLE
  .\scripts\meta_ads_readonly\export_meta_ads_readonly.ps1 `
    -EnvPath "C:\Users\TECH\AppData\Local\Capacita\MetaAds\.env" `
    -DatePreset "last_30d" `
    -TimeIncrement 1
#>

[CmdletBinding()]
param(
  [Parameter(Mandatory = $true)]
  [string]$EnvPath,

  [Parameter(Mandatory = $false)]
  [ValidateSet('today','yesterday','last_3d','last_7d','last_14d','last_28d','last_30d','last_90d','this_week_mon_today','this_week_sun_today','last_week_mon_sun','last_week_sun_sat','this_month','last_month','this_quarter','maximum')]
  [string]$DatePreset = 'last_30d',

  [Parameter(Mandatory = $false)]
  [int]$TimeIncrement = 1
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Read-DotEnv {
  param([Parameter(Mandatory=$true)][string]$Path)
  if (-not (Test-Path -LiteralPath $Path)) {
    throw "No existe EnvPath: $Path"
  }

  $map = @{}
  Get-Content -LiteralPath $Path | ForEach-Object {
    $line = $_.Trim()
    if (-not $line -or $line.StartsWith('#')) { return }
    $idx = $line.IndexOf('=')
    if ($idx -lt 1) { return }
    $key = $line.Substring(0, $idx).Trim()
    $value = $line.Substring($idx + 1).Trim().Trim('"')
    if ($key) { $map[$key] = $value }
  }
  return $map
}

function Assert-RequiredEnv {
  param([hashtable]$Env)
  foreach ($key in @('META_GRAPH_VERSION','META_ACCESS_TOKEN','META_AD_ACCOUNT_ID','META_EXPORT_ROOT')) {
    if (-not $Env.ContainsKey($key) -or [string]::IsNullOrWhiteSpace([string]$Env[$key])) {
      throw "Falta variable requerida en .env: $key"
    }
  }
  if (-not ([string]$Env['META_AD_ACCOUNT_ID']).StartsWith('act_')) {
    throw "META_AD_ACCOUNT_ID debe venir como act_<id>."
  }
}

function New-ExportDir {
  param([string]$Root)
  $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
  $dir = Join-Path $Root "meta-ads-export-$stamp"
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $dir 'raw-json') | Out-Null
  New-Item -ItemType Directory -Force -Path (Join-Path $dir 'csv') | Out-Null
  return $dir
}

function ConvertTo-QueryString {
  param([hashtable]$Params)
  $pairs = New-Object System.Collections.Generic.List[string]
  foreach ($key in $Params.Keys) {
    $value = [string]$Params[$key]
    if ([string]::IsNullOrWhiteSpace($value)) { continue }
    $pairs.Add(('{0}={1}' -f [uri]::EscapeDataString($key), [uri]::EscapeDataString($value)))
  }
  return ($pairs -join '&')
}

function Invoke-MetaGet {
  param(
    [Parameter(Mandatory=$true)][string]$GraphVersion,
    [Parameter(Mandatory=$true)][string]$Token,
    [Parameter(Mandatory=$true)][string]$Path,
    [Parameter(Mandatory=$false)][hashtable]$Params = @{},
    [Parameter(Mandatory=$false)][switch]$Paged
  )

  $base = "https://graph.facebook.com/$GraphVersion/$Path"
  $qs = ConvertTo-QueryString -Params $Params
  $url = if ($qs) { "$base`?$qs" } else { $base }
  $headers = @{ Authorization = "Bearer $Token" }

  if (-not $Paged) {
    return Invoke-RestMethod -Method Get -Uri $url -Headers $headers
  }

  $all = New-Object System.Collections.Generic.List[object]
  $pageUrl = $url
  $page = 0
  while ($pageUrl) {
    $page++
    $response = Invoke-RestMethod -Method Get -Uri $pageUrl -Headers $headers
    if ($null -ne $response.data) {
      foreach ($item in @($response.data)) { $all.Add($item) }
    }
    $next = $null
    if ($null -ne $response.paging -and $null -ne $response.paging.next) {
      $next = [string]$response.paging.next
    }
    $pageUrl = $next
  }
  return $all
}

function Save-Json {
  param([Parameter(Mandatory=$true)]$Object, [Parameter(Mandatory=$true)][string]$Path)
  $Object | ConvertTo-Json -Depth 80 | Set-Content -LiteralPath $Path -Encoding UTF8
}

function Export-CsvSafe {
  param([Parameter(Mandatory=$true)]$Rows, [Parameter(Mandatory=$true)][string]$Path)
  $array = @($Rows)
  if ($array.Count -eq 0) {
    "" | Set-Content -LiteralPath $Path -Encoding UTF8
    return
  }
  $array | Export-Csv -LiteralPath $Path -NoTypeInformation -Encoding UTF8
}

function Flatten-InsightRows {
  param([object[]]$Rows)
  foreach ($row in @($Rows)) {
    [pscustomobject]@{
      date_start          = $row.date_start
      date_stop           = $row.date_stop
      campaign_name       = $row.campaign_name
      adset_name          = $row.adset_name
      ad_name             = $row.ad_name
      spend               = $row.spend
      impressions         = $row.impressions
      reach               = $row.reach
      frequency           = $row.frequency
      clicks              = $row.clicks
      inline_link_clicks  = $row.inline_link_clicks
      ctr                 = $row.ctr
      cpc                 = $row.cpc
      cpm                 = $row.cpm
      actions_json        = if ($null -ne $row.actions) { ($row.actions | ConvertTo-Json -Compress -Depth 20) } else { $null }
      cost_per_action_json = if ($null -ne $row.cost_per_action_type) { ($row.cost_per_action_type | ConvertTo-Json -Compress -Depth 20) } else { $null }
      breakdown_publisher_platform = $row.publisher_platform
      breakdown_platform_position  = $row.platform_position
      breakdown_impression_device  = $row.impression_device
      breakdown_age                = $row.age
      breakdown_gender             = $row.gender
      breakdown_region             = $row.region
    }
  }
}

$envMap = Read-DotEnv -Path $EnvPath
Assert-RequiredEnv -Env $envMap

$graphVersion = [string]$envMap['META_GRAPH_VERSION']
$token = [string]$envMap['META_ACCESS_TOKEN']
$adAccountId = [string]$envMap['META_AD_ACCOUNT_ID']
$exportRoot = [string]$envMap['META_EXPORT_ROOT']
$exportDir = New-ExportDir -Root $exportRoot
$rawDir = Join-Path $exportDir 'raw-json'
$csvDir = Join-Path $exportDir 'csv'

$manifest = [ordered]@{
  status = 'STARTED'
  started_at = (Get-Date).ToString('s')
  graph_version = $graphVersion
  ad_account_id_present = $true
  date_preset = $DatePreset
  time_increment = $TimeIncrement
  export_dir = $exportDir
  endpoints = @()
  errors = @()
}

try {
  Write-Host "META_ADS_READONLY_EXPORT_START"
  Write-Host "Export dir: $exportDir"

  $me = Invoke-MetaGet -GraphVersion $graphVersion -Token $token -Path 'me' -Params @{ fields = 'id,name' }
  Save-Json $me (Join-Path $rawDir '00_me.json')
  $manifest.endpoints += @{ name='me'; status='ok' }

  $accountFields = 'id,name,account_status,currency,timezone_name,amount_spent,balance,business,created_time'
  $account = Invoke-MetaGet -GraphVersion $graphVersion -Token $token -Path $adAccountId -Params @{ fields = $accountFields }
  Save-Json $account (Join-Path $rawDir '01_account.json')
  $manifest.endpoints += @{ name='account'; status='ok' }

  $campaignFields = 'id,name,status,effective_status,objective,buying_type,special_ad_categories,created_time,updated_time,start_time,stop_time,daily_budget,lifetime_budget,configured_status'
  $campaigns = Invoke-MetaGet -GraphVersion $graphVersion -Token $token -Path "$adAccountId/campaigns" -Params @{ fields=$campaignFields; limit='500' } -Paged
  Save-Json $campaigns (Join-Path $rawDir '02_campaigns.json')
  Export-CsvSafe $campaigns (Join-Path $csvDir '02_campaigns.csv')
  $manifest.endpoints += @{ name='campaigns'; status='ok'; rows=@($campaigns).Count }

  $adsetFields = 'id,name,campaign_id,campaign{name},status,effective_status,optimization_goal,billing_event,bid_strategy,daily_budget,lifetime_budget,targeting,promoted_object,created_time,updated_time,start_time,end_time'
  $adsets = Invoke-MetaGet -GraphVersion $graphVersion -Token $token -Path "$adAccountId/adsets" -Params @{ fields=$adsetFields; limit='500' } -Paged
  Save-Json $adsets (Join-Path $rawDir '03_adsets.json')
  Export-CsvSafe $adsets (Join-Path $csvDir '03_adsets.csv')
  $manifest.endpoints += @{ name='adsets'; status='ok'; rows=@($adsets).Count }

  $adFields = 'id,name,campaign_id,adset_id,status,effective_status,creative{id,name,object_story_spec,asset_feed_spec,thumbnail_url,call_to_action_type},created_time,updated_time'
  $ads = Invoke-MetaGet -GraphVersion $graphVersion -Token $token -Path "$adAccountId/ads" -Params @{ fields=$adFields; limit='500' } -Paged
  Save-Json $ads (Join-Path $rawDir '04_ads.json')
  Export-CsvSafe $ads (Join-Path $csvDir '04_ads.csv')
  $manifest.endpoints += @{ name='ads'; status='ok'; rows=@($ads).Count }

  $insightFields = 'campaign_name,adset_name,ad_name,spend,impressions,reach,frequency,clicks,inline_link_clicks,actions,cost_per_action_type,cpc,ctr,cpm'
  foreach ($level in @('campaign','adset','ad')) {
    $params = @{ level=$level; date_preset=$DatePreset; fields=$insightFields; limit='500' }
    if ($TimeIncrement -gt 0) { $params['time_increment'] = [string]$TimeIncrement }
    try {
      $rows = Invoke-MetaGet -GraphVersion $graphVersion -Token $token -Path "$adAccountId/insights" -Params $params -Paged
      Save-Json $rows (Join-Path $rawDir "05_insights_${level}.json")
      $flat = @(Flatten-InsightRows -Rows @($rows))
      Export-CsvSafe $flat (Join-Path $csvDir "05_insights_${level}.csv")
      $manifest.endpoints += @{ name="insights_$level"; status='ok'; rows=@($rows).Count }
    } catch {
      $manifest.errors += @{ name="insights_$level"; message=$_.Exception.Message }
      $manifest.endpoints += @{ name="insights_$level"; status='error' }
    }
  }

  $breakdowns = @(
    @{ name='publisher_platform_platform_position'; value='publisher_platform,platform_position' },
    @{ name='impression_device'; value='impression_device' },
    @{ name='age_gender'; value='age,gender' },
    @{ name='region'; value='region' }
  )

  foreach ($bd in $breakdowns) {
    try {
      $params = @{ level='ad'; date_preset=$DatePreset; fields=$insightFields; breakdowns=$bd.value; limit='500' }
      if ($TimeIncrement -gt 0) { $params['time_increment'] = [string]$TimeIncrement }
      $rows = Invoke-MetaGet -GraphVersion $graphVersion -Token $token -Path "$adAccountId/insights" -Params $params -Paged
      Save-Json $rows (Join-Path $rawDir "06_breakdown_$($bd.name).json")
      $flat = @(Flatten-InsightRows -Rows @($rows))
      Export-CsvSafe $flat (Join-Path $csvDir "06_breakdown_$($bd.name).csv")
      $manifest.endpoints += @{ name="breakdown_$($bd.name)"; status='ok'; rows=@($rows).Count }
    } catch {
      $manifest.errors += @{ name="breakdown_$($bd.name)"; message=$_.Exception.Message }
      $manifest.endpoints += @{ name="breakdown_$($bd.name)"; status='error' }
    }
  }

  $summary = [ordered]@{
    status = 'EXPORT_OK'
    generated_at = (Get-Date).ToString('s')
    date_preset = $DatePreset
    campaigns = @($campaigns).Count
    adsets = @($adsets).Count
    ads = @($ads).Count
    errors = @($manifest.errors).Count
    export_dir = $exportDir
  }
  Save-Json $summary (Join-Path $exportDir 'summary.json')

  $md = @"
# Meta Ads read-only export summary

Estado: `EXPORT_OK`

- Fecha ejecucion: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
- Date preset: `$DatePreset`
- Time increment: `$TimeIncrement`
- Campanas exportadas: $(@($campaigns).Count)
- Conjuntos exportados: $(@($adsets).Count)
- Anuncios exportados: $(@($ads).Count)
- Errores parciales: $(@($manifest.errors).Count)
- Ruta local: `$exportDir`

## Seguridad

- Token no impreso.
- App Secret no usado.
- Outputs crudos quedan fuera de GitHub.
- Antes de versionar conclusiones, sanitizar IDs completos, URLs sensibles y datos personales.
"@
  $md | Set-Content -LiteralPath (Join-Path $exportDir 'SUMMARY.md') -Encoding UTF8

  $manifest.status = 'EXPORT_OK'
  $manifest.finished_at = (Get-Date).ToString('s')
  Save-Json $manifest (Join-Path $exportDir 'manifest.json')

  Write-Host "EXPORT_OK"
  Write-Host "Campaigns: $(@($campaigns).Count)"
  Write-Host "Adsets: $(@($adsets).Count)"
  Write-Host "Ads: $(@($ads).Count)"
  Write-Host "Errors: $(@($manifest.errors).Count)"
  Write-Host "Output: $exportDir"
}
catch {
  $manifest.status = 'EXPORT_FAIL'
  $manifest.finished_at = (Get-Date).ToString('s')
  $manifest.errors += @{ name='fatal'; message=$_.Exception.Message }
  Save-Json $manifest (Join-Path $exportDir 'manifest.json')
  Write-Error $_
  exit 1
}
