import importlib
# from relive import Test
import inspect
print(importlib.import_module("relive"))
obj = Test()

print(obj.__module__)
print(inspect.getmodule(obj).Test)
