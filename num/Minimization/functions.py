import sympy as sy
import numpy as np
import math as mt
from numpy import linalg

from qr import qr_decomp, qr_solve, qr_inverse

def Rosenbrock(X):
    x = X[0]
    y = X[1]

    FX = (1 - x)**2 + 100*(y - x**2)**2

    J = np.empty((len(X), len(X)))
    J[0, 0] = 400*(3*x**2 - y) + 2.0
    J[0, 1] = -400*x
    J[1, 0] = -400*x
    J[1, 1] = 200

    dfdx = np.empty(len(X)) #Derivatives
    dfdx[0] = 400*x**3 - 400*x*y + 2*x - 2.0
    dfdx[1] = 200*(y - x**2)
    return FX, J, dfdx

def Himmelblau(X):
    x = X[0]
    y = X[1]

    FX = (x**2 + y - 11)**2 + (x + y**2 - 7)**2

    J = np.empty((len(X), len(X)))
    J[0, 0] = 4*(y + x**2 - 11) + 8*x**2 +2
    J[0, 1] = 4*x + 4*y
    J[1, 0] = 4*x + 4*y
    J[1, 1] = 4*(x + y**2 - 7) + 8*y**2 +2

    dfdx = np.empty(len(X)) #Derivatives
    dfdx[0] = 2 * (2 * x * (x ** 2 + y - 11) + x + y ** 2 - 7)
    dfdx[1] = 2 * (x ** 2 + 2 * y * (x + y ** 2 - 7) + y - 11)
    return FX, J, dfdx

def decay(t, u):
    return (u[0]*np.exp(-t/u[1])+u[2])

def M_func(t, y, u, v):
    s = 0
    for i in range(len(t)):
        s = s + ((decay(t[i], v) - y[i])**2/u[i]**2)
    return np.array([s])