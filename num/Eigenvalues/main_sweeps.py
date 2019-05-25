
import sympy as sy
import numpy as np
import math as mt
from numpy import linalg

from Jacobi import jacobi_iter

rots = int(0)
n = int(4)
A = np.empty((n, n))
np.set_printoptions(precision=5)

# Creating a symmetric matrix A
for i in range(n):
    A[i, i] = np.random.rand()
    for j in range(i+1, n):
        A[i, j] = np.random.rand()
        A[j, i] = A[i, j]

print('JACOBI DIAGONALIZATION WITH CYCLIC SWEEPS')
print('\nThe A matrix about to be diagonalized is:\n')
print(A)
e, V = np.linalg.eig(A)
print('\nThe eigenvalues of A obtained analyticaly are:\n')
print(e)

sweeps, e, V = jacobi_iter(A)
print('\nThe eigenvalues obtained from Jacobi after', sweeps, 'iterations are:\n')
print(e)
print('\nThe D matrix is then:\n')
D = np.zeros((n, n))
for i in range(n):
    D[i, i] = e[i]
print(D)
print('\nThe eigenvector matrix obtained after', sweeps, 'iterations is:\n')
print(V)
print('\nThe sign-differences and the differces in the order of the colums with the')
print('matrix obtained analyticaly are not important as long as:')
print('1.- The signs are complementary, i.e a column (a -b c d) becomes (-a b -c -d)')
print('2.- The columns have element with the sabe absolute value in the same position')

print('\nCheck that V*D*Vt = A:\n')
DVt = np.matmul(D, V.T)
VDVt = np.matmul(V, DVt)
print(VDVt)

print('\nCheck that Vt*A*V = D:\n')
VtA = np.matmul(V.T, VDVt)
VtAV = np.matmul(VtA, V)
print(VtAV)