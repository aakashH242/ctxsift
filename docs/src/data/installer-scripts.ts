const DEFAULT_PACKAGE_NAME = 'ctxsift';
const DEFAULT_REPO_URL = 'https://github.com/aakashh242/ctxsift';

type InstallFlavor = 'base' | 'gpu' | 'quant' | 'all';
type UnixPlatform = 'linux' | 'macos';

function trimTrailingSlash(value: string): string {
  return value.replace(/\/+$/, '');
}

function siteBaseUrl(): string {
  const explicit = import.meta.env.PUBLIC_LANDING_URL || import.meta.env.PUBLIC_SITE_URL || '';
  return explicit ? trimTrailingSlash(explicit) : '';
}

export function docsUrl(): string {
  const base = siteBaseUrl();
  return base ? `${base}/docs/getting-started/installation/` : `${repoUrl()}#install`;
}

export function repoUrl(): string {
  return import.meta.env.PUBLIC_REPO_URL || DEFAULT_REPO_URL;
}

function packageName(): string {
  return import.meta.env.PUBLIC_INSTALL_PACKAGE || DEFAULT_PACKAGE_NAME;
}

function packageWithExtras(flavor: InstallFlavor): string {
  if (flavor === 'gpu') {
    return `${packageName()}[gpu]`;
  }
  if (flavor === 'quant') {
    return `${packageName()}[gpu,quant]`;
  }
  if (flavor === 'all') {
    return `${packageName()}[all]`;
  }
  return packageName();
}

function installSpec(flavor: InstallFlavor, version: string): string {
  const base = packageWithExtras(flavor);
  return version ? `${base}==${version}` : base;
}

function unixPrereq(platform: UnixPlatform): string {
  if (platform === 'macos') {
    return 'If local CPU wheels are unavailable, install Xcode Command Line Tools with: xcode-select --install';
  }
  return 'If local CPU wheels are unavailable, install a compiler toolchain first, for example: sudo apt install build-essential';
}

export function buildUnixInstaller(platform: UnixPlatform): string {
  const platformLabel = platform === 'macos' ? 'macOS' : 'Linux';
  const installationDocs = docsUrl();
  const repository = repoUrl();
  return `#!/usr/bin/env bash
set -euo pipefail

PACKAGE_NAME=${JSON.stringify(packageName())}
DOCS_URL=${JSON.stringify(installationDocs)}
REPO_URL=${JSON.stringify(repository)}
PLATFORM_LABEL=${JSON.stringify(platformLabel)}
PREREQ_NOTE=${JSON.stringify(unixPrereq(platform))}

printf '\nCtxSift installer for %s\n' "$PLATFORM_LABEL"
printf 'Docs: %s\n' "$DOCS_URL"
printf 'Repository: %s\n\n' "$REPO_URL"

if ! command -v uv >/dev/null 2>&1; then
  printf 'uv is required but was not found on PATH.\n'
  printf 'Install uv first: https://docs.astral.sh/uv/getting-started/installation/\n'
  exit 1
fi

printf '%s\n\n' "$PREREQ_NOTE"

read -r -p 'Version to install [latest]: ' requested_version
requested_version="$(printf '%s' "$requested_version" | tr -d '[:space:]')"

printf 'Extras: base, gpu, quant, all\n'
read -r -p 'Extras [base]: ' requested_extras
requested_extras="$(printf '%s' "$requested_extras" | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')"

case "$requested_extras" in
  ''|base)
    requested_extras='base'
    ;;
  gpu)
    requested_extras='gpu'
    ;;
  quant)
    requested_extras='quant'
    ;;
  all)
    requested_extras='all'
    ;;
  *)
    printf 'Unknown extras choice: %s\n' "$requested_extras"
    printf 'Choose one of: base, gpu, quant, all\n'
    exit 1
    ;;
esac

build_spec() {
  local extras="$1"
  local version="$2"
  local spec="$PACKAGE_NAME"
  case "$extras" in
    gpu)
      spec="$PACKAGE_NAME[gpu]"
      ;;
    quant)
      spec="$PACKAGE_NAME[gpu,quant]"
      ;;
    all)
      spec="$PACKAGE_NAME[all]"
      ;;
  esac
  if [[ -n "$version" ]]; then
    spec="$spec==$version"
  fi
  printf '%s' "$spec"
}

install_target="$(build_spec "$requested_extras" "$requested_version")"

printf '\nRunning: uv tool install --reinstall %s\n\n' "$install_target"
uv tool install --reinstall "$install_target"

printf '\nCtxSift installed. Next steps:\n'
printf '  ctxsift doctor\n'
printf '  %s\n' "$DOCS_URL"
`;
}

export function buildPowerShellInstaller(): string {
  const installationDocs = docsUrl();
  const repository = repoUrl();
  return `$ErrorActionPreference = 'Stop'

$packageName = ${JSON.stringify(packageName())}
$docsUrl = ${JSON.stringify(installationDocs)}
$repoUrl = ${JSON.stringify(repository)}

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
$requestedExtras = (Read-Host 'Extras [base] (base, gpu, quant, all)').Trim().ToLowerInvariant()

if ([string]::IsNullOrWhiteSpace($requestedExtras)) {
    $requestedExtras = 'base'
}

switch ($requestedExtras) {
    'base' { $packageSpec = $packageName }
  'gpu' { $packageSpec = "$($packageName)[gpu]" }
  'quant' { $packageSpec = "$($packageName)[gpu,quant]" }
  'all' { $packageSpec = "$($packageName)[all]" }
    default {
        Write-Host "Unknown extras choice: $requestedExtras"
        Write-Host 'Choose one of: base, gpu, quant, all'
        exit 1
    }
}

if (-not [string]::IsNullOrWhiteSpace($requestedVersion)) {
    $packageSpec = "$packageSpec==$requestedVersion"
}

Write-Host ''
Write-Host "Running: uv tool install --reinstall $packageSpec"
Write-Host ''
uv tool install --reinstall $packageSpec

Write-Host ''
Write-Host 'CtxSift installed. Next steps:'
Write-Host '  ctxsift doctor'
Write-Host "  $docsUrl"
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

export function installerSpecPreview(flavor: InstallFlavor, version: string): string {
  return installSpec(flavor, version);
}