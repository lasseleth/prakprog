import sympy as sy
import numpy as np
import math as mt
from numpy import linalg
from qr import qr_decomp, qr_solve, qr_inverse

def newton(f, x0, dx, eps):
    stepsmax = 100000
    steps = 0
    x = x0.copy()
    n = len(x)
    J1 = np.empty((n, n))
    R1 = np.empty((n, n))
    Dx = np.empty(n)

    while True:
        fx = f(x)
        for j in range(n):
            x[j] = x[j] + dx # xp + dx
            fxp = f(x)
            fxp = fxp - fx # df
            for i in range(n):
                J1[i, j] = fxp[i]/dx
            x[j] = x[j] - dx

        fxm = -1.0*fx
        (J, R) = qr_decomp(J1)
        Dx_sol = qr_solve(J, R, fxm)

        lamb = 2.0
        while True:
            lamb = lamb/2.0
            y = x + Dx_sol*lamb
            fy = f(y)
            if (np.linalg.norm(fy)<(1-lamb/2.0)*np.linalg.norm(fx) or lamb<0.02):
                break
        x = y.copy()
        fx = fy.copy()
        steps = steps + 1
        if (np.linalg.norm(fx)<eps or np.linalg.norm(Dx_sol)<dx): # steps>stepsmax): #
            print('Process finish after %i iterations.' % (steps))
            break
    return x


def newton_w_jacobian(f, x0, eps):
    stepsmax = 100000
    steps = 0
    x = x0.copy()
    n = len(x)
    J1 = np.empty((n, n))
    R1 = np.empty((n, n))
    Dx = np.empty(n)

    while True:
        fx = f(x, J1)
        fxm = -1.0*fx
        (J, R) = qr_decomp(J1)
        Dx_sol = qr_solve(J, R, fxm)

        lamb = 2.0
        while True:
            lamb = lamb/2.0
            J2 = np.empty((n, n))
            y = x + Dx_sol*lamb
            fy = f(y, J2)
            if (np.linalg.norm(fy)<(1-lamb/2.0)*np.linalg.norm(fx) or lamb<0.02):
                break
        x = y.copy()
        fx = fy.copy()
        steps = steps + 1
        if (np.linalg.norm(fx)<eps): # steps>stepsmax): #
            print('Process finish after %i iterations.' % (steps))
            break
    return x