#!/usr/bin/env bash
# Uneri — shared shell helpers.
# Not meant to be executed directly.

# Guard against direct execution.
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "lib.sh is a library and should be sourced, not executed." >&2
  exit 1
fi

# ---- Paths -----------------------------------------------------------------
UNERI_THEMES_DIR="${HOME}/.local/share/themes"
UNERI_ICONS_DIR="${HOME}/.local/share/icons"
UNERI_FONTS_DIR="${HOME}/.local/share/fonts/Monaspace"
UNERI_VARIANTS=("Uneri-Dark" "Uneri-Light")
UNERI_FONT_NAME="Monaspace Neon"

# ---- Logging -----------------------------------------------------------------
uneri_c_reset=$'\033[0m'
uneri_c_blue=$'\033[38;5;38m'
uneri_c_green=$'\033[38;5;114m'
uneri_c_yellow=$'\033[38;5;179m'
uneri_c_red=$'\033[38;5;203m'

uneri_log()  { printf '%s[uneri]%s %s\n'  "${uneri_c_blue}"   "${uneri_c_reset}" "$*"; }
uneri_ok()   { printf '%s[  ok   ]%s %s\n'  "${uneri_c_green}"  "${uneri_c_reset}" "$*"; }
uneri_warn() { printf '%s[ warn  ]%s %s\n'  "${uneri_c_yellow}" "${uneri_c_reset}" "$*" >&2; }
uneri_err()  { printf '%s[ error ]%s %s\n'  "${uneri_c_red}"    "${uneri_c_reset}" "$*" >&2; }
uneri_die()  { uneri_err "$*"; exit 1; }

# ---- Environment detection ----------------------------------------------------
uneri_check_environment() {
  local os_ok=0 de_ok=0

  if [[ -r /etc/os-release ]]; then
    # shellcheck disable=SC1091
    source /etc/os-release
    if [[ "${ID:-}" == "ubuntu" || "${ID_LIKE:-}" == *ubuntu* ]]; then
      os_ok=1
    fi
  fi
  if [[ "${os_ok}" -eq 0 ]]; then
    uneri_warn "this does not look like Ubuntu — Uneri targets Ubuntu 26.04 GNOME and may not look right elsewhere"
  fi

  if [[ "${XDG_CURRENT_DESKTOP:-}" == *GNOME* || "${DESKTOP_SESSION:-}" == *gnome* ]]; then
    de_ok=1
  fi
  if [[ "${de_ok}" -eq 0 ]]; then
    uneri_warn "GNOME does not appear to be the running desktop — GTK theming will still install, but shell theming needs GNOME"
  fi
}

uneri_require_cmd() {
  local cmd="$1"
  command -v "${cmd}" >/dev/null 2>&1
}
