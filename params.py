from dtu import Parameter


class Param(Parameter):
    a: int = 2

    def __init__(self, name, s=4) -> None:
        self.name = name
        self.s = s


class Param2(Parameter):
    a: int = 2

    def __init__(self, name, num, s=4, d="ef") -> None:
        self.name = name
        self.s = s
