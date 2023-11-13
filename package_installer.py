import sys
import venv
from os import getcwd, path
from subprocess import run
from time import time

# Create a new virtual environment, given that there isn't one already.
venv_folder = path.join(getcwd(), "subprocess_venv")
if not path.exists(venv_folder):

    start = time()

    print("Creating virtual environment")
    venv.create("subprocess_venv", with_pip=True)

    print("Installing dependencies...")

    # Add pip installation names here for any new package.
    packages = ["ntplib", "pygame"]
    for package in packages:
        run([sys.executable, "-m", "pip", "install", package], check=True)
        print(f"Installed package: {package}")

    print(f"Venv creation completed in {round(time()-start, 2)}s")
