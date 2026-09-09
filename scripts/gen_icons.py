#!/usr/bin/env python3
"""
Generates the original Uneri icon set as SVGs.
Design language: geometric construction, consistent stroke/fill logic,
graphite surfaces with a single sky-blue accent, clean silhouettes that
stay legible from 16px to 128px.
"""
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Generate icons.")
parser.add_argument(
    "variant",
    nargs="?",
    choices=["Dark", "Light"],
    help="Theme variant to generate: Dark or Light"
)
args = parser.parse_args()

if not args.variant:
    print("variant not given")
    exit(-1)

VARIANT_LOWERCASE = args.variant.lower()
VARIANT = VARIANT_LOWERCASE.capitalize()

if VARIANT_LOWERCASE == "light":
    GRAPHITE     = "#f8e1c0"
    GRAPHITE_DK  = "#ead0a8"
    GRAPHITE_LT  = "#fff1d8"
    ACCENT       = "#6f9696"
    ACCENT_DK    = "#287fa3"
    PAPER        = "#574a3d"
    MUTED        = "#7c7a72"
    SUCCESS      = "#4ca982"
    WARNING      = "#d99b3d"
    ERROR        = "#d85c5c"
else:
    GRAPHITE      = "#2c333f"
    GRAPHITE_DK   = "#20262f"
    GRAPHITE_LT   = "#3a4250"
    ACCENT        = "#5ec2f2"
    ACCENT_DK     = "#3fa8db"
    PAPER         = "#e6eaf0"
    MUTED         = "#7c8698"
    SUCCESS       = "#5fd6a5"
    WARNING       = "#e8b85f"
    ERROR         = "#ef6a6a"


ROOT_DIR = Path(__file__).resolve().parent.parent
ICON_THEME_PATH = "{0}/icons/{1}".format(ROOT_DIR, "Uneri-{0}".format(VARIANT))
BASE = "{0}/icons/{1}".format(ROOT_DIR, "Uneri-{0}/icons".format(VARIANT))


def generate_index_theme():
    content = """[Icon Theme]
Name=Uneri-{0}
Comment=Uneri icon set
Inherits=Adwaita,hicolor
Example=folder

Directories=scalable/places,scalable/actions,scalable/devices,scalable/mimetypes,scalable/status,symbolic/actions,symbolic/status

[scalable/places]
Size=48
MinSize=16
MaxSize=512
Type=Scalable
Context=Places

[scalable/actions]
Size=24
MinSize=16
MaxSize=512
Type=Scalable
Context=Actions

[scalable/devices]
Size=48
MinSize=16
MaxSize=512
Type=Scalable
Context=Devices

[scalable/mimetypes]
Size=48
MinSize=16
MaxSize=512
Type=Scalable
Context=MimeTypes

[scalable/status]
Size=24
MinSize=16
MaxSize=512
Type=Scalable
Context=Status

[symbolic/actions]
Size=16
MinSize=8
MaxSize=512
Type=Scalable
Context=Actions

[symbolic/status]
Size=16
MinSize=8
MaxSize=512
Type=Scalable
Context=Status
""".format(VARIANT)

    index_file = "{0}/icons/index.theme".format(ICON_THEME_PATH)
    with open(index_file, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Generated: {index_file}")


def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content.strip() + "\n")
    print("wrote", path)

def svg(body, vb=24):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb} {vb}">\n{body}\n</svg>'

# ---------------------------------------------------------------------------
# Shared shape helpers
# ---------------------------------------------------------------------------

def folder_base(tab_accent=False, badge=""):
    """Standard Uneri folder silhouette: a flat-fronted folder with a
    small angled tab, in graphite, with a thin accent top edge."""
    tab_fill = ACCENT if tab_accent else GRAPHITE_LT
    return f'''
  <path d="M3 7.5c0-1.1.9-2 2-2h4.2l1.6 1.9H19c1.1 0 2 .9 2 2V17c0 1.1-.9 2-2 2H5c-1.1 0-2-.9-2-2V7.5z"
        fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <path d="M3 7.5c0-1.1.9-2 2-2h4.2l1.6 1.9H19c1.1 0 2 .9 2 2v.3H3v-2.2z" fill="{tab_fill}"/>
  {badge}'''

