const DEFAULT_PACKAGE_NAME = 'ctxsift';
const DEFAULT_REPO_URL = 'https://ctxsift.dev/docs/getting-started/installation';
const DEFAULT_PYPI_INDEX = 'https://pypi.org/simple';
const DEFAULT_LINUX_CUDA_INDEX = 'https://download.pytorch.org/whl/cu124';
const DEFAULT_WINDOWS_CUDA_INDEX = 'https://download.pytorch.org/whl/cu124';
const DEFAULT_WINDOWS_TORCH_WHEEL =
  'https://download.pytorch.org/whl/cu124/torch-2.6.0%2Bcu124-cp312-cp312-win_amd64.whl';
const DEFAULT_INDEX_STRATEGY = 'unsafe-best-match';

type InstallToken = 'remote' | 'gpu' | 'quant' | 'all';
type UnixPlatform = 'linux' | 'macos';

function envValue(name: string): string {
  const env = (import.meta as ImportMeta & { env?: Record<string, string | undefined> }).env;
  return env?.[name] || '';
}

function trimTrailingSlash(value: string): string {
  return value.replace(/\/+$/, '');
}

function siteBaseUrl(): string {
  const explicit = envValue('PUBLIC_LANDING_URL') || envValue('PUBLIC_SITE_URL');
  return explicit ? trimTrailingSlash(explicit) : '';
}

export function docsUrl(): string {
  const base = siteBaseUrl();
  return base ? `${base}/docs/getting-started/installation/` : `${repoUrl()}#install`;
}

export function repoUrl(): string {
  return envValue('PUBLIC_REPO_URL') || DEFAULT_REPO_URL;
}

function packageName(): string {
  return envValue('PUBLIC_INSTALL_PACKAGE') || DEFAULT_PACKAGE_NAME;
}

function packageWithExtras(tokens: InstallToken[]): string {
  const normalized = normalizeInstallTokens(tokens);
  if (!normalized.length) {
    return packageName();
  }
  if (normalized.includes('all')) {
    return `${packageName()}[all]`;
  }
  return `${packageName()}[${normalized.join(',')}]`;
}

function installSpec(tokens: InstallToken[], version: string): string {
  const base = packageWithExtras(tokens);
  return version ? `${base}==${version}` : base;
}

function normalizeInstallTokens(tokens: InstallToken[]): InstallToken[] {
  if (tokens.includes('all')) {
    return ['all'];
  }
  const ordered: InstallToken[] = [];
  if (tokens.includes('remote')) {
    ordered.push('remote');
  }
  if (tokens.includes('gpu') || tokens.includes('quant')) {
    ordered.push('gpu');
  }
  if (tokens.includes('quant')) {
    ordered.push('quant');
  }
  return ordered;
}

function unixPrereq(platform: UnixPlatform): string {
  if (platform === 'macos') {
    return 'If local CPU wheels are unavailable, install Xcode Command Line Tools with: xcode-select --install';
  }
  return 'If local CPU wheels are unavailable, install a compiler toolchain first, for example: sudo apt install build-essential';
}

function installerPromptDescription(platform: UnixPlatform): string {
  if (platform === 'macos') {
    return 'The installer asks for a version and extras. On macOS, GPU extras are blocked because CtxSift GPU mode currently targets CUDA on Linux and Windows.';
  }
  return 'The installer asks for a version and extras. On GPU installs, it also asks for the CUDA wheel index and, on Windows, the exact torch wheel URL.';
}

