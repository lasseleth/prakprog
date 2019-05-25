import sympy as sy
import numpy as np
import time

from Jacobi import jacobi_iter, jacobi_time

np.set_printoptions(precision=5)

# print('\nTIMING THE JACOBI_ITER ALGORITHM FOR VARIOUS MATRIX SIZES:\n')
n_t = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]
times = jacobi_time(n_t)
for i in range(len(n_t)):
    print(n_t[i], times[i]/times[len(n_t)-1], n_t[i]**3/n_t[len(n_t)-1]**3)