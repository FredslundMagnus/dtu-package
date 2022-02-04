from __future__ import annotations
from dataclasses import dataclass as dtu
from inspect import signature
from random import randint

dtu


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
        file.write(f"mkdir ../outputs/{name}/{folder}\n")


def genExperiments(features, folders, file, name, n, cpu, **params):
    createFolders(name, folders, file)
    check(params, features)
    for i in range(n):
        params['ID'] = i
        file.write(f'bsub -o "../outputs/{name}/Markdown/{name}_{i}.md" -J "{name}_{i}" -env MYARGS="-name {name}-{i} {" ".join(f"-{name} {value}" for name, value in params.items())}" < submit_{"cpu" if cpu else "gpu"}.sh\n')


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
            file = open('Utils/experiments.sh', 'w')
            file.write('#!/bin/sh\n')
            file.write(f'#{"".join([str(randint(0, 9)) for _ in range(10)])}\n')
            Parameters.__first__ = False
        else:
            file = open('Utils/experiments.sh', 'a')
        self.folders = list(self.folders)
        features, folders = dict(self.__annotations__), ['', 'Markdown'] + self.folders
        genExperiments(features, folders, file, self.name, self.instances, not self.GPU, **{k: v for k, v in self.__dict__.items() if k not in {"name", "instances", "folders"}})
        file.close()

    @classmethod
    def start(cls) -> None:
        values = {name: value for name, value in cls.__dict__.items() if name[0] != "_" and name != "run"}
        values['cls'] = cls
        values['self'] = cls
        if 'database' in values:
            values['database'].__create__(values['name'])
        args = [values[name] for name in signature(cls.run).parameters]
        if 'database' in args:
            args['database'].__create__(args['name'])
        annotations = [(v.name, v.annotation) for v in signature(cls.run).parameters.values() if v.name not in {"cls", "self"}]

        isRunning: bool = cls.__module__ == "__main__"
        if isRunning:
            for name, annotation in annotations:
                if cls.__annotations__[name] != annotation:
                    _class_ = cls.__annotations__[name].__name__ if hasattr(cls.__annotations__[name], "__name__") else cls.__annotations__[name]
                    raise TypeError(f"The type of '{name}' should be '{_class_}' in run!")
            cls.run(*args)
