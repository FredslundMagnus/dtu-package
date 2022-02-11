from __future__ import annotations
import importlib
import inspect
from dataclasses import dataclass as dtu
from inspect import signature
from sys import argv
dtu


def _get_transfer_format(module, class_name, args, kwargs, symbol="~") -> str:
    return (module.__name__ + symbol + class_name + symbol + str(args) + symbol + str(kwargs)).replace(" ", "@")


def _get_par_str(class_name, args, kwargs: dict[str, object]) -> str:
    _args = [colorize(arg) for arg in args]
    _kwargs = [f"<c>{key}</c><k>=</k>{colorize(value)}" for key, value in kwargs.items()]
    return f"<d>{class_name}</d><k>(</k>{'<k>,</k> '.join(_args+_kwargs)}<k>)</k>"


class _Parameter(type):
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


class Parameter(_Parameter):
    pass


def relive(_code: str) -> _Parameter:
    module_name, class_name,  args, kwargs = _code.replace("@", " ").split("~")
    module = importlib.import_module(module_name)
    _class = module.__getattribute__(class_name)
    return _class.__call__(*eval(args), **eval(kwargs))


def setup(github_link: str, python: str = "3.9.6", packages: list[str] = ["torch", "torchvision", "matplotlib"], first_time: bool = True):
    """
    github_link="https://github.com/FredslundMagnus/dtu-package.git"
    python="3.9.6" # see module available for newest
    packages=["torch", "torchvision", "matplotlib"]
    """
    name = github_link.split("/")[-1][:-4]
    newline = "\n"
    if first_time:
        print("""
Do these step by step:
cd ~
vi .profile
i (insert mode)
PATH=$PATH:$HOME/bin:. (Change to this)
esc esc :wq enter (quiting and saving)
mkdir bin
""")
    print(f"""
Copy all this and put it in the server terminal:
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
        if value.__class__ not in {int, str, bool, float} and value.__class__.__class__ is not _Parameter:
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


def colorize(obj: object) -> str:
    if type(obj) in {int, float}:
        return f"<f>{obj}</f>"
    if type(obj) is str:
        return f'<j>"{obj}"</j>'
    if type(obj) is bool:
        return f"<e>{obj}</e>"


def print_parameters(values: dict[str, object], override: dict[str, object]) -> None:
    for key, value in override.items():
        values[key] = value
    a = 20
    print("""
<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>
""")
    print("# Parameters\n")
    print("| PARAMETER".ljust(a) + "| TYPE".ljust(a) + "| VALUE".ljust(a) + "|")
    print("|".ljust(a, "-") + "|".ljust(a, "-") + "|".ljust(a, "-") + "|")
    for key, value in values.items():
        if key not in {"instances", "cls", "self", "isServer", "ID"}:
            print(f"| <c>{key}</c>".ljust(a) + f"| <d>{type(value).__name__}</d>".ljust(a) + f"| {colorize(value) if type(type(value)) is type else value._par_str}".ljust(a-1) + " |")
    print("\n# Output\n")
    print("```python")


def createFolders(name, folders, file):
    for folder in folders:
        file.write(f"mkdir -p outputs/{name}/{folder}\n")


def change_parameter(params: dict[str, object]) -> dict[str, object]:
    for key, value in params.items():
        if value.__class__.__class__ is _Parameter:
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
            print("```")

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
