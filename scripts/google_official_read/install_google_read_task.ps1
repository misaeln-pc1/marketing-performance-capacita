param(
    [string]$DailyAt = '05:30'
)

$ErrorActionPreference = 'Stop'

if ($DailyAt -notmatch '^([01]\d|2[0-3]):[0-5]\d$') {
    throw 'INVALID_DAILY_TIME: expected HH:mm'
}

$TaskName = 'Capacita-Marketing-Google-Read'
$Runner = (Resolve-Path (Join-Path $PSScriptRoot 'run_daily_google_read.ps1')).Path
$Time = [DateTime]::ParseExact($DailyAt, 'HH:mm', $null)

$ActionArgs = "-NoProfile -ExecutionPolicy Bypass -File `"$Runner`""
$Action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument $ActionArgs
$Trigger = New-ScheduledTaskTrigger -Daily -At $Time
$Principal = New-ScheduledTaskPrincipal `
    -UserId ("{0}\{1}" -f $env:USERDOMAIN, $env:USERNAME) `
    -LogonType Interactive `
    -RunLevel Limited
$Settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 20)

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Principal $Principal `
    -Settings $Settings `
    -Description 'Capacita Marketing: health check Google Ads + GA4 and GA4 reporting bridge. READ-only sources.' `
    -Force | Out-Null

$Task = Get-ScheduledTask -TaskName $TaskName
Write-Host "GOOGLE_READ_SCHEDULE=PASS"
Write-Host "TASK_NAME=$($Task.TaskName)"
Write-Host "DAILY_AT=$DailyAt"
Write-Host 'START_WHEN_AVAILABLE=YES'
Write-Host 'NOTE=Runs under the current interactive user without storing a Windows password.'
