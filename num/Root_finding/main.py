import sympy as sy
import numpy as np
import math as mt
from numpy import linalg

from qr import qr_decomp, qr_solve, qr_inverse
from newtonian import newton, newton_w_jacobian
from funcs import F_func, F_w_jacobian, GradRosenbrock, GradRosenbrock_w_jacobian, GradHimmelblau, GradHimmelblau_w_jacobian

dx = 0.00001
eps = 0.001

func_use = 0

# Functions Newton
print('\nFUNCTIONS SOLVED THROUGH NEWTON METHOD')

x_1 = [-2.0, 9.0]
print('Function One:')
x_sol1 = newton(F_func, x_1, 0.1*dx, eps)
print('x = ', x_sol1)
fx_sol1 = F_func(x_sol1)
print('f(x) = ', fx_sol1)

x_2 = [0.6, 1.5]
print('Rosenbrock function:') 
x_sol2 = newton(GradRosenbrock, x_2, 100*dx, 0.1*eps)
print('x = ', x_sol2)
fx_sol2 = GradRosenbrock(x_sol2)
print('f(x) = ', fx_sol2)

x_3 = [2.3, 1.6]
print('Himmelblau function:') # IMPROVE
x_sol3 = newton(GradHimmelblau, x_3, 100*dx, 0.01*eps)
print('x = ', x_sol3)
fx_sol3 = GradHimmelblau(x_sol3)
print('f(x) = ', fx_sol3)


print('\nFUNCTIONS SOLVED THROUGH NEWTON METHOD WITH JACOBIAN')
x_4 = [-2.0, 9.0]
print('Function One:')
x_sol4 = newton_w_jacobian(F_w_jacobian, x_4, eps)
print('x = ', x_sol4)
fx_sol4 = F_func(x_sol4)
print('f(x) = ', fx_sol4)

x_5 = [0.6, 1.5]
print('Rosenbrock function:') 
x_sol5 = newton_w_jacobian(GradRosenbrock_w_jacobian, x_5, 0.1*eps)
print('x = ', x_sol5)
fx_sol5 = GradRosenbrock(x_sol5)
print('f(x) = ', fx_sol5)

x_6 = [2.3, 1.6]
print('Himmelblau function:') 
x_sol6 = newton_w_jacobian(GradHimmelblau_w_jacobian, x_6, 0.01*eps)
print('x = ', x_sol6)
fx_sol6 = GradHimmelblau(x_sol6)
print('f(x) = ', fx_sol6)