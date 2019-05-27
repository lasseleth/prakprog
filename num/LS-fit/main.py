import sympy as sy
import numpy as np
import math as mt
from qr import qr_decomp, qr_solve, qr_inverse

def func(i, x):
    if i == 0:
        return np.log(x)
    elif i == 1:
        return 1.0
    elif i == 2:
        return x
    else:
        print('Wrong value of i selected, please make i = 1, i = 2 or i = 3.')

x = [0.1, 1.33, 2.55, 3.78, 5.0, 6.22, 7.45, 8.68, 9.9]
y = [-15.3, 0.32, 2.45, 2.75, 2.27, 1.35, 0.157, -1.23, -2.75]
dy = [1.04, 0.594, 0.983, 0.998, 1.11, 0.398, 0.535, 0.968, 0.478]

n = len(x) # Lines
m = int(3) # Columns
A = np.empty((n, m))
b = np.empty(n)

for i in range(n):
    print(x[i], y[i], dy[i])
print('\n')

for i in range(n):
    b[i] = y[i]/dy[i]
    for j in range(m):
        A[i, j] = func(j, x[i])/dy[i]

(Q, R) = qr_decomp(A)
c = qr_solve(Q, R, b)

R_inv = qr_inverse(R)
S = np.zeros((m, m))
alph = 1.0
beta = 0.0
S = alph * np.matmul(R_inv, R_inv.T) + beta * S
print("\nThe fit calculated:")
print("(%g +/- %g)*log(x) + (%g +/- %g)*1.0 + (%g +/- %g)*x\n" % (c[0], S[0, 0]**0.5, c[1], S[1, 1]**0.5, c[2], S[2, 2]**0.5))
N = int(1000)
for i in range(1,N):
    X = i/100.0
    Y = c[0]*func(0, X) + c[1]*func(1, X) + c[2]*func(2, X)
    Y_max = (c[0] + S[0, 0]**0.5)*func(0, X) + (c[1] + S[1, 1]**0.5)*func(1, X) + (c[2] + S[2, 2]**0.5)*func(2, X)
    Y_min = (c[0] - S[0, 0]**0.5)*func(0, X) + (c[1] - S[1, 1]**0.5)*func(1, X) + (c[2] - S[2, 2]**0.5)*func(2, X)
    print(X, Y, Y_max, Y_min)