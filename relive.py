import inspect
import importlib


def _get_transfer_format(module, class_name, args, kwargs, symbol="~"):
    return (module.__name__ + symbol + class_name + symbol + str(args) + symbol + str(kwargs)).replace(" ", "¨")


class Parameter(type):
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
            old_init(self, *args, **kwargs)
        x.__init__ = init
        return x


def relive(_code: str) -> Parameter:
    module_name, class_name,  args, kwargs = _code.replace("¨", " ").split("~")
    module = importlib.import_module(module_name)
    _class = module.__getattribute__(class_name)
    return _class.__call__(*eval(args), **eval(kwargs))


class P1(metaclass=Parameter):
    a: int = 2

    def __init__(self, name, s=4) -> None:
        pass


obj = P1("gs s", s=7)
_code = obj._get_transfer_format
print(P1("gs s", s=7))
obj2 = relive(_code)
print(obj.__dict__, obj2.__dict__)
# Mistery = P2()
# print(Bruce)
# print(Mistery)
