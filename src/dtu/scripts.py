from __future__ import annotations
import subprocess
from sys import argv, platform
isLinux: bool = False
if platform == "linux" or platform == "linux2":
    isLinux = True

# import sys


# def install(package):
#     # pipmain(["install", "--upgrade", "--force-reinstall", package])
#     try:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", package], shell=True)
#     except Exception as e:
#         print(e)


def run_command(command: str):
    print("running:", command)
    try:
        li: list[str] = command.split(" ")
        if li[0] == "mkdir":
            print("Creating dir")
            subprocess.check_call([command])
            return
        if li[0] == "bsub":
            print("special")
            subprocess.check_call([command])
            return
        subprocess.check_call(li, shell=True)
    except Exception as e:
        print(e)


args = argv[1:]


def help() -> None:
    print("Welcome to the dtu package! Try one of the following commands:")
    if isLinux:
        print("dtu run")
        print("dtu save")
        print("dtu status")
    print("dtu init")
    print("dtu generate")


def cli():
    if len(args) == 0:
        return help()
    if args[0] == "run" and isLinux:
        return run()
    if args[0] == "save" and isLinux:
        return save()
    if args[0] == "status" and isLinux:
        return status()
    if args[0] == "generate":
        return generate()
    if args[0] == "init":
        return init()
    help()


def run():
    run_command("git pull")
    # run_command("chmod +x experiments.sh")
    # run_command("./experiments.sh")
    with open("experiments.sh", 'r') as file:
        print("First", file.readline())
        print("Second", file.readline())
        for line in file:
            run_command(line)
    if args[-1] == "-w" or args[-1] == "--watch":
        run_command("bstat watch")


def save():
    print(f"You just got saved!")


def status():
    print(f"Here is a status!")


def generate():
    try:
        import generate
        run_command("git add .")
        run_command('git commit -m "Experiments"')
        run_command("git pull")
        run_command("git push")
    except Exception:
        print("Are you starting a new project?")
        print('Please run "dtu init" before generating experiments')


def init():
    with open('generate.py', 'a') as f:
        f.write("""from main import Defaults

Defaults("Example1", b=4, d="dsf")
Defaults("Example2", b=4, d="dssf", GPU=True)
Defaults("Example3", a=2, instances=2)
""")
    with open('main.py', 'a') as f:
        f.write("""from dtu.server import Parameters, dtu


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: bool = False
    time: int = 3600

    b: float = 2.0
    a: int = 1
    d: str = "fd"

    def run(d: str, b: float) -> None:
        print(b, d)


Defaults.start()
""")
    with open('.gitignore', 'a') as f:
        f.write("""*pyc
.vscode/*
__pycache__
""")
    with open('experiments.sh', 'w') as f:
        f.write("")

# def upgrade():
#     install("git+https://github.com/FredslundMagnus/dtu-package.git")
#     # print("C:/Users/magnu/AppData/Local/Microsoft/WindowsApps/python.exe -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/python-helpers.git")
#     print("Otherwise run this:")
#     print(sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "git+https://github.com/FredslundMagnus/python-helpers.git")
