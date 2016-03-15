import numpy as np


x = [np.random.rand(10, 1), np.random.rand(10, 1)]
y = np.hstack(x)
print(x)
print(y)
