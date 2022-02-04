from sys import argv
# import subprocess
# import sys


# def install(package):
#     # pipmain(["install", "--upgrade", "--force-reinstall", package])
#     try:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", package], shell=True)
#     except Exception as e:
#         print(e)


# def run_command(command: str):
#     print("running:", command)
#     try:
#         subprocess.check_call(command.split(" "), shell=True)
#     except Exception as e:
#         print(e)


args = argv[1:]


def help() -> None:
    print("Welcome to the dtu package! Try one of the following commands:")
    print("dtu run")
    print("dtu save")
    print("dtu status")
    print("dtu upgrade")
    print("dtu init")


def cli():
    if len(args) == 0:
        return help()
    if args[0] == "run":
        return run()
    if args[0] == "save":
        return save()
    if args[0] == "status":
        return status()
    if args[0] == "upgrade":
        return upgrade()
    if args[0] == "init":
        return init()
    help()


def run():
    print(f"I just ran!")


def save():
    print(f"You just got saved!")


def status():
    print(f"Here is a status!")

def upgrade():
    print(f"Here is a upgrade!")

def init():
    print(f"Here is a upgrade!")


# def upgrade():
#     install("git+https://github.com/FredslundMagnus/dtu-package.git")
#     # print("C:/Users/magnu/AppData/Local/Microsoft/WindowsApps/python.exe -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/python-helpers.git")
#     print("Otherwise run this:")
#     print(sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "git+https://github.com/FredslundMagnus/python-helpers.git")