# ---------------------------------------------------------------------------
# PLACES
# ---------------------------------------------------------------------------

write("scalable/places/folder.svg", svg(folder_base()))

write("scalable/places/folder-home.svg", svg(folder_base(badge=f'''
  <path d="M12 9.6l3.6 3.1v4.3h-2.3v-2.7h-2.6v2.7H8.4v-4.3z" fill="{ACCENT}"/>''')))

write("scalable/places/user-desktop.svg", svg(f'''
  <rect x="2.5" y="4" width="19" height="12.5" rx="1.4" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <rect x="4.2" y="5.7" width="15.6" height="9.1" rx="0.4" fill="{GRAPHITE_DK}"/>
  <path d="M6 15.8h6l-2 1.4" fill="none" stroke="{ACCENT}" stroke-width="1.1" stroke-linecap="round"/>
  <rect x="9" y="18.2" width="6" height="1.4" rx="0.7" fill="{GRAPHITE_LT}"/>
  <rect x="7.2" y="19.4" width="9.6" height="1.4" rx="0.7" fill="{GRAPHITE_LT}"/>
'''))

write("scalable/places/folder-download.svg", svg(folder_base(badge=f'''
  <path d="M12 8.8v5.4M9.6 12.4l2.4 2.4 2.4-2.4" fill="none" stroke="{ACCENT}"
        stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M9 17h6" stroke="{ACCENT}" stroke-width="1.4" stroke-linecap="round"/>''')))

write("scalable/places/folder-documents.svg", svg(folder_base(badge=f'''
  <rect x="8.4" y="9.4" width="7.2" height="6.4" rx="0.6" fill="{PAPER}"/>
  <path d="M9.6 11.2h4.8M9.6 12.9h4.8M9.6 14.6h3.2" stroke="{GRAPHITE}" stroke-width="0.7" stroke-linecap="round"/>''')))

write("scalable/places/folder-music.svg", svg(folder_base(badge=f'''
  <path d="M10 15.6V10l5-1v5.2" fill="none" stroke="{ACCENT}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="9.3" cy="15.9" r="1.3" fill="{ACCENT}"/>
  <circle cx="14.3" cy="14.5" r="1.3" fill="{ACCENT}"/>''')))

write("scalable/places/folder-pictures.svg", svg(folder_base(badge=f'''
  <rect x="8.2" y="9.6" width="7.6" height="5.8" rx="0.6" fill="{PAPER}"/>
  <circle cx="10.1" cy="11.4" r="0.9" fill="{WARNING}"/>
  <path d="M8.6 15.1l2.3-2.3 1.6 1.6 1.7-2.1 2.2 2.8" fill="none" stroke="{GRAPHITE}" stroke-width="0.9" stroke-linejoin="round" stroke-linecap="round"/>''')))

write("scalable/places/folder-videos.svg", svg(folder_base(badge=f'''
  <rect x="8.3" y="9.6" width="7.4" height="5.8" rx="0.8" fill="{PAPER}"/>
  <path d="M11 11.4l3 1.5-3 1.5z" fill="{ACCENT}"/>''')))

write("scalable/places/folder-remote.svg", svg(folder_base(badge=f'''
  <circle cx="12" cy="12.6" r="3.1" fill="none" stroke="{ACCENT}" stroke-width="1"/>
  <path d="M9 12.6h6M12 9.5c1.4 1.6 1.4 4.5 0 6.1M12 9.5c-1.4 1.6-1.4 4.5 0 6.1" fill="none" stroke="{ACCENT}" stroke-width="0.8"/>''')))

write("scalable/places/user-trash.svg", svg(f'''
  <path d="M6.3 8.2h11.4l-1 10.4c-.1 1.1-1 1.9-2.1 1.9h-5.2c-1.1 0-2-.8-2.1-1.9z" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <rect x="4.8" y="6" width="14.4" height="2.1" rx="0.6" fill="{GRAPHITE_LT}"/>
  <rect x="9.6" y="4" width="4.8" height="1.7" rx="0.5" fill="{GRAPHITE_LT}"/>
  <path d="M10 10.6v6.4M12 10.6v6.4M14 10.6v6.4" stroke="{ACCENT}" stroke-width="1" stroke-linecap="round"/>
'''))

