[CmdletBinding()]
param(
    [ValidateSet('Prepare', 'Doctor', 'Run', 'Status')]
    [string]$Action = 'Run',

    [string]$TunnelId,

    [string]$LocalStateDirectory = (Join-Path $env:LOCALAPPDATA 'Capacita\GoogleAdsMcpRead')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$TunnelClientPath = 'C:\Tools\OpenAI\tunnel-client\tunnel-client.exe'
$ServiceAccountPath = 'C:\Users\TECH\secrets\google-ads-mcp-service-account.json'
$ExpectedProjectId = 'capacitacl-210323'
$ProfileName = 'capacita-google-ads-read'
$TunnelIdPath = Join-Path $LocalStateDirectory 'tunnel-id.txt'
$ProfileDirectory = Join-Path $LocalStateDirectory 'profiles'
$HealthUrlPath = Join-Path $LocalStateDirectory 'health-url.txt'
$PidPath = Join-Path $LocalStateDirectory 'tunnel-client.pid'

function Assert-Prerequisites {
    if (-not (Test-Path -LiteralPath $TunnelClientPath -PathType Leaf)) {
        throw 'TUNNEL_CLIENT_NOT_FOUND'
    }

    if (-not (Test-Path -LiteralPath $ServiceAccountPath -PathType Leaf)) {
        throw 'GOOGLE_ADS_SERVICE_ACCOUNT_JSON_NOT_FOUND'
    }

    $serviceAccount = Get-Content -LiteralPath $ServiceAccountPath -Raw | ConvertFrom-Json
    if ($serviceAccount.type -ne 'service_account') {
        throw 'GOOGLE_ADS_CREDENTIAL_TYPE_INVALID'
    }
    if ($serviceAccount.project_id -ne $ExpectedProjectId) {
        throw 'GOOGLE_ADS_SERVICE_ACCOUNT_PROJECT_MISMATCH'
    }
    if ([string]::IsNullOrWhiteSpace([string]$serviceAccount.client_email) -or
        [string]::IsNullOrWhiteSpace([string]$serviceAccount.private_key)) {
        throw 'GOOGLE_ADS_SERVICE_ACCOUNT_FIELDS_MISSING'
    }

    $pipx = Get-Command pipx -CommandType Application -ErrorAction SilentlyContinue
    if ($null -eq $pipx) {
        throw 'PIPX_NOT_FOUND'
    }

    return $pipx.Source
}

function Resolve-TunnelId {
    param([string]$RequestedTunnelId)

    $candidates = [System.Collections.Generic.HashSet[string]]::new(
        [System.StringComparer]::Ordinal
    )

    if (-not [string]::IsNullOrWhiteSpace($RequestedTunnelId)) {
        [void]$candidates.Add($RequestedTunnelId.Trim())
    }

    foreach ($scope in @('Process', 'User', 'Machine')) {
        $value = [Environment]::GetEnvironmentVariable('CONTROL_PLANE_TUNNEL_ID', $scope)
        if (-not [string]::IsNullOrWhiteSpace($value)) {
            [void]$candidates.Add($value.Trim())
        }
    }

    if (Test-Path -LiteralPath $TunnelIdPath -PathType Leaf) {
        $value = (Get-Content -LiteralPath $TunnelIdPath -Raw).Trim()
        if (-not [string]::IsNullOrWhiteSpace($value)) {
            [void]$candidates.Add($value)
        }
    }

    $historyPaths = @(
        (Join-Path $env:APPDATA 'Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt'),
        (Join-Path $env:APPDATA 'Microsoft\PowerShell\PSReadLine\ConsoleHost_history.txt')
    )

    foreach ($historyPath in $historyPaths) {
        if (-not (Test-Path -LiteralPath $historyPath -PathType Leaf)) {
            continue
        }
        foreach ($line in Get-Content -LiteralPath $historyPath -ErrorAction SilentlyContinue) {
            foreach ($match in [regex]::Matches([string]$line, 'tunnel_[A-Za-z0-9]{16,}')) {
                [void]$candidates.Add($match.Value)
            }
        }
    }

    $codexSessionRoot = Join-Path $env:USERPROFILE '.codex\sessions'
    if (Test-Path -LiteralPath $codexSessionRoot -PathType Container) {
        $recentSessionFiles = @(
            Get-ChildItem -LiteralPath $codexSessionRoot -Filter '*.jsonl' -File -Recurse -ErrorAction SilentlyContinue |
                Sort-Object LastWriteTime -Descending |
                Select-Object -First 20
        )
        foreach ($sessionFile in $recentSessionFiles) {
            foreach ($line in Get-Content -LiteralPath $sessionFile.FullName -ErrorAction SilentlyContinue) {
                foreach ($match in [regex]::Matches([string]$line, 'tunnel_[A-Za-z0-9]{16,}')) {
                    [void]$candidates.Add($match.Value)
                }
            }
        }
    }

    $documentationPlaceholder = 'tunnel_0123456789abcdef0123456789abcdef'
    $valid = @(
        $candidates | Where-Object {
            $_ -match '^tunnel_[A-Za-z0-9]{16,}$' -and $_ -ne $documentationPlaceholder
        }
    )
    if ($valid.Count -ne 1) {
        throw "TUNNEL_ID_UNIQUE_RECOVERY_FAILED_COUNT=$($valid.Count)"
    }

    return $valid[0]
}

function Set-ProcessApiKey {
    if (-not [string]::IsNullOrWhiteSpace($env:CONTROL_PLANE_API_KEY)) {
        return $false
    }

    $secureValue = Read-Host 'CONTROL_PLANE_API_KEY (entrada oculta, sólo memoria de este proceso)' -AsSecureString
    if ($secureValue.Length -eq 0) {
        throw 'CONTROL_PLANE_API_KEY_EMPTY'
    }

    $pointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureValue)
    try {
        $env:CONTROL_PLANE_API_KEY = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($pointer)
    }
    finally {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($pointer)
    }

    return $true
}

