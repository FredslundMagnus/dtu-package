from dtu import Parameter


class Param(metaclass=Parameter):
    a: int = 2

    def __init__(self, name, s=4) -> None:
        self.name = name
        self.s = s
