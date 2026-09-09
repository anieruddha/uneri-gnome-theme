#!/usr/bin/env bash
# Uneri icon theme installer.
#
# Installs the requested Uneri icon theme into the current user's
# icon directory.
#
# Does not modify gsettings or apply the icon theme.
#
# Usage:
#   ./scripts/install-icons.sh dark
#   ./scripts/install-icons.sh light

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

SOURCE_DIR="${SCRIPT_DIR}/icons/${ICON_THEME_NAME}"
TARGET_DIR="${UNERI_ICONS_DIR}/${ICON_THEME_NAME}"

uneri_log "${SOURCE_DIR} \n ${TARGET_DIR}"

if [[ ! -d "${SOURCE_DIR}" ]]; then
  uneri_log "${ICON_THEME_NAME} icons do not exist — generating them."

  python3 "${SCRIPT_DIR}/scripts/gen_icons.py" "${VARIANT}"

  uneri_ok "Generated ${ICON_THEME_NAME} icons"
fi

if [[ ! -d "${SOURCE_DIR}" ]]; then
  uneri_die "Icon generation completed, but source directory does not exist: ${SOURCE_DIR}"
fi

mkdir -p "${UNERI_ICONS_DIR}"

rm -rf -- "${TARGET_DIR}"
cp -r "${SOURCE_DIR}" "${TARGET_DIR}"

if uneri_require_cmd gtk-update-icon-cache; then
  gtk-update-icon-cache -f -t "${TARGET_DIR}" >/dev/null 2>&1 \
    && uneri_ok "Refreshed icon cache" \
    || uneri_warn "gtk-update-icon-cache reported an issue (non-fatal)"
fi

uneri_ok "Installed ${ICON_THEME_NAME} icon theme."
