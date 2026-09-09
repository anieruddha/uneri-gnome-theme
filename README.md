# Uneri

A ubuntu theme I wrote (use AI assistant) for my laptop. Generate & create few icons. For rest of icon fallback to system default 

## Install
```
git clone <repository>
cd Uneri
./install.sh
```

Without --variant, install.sh installs both Dark and Light theme and Dark and Light icon variants.

`Monaspace Neon` is always installed as part of the installation process.
If Monaspace Neon is already available, the existing installation is left
untouched.


## Apply / Switch between Dark and Light

The theme and icon installers install files only. They do not change the
currently active GNOME appearance.

```
./apply-theme.sh dark
./apply-theme.sh light
```


## Reset appearance
It reset GNOME appearance to Ubuntu defaults.

```
./reset-theme.sh

```


## Uninstall
```
./uninstall.sh
```

Without --variant, uninstall.sh removes both the Dark and Light Uneri themes and icon themes.

It calls reset.sh first to restore the active appearance to Ubuntu defaults.

The Monaspace Neon font is not removed by default.

## Font: Monaspace Neon

Uneri uses Monaspace Neon as its desktop UI font, with control
spacing and sizing tuned around its geometry.

The terminal font is not changed by Uneri.

Monaspace Neon is installed into:
```
~/.local/share/fonts/Monaspace
```

