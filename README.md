# GNOME Text Editor (Custom Build)

Custom Flatpak build for GNOME Text Editor with 12+ premium themes and critical patches.

## 🎨 Themes Included
* Deep Oceanic (Default)
* Andromeda
* Ant
* Dracula
* Kimi
* Nord
* Solarized (Multiple variants)
* Space KDE
* Sweet

### 🚀 Quick Links
- **Download Installer:** [Latest Build Releases](https://github.com/jonathonp3/gnome-text-editor-custom/releases/tag/latest-build)

### 🔗 Upstream Sources
*   **Stable Manifest Source:** [Flathub - org.gnome.TextEditor](https://github.com/flathub/org.gnome.TextEditor)


## 📥 Getting Started
```bash
Clone the repository
git clone git@github.com:jonathonp3/wolf-oss-apps.git
cd wolf-oss-apps
```

Set up remotes
```bash
flatpak remote-add --user --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```
Run the theme injector
```bash
python3 update_manifest.py
```

## Build Instructions
Stable Version (v50)

1. Install SDK
```bash
flatpak install --user -y flathub org.gnome.Sdk//50 org.gnome.Platform//50
```
2. Build
```bash
flatpak run org.flatpak.Builder --force-clean --ccache --disable-rofiles-fuse --repo=repo-stable build-dir-stable org.gnome.TextEditor.json
```
3. Bundle & Install
```bash
flatpak build-bundle repo-stable gnome-text-editor-stable.flatpak org.gnome.TextEditor stable
flatpak install --user --reinstall gnome-text-editor-stable.flatpak
```

## 🛠️ Modifying Themes

If you add or remove an .xml theme file:

1. Sync Manifest:
```bash
python3 update_manifest.py
```
2. Clean Cache: 
```bash
rm -rf build-dir-stable repo-stable .flatpak-builder
```
3. Rebuild: Run the Build, Bundle, and Install commands above.


***
ython3 update_manifest.py
