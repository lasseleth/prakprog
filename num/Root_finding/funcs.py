import sympy as sy
import numpy as np
import math as mt

def F_func(x):
    fx = np.empty(len(x))
    A = 10000
    v1 = A*x[0]*x[1] - 1.0
    v2 = np.exp(-x[0]) + np.exp(-x[1]) - 1.0 - 1.0/A
    fx[0] = v1
    fx[1] = v2
    return fx

def F_w_jacobian(x, J):
    fx = np.empty(len(x))
    A = 10000
    v1 = A*x[0]*x[1] - 1.0
    v2 = np.exp(-x[0]) + np.exp(-x[1]) - 1.0 - 1.0/A
    fx[0] = v1
    fx[1] = v2

    J[0, 0] = A*x[1]
    J[0, 1] = A*x[0]
    J[1, 0] = -np.exp(-x[0])
    J[1, 1] = -np.exp(-x[1])
    return fx

def GradRosenbrock(X):
    FX = np.empty(len(X))
    x = X[0]
    y = X[1]

    FX[0] = (200*x**3 - 200*x*y + x - 1)
    FX[1] = 100*(y - x**2)
    return FX

def GradRosenbrock_w_jacobian(X, J):
    FX = np.empty(len(X))
    x = X[0]
    y = X[1]

    FX[0] = (200*x**3 - 200*x*y + x - 1)
    FX[1] = 100*(y - x**2)

    J[0, 0] = 2.0*(600.0*x**2 - 200.0*y + 1.0)
    J[0, 1] = -400*x
    J[1, 0] = -400*x
    J[1, 1] = 200
    return FX

def GradHimmelblau(X):
    FX = np.empty(len(X))
    x = X[0]
    y = X[1]
    FX[0] = 4*x*(y + x**2 - 11) + 2*x + 2*y**2 -14
    FX[1] = 4*y*(x + y**2 - 7) + 2*x**2 + 2*y - 22
    return FX

def GradHimmelblau_w_jacobian(X, J):
    FX = np.empty(len(X))
    x = X[0]
    y = X[1]

    FX[0] = 4*x*(y + x**2 - 11) + 2*x + 2*y**2 -14
    FX[1] = 4*y*(x + y**2 - 7) + 2*x**2 + 2*y -22

    J[0, 0] = 4*(y + x**2 - 11) + 8*x**2 +2
    J[0, 1] = 4*x + 4*y
    J[1, 0] = 4*x + 4*y
    J[1, 1] = 4*(x + y**2 - 7) + 8*y**2 +2
    return FX