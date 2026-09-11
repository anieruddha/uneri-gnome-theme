# Uneri

I wrote this ubuntu theme for for my laptop. 
icons copied that to `<Home>/.local/share/icons`. 
Themes copied to `<Home>/.local/share/themes`

This is not complete icon set, doesnt cover all icons for other icon it fallback to system default.

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

apply-theme.sh switch between dark & light theme. Instead of script you can use ubuntu-tweak to change theme

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

## Screenshots

#### Dark Theme
GTK 3 Widgets
![GTK 3 Widgets](./screenshots/gtk3-dark.png?raw=true "Uneri Dark Theme GTK 3")
GTK 4 Widgets
![GTK 4 Widgets](./screenshots/gtk4-dark.png?raw=true "Uneri Dark Theme GTK 4")

#### Light Theme
GTK 3 Widgets
![GTK 3 Widgets](./screenshots/gtk3-light.png?raw=true "Uneri Light Theme GTK 3")
GTK 4 Widgets
![GTK 4 Widgets](./screenshots/gtk4-light.png?raw=true "Uneri Light Theme GTK 4")