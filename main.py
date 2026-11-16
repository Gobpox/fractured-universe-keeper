"""The Keeper of the Fractured Universe entry renderer."""

import os
import shutil

source = os.path.join(os.path.dirname(__file__), "keeper.jpg")
if not os.path.isfile(source):
    raise SystemExit(f"Error: source artwork not found: {source}")

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
shutil.copyfile(source, os.path.join(output_dir, "entry.png"))
