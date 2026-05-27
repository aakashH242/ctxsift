#!/usr/bin/env bash
set -euo pipefail

PACKAGE_NAME="ctxsift"
DOCS_URL="https://ctxsift.dev/docs/getting-started/installation"
REPO_URL="https://github.com/aakashh242/ctxsift"
PLATFORM_LABEL="Linux"
PREREQ_NOTE="If local CPU wheels are unavailable, install a compiler toolchain first, for example: sudo apt install build-essential"
DEFAULT_PYPI_INDEX="https://pypi.org/simple"
DEFAULT_CUDA_INDEX="https://download.pytorch.org/whl/cu124"
DEFAULT_INDEX_STRATEGY="unsafe-best-match"
IS_MACOS=0

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
  lowered="${lowered// /}"
  lowered="${lowered//;/,}"
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
  for token in "${parts[@]}"; do
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
  printf '%s' "${normalized[*]}" | tr ' ' ','
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
requested_version="$(trim "$requested_version")"

printf 'Allowed extras: remote, gpu, quant, all\n'
printf 'Examples: remote | gpu | gpu,quant | remote,gpu | all\n'
read -r -p 'Extras [base]: ' requested_extras
requested_extras="$(trim "$requested_extras")"

normalized_extras="$(normalize_extra_tokens "$requested_extras")"
if [[ "$normalized_extras" == INVALID:* ]]; then
  printf 'Unknown extras choice: %s\n' "${normalized_extras#INVALID:}"
  printf 'Choose only from: remote, gpu, quant, all\n'
  exit 1
fi

if (( IS_MACOS )) && [[ "$normalized_extras" == *gpu* || "$normalized_extras" == all ]]; then
  printf 'GPU extras are not supported by this macOS installer. Use base or remote extras only.\n'
  exit 1
fi

install_target="$(build_package_spec "$normalized_extras" "$requested_version")"
needs_gpu_install=0
if [[ "$normalized_extras" == *gpu* || "$normalized_extras" == all ]]; then
  needs_gpu_install=1
fi

cmd=(uv tool install --reinstall "$install_target")
if (( needs_gpu_install )); then
  read -r -p "CUDA wheel index [${DEFAULT_CUDA_INDEX}]: " requested_cuda_index
  requested_cuda_index="$(trim "$requested_cuda_index")"
  resolved_cuda_index="$(normalize_cuda_index "$requested_cuda_index")"
  cmd+=(--default-index "$DEFAULT_PYPI_INDEX" --index "$resolved_cuda_index" --index-strategy "$DEFAULT_INDEX_STRATEGY")
fi

printf '\nRunning:'
printf ' %q' "${cmd[@]}"
printf '\n\n'
"${cmd[@]}"

printf '\nCtxSift installed. Next steps:\n'
printf '  ctxsift doctor\n'
printf '  %s\n' "$DOCS_URL"
printf 'If ctxsift is not found, run: uv tool update-shell\n'
