from __future__ import annotations
import importlib
import inspect
from dataclasses import dataclass as dtu
from inspect import signature
from sys import argv
dtu


def _get_transfer_format(module, class_name, args, kwargs, symbol="~") -> str:
    return (module.__name__ + symbol + class_name + symbol + str(args) + symbol + str(kwargs)).replace(" ", "@")


def _get_par_str(class_name, args, kwargs) -> str:
    temp: str = class_name + "("
    if args:
        temp += str(args)[1:-1]
        if temp[-1] == ",":
            temp = temp[:-1]
    if kwargs:
        str(kwargs)[2:-1].replace("': ", '=').replace(", '", ", ")
    temp += ")"
    return temp


class Parameter(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)

        old_init = x.__init__

        def init(self, *args, **kwargs):
            self._get_transfer_format = _get_transfer_format(
                inspect.getmodule(self),
                self.__class__.__name__,
                args,
                kwargs
            )
            self._par_str = _get_par_str(
                self.__class__.__name__,
                args,
                kwargs
            )
            old_init(self, *args, **kwargs)
        x.__init__ = init
        return x


def relive(_code: str) -> Parameter:
    module_name, class_name,  args, kwargs = _code.replace("@", " ").split("~")
    module = importlib.import_module(module_name)
    _class = module.__getattribute__(class_name)
    return _class.__call__(*eval(args), **eval(kwargs))


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
        if value.__class__ not in {int, str, bool, float} and value.__class__.__class__ is not Parameter:
            raise Exception(f"Problem with {key}: {value}. You can only user int, str, bool, float or objects with metaclass=Parameter")
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


def print_parameters(values: dict[str, object], override: dict[str, object]) -> None:
    for key, value in override.items():
        values[key] = value
    print("\nParameters:".ljust(30), "Values")
    for key, value in values.items():
        if key not in {"instances", "cls", "self", "isServer", "ID"}:
            print(f"{key}:".ljust(30), f"{value if type(type(value)) is type else value._par_str}")
    print("")


def createFolders(name, folders, file):
    for folder in folders:
        file.write(f"mkdir -p outputs/{name}/{folder}\n")


def change_parameter(params: dict[str, object]) -> dict[str, object]:
    for key, value in params.items():
        if value.__class__.__class__ is Parameter:
            params[key] = value._get_transfer_format
    return params


def genExperiments(features, folders, file, name, n, cpu, **params):
    createFolders(name, folders, file)
    check(params, features)
    params = change_parameter(params)
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
                    if annotation != bool and annotation != 'bool':
                        raise TypeError(f"The type of 'isServer' should be 'bool' in run!")
                elif cls.__annotations__[name] != annotation:
                    _class_ = cls.__annotations__[name].__name__ if hasattr(cls.__annotations__[name], "__name__") else cls.__annotations__[name]
                    raise TypeError(f"The type of '{name}' should be '{_class_}' in run!")
            if values['isServer']:
                print_parameters(values, override)
            cls.run(*args)

    @classmethod
    def override(cls, args) -> dict[str, object]:
        if len(args) == 0:
            return {}
        temp = {}
        for _key, value in zip(args[::2], args[1::2]):
            key: str = _key[1:]
            _type = cls.__annotations__[key] if key != "ID" else int
            try:
                _type: type = _type if isinstance(_type, type) else eval(_type)
            except NameError:
                value = relive(value)
            if _type in {int, bool, float}:
                value = eval(value)
            temp[key] = value
        return temp
