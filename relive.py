from dtu import Parameter


class P1(metaclass=Parameter):
    a: int = 2

    def __init__(self, name, s=4) -> None:
        self.name = name
        self.s = s


class P2():
    a: int = 2

    def __init__(self, name, s=4) -> None:
        self.name = name
        self.s = s


# obj = P1("gs s", s=7)
# _code = obj._get_transfer_format
# print(P1("gs s", s=7))
# obj2 = relive(_code)
# print(obj.__dict__, obj2.__dict__)
# Mistery = P2()
# print(Bruce)
# print(Mistery)