write("scalable/places/user-trash-full.svg", svg(f'''
  <path d="M6.3 8.2h11.4l-1 10.4c-.1 1.1-1 1.9-2.1 1.9h-5.2c-1.1 0-2-.8-2.1-1.9z" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <rect x="4.8" y="6" width="14.4" height="2.1" rx="0.6" fill="{GRAPHITE_LT}"/>
  <rect x="9.6" y="4" width="4.8" height="1.7" rx="0.5" fill="{GRAPHITE_LT}"/>
  <path d="M10 10.6v6.4M12 10.6v6.4M14 10.6v6.4" stroke="{WARNING}" stroke-width="1" stroke-linecap="round"/>
'''))

write("scalable/places/network-server.svg", svg(f'''
  <rect x="4" y="4.5" width="16" height="15" rx="1.4" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <rect x="6" y="6.6" width="12" height="3.4" rx="0.6" fill="{GRAPHITE_LT}"/>
  <rect x="6" y="11" width="12" height="3.4" rx="0.6" fill="{GRAPHITE_LT}"/>
  <circle cx="16.2" cy="8.3" r="0.7" fill="{ACCENT}"/>
  <circle cx="16.2" cy="12.7" r="0.7" fill="{ACCENT}"/>
  <path d="M7 17h10" stroke="{MUTED}" stroke-width="1" stroke-linecap="round"/>
'''))

write("scalable/places/network-workgroup.svg", svg(f'''
  <circle cx="12" cy="12" r="8" fill="none" stroke="{ACCENT}" stroke-width="1.3"/>
  <ellipse cx="12" cy="12" rx="3.4" ry="8" fill="none" stroke="{ACCENT}" stroke-width="1"/>
  <path d="M4 12h16M5.4 7.3h13.2M5.4 16.7h13.2" stroke="{ACCENT}" stroke-width="1"/>
'''))

# ---------------------------------------------------------------------------
# DEVICES
# ---------------------------------------------------------------------------

write("scalable/devices/computer.svg", svg(f'''
  <rect x="3" y="4.5" width="18" height="11.5" rx="1.3" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <rect x="4.6" y="6" width="14.8" height="8.3" rx="0.4" fill="{GRAPHITE_DK}"/>
  <path d="M7 19.5h10" stroke="{GRAPHITE_LT}" stroke-width="1.6" stroke-linecap="round"/>
  <path d="M10 16.3l-.6 3.2M14 16.3l.6 3.2" stroke="{GRAPHITE_LT}" stroke-width="1.2" stroke-linecap="round"/>
  <circle cx="12" cy="10.1" r="1.6" fill="none" stroke="{ACCENT}" stroke-width="1"/>
'''))

write("scalable/devices/drive-harddisk.svg", svg(f'''
  <rect x="3" y="7" width="18" height="10" rx="2" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <circle cx="8" cy="12" r="2.4" fill="none" stroke="{ACCENT}" stroke-width="1.1"/>
  <circle cx="8" cy="12" r="0.5" fill="{ACCENT}"/>
  <rect x="13" y="10.6" width="6" height="1.1" rx="0.55" fill="{GRAPHITE_LT}"/>
  <rect x="13" y="12.6" width="4.5" height="1.1" rx="0.55" fill="{GRAPHITE_LT}"/>
'''))

write("scalable/devices/drive-removable-media.svg", svg(f'''
  <path d="M8 3h6l3 4.5v11a1.5 1.5 0 01-1.5 1.5h-9A1.5 1.5 0 015 17V8z" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <rect x="9" y="9.5" width="6" height="4.5" rx="0.5" fill="{GRAPHITE_DK}"/>
  <rect x="10.2" y="10.5" width="1.4" height="2.5" fill="{ACCENT}"/>
  <rect x="9.4" y="16" width="5.2" height="1.6" rx="0.4" fill="{GRAPHITE_LT}"/>
'''))

write("scalable/devices/camera-photo.svg", svg(f'''
  <rect x="3" y="7.5" width="18" height="11.5" rx="2" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <path d="M8.6 7.5l1.1-2h4.6l1.1 2z" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <circle cx="12" cy="13.2" r="3.2" fill="none" stroke="{ACCENT}" stroke-width="1.2"/>
  <circle cx="12" cy="13.2" r="1.1" fill="{ACCENT}"/>
  <circle cx="17.5" cy="10.2" r="0.7" fill="{ACCENT_DK}"/>
'''))

