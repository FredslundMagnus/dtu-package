from main import Defaults
from relive import Param, Param2

Defaults("Example1", b=4, d="dsf")
Defaults("Example2", b=4, d="dssf", GPU=True)
Defaults("Example3", a=2, instances=2, k=Param("name2", s=11), l=Param2("fff", 1119, s=2, d="fgrs"))
