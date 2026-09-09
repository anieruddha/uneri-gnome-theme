#!/usr/bin/env bash

# Uneri theme installer.
#
# Installs the requested Uneri GTK/GNOME Shell theme
# into the current user's theme directory.
#
# Does not modify gsettings or apply any theme.
#
# Usage:
#   ./scripts/install-theme.sh dark
#   ./scripts/install-theme.sh light

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"
source "${SCRIPT_DIR}/scripts/lib.sh"

VARIANT="${1:-}"
VARIANT="${VARIANT,,}"
VARIANT="${VARIANT^}"

case "${VARIANT}" in
  Dark)  THEME_NAME="Uneri-Dark" ;;
  Light) THEME_NAME="Uneri-Light" ;;
  *)
    uneri_err "Usage: $0 <dark|light>"
    exit 1
    ;;
esac

uneri_log "Installing ${THEME_NAME} theme to ${UNERI_THEMES_DIR}"

SOURCE_DIR="${SCRIPT_DIR}/themes/${THEME_NAME}"
TARGET_DIR="${UNERI_THEMES_DIR}/${THEME_NAME}"

if [[ ! -d "${SOURCE_DIR}" ]]; then
  uneri_die "Theme source directory does not exist: ${SOURCE_DIR}"
fi

mkdir -p "${UNERI_THEMES_DIR}"

rm -rf -- "${TARGET_DIR}"
cp -r "${SOURCE_DIR}" "${TARGET_DIR}"

uneri_ok "Installed ${THEME_NAME}"
