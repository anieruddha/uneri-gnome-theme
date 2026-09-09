#!/usr/bin/env bash
# Uneri uninstaller.
#
# Resets the active appearance to Ubuntu defaults and removes
# Uneri theme and icon files through the component uninstall scripts.
#
# Usage:
#   ./uninstall.sh
#   ./uninstall.sh --variant dark
#   ./uninstall.sh --variant light
#   ./uninstall.sh --font
#   ./uninstall.sh --variant dark --font

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
source "${SCRIPT_DIR}/scripts/lib.sh"

VARIANT=""
DO_FONT=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --variant)
      VARIANT="${2:-}"
      shift 2
      ;;
    --variant=*)
      VARIANT="${1#*=}"
      shift
      ;;
    --font)
      DO_FONT=1
      shift
      ;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *)
      uneri_die "unknown argument: $1"
      ;;
  esac
done

if [[ -n "${VARIANT}" ]]; then
  VARIANT="${VARIANT,,}"
  VARIANT="${VARIANT^}"

  if [[ "${VARIANT}" != "Dark" && "${VARIANT}" != "Light" ]]; then
    uneri_die "--variant must be 'dark' or 'light', got: ${VARIANT}"
  fi
fi

uneri_log "Uninstalling Uneri"

# ---------------------------------------------------------------------------
# 1. Reset to Ubuntu defaults.
# ---------------------------------------------------------------------------
"${SCRIPT_DIR}/reset-theme.sh"

# ---------------------------------------------------------------------------
# 2. Remove theme and icon files
# ---------------------------------------------------------------------------
if [[ -n "${VARIANT}" ]]; then
  "${SCRIPT_DIR}/scripts/uninstall-theme.sh" "${VARIANT}"
  "${SCRIPT_DIR}/scripts/uninstall-icons.sh" "${VARIANT}"
else
  "${SCRIPT_DIR}/scripts/uninstall-theme.sh" dark
  "${SCRIPT_DIR}/scripts/uninstall-theme.sh" light
  "${SCRIPT_DIR}/scripts/uninstall-icons.sh" dark
  "${SCRIPT_DIR}/scripts/uninstall-icons.sh" light
fi

# ---------------------------------------------------------------------------
# 3. Font is optional and managed by its own uninstall script.
# ---------------------------------------------------------------------------
if [[ "${DO_FONT}" -eq 1 ]]; then
  "${SCRIPT_DIR}/scripts/uninstall-font.sh"
else
  uneri_log "Keeping Monaspace Neon font. Use --font to remove it."
fi

uneri_ok "Uneri uninstall complete."
