import sys
import os
import re
import shutil
from pathlib import Path

sys.path.append("..")
sys.modules["clickgen"] = __import__(
    "cursors.clickgen.src.clickgen"
).clickgen.src.clickgen

from clickgen.scripts.ctgen import main

# Move SVG files
if not os.path.exists("./svg"):
    os.makedirs("./svg")
for file in Path("./import").glob("*.svg"):
    shutil.move(file, f"./svg/{file.name}")

# Move PNG files
if not os.path.exists("./png"):
    os.makedirs("./png")
for file in Path("./import").glob("*.png"):
    filename = file.name
    match = re.search(r"(-[0-9]+\.png)$", filename)

    if match:
        suffix = match.group(1)
        filename = filename[: -len(suffix)]
        size = re.search(r"[0-9]+", suffix).group(0)
        dir_path = f"./png/{size}/"

        os.makedirs(dir_path, exist_ok=True)
        shutil.move(file, f"{dir_path}{filename}.png")

# Remove import directory if empty
p = Path("./import")
if p.exists() and p.is_dir() and not any(p.iterdir()):
    p.rmdir()

shutil.rmtree("./build")

sys.argv = ["ctgen", "-p", "x11", "config.json"]
main()

sys.argv = ["ctgen", "-p", "windows", "-n", "Sidney's", "config.json"]
main()
