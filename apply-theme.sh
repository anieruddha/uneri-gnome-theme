#!/usr/bin/env bash
# Switch between Uneri Dark and Uneri Light.
#
# Usage:
#   ./apply-theme.sh dark
#   ./apply-theme.sh light
#
# Applies gsettings changes only — no daemon, no background process.
# GNOME Shell theming additionally requires the 'User Themes' extension;
# if it's installed and enabled this script updates it too.

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
source "${SCRIPT_DIR}/scripts/lib.sh"


VARIANT="${1:-}"
VARIANT="${VARIANT,,}"
VARIANT="${VARIANT^}"

UNERI_ICON_THEME_NAME="Uneri-${VARIANT}"

case "${VARIANT}" in
  Dark)  GTK_THEME="Uneri-Dark";  SCHEME="prefer-dark" ;;
  Light) GTK_THEME="Uneri-Light"; SCHEME="prefer-light" ;;
  *)
    uneri_err "Usage: $0 <Dark|Light>"
    exit 1
    ;;
esac

if ! uneri_require_cmd gsettings; then
  uneri_die "gsettings is not available — this script requires GNOME's gsettings tool."
fi

if [[ ! -d "${UNERI_THEMES_DIR}/${GTK_THEME}" ]]; then
  uneri_die "${GTK_THEME} isn't installed under ${UNERI_THEMES_DIR}. Run ./install.sh first."
fi

uneri_log "Switching to Uneri ${VARIANT^}"

uneri_log "VARIANT=${VARIANT}"
uneri_log "UNERI_ICON_THEME_NAME=${UNERI_ICON_THEME_NAME}"

gsettings set org.gnome.desktop.interface gtk-theme "${GTK_THEME}"
gsettings set org.gnome.desktop.interface icon-theme "${UNERI_ICON_THEME_NAME}"
gsettings set org.gnome.desktop.interface color-scheme "${SCHEME}"
gsettings set org.gnome.desktop.interface font-name "${UNERI_FONT_NAME} 10.5"
gsettings set org.gnome.desktop.interface document-font-name "${UNERI_FONT_NAME} 10.5"
gsettings set org.gnome.desktop.wm.preferences theme "${GTK_THEME}" 2>/dev/null || true
gsettings set org.gnome.desktop.interface monospace-font-name "${UNERI_FONT_NAME} 10.5"

# GNOME Shell theming — only touch this if the User Themes extension's
# schema is actually present, so we never error out on stock GNOME.
if gsettings list-schemas 2>/dev/null | grep -q "org.gnome.shell.extensions.user-theme"; then
  gsettings set org.gnome.shell.extensions.user-theme name "${GTK_THEME}"
  uneri_ok "Applied GNOME Shell theme via User Themes extension"
else
  uneri_warn "'User Themes' extension not detected — GTK apps and icons are themed,"
  uneri_warn "but the top bar / overview / quick settings will stay on the default"
  uneri_warn "shell theme until you install and enable that extension."
fi

uneri_ok "Now using Uneri ${VARIANT^}"
