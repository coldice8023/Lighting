#configure plotting
import matplotlib
import GPy
import numpy as np
from matplotlib import pyplot as plt
# matplotlib.rcParams['figure.figsize'] = (8,5)
# matplotlib.rcParams['text.usetex'] = True
# matplotlib.rcParams['font.size'] = 16
# matplotlib.rcParams['font.family'] = 'serif'
# np.random.seed(1)


def f(x): return 2 - x ** 2

k = GPy.kern.RBF(1, variance=7., lengthscale=0.2)
x = np.linspace(-2, 2, num=101)
fx = np.array(list(map(f, x)))
plt.plot(x, fx, 'r-', linewidth=3)
plt.show()

print(fx)