param(
    [Parameter(Mandatory=$true)]
    [string]$OAuthClientJson,

    [Parameter(Mandatory=$true)]
    [string]$GoogleAdsConfigPath,

    [Parameter(Mandatory=$true)]
    [string]$GA4PropertyId,

    [Parameter(Mandatory=$true)]
    [string]$SpreadsheetId,

    [string]$DailyAt = '05:30'
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
if ($DailyAt -notmatch '^([01]\d|2[0-3]):[0-5]\d$') {
    throw 'INVALID_DAILY_TIME'
}

$Requirements = Join-Path $PSScriptRoot 'requirements.txt'
$DailyRunner = Join-Path $PSScriptRoot 'run_daily_google_read.py'
$TaskInstaller = Join-Path $PSScriptRoot 'install_google_read_task.ps1'
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

Write-Host 'Running live health checks and first GA4 bridge refresh...'
python $DailyRunner
$DailyExit = $LASTEXITCODE
if ($DailyExit -ne 0) {
    Write-Host 'CAPACITA_GOOGLE_READ_SETUP=HOLD_LIVE_CHECK'
    exit $DailyExit
}

Write-Host "Installing resilient daily task at $DailyAt..."
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File $TaskInstaller -DailyAt $DailyAt
if ($LASTEXITCODE -ne 0) {
    Write-Host 'CAPACITA_GOOGLE_READ_SETUP=HOLD_SCHEDULER'
    exit $LASTEXITCODE
}

Write-Host 'CAPACITA_GOOGLE_READ_SETUP=PASS'
Write-Host 'Credentials are stored by gcloud ADC outside the repository.'
Write-Host 'Daily task installed with StartWhenAvailable.'
Write-Host 'No Google Ads or GA4 configuration writes were executed.'
exit 0
