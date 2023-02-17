import numpy as np
from sys import path
path.append('./')
from effect_size_analysis.cliff_delta import cliff_delta

x1 = np.random.rand(1009) * 10
x2 = np.random.rand(1009) * 4

print(cliff_delta(x1, x2, 0.05, True))