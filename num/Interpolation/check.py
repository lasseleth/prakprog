import numpy as np
from scipy.interpolate import interp1d

# We keep on working with the function y = x**2. This means that:
# The analytical derivative is: y' = 2 * x
# The analytical integral is: Y = x**3 / 3

# To calculate the exact splines the function interp1d from
# scipy.interpolate has been used

X = [0, 2, 4, 6, 8, 10]
Y = [0, 4, 16, 36, 64, 100]
N = len(X)

# Defining precise vectors to evaluate the integrals, derivatives and splines
n_prec = 1000
x_prec = np.linspace(X[0], X[N-1], n_prec)
y_prec = np.empty(n_prec)
dy_prec = np.empty(n_prec)
Y_prec = np.empty(n_prec)

for i in range(n_prec):
    y_prec = x_prec[i]**2
    dy_prec = 2*x_prec[i]
    Y_prec = (1/3)*x_prec[i]**3
    linear_prec = interp1d(X, Y, kind='linear')(x_prec[i])
    quadratic_prec = interp1d(X, Y, kind='quadratic')(x_prec[i])
    cubic_prec = interp1d(X, Y, kind='cubic')(x_prec[i])
    print("%.3f %0.3f %0.3f %0.4f %0.4f %0.3f %0.3f" % (x_prec[i], y_prec, linear_prec, quadratic_prec+10, cubic_prec+20, dy_prec, Y_prec))