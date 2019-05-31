import numpy as np
from MonteCarlo import mc

def f2D(x):
    return np.exp(-x[0, 0]**2 - x[0, 1]**2) #Function

dimen = 2
N = 1
a = np.array([-10, -10])
b = np.array([10, 10])

for i in range(11):
    N = N*2
    S, err = mc(dimen, a, b, f2D, N)
    print('%i %g %g' % (N, err, 25.055/N**0.5))
