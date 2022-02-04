from __future__ import annotations
import subprocess
from sys import argv, platform
from os import remove
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
    if isLinux:
        print("dtu run (--no-watch)")
        print("dtu save")
        print("dtu status (--no-watch)")
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
    run_clean("git pull")
    with open("experiments.sh", 'r') as file:
        temp = file.read()
        print(hash(temp))
    with open("experiments.sh", 'r') as file:
        file.readline()
        # __secret__: str = ""
        # try:
        #     with open("__secret__.pyc", 'r') as secret:
        #         __secret__ = secret.read()
        # except IOError:
        #     pass
        # with open("__secret__.pyc", 'w') as secret:
        #     temp = file.readline()
        #     if __secret__ == temp:
        #         answer = input("Are you sure you want to run the same experiments again? (y/n) ")
        #         if answer != "y" and answer != "Y" and answer != "yes" and answer != "Yes" and answer != "YES":
        #             return
        #     secret.write(temp)
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
