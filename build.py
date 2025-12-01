import sys
import shutil

sys.path.append("..")
sys.modules["clickgen"] = __import__(
    "cursors.clickgen.src.clickgen"
).clickgen.src.clickgen

from clickgen.scripts.ctgen import main

# shutil.rmtree("./build")

# sys.argv = ["ctgen", "-p", "x11", "config.json"]
main()

# sys.argv = ["ctgen", "-p", "windows", "-n", "Sidney's", "config.json"]
# main()
