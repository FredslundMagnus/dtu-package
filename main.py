from __future__ import annotations
from src.dtu.server import Parameters, dtu

@dtu
class Defaults(Parameters):
    name: str = "local"
    instances: int = 1
    GPU: bool = False
    time: int = 3600

    b: float = 2.0
    a: int = 1
    d: str = "fd"

    def run(self, b: float, d: str, a: int) -> None:
        print(b,d, self.time)


Defaults.start()
