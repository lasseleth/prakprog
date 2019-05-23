
import sympy as sy
import numpy as np

from GR import qr_gs_decomp, qr_gs_solve, qr_gs_inverse

n = int(5) # Number of lines
m = int(4) # Number of columns
A = np.random.rand(n, m)

print('\nQR Decomposition\n')
print('Random 5x4 matrix A:\n')
print(A)
# Decomposition QR
(Q, R) = qr_gs_decomp(A)

print('\nMatrix Q 5x4:\n')
print(Q)
print('\nMatrix upper triangular R 4x4:\n')
print(R)

# Check Qt*Q = 1 and Q*R = A 
print('\nCheck that Qt*Q = I:\n')
QtQ = np.matmul(Q.T, Q)
print(QtQ)

print('\nCheck that Q*R = A:\n')
QR = np.matmul(Q, R)
print(QR)

# Linear equation solve
print('\nSolving linear equation system\n')
ns = int(4)
x = np.empty(ns)
b = np.random.rand(ns)
AA = np.random.rand(ns, ns)
RR = np.empty((ns, ns))
print('Random matrix A:\n')
print(AA)
# Decomposition QR
(Qb, Rb) = qr_gs_decomp(AA)

# System solving
x_sol = qr_gs_solve(Qb, Rb, b)

print('\nRandom vector b:\n')
print(b)

print('\nSolution (x) of the system of linear equations A*x = Q*Rx = b:\n')
print(x_sol)

# Check that we get b back after A*x
print('\nCheck that A*x = b:\n')
b2 = np.empty(ns)
A2 = np.matmul(Qb, Rb)
b2 = np.matmul(A2, x_sol)
print(b2)

#print(np.linalg.solve(A2, b))

# Inverse calculation
print('\nInverse  calculation:\n')
# We will use the same A matrix from the equation system
B = np.empty((ns, ns))
B_sol = qr_gs_inverse(AA)
print('Inverse matrix of A (from the linear equation system), B:\n')
print(B_sol)

print('\nChecking that A*B = I:\n')
I1 = np.matmul(AA, B_sol)
print(I1)

print('\nChecking that B*A = I:\n')
I2 = np.matmul(B_sol, AA)
print(I2)