export function buildUnixInstaller(platform: UnixPlatform): string {
  const platformLabel = platform === 'macos' ? 'macOS' : 'Linux';
  const installationDocs = docsUrl();
  const repository = repoUrl();
  const defaultCudaIndex = DEFAULT_LINUX_CUDA_INDEX;
  return `#!/usr/bin/env bash
set -euo pipefail

PACKAGE_NAME=${JSON.stringify(packageName())}
DOCS_URL=${JSON.stringify(installationDocs)}
REPO_URL=${JSON.stringify(repository)}
PLATFORM_LABEL=${JSON.stringify(platformLabel)}
PREREQ_NOTE=${JSON.stringify(unixPrereq(platform))}
DEFAULT_PYPI_INDEX=${JSON.stringify(DEFAULT_PYPI_INDEX)}
DEFAULT_CUDA_INDEX=${JSON.stringify(defaultCudaIndex)}
DEFAULT_INDEX_STRATEGY=${JSON.stringify(DEFAULT_INDEX_STRATEGY)}
IS_MACOS=${platform === 'macos' ? '1' : '0'}

trim() {
  printf '%s' "$1" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//'
}

normalize_cuda_index() {
  local raw="$1"
  if [[ -z "$raw" ]]; then
    printf '%s' "$DEFAULT_CUDA_INDEX"
    return
  fi
  if [[ "$raw" == http://* || "$raw" == https://* ]]; then
    printf '%s' "$raw"
    return
  fi
  printf 'https://download.pytorch.org/whl/%s' "$raw"
}

normalize_extra_tokens() {
  local raw="$1"
  local lowered
  lowered="$(printf '%s' "$raw" | tr '[:upper:]' '[:lower:]')"
  lowered="\${lowered// /}"
  lowered="\${lowered//;/,}"
  if [[ -z "$lowered" || "$lowered" == "base" || "$lowered" == "none" ]]; then
    printf ''
    return
  fi
  if [[ "$lowered" == "all" ]]; then
    printf 'all'
    return
  fi

  local wants_remote=0
  local wants_gpu=0
  local wants_quant=0
  IFS=',' read -r -a parts <<< "$lowered"
  for token in "\${parts[@]}"; do
    case "$token" in
      '')
        ;;
      remote)
        wants_remote=1
        ;;
      gpu)
        wants_gpu=1
        ;;
      quant)
        wants_quant=1
        wants_gpu=1
        ;;
      *)
        printf 'INVALID:%s' "$token"
        return
        ;;
    esac
  done

  local normalized=()
  if (( wants_remote )); then
    normalized+=('remote')
  fi
  if (( wants_gpu )); then
    normalized+=('gpu')
  fi
  if (( wants_quant )); then
    normalized+=('quant')
  fi
  printf '%s' "\${normalized[*]}" | tr ' ' ','
}

build_package_spec() {
  local normalized="$1"
  local version="$2"
  local spec="$PACKAGE_NAME"
  if [[ -n "$normalized" ]]; then
    spec="$PACKAGE_NAME[$normalized]"
  fi
  if [[ -n "$version" ]]; then
    spec="$spec==$version"
  fi
  printf '%s' "$spec"
}

printf '\\nCtxSift installer for %s\\n' "$PLATFORM_LABEL"
printf 'Docs: %s\\n' "$DOCS_URL"
printf 'Repository: %s\\n\\n' "$REPO_URL"

if ! command -v uv >/dev/null 2>&1; then
  printf 'uv is required but was not found on PATH.\\n'
  printf 'Install uv first: https://docs.astral.sh/uv/getting-started/installation/\\n'
  exit 1
fi

printf '%s\\n\\n' "$PREREQ_NOTE"

read -r -p 'Version to install [latest]: ' requested_version
requested_version="$(trim "$requested_version")"

printf 'Allowed extras: remote, gpu, quant, all\\n'
printf 'Examples: remote | gpu | gpu,quant | remote,gpu | all\\n'
read -r -p 'Extras [base]: ' requested_extras
requested_extras="$(trim "$requested_extras")"

normalized_extras="$(normalize_extra_tokens "$requested_extras")"
if [[ "$normalized_extras" == INVALID:* ]]; then
  printf 'Unknown extras choice: %s\\n' "\${normalized_extras#INVALID:}"
  printf 'Choose only from: remote, gpu, quant, all\\n'
  exit 1
fi

if (( IS_MACOS )) && [[ "$normalized_extras" == *gpu* || "$normalized_extras" == all ]]; then
  printf 'GPU extras are not supported by this macOS installer. Use base or remote extras only.\\n'
  exit 1
fi

install_target="$(build_package_spec "$normalized_extras" "$requested_version")"
needs_gpu_install=0
if [[ "$normalized_extras" == *gpu* || "$normalized_extras" == all ]]; then
  needs_gpu_install=1
fi

cmd=(uv tool install --reinstall "$install_target")
if (( needs_gpu_install )); then
  read -r -p "CUDA wheel index [\${DEFAULT_CUDA_INDEX}]: " requested_cuda_index
  requested_cuda_index="$(trim "$requested_cuda_index")"
  resolved_cuda_index="$(normalize_cuda_index "$requested_cuda_index")"
  cmd+=(--default-index "$DEFAULT_PYPI_INDEX" --index "$resolved_cuda_index" --index-strategy "$DEFAULT_INDEX_STRATEGY")
fi

printf '\\nRunning:'
printf ' %q' "\${cmd[@]}"
printf '\\n\\n'
"\${cmd[@]}"

printf '\\nCtxSift installed. Next steps:\\n'
printf '  ctxsift doctor\\n'
printf '  %s\\n' "$DOCS_URL"
printf 'If ctxsift is not found, run: uv tool update-shell\\n'
`;
}

export function buildPowerShellInstaller(): string {
  const installationDocs = docsUrl();
  const repository = repoUrl();
  return `$ErrorActionPreference = 'Stop'

$packageName = ${JSON.stringify(packageName())}
$docsUrl = ${JSON.stringify(installationDocs)}
$repoUrl = ${JSON.stringify(repository)}
$defaultPypiIndex = ${JSON.stringify(DEFAULT_PYPI_INDEX)}
$defaultCudaIndex = ${JSON.stringify(DEFAULT_WINDOWS_CUDA_INDEX)}
$defaultTorchWheel = ${JSON.stringify(DEFAULT_WINDOWS_TORCH_WHEEL)}
$defaultIndexStrategy = ${JSON.stringify(DEFAULT_INDEX_STRATEGY)}

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
    if ($_ -match '\\s') { '"' + $_ + '"' } else { $_ }
}) -join ' '))
Write-Host ''

& uv @arguments

Write-Host ''
Write-Host 'CtxSift installed. Next steps:'
Write-Host '  ctxsift doctor'
Write-Host "  $docsUrl"
Write-Host 'If ctxsift is not found, run: uv tool update-shell'
`;
}

export function suggestedDownloadName(platform: 'linux' | 'macos' | 'windows'): string {
  if (platform === 'windows') {
    return 'ctxsift-install.ps1';
  }
  if (platform === 'macos') {
    return 'ctxsift-install-macos.sh';
  }
  return 'ctxsift-install-linux.sh';
}

export function installerSpecPreview(tokens: InstallToken[], version: string): string {
  return installSpec(tokens, version);
}

export function installerPromptSummary(platform: UnixPlatform | 'windows'): string {
  if (platform === 'windows') {
    return 'The installer asks for a version, extras, a CUDA wheel index for GPU installs, and an exact torch wheel URL on Windows.';
  }
  return installerPromptDescription(platform);
}