write("scalable/devices/audio-headphones.svg", svg(f'''
  <path d="M5 13v-1a7 7 0 0114 0v1" fill="none" stroke="{ACCENT}" stroke-width="1.4" stroke-linecap="round"/>
  <rect x="3.6" y="12.5" width="3.4" height="5.5" rx="1.5" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <rect x="17" y="12.5" width="3.4" height="5.5" rx="1.5" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
'''))

write("scalable/devices/printer.svg", svg(f'''
  <rect x="4" y="8.5" width="16" height="7.5" rx="1.2" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <rect x="6.4" y="4" width="11.2" height="5.2" rx="0.6" fill="{GRAPHITE_LT}"/>
  <rect x="6.4" y="15.4" width="11.2" height="5.4" rx="0.5" fill="{PAPER}"/>
  <circle cx="16.6" cy="11" r="0.7" fill="{ACCENT}"/>
  <path d="M9 18h6" stroke="{GRAPHITE}" stroke-width="0.7" stroke-linecap="round"/>
'''))

# ---------------------------------------------------------------------------
# MIMETYPES
# ---------------------------------------------------------------------------

def page(corner_color, glyph=""):
    return f'''
  <path d="M6 3h8l4 4v13.2A0.8 0.8 0 0117.2 21H6.8A0.8 0.8 0 016 20.2V3z"
        fill="{PAPER}" stroke="{GRAPHITE}" stroke-width="0.6"/>
  <path d="M14 3v3.4c0 .6.4 1 1 1H18z" fill="{corner_color}"/>
  {glyph}'''

write("scalable/mimetypes/text-x-generic.svg", svg(page(GRAPHITE_LT, f'''
  <path d="M8.4 12h7.2M8.4 14.2h7.2M8.4 16.4h4.8" stroke="{GRAPHITE}" stroke-width="0.8" stroke-linecap="round"/>''')))

write("scalable/mimetypes/image-x-generic.svg", svg(page(ACCENT, f'''
  <rect x="8" y="11.4" width="8" height="6" rx="0.5" fill="{GRAPHITE}"/>
  <circle cx="9.9" cy="13.1" r="0.75" fill="{WARNING}"/>
  <path d="M8.4 16.7l2.3-2.3 1.6 1.6 1.8-2.2 2.1 2.9" fill="none" stroke="{PAPER}" stroke-width="0.8" stroke-linejoin="round" stroke-linecap="round"/>''')))

write("scalable/mimetypes/audio-x-generic.svg", svg(page(SUCCESS, f'''
  <path d="M9.6 17V11.4l5-1v5.2" fill="none" stroke="{GRAPHITE}" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="8.9" cy="17.3" r="1.2" fill="{GRAPHITE}"/>
  <circle cx="13.9" cy="15.9" r="1.2" fill="{GRAPHITE}"/>''')))

write("scalable/mimetypes/video-x-generic.svg", svg(page(ERROR, f'''
  <rect x="8" y="11.4" width="8" height="6" rx="0.7" fill="{GRAPHITE}"/>
  <path d="M11 13l3 1.4-3 1.4z" fill="{PAPER}"/>''')))

write("scalable/mimetypes/package-x-generic.svg", svg(f'''
  <path d="M12 3l8 4.2v9.6L12 21l-8-4.2V7.2z" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <path d="M4 7.2l8 4.2 8-4.2M12 11.4V21" fill="none" stroke="{GRAPHITE_DK}" stroke-width="0.7"/>
  <path d="M8 5.1l8 4.2" stroke="{ACCENT}" stroke-width="0.9" stroke-linecap="round"/>
'''))

write("scalable/mimetypes/application-x-executable.svg", svg(f'''
  <rect x="4" y="4" width="16" height="16" rx="3.5" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  <path d="M9.5 8.5l4 3.5-4 3.5z" fill="{ACCENT}"/>
'''))

write("scalable/mimetypes/x-office-document.svg", svg(page(ACCENT, f'''
  <path d="M8.4 12h7.2M8.4 14.2h5.6M8.4 16.4h7.2" stroke="{GRAPHITE}" stroke-width="0.8" stroke-linecap="round"/>''')))

