#!/usr/bin/env bash
# Uneri theme uninstaller.
#
# Removes the requested Uneri GTK/GNOME Shell theme
# from the current user's theme directory.
#
# Does not modify gsettings or change the current appearance.
#
# Usage:
#   ./scripts/uninstall-theme.sh dark
#   ./scripts/uninstall-theme.sh light

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

THEME_DIR="${UNERI_THEMES_DIR}/${THEME_NAME}"

uneri_log "Removing ${THEME_NAME} theme"

if [[ ! -e "${THEME_DIR}" ]]; then
  uneri_log "${THEME_NAME} is not installed — nothing to remove."
  exit 0
fi

EXPECTED_THEME_DIR="${HOME}/.local/share/themes/${THEME_NAME}"

if [[ "${THEME_DIR}" != "${EXPECTED_THEME_DIR}" ]]; then
  uneri_die "refusing to remove unexpected theme directory: ${THEME_DIR}"
fi

rm -rf -- "${THEME_DIR}"

uneri_ok "Removed ${THEME_NAME} theme."
