param(
    [Parameter(Mandatory=$true)]
    [string]$OAuthClientJson,

    [Parameter(Mandatory=$true)]
    [string]$GoogleAdsConfigPath,

    [Parameter(Mandatory=$true)]
    [string]$GA4PropertyId,

    [Parameter(Mandatory=$true)]
    [string]$SpreadsheetId
)

$ErrorActionPreference = 'Stop'

$AdwordsScope = 'https://www.googleapis.com/auth/adwords'
$AnalyticsScope = 'https://www.googleapis.com/auth/analytics.readonly'
$SheetsScope = 'https://www.googleapis.com/auth/spreadsheets'
$CloudScope = 'https://www.googleapis.com/auth/cloud-platform'

Write-Host 'CAPACITA_GOOGLE_READ_SETUP=START'

if (-not (Get-Command gcloud -ErrorAction SilentlyContinue)) {
    throw 'GCLOUD_NOT_FOUND: install Google Cloud CLI first.'
}
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw 'PYTHON_NOT_FOUND'
}
if (-not (Test-Path $OAuthClientJson)) {
    throw 'OAUTH_CLIENT_JSON_NOT_FOUND'
}
if (-not (Test-Path $GoogleAdsConfigPath)) {
    throw 'GOOGLE_ADS_CONFIG_NOT_FOUND'
}
if ($GA4PropertyId -notmatch '^(properties/)?\d+$') {
    throw 'INVALID_GA4_PROPERTY_ID'
}
if ([string]::IsNullOrWhiteSpace($SpreadsheetId)) {
    throw 'INVALID_SPREADSHEET_ID'
}

$Requirements = Join-Path $PSScriptRoot 'requirements.txt'
$HealthCheck = Join-Path $PSScriptRoot 'check_google_read.py'
$PublishGA4 = Join-Path $PSScriptRoot 'publish_ga4_to_sheet.py'
$ResolvedAdsConfig = (Resolve-Path $GoogleAdsConfigPath).Path

Write-Host 'Installing/updating official Google client libraries...'
python -m pip install -r $Requirements
if ($LASTEXITCODE -ne 0) { throw 'PYTHON_DEPENDENCY_INSTALL_FAILED' }

Write-Host 'Opening ONE Google authorization flow for Google Ads + GA4 READ + reporting Sheet...'
$Scopes = "$AdwordsScope,$AnalyticsScope,$SheetsScope,$CloudScope"
gcloud auth application-default login --client-id-file="$OAuthClientJson" --scopes="$Scopes"
if ($LASTEXITCODE -ne 0) { throw 'ADC_LOGIN_FAILED' }

# Persist only non-secret runtime pointers. ADC tokens remain managed by gcloud outside GitHub.
[Environment]::SetEnvironmentVariable('GOOGLE_ADS_CONFIGURATION_FILE_PATH', $ResolvedAdsConfig, 'User')
[Environment]::SetEnvironmentVariable('GA4_PROPERTY_ID', $GA4PropertyId, 'User')
[Environment]::SetEnvironmentVariable('GOOGLE_MARKETING_SPREADSHEET_ID', $SpreadsheetId, 'User')
[Environment]::SetEnvironmentVariable('GA4_REFRESH_LOOKBACK_DAYS', '3', 'User')

$env:GOOGLE_ADS_CONFIGURATION_FILE_PATH = $ResolvedAdsConfig
$env:GA4_PROPERTY_ID = $GA4PropertyId
$env:GOOGLE_MARKETING_SPREADSHEET_ID = $SpreadsheetId
$env:GA4_REFRESH_LOOKBACK_DAYS = '3'

Write-Host 'Running unified READ-only health check...'
python $HealthCheck
$HealthExit = $LASTEXITCODE
if ($HealthExit -ne 0) {
    Write-Host 'CAPACITA_GOOGLE_READ_SETUP=HOLD_HEALTH'
    exit $HealthExit
}

Write-Host 'Publishing the first GA4 paid-Google snapshot to the existing reporting Sheet...'
python $PublishGA4
$PublishExit = $LASTEXITCODE
if ($PublishExit -ne 0) {
    Write-Host 'CAPACITA_GOOGLE_READ_SETUP=HOLD_GA4_BRIDGE'
    exit $PublishExit
}

Write-Host 'CAPACITA_GOOGLE_READ_SETUP=PASS'
Write-Host 'Credentials are stored by gcloud ADC outside the repository.'
Write-Host 'No Google Ads or GA4 configuration writes were executed.'
exit 0
