$ErrorActionPreference = 'Stop'

$packageName = "ctxsift"
$docsUrl = "https://ctxsift.dev/docs/getting-started/installation"
$repoUrl = "https://github.com/aakashh242/ctxsift"
$defaultPypiIndex = "https://pypi.org/simple"
$defaultCudaIndex = "https://download.pytorch.org/whl/cu124"
$defaultTorchWheel = "https://download.pytorch.org/whl/cu124/torch-2.6.0%2Bcu124-cp312-cp312-win_amd64.whl"
$defaultIndexStrategy = "unsafe-best-match"

function Normalize-Extras {
    param([string]$Raw)

    $value = if ($null -eq $Raw) { '' } else { $Raw }
    $value = $value.Trim().ToLowerInvariant().Replace(';', ',').Replace(' ', '')
    if ([string]::IsNullOrWhiteSpace($value) -or $value -eq 'base' -or $value -eq 'none') {
        return ''
    }
    if ($value -eq 'all') {
        return 'all'
    }

    $allowed = @('remote', 'gpu', 'quant')
    $tokens = @()
    foreach ($token in ($value -split ',')) {
        if ([string]::IsNullOrWhiteSpace($token)) {
            continue
        }
        if ($allowed -notcontains $token) {
            throw "Unknown extras choice: $token"
        }
        $tokens += $token
    }

    $normalized = New-Object System.Collections.Generic.List[string]
    if ($tokens -contains 'remote') {
        $normalized.Add('remote')
    }
    if (($tokens -contains 'gpu') -or ($tokens -contains 'quant')) {
        $normalized.Add('gpu')
    }
    if ($tokens -contains 'quant') {
        $normalized.Add('quant')
    }
    return ($normalized | Select-Object -Unique) -join ','
}

function Normalize-CudaIndex {
    param([string]$Raw)

    $value = if ($null -eq $Raw) { '' } else { $Raw }
    $value = $value.Trim()
    if ([string]::IsNullOrWhiteSpace($value)) {
        return $defaultCudaIndex
    }
    if ($value -match '^https?://') {
        return $value
    }
    return "https://download.pytorch.org/whl/$value"
}

function Build-PackageSpec {
    param(
        [string]$NormalizedExtras,
        [string]$Version
    )

    $spec = $packageName
    if (-not [string]::IsNullOrWhiteSpace($NormalizedExtras)) {
        $spec = "$($packageName)[$NormalizedExtras]"
    }
    if (-not [string]::IsNullOrWhiteSpace($Version)) {
        $spec = "$spec==$Version"
    }
    return $spec
}

Write-Host ''
Write-Host 'CtxSift installer for Windows'
Write-Host "Docs: $docsUrl"
Write-Host "Repository: $repoUrl"
Write-Host ''

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host 'uv is required but was not found on PATH.'
    Write-Host 'Install uv first: https://docs.astral.sh/uv/getting-started/installation/'
    exit 1
}

Write-Host 'If local CPU wheels are unavailable, install Visual Studio Build Tools with Desktop development with C++.'
Write-Host ''

$requestedVersion = (Read-Host 'Version to install [latest]').Trim()
Write-Host 'Allowed extras: remote, gpu, quant, all'
Write-Host 'Examples: remote | gpu | gpu,quant | remote,gpu | all'
$requestedExtras = Read-Host 'Extras [base]'

try {
    $normalizedExtras = Normalize-Extras $requestedExtras
} catch {
    Write-Host $_.Exception.Message
    Write-Host 'Choose only from: remote, gpu, quant, all'
    exit 1
}

$packageSpec = Build-PackageSpec $normalizedExtras $requestedVersion
$needsGpuInstall = $normalizedExtras -eq 'all' -or $normalizedExtras.Contains('gpu')

$arguments = New-Object System.Collections.Generic.List[string]
$arguments.Add('tool')
$arguments.Add('install')
$arguments.Add('--reinstall')
$arguments.Add($packageSpec)

if ($needsGpuInstall) {
    $requestedCudaIndex = Read-Host "CUDA wheel index [$defaultCudaIndex]"
    $resolvedCudaIndex = Normalize-CudaIndex $requestedCudaIndex
    $requestedTorchWheel = (Read-Host "Exact torch wheel URL [$defaultTorchWheel]").Trim()
    if ([string]::IsNullOrWhiteSpace($requestedTorchWheel)) {
        $requestedTorchWheel = $defaultTorchWheel
    }
    $arguments.Add('--with')
    $arguments.Add("torch @ $requestedTorchWheel")
    $arguments.Add('--default-index')
    $arguments.Add($defaultPypiIndex)
    $arguments.Add('--index')
    $arguments.Add($resolvedCudaIndex)
    $arguments.Add('--index-strategy')
    $arguments.Add($defaultIndexStrategy)
}

Write-Host ''
Write-Host 'Running:'
Write-Host ('uv ' + (($arguments | ForEach-Object {
    if ($_ -match '\s') { '"' + $_ + '"' } else { $_ }
}) -join ' '))
Write-Host ''

& uv @arguments

Write-Host ''
Write-Host 'CtxSift installed. Next steps:'
Write-Host '  ctxsift doctor'
Write-Host "  $docsUrl"
Write-Host 'If ctxsift is not found, run: uv tool update-shell'
