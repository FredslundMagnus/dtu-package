from __future__ import annotations
from dataclasses import dataclass as dtu
from inspect import signature
from sys import argv
dtu


def setup(github_link: str, python: str = "3.9.6", packages: list[str] = ["torch", "torchvision", "matplotlib"]):
    """
    github_link="https://github.com/FredslundMagnus/dtu-package.git"
    python="3.9.6" # see module available for newest
    packages=["torch", "torchvision", "matplotlib"]
    """
    name = github_link.split("/")[-1][:-4]
    newline = "\n"
    print(f"""
cd ~/Desktop
mkdir {name}
cd {name}
module load python3/{python}
python3 -m venv project-env
source project-env/bin/activate
python -m pip install git+https://github.com/FredslundMagnus/dtu-package.git{(newline + "python -m pip install " + " ".join(packages)) if packages else ""}
git config --global credential.helper store
git clone {github_link}
yes | cp project-env/bin/dtu_server ~/bin/dtu
cd {name}
deactivate
dtu
""")


def check(params, features):
    for key, value in params.items():
        if key not in features:
            raise Exception(f'The feature "{key}" does not exist.')
        if value.__class__ != features[key]:
            if value.__class__ == int and (features[key] == float or features[key] == 'float'):
                params[key] = float(value)
            else:
                _class_ = features[key].__name__ if hasattr(features[key], "__name__") else features[key]
                if value.__class__.__name__ != _class_:
                    raise Exception(f'The feature "{key}" should be of type {_class_}.')
                # else:
                #     params[key] = value.__name__


def createFolders(name, folders, file):
    for folder in folders:
        file.write(f"mkdir -p outputs/{name}/{folder}\n")


def genExperiments(features, folders, file, name, n, cpu, **params):
    createFolders(name, folders, file)
    check(params, features)
    for i in range(n):
        params['ID'] = i
        file.write(f'bsub -o "outputs/{name}/Markdown/{name}_{i}.md" -J "{name}_{i}" -env MYARGS="-name {name}-{i} {" ".join(f"-{name} {value}" for name, value in params.items())}" < submit_{"cpu" if cpu else "gpu"}.sh\n')


class Parameters():
    name: str = "local"
    ID: int = 0
    folders: list[str] = []
    instances: int = 1
    GPU: bool = False
    time: int = 3600
    isServer: bool = False
    __first__: bool = True

    def __post_init__(self):
        if Parameters.__first__:
            file = open('experiments.sh', 'w')
            file.write('#!/bin/sh\n')
            Parameters.__first__ = False
        else:
            file = open('experiments.sh', 'a')
        self.folders = list(self.folders)
        features, folders = dict(self.__annotations__), ['Markdown'] + self.folders
        genExperiments(features, folders, file, self.name, self.instances, not self.GPU, **{k: v for k, v in self.__dict__.items() if k not in {"name", "instances", "folders"}})
        file.close()

    @classmethod
    def start(cls) -> None:
        override = cls.override(argv[1:])
        values = {name: value for name, value in cls.__dict__.items() if name[0] != "_" and name != "run"}
        values['cls'] = cls
        values['self'] = cls
        values['isServer'] = len(argv[1:]) > 1
        args = [(override[name] if name in override else values[name]) for name in signature(cls.run).parameters]
        annotations = [(v.name, v.annotation) for v in signature(cls.run).parameters.values() if v.name not in {"cls", "self"}]

        isRunning: bool = cls.__module__ == "__main__"
        if isRunning:
            for name, annotation in annotations:
                if name == "isServer":
                    print(annotations, type(annotations))
                    if annotations != bool and annotations != 'bool':
                        raise TypeError(f"The type of 'isServer' should be 'bool' in run!")
                elif cls.__annotations__[name] != annotation:
                    _class_ = cls.__annotations__[name].__name__ if hasattr(cls.__annotations__[name], "__name__") else cls.__annotations__[name]
                    raise TypeError(f"The type of '{name}' should be '{_class_}' in run!")
            cls.run(*args)

    @classmethod
    def override(cls, args) -> dict[str, object]:
        if len(args) == 0:
            return {}
        temp = {}
        for _key, value in zip(args[::2], args[1::2]):
            key: str = _key[1:]
            _type = cls.__annotations__[key] if key != "ID" else int
            _type: type = _type if isinstance(_type, type) else eval(_type)
            if _type in {int, bool, float}:
                value = eval(value)
            temp[key] = value
        return temp
