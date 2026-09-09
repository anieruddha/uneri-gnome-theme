#!/usr/bin/env bash
# Uneri icon theme uninstaller.
#
# Removes the requested Uneri icon theme from the current user's
# icon directory.
#
# Does not modify gsettings or change the active icon theme.
#
# Usage:
#   ./scripts/uninstall-icons.sh dark
#   ./scripts/uninstall-icons.sh light

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"
source "${SCRIPT_DIR}/scripts/lib.sh"

VARIANT="${1:-}"
VARIANT="${VARIANT,,}"
VARIANT="${VARIANT^}"

case "${VARIANT}" in
  Dark)  ICON_THEME_NAME="Uneri-Dark" ;;
  Light) ICON_THEME_NAME="Uneri-Light" ;;
  *)
    uneri_err "Usage: $0 <dark|light>"
    exit 1
    ;;
esac

ICON_THEME_DIR="${UNERI_ICONS_DIR}/${ICON_THEME_NAME}"
EXPECTED_ICON_THEME_DIR="${HOME}/.local/share/icons/${ICON_THEME_NAME}"

uneri_log "Removing ${ICON_THEME_NAME} icon theme"

if [[ "${ICON_THEME_DIR}" != "${EXPECTED_ICON_THEME_DIR}" ]]; then
  uneri_die "refusing to remove unexpected icon theme directory: ${ICON_THEME_DIR}"
fi

if [[ ! -e "${ICON_THEME_DIR}" ]]; then
  uneri_log "${ICON_THEME_NAME} is not installed — nothing to remove."
  exit 0
fi

rm -rf -- "${ICON_THEME_DIR}"

if uneri_require_cmd gtk-update-icon-cache; then
  gtk-update-icon-cache -f -t "${UNERI_ICONS_DIR}" >/dev/null 2>&1 || true
fi

uneri_ok "Removed ${ICON_THEME_NAME} icon theme."
