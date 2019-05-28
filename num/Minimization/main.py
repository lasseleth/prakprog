import sympy as sy
import numpy as np
import math as mt
from numpy import linalg

from qr import qr_decomp, qr_solve, qr_inverse
from newtonian import newton, quasinewton
from functions import Himmelblau, Rosenbrock, decay, M_func

eps = 1e-7
dx = 1e-10

print('------------ MINIMIZATION WITH NEWTONIAN METHOD ------------')
x = [10.0, 12.0]

min_R = newton(Rosenbrock, x, eps)
print('The Rosenbrock function has a minimum at:', min_R)
min_H = newton(Himmelblau, x, eps)
print('The Himmelblau function has a minimum at:', min_H)

print('\n ------------ MINIMIZATION WITH QUASI-NEWTONIAN METHOD ------------')
X = [3.0, 3.0]

Min_R = quasinewton(Rosenbrock, X, dx, eps)
print('The Rosenbrock function has a minimum at:', Min_R)
Min_H = quasinewton(Himmelblau, X, dx, eps)
print('The Himmelblau function has a minimum at:', Min_H)

print('\nThe Newtonian method for the Root Finding excercise took 89 iterations for the Rosenbrok function and 5 iterations for the Himmelblau funtion.')
print('However, the starting points were closer to the solutions.')

print('\n ------------ MINIMIZATION WITH QUASI-NEWTON METHOD FOR THE GIVEN POINTS ------------')
x_fit = np.array([0.23, 1.29, 2.35, 3.41, 4.47, 5.53, 6.59, 7.65, 8.71, 9.77])
y_fit = np.array([4.64, 3.38, 3.01, 2.55, 2.29, 1.67, 1.59, 1.69, 1.38, 1.46])
error = np.array([0.42, 0.37, 0.34, 0.31, 0.29, 0.27, 0.26, 0.25, 0.24, 0.24])

fit_func = lambda p: M_func(x_fit, y_fit, error, p)
X_fit = [1.0, 1.0, 1.0]

FIT = quasinewton(fit_func, X_fit, dx, eps)
print('The fit can be seen in the plot "plot.svg".')
print('\n')

for i in range(1000):
    print('%0.2f %f' % (i/100, decay(i/100, FIT)))