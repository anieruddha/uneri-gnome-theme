#!/usr/bin/env bash
# Uneri appearance reset.
# Resets the active GNOME appearance to Ubuntu defaults.
# Usage:
#   ./reset-theme.sh

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
source "${SCRIPT_DIR}/scripts/lib.sh"

for arg in "$@"; do
  case "${arg}" in
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *)
      uneri_die "unknown argument: ${arg}"
      ;;
  esac
done

uneri_log "Resetting GNOME appearance to Ubuntu defaults"

if ! uneri_require_cmd gsettings; then
  uneri_die "gsettings is not available — cannot reset the appearance."
fi

gsettings set org.gnome.desktop.interface gtk-theme "Yaru"
gsettings set org.gnome.desktop.interface icon-theme "Yaru"
gsettings set org.gnome.desktop.interface color-scheme "default"
gsettings set org.gnome.desktop.interface font-name "Ubuntu 11"
gsettings set org.gnome.desktop.interface document-font-name "Ubuntu 11"
gsettings set org.gnome.desktop.interface monospace-font-name "Ubuntu Mono 13"

gsettings set org.gnome.desktop.wm.preferences theme "Yaru" 2>/dev/null || true

if gsettings list-schemas 2>/dev/null | grep -q "org.gnome.shell.extensions.user-theme"; then
  gsettings set org.gnome.shell.extensions.user-theme name "" 2>/dev/null || true
fi

uneri_ok "GNOME appearance reset to Ubuntu defaults."