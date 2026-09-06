<#
.SYNOPSIS
  Unit/Mock test for Meta Ads export script functions under Set-StrictMode Latest.
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Write-Host "=== TEST: Meta Ads Export Mock Under Strict Mode ==="

# Define the functions directly or dot-source
function Get-PropSafe {
  param(
    [Parameter(Mandatory=$false)]$Object,
    [Parameter(Mandatory=$true)][string]$PropertyName
  )
  if ($null -eq $Object) { return $null }
  if ($Object -is [System.Collections.IDictionary]) {
    if ($Object.Contains($PropertyName)) { return $Object[$PropertyName] }
    return $null
  }
  if ($null -ne $Object.PSObject -and $null -ne $Object.PSObject.Properties[$PropertyName]) {
    return $Object.PSObject.Properties[$PropertyName].Value
  }
  return $null
}

function Flatten-InsightRows {
  param([object[]]$Rows)
  foreach ($row in @($Rows)) {
    if ($null -eq $row) { continue }
    $actions = Get-PropSafe $row 'actions'
    $costPerAction = Get-PropSafe $row 'cost_per_action_type'
    [pscustomobject]@{
      date_start          = Get-PropSafe $row 'date_start'
      date_stop           = Get-PropSafe $row 'date_stop'
      campaign_name       = Get-PropSafe $row 'campaign_name'
      adset_name          = Get-PropSafe $row 'adset_name'
      ad_name             = Get-PropSafe $row 'ad_name'
      spend               = Get-PropSafe $row 'spend'
      impressions         = Get-PropSafe $row 'impressions'
      reach               = Get-PropSafe $row 'reach'
      frequency           = Get-PropSafe $row 'frequency'
      clicks              = Get-PropSafe $row 'clicks'
      inline_link_clicks  = Get-PropSafe $row 'inline_link_clicks'
      ctr                 = Get-PropSafe $row 'ctr'
      cpc                 = Get-PropSafe $row 'cpc'
      cpm                 = Get-PropSafe $row 'cpm'
      actions_json        = if ($null -ne $actions) { ($actions | ConvertTo-Json -Compress -Depth 20) } else { $null }
      cost_per_action_json = if ($null -ne $costPerAction) { ($costPerAction | ConvertTo-Json -Compress -Depth 20) } else { $null }
      breakdown_publisher_platform = Get-PropSafe $row 'publisher_platform'
      breakdown_platform_position  = Get-PropSafe $row 'platform_position'
      breakdown_impression_device  = Get-PropSafe $row 'impression_device'
      breakdown_age                = Get-PropSafe $row 'age'
      breakdown_gender             = Get-PropSafe $row 'gender'
      breakdown_region             = Get-PropSafe $row 'region'
    }
  }
}

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

Write-Host "META_SCRIPT_RUNTIME=MOCK_PASS"
Write-Host "All Meta script strict-mode tests passed."
exit 0
