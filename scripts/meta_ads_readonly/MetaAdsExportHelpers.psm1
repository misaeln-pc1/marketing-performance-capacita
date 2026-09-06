<#
.SYNOPSIS
  Helper functions for Meta Ads export and sanitization.
#>

Set-StrictMode -Version Latest

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

function Sanitize-MetaText {
  param([Parameter(Mandatory=$false)][string]$Text)
  if ([string]::IsNullOrWhiteSpace($Text)) { return '' }
  $s = $Text
  # Mask access tokens
  $s = [regex]::Replace($s, '(?i)(access_token|bearer)[=:\s]+[a-zA-Z0-9_\-\.]+', '$1=***MASKED***')
  $s = [regex]::Replace($s, 'EAAB[a-zA-Z0-9]+', '***MASKED_META_TOKEN***')
  # Mask sensitive URLs containing query tokens
  $s = [regex]::Replace($s, 'https?://[^\s"''<>]+\?[^\s"''<>]*access_token=[^\s"''&]+', 'https://graph.facebook.com/***MASKED_URL***')
  return $s
}

function Sanitize-MetaUri {
  param([Parameter(Mandatory=$false)][string]$UriString)
  if ([string]::IsNullOrWhiteSpace($UriString)) { return $null }
  return (Sanitize-MetaText -Text $UriString)
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

Export-ModuleMember -Function Get-PropSafe, Flatten-InsightRows, Sanitize-MetaText, Sanitize-MetaUri
