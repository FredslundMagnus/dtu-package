from __future__ import annotations
import subprocess
from sys import argv, platform
from os import remove
isLinux: bool = False
if platform == "linux" or platform == "linux2":
    isLinux = True


def myHash(text: str) -> int:
    hash = 0
    for ch in text:
        hash = (hash*281 ^ ord(ch)*997) & 0xFFFFFFFFFFFFFFFF
    return hash


# import sys


# def install(package):
#     # pipmain(["install", "--upgrade", "--force-reinstall", package])
#     try:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", package], shell=True)
#     except Exception as e:
#         print(e)


def run_command(command: str):
    try:
        subprocess.check_call(command.split(" "), shell=True)
    except Exception as e:
        print(e)


def generate_submit(command: str):
    with open("submit_cpu.sh", "w") as f:
        f.write("""#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS""")

    with open("submit_gpu.sh", "w") as f:
        f.write("""#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS""")


def run_clean(command: str):
    try:
        if command.split(" ")[0] == "bsub":
            generate_submit(command)
        subprocess.check_call([command], shell=True)
    except Exception as e:
        print(e)


args = argv[1:]


def help() -> None:
    print("Welcome to the dtu package! Try one of the following commands:")
    print("dtu init")
    print("dtu generate")


def help_server() -> None:
    print("Welcome to the dtu package! Try one of the following commands:")
    print("dtu goto $NAME")
    print("dtu run (--no-watch)")
    print("dtu save")
    print("dtu status (--no-watch)")


def cli():
    if len(args) == 0:
        return help()
    if args[0] == "generate":
        return generate()
    if args[0] == "init":
        return init()
    help()


def goto(name: str):
    run_clean(f"cd ~/Desktop/{name}/{name}/")
    run_clean("cp ../project-env/bin/dtu_server ~/bin/dtu")


def cli_server():
    if len(args) == 0:
        return help_server()
    if args[0] == "run":
        return run()
    if args[0] == "save":
        return save()
    if args[0] == "status":
        return status()
    if args[0] == "goto" and len(args) == 2:
        return goto(args[1])
    help_server()


def read(file: str) -> str:
    try:
        with open(file, 'r') as f:
            return f.read()
    except IOError:
        return ""


def check_not_the_same():
    with open("experiments.sh", 'r') as file:
        current = str(myHash(file.read()))
    old = read("__secret__.pyc")
    with open("__secret__.pyc", 'w') as secret:
        secret.write(current)
    if current != old:
        return
    answer = input("Are you sure you want to run the same experiments again? (y/n): ")
    if answer not in {"y", "Y", "yes", "Yes", "Yes"}:
        quit()


def run():
    run_clean("git pull")
    check_not_the_same()
    with open("experiments.sh", 'r') as file:
        file.readline()
        for line in file:
            run_clean(line)
    remove("submit_gpu.sh")
    remove("submit_cpu.sh")
    status()


def save():
    run_clean("git add .")
    run_clean('git commit -m "Just Trained"')
    run_clean("git pull")
    run_clean("git push")


def status():
    if args[-1] != "--no-watch":
        run_clean("watch bstat")
    else:
        run_clean("bstat")


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

    with open('setup.py', 'a') as f:
        f.write("""from dtu.server import setup
# see 'module available' on server for newest python version
setup(github_link, python="3.9.6", packages=["torch", "torchvision", "matplotlib"])
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
