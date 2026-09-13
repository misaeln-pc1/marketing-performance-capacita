param(
    [Parameter(Mandatory=$true)]
    [string]$OAuthClientJson,

    [Parameter(Mandatory=$true)]
    [string]$GoogleAdsConfigPath
)

$ErrorActionPreference = 'Stop'

$AdwordsScope = 'https://www.googleapis.com/auth/adwords'
$AnalyticsScope = 'https://www.googleapis.com/auth/analytics.readonly'
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

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$Requirements = Join-Path $PSScriptRoot 'requirements.txt'
$HealthCheck = Join-Path $PSScriptRoot 'check_google_read.py'

Write-Host 'Installing/updating official Google client libraries...'
python -m pip install -r $Requirements
if ($LASTEXITCODE -ne 0) { throw 'PYTHON_DEPENDENCY_INSTALL_FAILED' }

Write-Host 'Opening ONE Google authorization flow for Google Ads + GA4 read scopes...'
$Scopes = "$AdwordsScope,$AnalyticsScope,$CloudScope"
gcloud auth application-default login --client-id-file="$OAuthClientJson" --scopes="$Scopes"
if ($LASTEXITCODE -ne 0) { throw 'ADC_LOGIN_FAILED' }

$env:GOOGLE_ADS_CONFIGURATION_FILE_PATH = (Resolve-Path $GoogleAdsConfigPath).Path

Write-Host 'Running unified READ-only health check...'
python $HealthCheck
$HealthExit = $LASTEXITCODE

if ($HealthExit -eq 0) {
    Write-Host 'CAPACITA_GOOGLE_READ_SETUP=PASS'
    Write-Host 'Credentials are stored by gcloud ADC outside the repository.'
    exit 0
}

Write-Host 'CAPACITA_GOOGLE_READ_SETUP=HOLD'
exit $HealthExit