function Write-LocalProfile {
    param(
        [string]$ResolvedTunnelId,
        [string]$PipxPath
    )

    New-Item -ItemType Directory -Path $ProfileDirectory -Force | Out-Null
    Set-Content -LiteralPath $TunnelIdPath -Value $ResolvedTunnelId -Encoding ascii -NoNewline

    $pipxCommandPath = $PipxPath.Replace('\', '/')
    $mcpCommand = $pipxCommandPath + ' run --spec git+https://github.com/googleads/google-ads-mcp.git google-ads-mcp'
    & $TunnelClientPath init `
        --force `
        --sample sample_mcp_stdio_local `
        --profile $ProfileName `
        --profile-dir $ProfileDirectory `
        --tunnel-id $ResolvedTunnelId `
        --mcp-command $mcpCommand `
        --control-plane-api-key-ref 'env:CONTROL_PLANE_API_KEY' `
        --health-listen-addr '127.0.0.1:0'

    if ($LASTEXITCODE -ne 0) {
        throw "TUNNEL_PROFILE_INIT_FAILED_EXIT=$LASTEXITCODE"
    }
}

$promptedForApiKey = $false
try {
    $pipxPath = Assert-Prerequisites
    $resolvedTunnelId = Resolve-TunnelId -RequestedTunnelId $TunnelId
    New-Item -ItemType Directory -Path $LocalStateDirectory -Force | Out-Null
    Write-LocalProfile -ResolvedTunnelId $resolvedTunnelId -PipxPath $pipxPath

    $env:GOOGLE_APPLICATION_CREDENTIALS = $ServiceAccountPath
    $env:GOOGLE_PROJECT_ID = $ExpectedProjectId
    $env:GOOGLE_CLOUD_PROJECT = $ExpectedProjectId
    $env:CONTROL_PLANE_TUNNEL_ID = $resolvedTunnelId

    Write-Output 'LOCAL_LAUNCHER_REPRODUCIBLE=PASS'
    Write-Output 'TUNNEL_ID_RECOVERY=PASS'
    Write-Output 'GOOGLE_ADS_SERVICE_ACCOUNT_LOCAL=PASS'
    Write-Output 'SECRETS_PERSISTED_BY_LAUNCHER=0'

    if ($Action -eq 'Prepare') {
        Write-Output 'LOCAL_PROFILE=PASS'
        exit 0
    }

    if ($Action -eq 'Status') {
        if (-not (Test-Path -LiteralPath $HealthUrlPath -PathType Leaf)) {
            throw 'TUNNEL_HEALTH_URL_FILE_NOT_FOUND'
        }
        & $TunnelClientPath health `
            --url-file $HealthUrlPath `
            --pid-file $PidPath `
            --require-control-plane-poll `
            --json
        exit $LASTEXITCODE
    }

    $promptedForApiKey = Set-ProcessApiKey

    & $TunnelClientPath doctor `
        --profile $ProfileName `
        --profile-dir $ProfileDirectory `
        --explain `
        --json
    if ($LASTEXITCODE -ne 0) {
        throw "TUNNEL_DOCTOR_FAILED_EXIT=$LASTEXITCODE"
    }

    Write-Output 'TUNNEL_DOCTOR=PASS'
    if ($Action -eq 'Doctor') {
        exit 0
    }

    Remove-Item -LiteralPath $HealthUrlPath -Force -ErrorAction SilentlyContinue
    Remove-Item -LiteralPath $PidPath -Force -ErrorAction SilentlyContinue

    & $TunnelClientPath run `
        --profile $ProfileName `
        --profile-dir $ProfileDirectory `
        --health.url-file $HealthUrlPath `
        --pid.file $PidPath
    exit $LASTEXITCODE
}
finally {
    if ($promptedForApiKey) {
        Remove-Item Env:CONTROL_PLANE_API_KEY -ErrorAction SilentlyContinue
    }
}