# ---------------------------------------------------------------------------
# STATUS
# ---------------------------------------------------------------------------

write("scalable/status/dialog-information.svg", svg(f'''
  <circle cx="12" cy="12" r="9" fill="{ACCENT}"/>
  <rect x="11.1" y="10.2" width="1.8" height="6.6" rx="0.9" fill="{GRAPHITE_DK}"/>
  <circle cx="12" cy="7.6" r="1.1" fill="{GRAPHITE_DK}"/>
'''))

write("scalable/status/dialog-warning.svg", svg(f'''
  <path d="M12 3.2L21.5 20H2.5z" fill="{WARNING}"/>
  <rect x="11.1" y="9.5" width="1.8" height="5.4" rx="0.9" fill="{GRAPHITE_DK}"/>
  <circle cx="12" cy="16.8" r="1.1" fill="{GRAPHITE_DK}"/>
'''))

write("scalable/status/dialog-error.svg", svg(f'''
  <circle cx="12" cy="12" r="9" fill="{ERROR}"/>
  <path d="M8.6 8.6l6.8 6.8M15.4 8.6l-6.8 6.8" stroke="{PAPER}" stroke-width="1.6" stroke-linecap="round"/>
'''))

write("scalable/status/emblem-ok-symbolic.svg", svg(f'''
  <circle cx="12" cy="12" r="9" fill="{SUCCESS}"/>
  <path d="M7.5 12.3l3 3 6-6.3" fill="none" stroke="{GRAPHITE_DK}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
'''))

write("scalable/status/network-wireless-signal-good.svg", svg(f'''
  <path d="M4 15a11.3 11.3 0 0116 0" fill="none" stroke="{ACCENT}" stroke-width="1.6" stroke-linecap="round"/>
  <path d="M7 17.6a7 7 0 0110 0" fill="none" stroke="{ACCENT}" stroke-width="1.6" stroke-linecap="round"/>
  <circle cx="12" cy="19.6" r="1.3" fill="{ACCENT}"/>
'''))

write("scalable/status/battery-good.svg", svg(f'''
  <rect x="3" y="8" width="16" height="8" rx="1.6" fill="none" stroke="{GRAPHITE}" stroke-width="1.2"/>
  <rect x="19.6" y="10.4" width="1.6" height="3.2" rx="0.6" fill="{GRAPHITE}"/>
  <rect x="4.6" y="9.6" width="8.4" height="4.8" rx="0.7" fill="{SUCCESS}"/>
'''))

# ---------------------------------------------------------------------------
# ACTIONS (full color, scalable)
# ---------------------------------------------------------------------------

def action_disc(glyph, fill=ACCENT):
    return f'''
  <circle cx="12" cy="12" r="9.5" fill="{GRAPHITE}" stroke="{GRAPHITE_DK}" stroke-width="0.6"/>
  {glyph}'''

write("scalable/actions/list-add.svg", svg(action_disc(f'<path d="M12 7.5v9M7.5 12h9" stroke="{ACCENT}" stroke-width="1.7" stroke-linecap="round"/>')))
write("scalable/actions/list-remove.svg", svg(action_disc(f'<path d="M7.5 12h9" stroke="{ACCENT}" stroke-width="1.7" stroke-linecap="round"/>')))
write("scalable/actions/edit-delete.svg", svg(action_disc(f'''
  <path d="M8.4 9.2h7.2l-.7 7.4c-.05.6-.55 1-1.1 1h-3.6c-.55 0-1.05-.4-1.1-1z" fill="none" stroke="{ACCENT}" stroke-width="1.2" stroke-linejoin="round"/>
  <path d="M9.6 9.2V7.9c0-.5.4-.9.9-.9h3c.5 0 .9.4.9.9v1.3" fill="none" stroke="{ACCENT}" stroke-width="1.1"/>''')))
write("scalable/actions/edit-copy.svg", svg(action_disc(f'''
  <rect x="6.6" y="6.6" width="8" height="9.4" rx="1" fill="none" stroke="{ACCENT}" stroke-width="1.1"/>
  <rect x="9.4" y="9.4" width="8" height="9.4" rx="1" fill="{GRAPHITE}" stroke="{ACCENT}" stroke-width="1.1"/>''')))
