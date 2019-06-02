import numpy as np
from search import half_int

def qspline(x, y):
    n = len(x)
    h = np.empty(n-1)
    p = np.empty(n-1)
    c = np.empty(n-1)
    b = np.empty(n-1)

    for i in range(n-1):
        h[i] = x[i+1] - x[i]
        p[i] = (y[i+1] - y[i])/h[i]

    c[0] = 0
    for i in range(n-2):
        c[i+1] = (p[i+1] - p[i] - c[i]*h[i])/h[i+1]
    c[n-2] = c[n-2]/2

    for i in range(n-3, -1, -1):
        c[i] = (p[i+1] - p[i] - c[i+1]*h[i+1])/h[i]

    for i in range(n-1):
        b[i] = p[i] - c[i]*h[i]

    return h, p, c, b


def eval_qspline(x, y, z):
    n = len(x)
    h = qspline(x, y)[0]
    p = qspline(x, y)[1]
    c = qspline(x, y)[2]
    b = qspline(x, y)[3]
    assert(n > 1 and z >= x[0] and z <= x[n-1])
    m = half_int(n, x, z) # Search
    dx = z - x[m]

    return (y[m] + b[m]*dx + c[m]*dx**2)

def deriv_qspline(x, y, z):
    n = len(x)
    h = qspline(x, y)[0]
    p = qspline(x, y)[1]
    c = qspline(x, y)[2]
    b = qspline(x, y)[3]
    assert(n > 1 and z >= x[0] and z <= x[n-1])
    m = half_int(n, x, z) # Search
    dx = z - x[m]

    return (b[m] + 2*c[m]*dx)

def integ_qspline(x, y, z):
    n = len(x)
    h = qspline(x, y)[0]
    p = qspline(x, y)[1]
    c = qspline(x, y)[2]
    b = qspline(x, y)[3]
    assert(n > 1 and z >= x[0] and z <= x[n-1])
    m = half_int(n, x, z) # Search

    integ_qspline = 0
    for l in range(m):
        dx = x[l+1] - x[l]
        integ_qspline = integ_qspline + y[l]*dx + 0.5*b[l]*dx**2 + (c[l]*dx**3)/3.0

    dx = z - x[m]
    integ_qspline = integ_qspline + y[m]*dx + 0.5*b[m]*dx**2 + (c[m]*dx**3)/3.0

    return integ_qspline