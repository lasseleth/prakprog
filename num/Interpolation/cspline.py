import numpy as np
from search import half_int

def cspline(x, y):
    n = len(x)
    h = np.empty(n-1)
    p = np.empty(n-1)
    D = np.empty(n)
    B = np.empty(n)
    b = np.empty(n)
    Q = np.empty(n-1)
    c = np.empty(n)
    d = np.empty(n)

    for i in range(n-1):
        h[i] = x[i+1] - x[i]
        p[i] = (y[i+1] - y[i])/h[i]

    D[0] = 2
    for i in range(n-2):
        D[i+1] = 2*h[i]/h[i+1] + 2
    D[n-1] = 2

    Q[0] = 1
    for i in range(n-2):
        Q[i+1] = h[i]/h[i+1]
        B[i+1] = 3*(p[i] + p[i+1]*h[i]/h[i+1])
    B[0] = 3*p[0]
    B[n-1] = 3*p[n-2]

    for i in range(1, n, 1):
        D[i] = D[i] - Q[i-1]/D[i-1]
        B[i] = B[i] - B[i-1]/D[i-1]
    b[n-1] = B[n-1]/D[n-1]

    for i in range(n-2, -1, -1):
        b[i] = (B[i] - Q[i]*b[i+1])/D[i]

    for i in range(n-1):
        c[i] = (-2*b[i] - b[i+1] + 3*p[i])/h[i]
        d[i] = (b[i] + b[i+1] - 2*p[i])/h[i]**2

    return h, p, b, c, d


def eval_cspline(x, y, z):
    n = len(x)
    #h = cspline(x, y)[0]
    #p = cspline(x, y)[1]
    b = cspline(x, y)[2]
    c = cspline(x, y)[3]
    d = cspline(x, y)[4]
    assert(n > 1 and z >= x[0] and z <= x[n-1])
    m = half_int(n, x, z) # Search
    dx = z - x[m]

    return (y[m] + b[m]*dx + c[m]*dx**2 + d[m]*dx**3)

def deriv_cspline(x, y, z):
    n = len(x)
    #h = cspline(x, y)[0]
    #p = cspline(x, y)[1]
    b = cspline(x, y)[2]
    c = cspline(x, y)[3]
    d = cspline(x, y)[4]
    assert(n > 1 and z >= x[0] and z <= x[n-1])
    m = half_int(n, x, z) # Search
    dx = z - x[m]

    return (b[m] + 2*c[m]*dx + 3*d[m]*dx**2)

def integ_cspline(x, y, z):
    n = len(x)
    #h = cspline(x, y)[0]
    #p = cspline(x, y)[1]
    b = cspline(x, y)[2]
    c = cspline(x, y)[3]
    d = cspline(x, y)[4]
    assert(n > 1 and z >= x[0] and z <= x[n-1])
    m = half_int(n, x, z) # Search

    integ_cspline = 0
    for l in range(m):
        dx = x[l+1] - x[l]
        integ_cspline = integ_cspline + y[l]*dx + 0.5*b[l]*dx**2 + (c[l]*dx**3)/3.0 + (d[l]*dx**4)/4.0

    dx = z - x[m]
    integ_cspline = integ_cspline + y[m]*dx + 0.5*b[m]*dx**2 + (c[m]*dx**3)/3.0 + (d[m]*dx**4)/4.0

    return integ_cspline