write("scalable/actions/edit-cut.svg", svg(action_disc(f'''
  <path d="M9.5 15.5L18 7M9.5 8.5L18 17" stroke="{ACCENT}" stroke-width="1.3" stroke-linecap="round"/>
  <circle cx="7.3" cy="8" r="1.4" fill="none" stroke="{ACCENT}" stroke-width="1.1"/>
  <circle cx="7.3" cy="16" r="1.4" fill="none" stroke="{ACCENT}" stroke-width="1.1"/>''')))
write("scalable/actions/edit-paste.svg", svg(action_disc(f'''
  <rect x="7.4" y="7.4" width="9.2" height="11.2" rx="1.2" fill="none" stroke="{ACCENT}" stroke-width="1.1"/>
  <rect x="10" y="5.6" width="4" height="2.4" rx="0.6" fill="{ACCENT}"/>''')))
write("scalable/actions/edit-find.svg", svg(action_disc(f'''
  <circle cx="11" cy="11" r="4" fill="none" stroke="{ACCENT}" stroke-width="1.4"/>
  <path d="M14.2 14.2l3.3 3.3" stroke="{ACCENT}" stroke-width="1.5" stroke-linecap="round"/>''')))
write("scalable/actions/document-save.svg", svg(action_disc(f'''
  <path d="M7 6.5h8l2.5 2.5v8.5A1.3 1.3 0 0116.2 18.8H7.8A1.3 1.3 0 016.5 17.5V7.8A1.3 1.3 0 017.8 6.5z" fill="none" stroke="{ACCENT}" stroke-width="1.1"/>
  <rect x="9" y="6.5" width="6" height="4" fill="{ACCENT}"/>
  <rect x="9.2" y="13" width="5.6" height="4" fill="none" stroke="{ACCENT}" stroke-width="0.9"/>''')))
write("scalable/actions/document-open.svg", svg(action_disc(f'''
  <path d="M6 17.5V7.7c0-.7.6-1.3 1.3-1.3H11l1.5 1.6h4.2c.7 0 1.3.6 1.3 1.3v.7" fill="none" stroke="{ACCENT}" stroke-width="1.1" stroke-linejoin="round"/>
  <path d="M6 17.5l1.8-6.4a1.2 1.2 0 011.2-.9h9.5a1 1 0 011 1.3l-1.7 5.2a1.3 1.3 0 01-1.2.9H7A1 1 0 016 17.5z" fill="none" stroke="{ACCENT}" stroke-width="1.1" stroke-linejoin="round"/>''')))
write("scalable/actions/document-print.svg", svg(action_disc(f'''
  <rect x="6.6" y="9.4" width="10.8" height="6" rx="0.9" fill="none" stroke="{ACCENT}" stroke-width="1.1"/>
  <path d="M8.6 9.4V6.4h6.8v3" fill="none" stroke="{ACCENT}" stroke-width="1"/>
  <rect x="8.6" y="14.4" width="6.8" height="3.3" fill="none" stroke="{ACCENT}" stroke-width="0.9"/>''')))
write("scalable/actions/view-refresh.svg", svg(action_disc(f'''
  <path d="M7 12a5 5 0 018.7-3.3M17 12a5 5 0 01-8.7 3.3" fill="none" stroke="{ACCENT}" stroke-width="1.4" stroke-linecap="round"/>
  <path d="M15.4 7.6h2.3v2.3M8.6 16.4H6.3v-2.3" fill="none" stroke="{ACCENT}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>''')))
