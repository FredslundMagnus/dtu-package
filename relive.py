from dtu import Parameter


class Param(metaclass=Parameter):
    a: int = 2

    def __init__(self, name, s=4) -> None:
        self.name = name
        self.s = s


class Param2(metaclass=Parameter):
    a: int = 2

    def __init__(self, name, num, s=4, d="ef") -> None:
        self.name = name
        self.s = s
