from __future__ import annotations
from dtu import Parameters, dtu
from params import Param, Param2


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: bool = False
    time: int = 3600

    b: float = 2.0
    a: int = 1
    d: str = "fd"
    k: Param = Param("sdf sdf", s=78)
    l: Param2 = Param2("s f", 5, s=1, d="76f")

    def run(self, d: str, b: float, isServer: bool, k: Param) -> None:
        print(b, d, self.time, isServer)
        print(k.name, k.a, k.s)


Defaults.start()
