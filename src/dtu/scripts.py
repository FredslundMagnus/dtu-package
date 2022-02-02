from sys import argv
import subprocess
import sys


def install(package):
    # pipmain(["install", "--upgrade", "--force-reinstall", package])
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", package], shell=True)
    except Exception as e:
        print(e)


args = argv[1:]


def run():
    print(f"I just ran, with {args = }!")


def save():
    print(f"You just hot saved, with {args = }!")


def upgrade():
    install("git+https://github.com/FredslundMagnus/dtu-package.git")
    # print("C:/Users/magnu/AppData/Local/Microsoft/WindowsApps/python.exe -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/python-helpers.git")
    print("Otherwise run this:")
    print(sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "git+https://github.com/FredslundMagnus/python-helpers.git")
