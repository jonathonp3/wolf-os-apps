import json
import os
import glob
from collections import OrderedDict

# --- CONFIGURATION ---
STABLE_MANIFEST = "org.gnome.TextEditor.json"
DEFAULT_THEME_ID = "solarized-light-cosmic-latte"
THEME_FILES = sorted(glob.glob("*.xml"))

def update_manifest(filename, app_id, branch_name):
    if not os.path.exists(filename):
        print(f" -> Error: {filename} not found.")
        return

    with open(filename, 'r') as f:
        data = json.load(f)

    print(f"Injecting themes and finish-args into {filename}...")

    # 1. Update finish-args for default theme
    if 'finish-args' not in data:
        data['finish-args'] = []

    data['finish-args'] = [
        arg for arg in data['finish-args']
        if "GTK_SOURCE_STYLE_SCHEME" not in arg
    ]
    data['finish-args'].append(f"--env=GTK_SOURCE_STYLE_SCHEME={DEFAULT_THEME_ID}")

    # 2. Create Custom Style Module
    new_module = {
        "name": "custom-gtksource-styles",
        "buildsystem": "simple",
        "build-commands": ["mkdir -p /app/share/gtksourceview-5/styles"],
        "sources": [{"type": "file", "path": t} for t in THEME_FILES]
    }

    for theme in THEME_FILES:
        new_module["build-commands"].append(
            f"install -Dm644 {theme} /app/share/gtksourceview-5/styles/"
        )

    modules = [m for m in data.get('modules', []) if m['name'] != "custom-gtksource-styles"]
    modules.insert(0, new_module)
    data['modules'] = modules

    # 3. RE-ORDER KEYS: Force branch under command, REMOVE name
    new_data = OrderedDict()
    new_data["app-id"] = app_id

    for key, value in data.items():
        # Skip keys we want to position/remove manually
        if key in ["app-id", "branch", "name", "id"]:
            continue

        new_data[key] = value

        # When we hit 'command', inject 'branch' immediately after
        if key == "command":
            new_data["branch"] = branch_name

    # 4. Save the final file
    with open(filename, 'w') as f:
        json.dump(new_data, f, indent=2)

    print(f"Success! {filename} updated.")

if __name__ == "__main__":
    update_manifest(STABLE_MANIFEST, "org.gnome.TextEditor", "stable")

