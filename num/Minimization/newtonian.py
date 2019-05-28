import sympy as sy
import numpy as np
import math as mt
from numpy import linalg
from qr import qr_decomp, qr_solve

def newton(f, x0, eps):
    steps = 0
    alph = 1e-2
    x = x0.copy()

    while True:
        steps = steps + 1
        (fx, H, dfdx) = f(x)
        (Q, R) = qr_decomp(H)
        Dx_sol = qr_solve(Q, R, -dfdx)
        lamb = 1.0
    
        while True:
            a = Dx_sol*lamb
            y = x + a
            (fy, Hy, dfy) = f(y)
            if (fy < fx + alph*np.dot(a.T, dfdx) or lamb < 0.02):
                break
            lamb = lamb/2.0
    
        x = y.copy()
        dfdx = dfy.copy()
    
        if (np.linalg.norm(dfdx) < eps): # steps>stepsmax): #
            print('Process finish after %i iterations.' % (steps))
            break
    return x

def grad(f, x, dx):
    fx = f(x)[0] # FX from the functions used i.e. first entry
    n = len(x)
    dfdx = np.empty(n)
    
    for i in range(n):
        x[i] = x[i] + dx
        dfdx[i] = (f(x)[0] - fx)/dx
        x[i] = x[i] - dx
    return dfdx

def quasinewton(f, x0, dx, eps):
    steps = 0
    alph = 1e-2
    x = x0.copy()
    n = len(x)
    dfdx = grad(f, x, dx)
    fx = f(x)[0]
    B = np.eye(n)
    
    while True:
        steps = steps + 1
        Dx_sol = np.dot(B, -dfdx) # Matrix with -dfdx values in the diagonal
                                   # and zeros out of the diagonal
        lamb = 2.0
    
        while True:
            lamb = lamb/2.0
            a = Dx_sol*lamb
            z = x + a
            fz = f(z)[0]
    
            if (np.abs(fz) < np.abs(fx) + alph*np.dot(a, dfdx)):
                break
    
            if (np.linalg.norm(a) < dx):
                B = np.eye(n)
                # Start the process again
                break
    
        dfdx_z = grad(f, z, dx)
        y = dfdx_z - dfdx
        w = a - np.dot(B, y)

        # Including Broyden's update
        if (np.abs(np.dot(y, a)) > eps):
            gamma  = np.dot(w, y)/(2*np.dot(a, y))
            b = (w - gamma*a)/np.dot(a, y)
            B = B + np.outer(a, b) + np.outer(b, a)

        x = z
        fx = fz
        dfdx = dfdx_z
    
        if (np.linalg.norm(dfdx) < eps or np.linalg.norm(Dx_sol) < dx):
            print('Process finish after %i iterations.' % (steps))
            break
    
    return x