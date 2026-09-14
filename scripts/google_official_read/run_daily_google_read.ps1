$ErrorActionPreference = 'Stop'

$Script = Join-Path $PSScriptRoot 'run_daily_google_read.py'
$LogRoot = Join-Path $env:LOCALAPPDATA 'Capacita\Marketing\google-read\logs'
New-Item -ItemType Directory -Force -Path $LogRoot | Out-Null
$LogPath = Join-Path $LogRoot ("google-read-{0}.log" -f (Get-Date -Format 'yyyy-MM-dd'))

try {
    $Output = & python $Script 2>&1
    $ExitCode = $LASTEXITCODE
    $Output | Out-File -FilePath $LogPath -Encoding utf8 -Append
    if ($ExitCode -ne 0) {
        "GOOGLE_READ_DAILY=HOLD exit=$ExitCode" | Out-File -FilePath $LogPath -Encoding utf8 -Append
        exit $ExitCode
    }
    "GOOGLE_READ_DAILY=PASS" | Out-File -FilePath $LogPath -Encoding utf8 -Append
    exit 0
}
catch {
    "GOOGLE_READ_DAILY=HOLD $($_.Exception.GetType().Name)" | Out-File -FilePath $LogPath -Encoding utf8 -Append
    exit 2
}
