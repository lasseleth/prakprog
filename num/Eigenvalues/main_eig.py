import sympy as sy
import numpy as np
import math as mt
from numpy import linalg
import time

from Jacobi import jacobi_eig_high, jacobi_eig_low, jacobi_iter

rots = int(0)
n = int(7)
A = np.empty((n, n))
A2 = np.empty((n, n))
A3 = np.empty((n, n))
A4 = np.empty((n, n))
A5 = np.empty((n, n))
A6 = np.empty((n, n))
np.set_printoptions(precision=5)

# Creating a symmetric matrix A
for i in range(n):
    A[i, i] = np.random.rand()
    A2[i, i] = A[i, i]
    A3[i, i] = A[i, i]
    A4[i, i] = A[i, i]
    A5[i, i] = A[i, i]
    for j in range(i+1, n):
        A[i, j] = np.random.rand()
        A[j, i] = A[i, j]
        A2[i, j] = A[i, j]
        A2[j, i] = A[j, i]
        A3[i, j] = A[i, j]
        A3[j, i] = A[j, i]
        A4[i, j] = A[i, j]
        A4[j, i] = A[j, i]
        A5[i, j] = A[i, j]
        A5[j, i] = A[j, i]

n_eig = int(1)
print('EIGENVALUE CALCULATION FROM LOW TO HIGH\n')
print('The number of eigenvalues that are going to be calculated is:', n_eig)
print('\nThe A matrix about to be diagonalized is:\n')
print(A)
e = np.linalg.eigvals(A)
print('\nThe eigenvalues of A obtained analyticaly are:\n')
print(e)

t_l_s = time.time()
sweeps, e, V = jacobi_eig_low(A, n_eig)
t_l_f = time.time()

t_h_s = time.time()
sweeps2, e2, V2 = jacobi_eig_high(A2, n_eig)
t_h_f = time.time()

time_eig_s = time.time()
sweeps3, e3, V3 = jacobi_eig_low(A3, n)
time_eig_f = time.time()

sweeps4, e4, V4 = jacobi_eig_high(A4, n)
print('\nThe lowest eigenvalue obtained after', sweeps, 'iterations and', t_l_f - t_l_s, 'seconds is:\n')
print(e)
print('\nAll the eigenvalues obtained after', sweeps3, 'iterations in ascending order are:\n')
print(e3)
print('\nThe highest eigenvalue obtained after', sweeps2, 'iterations and', t_h_f - t_h_s, 'seconds is:\n')
print(e2)
print('\nAll the eigenvalues obtained after', sweeps4, 'iterations in descending order are:\n')
print(e4)

time_cyclc_s = time.time()
its, ev, Vv = jacobi_iter(A5)
time_cyclc_f = time.time()

print('\nThe number of iterations needed by the cyclic algorithm was:', its)
print('The cyclic algorithm took', time_cyclc_f - time_cyclc_s, 'seconds to reach the solution.\n')

print('The number of iterations needed by the value-by-value algorithm was:', sweeps3)
print('The value-by-value algorithm took', time_eig_f - time_eig_s, 'seconds to reach the solution.\n')