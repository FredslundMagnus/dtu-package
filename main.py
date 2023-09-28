from __future__ import annotations
from dtu import Parameter, Parameters, dtu, GPU


class Param(Parameter):
    def __init__(self, name, s=4) -> None:
        self.name = name
        self.s = s


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: None | GPU = None
    time: int = 3600

    b: float = 2.0
    a: int = 1
    d: str = "fd"
    k: Param = Param("sdf sdf", s=78)

    def run(self, d: str, b: float, isServer: bool, k: Param) -> None:
        print(b, d, self.time, isServer)
        print(k.name, k.s)


Defaults.start()
