#!/usr/bin/env bash
# Installs Monaspace Neon (one weight family of GitHub's open-source
# Monaspace superfamily, SIL OFL 1.1) into the user's per-user font
# directory if it is not already present anywhere on the system.
#
# Safe to run standalone: ./scripts/install-font.sh

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"

# shellcheck source=lib.sh
source "${SCRIPT_DIR}/scripts/lib.sh"

MONASPACE_VERSION="v1.101"
MONASPACE_ZIP_URL="https://github.com/githubnext/monaspace/releases/download/${MONASPACE_VERSION}/monaspace-${MONASPACE_VERSION}.zip"

if uneri_require_cmd fc-cache; then
  fc-cache -f >/dev/null 2>&1 || true
fi

if uneri_require_cmd fc-match && [[ "$(fc-match -f '%{family}\n' 'Monaspace Neon' 2>/dev/null | head -n 1)" == "Monaspace Neon" ]]; then
  uneri_ok "Monaspace Neon is already installed and available — leaving the existing copy in place."
  exit 0
fi

if ! uneri_require_cmd curl && ! uneri_require_cmd wget; then
  uneri_warn "Neither curl nor wget is available — cannot fetch Monaspace Neon automatically."
  uneri_warn "Download it manually from https://github.com/githubnext/monaspace/releases"
  uneri_warn "and place the .ttf/.otf files in: ${UNERI_FONTS_DIR}"
  exit 0
fi

if ! uneri_require_cmd unzip; then
  uneri_warn "'unzip' is not available — cannot extract the Monaspace release archive."
  uneri_warn "Install it (e.g. 'sudo apt install unzip') and re-run this script, or install"
  uneri_warn "Monaspace Neon manually from https://github.com/githubnext/monaspace/releases"
  exit 0
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf -- "${TMP_DIR}"' EXIT

uneri_log "Downloading Monaspace Neon ${MONASPACE_VERSION}..."
if uneri_require_cmd curl; then
  curl -fsSL "${MONASPACE_ZIP_URL}" -o "${TMP_DIR}/monaspace.zip" || {
    uneri_warn "Download failed. Install Monaspace Neon manually from https://github.com/githubnext/monaspace/releases"
    exit 0
  }
else
  wget -q "${MONASPACE_ZIP_URL}" -O "${TMP_DIR}/monaspace.zip" || {
    uneri_warn "Download failed. Install Monaspace Neon manually from https://github.com/githubnext/monaspace/releases"
    exit 0
  }
fi

uneri_log "Extracting..."
unzip -q "${TMP_DIR}/monaspace.zip" -d "${TMP_DIR}/extracted"

mkdir -p "${UNERI_FONTS_DIR}"

# Only take the Neon family
find "${TMP_DIR}/extracted" -iname "*Neon*" \( -iname "*.ttf" -o -iname "*.otf" \) -print0 \
  | xargs -0 -I{} cp {} "${UNERI_FONTS_DIR}/"

count="$(find "${UNERI_FONTS_DIR}" -maxdepth 1 -iname "*.ttf" -o -iname "*.otf" | wc -l)"
if [[ "${count}" -eq 0 ]]; then
  uneri_warn "No Monaspace Neon font files found in the downloaded archive layout."
  uneri_warn "Install manually from https://github.com/githubnext/monaspace/releases"
  exit 0
fi

if uneri_require_cmd fc-cache; then
  fc-cache -f "${UNERI_FONTS_DIR}" >/dev/null 2>&1 || true
fi

uneri_ok "Installed Monaspace Neon (${count} files) to ${UNERI_FONTS_DIR}"
