<#
.SYNOPSIS
  Unit/Mock test for Meta Ads export script functions under Set-StrictMode Latest.
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Write-Host "=== TEST: Meta Ads Export Mock Under Strict Mode ==="

# Import helper module directly from production code location
$modulePath = Join-Path (Join-Path (Join-Path $PSScriptRoot '..') 'scripts') 'meta_ads_readonly\MetaAdsExportHelpers.psm1'
Import-Module $modulePath -DisableNameChecking -Force

# Test 1: Mock row missing ALL breakdown properties and actions
$mockRow1 = [pscustomobject]@{
  date_start    = '2026-08-01'
  date_stop     = '2026-08-31'
  campaign_name = 'TEST_CAMPAIGN'
  spend         = '12500'
  impressions   = '4500'
  clicks        = '120'
}

$results = @(Flatten-InsightRows -Rows @($mockRow1))

if ($results.Count -ne 1) {
  Write-Error "Failed: Expected 1 result row, got $($results.Count)"
  exit 1
}

$r = $results[0]
if ($r.spend -ne '12500' -or $r.campaign_name -ne 'TEST_CAMPAIGN') {
  Write-Error "Failed: Property values mismatch"
  exit 1
}

if ($null -ne $r.breakdown_publisher_platform) {
  Write-Error "Failed: Missing property should be null"
  exit 1
}

# Test 2: Mock row WITH actions array and breakdown
$mockRow2 = [pscustomobject]@{
  date_start         = '2026-08-01'
  date_stop          = '2026-08-31'
  campaign_name      = 'TEST_CAMPAIGN_2'
  spend              = '20000'
  actions            = @(@{ action_type = 'link_click'; value = '15' })
  publisher_platform = 'facebook'
}

$results2 = @(Flatten-InsightRows -Rows @($mockRow2))
$r2 = $results2[0]

if ($r2.breakdown_publisher_platform -ne 'facebook') {
  Write-Error "Failed: publisher_platform should be facebook"
  exit 1
}

if (-not $r2.actions_json.Contains('link_click')) {
  Write-Error "Failed: actions_json should contain link_click"
  exit 1
}
# Test 3: Sanitization of tokens, exceptions and URLs
$tokenSample = 'EAAB' + '1234567890abcdef'
$sampleErr = "Error calling endpoint with access_token=" + $tokenSample
$sanitizedErr = Sanitize-MetaText $sampleErr
if ($sanitizedErr -match 'EAAB' -or -not ($sanitizedErr -match 'MASKED')) {
  Write-Error "Failed: Token was not masked in exception text"
  exit 1
}

$sampleUri = "https://graph.facebook.com/v22.0/act_123/insights?access_token=" + $tokenSample + "&limit=500"
$sanitizedUri = Sanitize-MetaUri $sampleUri
if ($sanitizedUri -match 'EAAB' -or -not ($sanitizedUri -match 'MASKED')) {
  Write-Error "Failed: Token was not masked in URI string"
  exit 1
}

Write-Host "META_PRODUCTION_CODE_MOCK=PASS"
Write-Host "META_SCRIPT_RUNTIME=MOCK_PASS"
Write-Host "All Meta script strict-mode tests passed."
exit 0