write("scalable/actions/go-previous.svg", svg(action_disc(f'<path d="M14 7.5l-4.5 4.5 4.5 4.5" fill="none" stroke="{ACCENT}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')))
write("scalable/actions/go-next.svg", svg(action_disc(f'<path d="M10 7.5l4.5 4.5-4.5 4.5" fill="none" stroke="{ACCENT}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')))
write("scalable/actions/go-up.svg", svg(action_disc(f'<path d="M7.5 14l4.5-4.5 4.5 4.5" fill="none" stroke="{ACCENT}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')))
write("scalable/actions/go-down.svg", svg(action_disc(f'<path d="M7.5 10l4.5 4.5 4.5-4.5" fill="none" stroke="{ACCENT}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')))
write("scalable/actions/go-home.svg", svg(action_disc(f'<path d="M7 13.4l5-4 5 4v4.3a.9.9 0 01-.9.9H7.9a.9.9 0 01-.9-.9z" fill="none" stroke="{ACCENT}" stroke-width="1.2" stroke-linejoin="round"/>')))
write("scalable/actions/window-close.svg", svg(action_disc(f'<path d="M8.5 8.5l7 7M15.5 8.5l-7 7" stroke="{ERROR}" stroke-width="1.7" stroke-linecap="round"/>')))
write("scalable/actions/window-minimize.svg", svg(action_disc(f'<path d="M8 15h8" stroke="{ACCENT}" stroke-width="1.7" stroke-linecap="round"/>')))
write("scalable/actions/window-maximize.svg", svg(action_disc(f'<rect x="7.5" y="7.5" width="9" height="9" rx="1.1" fill="none" stroke="{ACCENT}" stroke-width="1.4"/>')))
write("scalable/actions/media-playback-start.svg", svg(action_disc(f'<path d="M9.5 7.8v8.4l7-4.2z" fill="{ACCENT}"/>')))
write("scalable/actions/media-playback-pause.svg", svg(action_disc(f'<rect x="8.6" y="7.6" width="2.4" height="8.8" rx="0.6" fill="{ACCENT}"/><rect x="13" y="7.6" width="2.4" height="8.8" rx="0.6" fill="{ACCENT}"/>')))
write("scalable/actions/emblem-system.svg", svg(action_disc(f'''
  <circle cx="12" cy="12" r="2.6" fill="none" stroke="{ACCENT}" stroke-width="1.3"/>
  <path d="M12 6.4v1.7M12 15.9v1.7M6.4 12h1.7M15.9 12h1.7M8.3 8.3l1.2 1.2M14.5 14.5l1.2 1.2M15.7 8.3l-1.2 1.2M9.5 14.5l-1.2 1.2"
        stroke="{ACCENT}" stroke-width="1.2" stroke-linecap="round"/>''')))

print("done")

# ---------------------------------------------------------------------------
# SYMBOLIC (monochrome, currentColor — for shell/menu contexts)
# ---------------------------------------------------------------------------

def symbolic(body):
    return svg(f'<g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">\n{body}\n</g>', vb=16)

write("symbolic/actions/open-menu-symbolic.svg", symbolic('<path d="M2.5 4.5h11M2.5 8h11M2.5 11.5h11"/>'))
write("symbolic/actions/list-add-symbolic.svg", symbolic('<path d="M8 3v10M3 8h10"/>'))
write("symbolic/actions/list-remove-symbolic.svg", symbolic('<path d="M3 8h10"/>'))
write("symbolic/actions/edit-find-symbolic.svg", symbolic('<circle cx="6.8" cy="6.8" r="3.6" fill="none"/><path d="M11.2 11.2l2.6 2.6"/>'))
write("symbolic/actions/window-close-symbolic.svg", symbolic('<path d="M4 4l8 8M12 4l-8 8"/>'))
write("symbolic/actions/view-more-symbolic.svg", symbolic('<circle cx="3.2" cy="8" r="1.1" fill="currentColor" stroke="none"/><circle cx="8" cy="8" r="1.1" fill="currentColor" stroke="none"/><circle cx="12.8" cy="8" r="1.1" fill="currentColor" stroke="none"/>'))
write("symbolic/actions/pan-down-symbolic.svg", symbolic('<path d="M4 6l4 4 4-4"/>'))
write("symbolic/actions/pan-up-symbolic.svg", symbolic('<path d="M4 10l4-4 4 4"/>'))
write("symbolic/status/emblem-ok-symbolic.svg", symbolic('<path d="M3.5 8.3l3 3 6-6.6"/>'))
write("symbolic/status/dialog-warning-symbolic.svg", symbolic('<path d="M8 2.5L14.5 13.5h-13z"/><path d="M8 6.5v3.4M8 12v.1"/>'))
write("symbolic/actions/document-save-symbolic.svg", symbolic('<path d="M3 3h7l3 3v7a1 1 0 01-1 1H3a1 1 0 01-1-1V4a1 1 0 011-1z"/><path d="M5.5 3v3.5h5V3"/>'))

generate_index_theme()

print("symbolic done")