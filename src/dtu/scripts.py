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


def dtu():
    if len(args) == 0:
        print("Welcome to the dtu package! Try one of the following commands:")
        print("dtu run")
        print("dtu save")
        print("dtu status")
        print("dtu update")
        return
    if args[1] == "run":
        return run()
    if args[1] == "save":
        return save()
    if args[1] == "status":
        return status()
    if args[1] == "update":
        return update(sys.executable)


def run():
    print(f"I just ran!")


def save():
    print(f"You just got saved!")


def status():
    print(f"Here is a status!")


def update(python: str):
    print(f"Updating... {python}")


def upgrade():
    install("git+https://github.com/FredslundMagnus/dtu-package.git")
    # print("C:/Users/magnu/AppData/Local/Microsoft/WindowsApps/python.exe -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/python-helpers.git")
    print("Otherwise run this:")
    print(sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "git+https://github.com/FredslundMagnus/python-helpers.git")
