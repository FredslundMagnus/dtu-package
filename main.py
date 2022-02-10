from __future__ import annotations
from dtu import Parameters, dtu
from relive import P1, P2


@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: bool = False
    time: int = 3600

    b: float = 2.0
    a: int = 1
    d: str = "fd"
    k: P1 = P1("sdf sdf", s=78)

    def run(self, d: str, b: float, isServer: bool, k: P1) -> None:
        print(b, d, self.time, isServer)
        print(k.name)


Defaults.start()
