from main import Defaults
from relive import P1

Defaults("Example1", b=4, d="dsf")
Defaults("Example2", b=4, d="dssf", GPU=True)
Defaults("Example3", a=2, instances=2, k=P1("name2", s=11))
