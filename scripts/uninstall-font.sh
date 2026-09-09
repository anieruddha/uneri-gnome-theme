#!/usr/bin/env bash
# Uneri Monaspace Neon font uninstaller.
# Removes only the Monaspace Neon font directory installed by Uneri.
# Safe to run standalone:
#   ./scripts/uninstall-font.sh

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." &>/dev/null && pwd)"
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

uneri_log "Uninstalling Monaspace Neon"

FONT_DIR="${UNERI_FONTS_DIR}"

if [[ -z "${FONT_DIR}" || "${FONT_DIR}" == "/" || "${FONT_DIR}" == "${HOME}" ]]; then
  uneri_die "refusing to remove unsafe font directory: ${FONT_DIR}"
fi

if [[ ! -d "${FONT_DIR}" ]]; then
  uneri_log "Monaspace Neon directory does not exist — nothing to remove."
  exit 0
fi

rm -rf -- "${FONT_DIR}"

if uneri_require_cmd fc-cache; then
  fc-cache -f >/dev/null 2>&1 || true
  uneri_ok "Font cache refreshed."
fi

uneri_ok "Monaspace Neon has been uninstalled."
