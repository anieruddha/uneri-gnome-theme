#!/usr/bin/env bash
# Uneri installer.
#
# Installs the Uneri theme, icons and Monaspace Neon font.
# Installation does not change the currently active GNOME appearance.
#
# Usage:
#   ./install.sh
#   ./install.sh --variant dark
#   ./install.sh --variant light
#
# Without --variant, both Dark and Light variants are installed.

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
source "${SCRIPT_DIR}/scripts/lib.sh"

VARIANT=""

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

uneri_log "Installing Uneri"

uneri_check_environment

# ---------------------------------------------------------------------------
# 1. Install theme and icons.
# ---------------------------------------------------------------------------
if [[ -n "${VARIANT}" ]]; then
  "${SCRIPT_DIR}/scripts/install-theme.sh" "${VARIANT}"
  "${SCRIPT_DIR}/scripts/install-icons.sh" "${VARIANT}"
else
  "${SCRIPT_DIR}/scripts/install-theme.sh" Dark
  "${SCRIPT_DIR}/scripts/install-theme.sh" Light
  "${SCRIPT_DIR}/scripts/install-icons.sh" Dark
  "${SCRIPT_DIR}/scripts/install-icons.sh" Light
fi

# ---------------------------------------------------------------------------
# 2. Install font.
# ---------------------------------------------------------------------------
"${SCRIPT_DIR}/scripts/install-font.sh"

uneri_ok "Uneri installation complete."
uneri_log "Nothing was applied automatically."