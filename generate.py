from main import Defaults, Param, GPU

Defaults("Example1", b=4, d="dsf")
Defaults("Example2", b=4, d="dssf", GPU=GPU.v16)
Defaults("Example3", a=2, instances=2, k=Param("name2", s=11))
