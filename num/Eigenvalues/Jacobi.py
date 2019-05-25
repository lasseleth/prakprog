import sympy as sy
import numpy as np
import math as mt
import time

def jacobi_iter(A):
    n = A.shape[0]
    iter = int(0)
    tol = 1.0e-15
    iter_mx = int(100)
    e = np.zeros(n)
    V = np.zeros((n, n))

    for i in range(0, n):
        V[i, i] = 1.0
    for l in range(0, iter_mx):
        s = 0 # sum of off-diagonal elements of A
        for i in range(0, n):
            s = s + np.sum(np.abs(A[i, (i+1):n]))
        if (s < tol):  #diagonal form of A
            iter = l
            for i in range(0, n):
                e[i] = A[i, i]
            break
        else:
            s_av = s/(n*(n-1)/2.0) # average value of off-diagonal elements
            for i in range(0, n):
                for j in range(i+1, n): # matrix columns
                    if (np.abs(A[i, j]) > s_av):
                        phi = 0.5 * mt.atan2(2.0*A[i, j],(A[i, i] - A[j, j]))
                        s = np.sin(phi)
                        c = np.cos(phi)
                        for k in range(i+1, j):
                            Aik = A[i, k]
                            A[i, k] = A[i, k]*c + A[k, j]*s
                            A[k, j] = A[k, j]*c - Aik*s
                        for k in range(j+1, n):
                            Aik = A[i, k]
                            A[i, k] = A[i, k]*c + A[j, k]*s
                            A[j, k] = A[j, k]*c - Aik*s
                        for k in range(0, i):
                            Aki = A[k, i]
                            A[k, i] = A[k, i]*c + A[k, j]*s
                            A[k, j] = A[k, j]*c - Aki*s
                        Aii = A[i, i]
                        A[i, i] = A[i, i]*c*c + 2.0*A[i, j]*c*s + A[j, j]*s*s
                        A[j, j] = A[j, j]*c*c - 2.0*A[i, j]*c*s + Aii*s*s
                        A[i, j] = 0.0
                        for k in range(0, n):
                            Vkj = V[k, j]
                            V[k, j] = V[k, j]*c - V[k, i]*s
                            V[k, i] = V[k, i]*c + Vkj*s
        iter = -l
    return iter, e, V

def jacobi_time(sizes):
    t = np.zeros(len(sizes))
    time_record = int(0)

    for m in sizes:
        M = np.empty((m, m))
        for i in range(m):
            M[i, i] = np.random.rand()
            for j in range(i+1, m):
                M[i, j] = np.random.rand()
                M[j, i] = M[i, j]

        time_start = time.time()
        its, ev, Vv = jacobi_iter(M)
        time_end = time.time()
        t[time_record] = time_end - time_start
        time_record = time_record + 1
    return t

def jacobi_eig_low(A, nums):
    # nums is the number of lowest eigenvalues that we want to calculate
    n = A.shape[0]
    iter = int(0)
    tol = 1.0e-15
    iter_mx = int(100)
    e = np.zeros(n)
    V = np.zeros((n, n))

    for i in range(0, n):
        V[i, i] = 1.0

    for l in range(0, iter_mx):
        s = 0 # sum of off-diagonal elements of A
        for i in range(0, nums):
            s = s + np.sum(np.abs(A[i, (i+1):n]))
        if (s < tol):
            # We have reached the diagonal form of A
            iter = l
            for i in range(0, n):
                e[i] = A[i, i]
            for i in range(nums, n):
                e[i] = 0.0
            break
        else:
            s_av = s/(n*(n-1)/2.0) # average value of off-diagonal elements
            for i in range(0, nums):
                for j in range(i+1, n):
                    if (np.abs(A[i, j]) > s_av):
                        phi = 0.5 * mt.atan2(2.0*A[i, j],(A[i, i] - A[j, j])) - mt.pi/2 # remove pi to get high to low
                        s = np.sin(phi)
                        c = np.cos(phi)
                        for k in range(i+1, j):
                            Aik = A[i, k]
                            A[i, k] = A[i, k]*c + A[k, j]*s
                            A[k, j] = A[k, j]*c - Aik*s
                        for k in range(j+1, n):
                            Aik = A[i, k]
                            A[i, k] = A[i, k]*c + A[j, k]*s
                            A[j, k] = A[j, k]*c - Aik*s
                        for k in range(0, i):
                            Aki = A[k, i]
                            A[k, i] = A[k, i]*c + A[k, j]*s
                            A[k, j] = A[k, j]*c - Aki*s
                        Aii = A[i, i]
                        A[i, i] = A[i, i]*c*c + 2.0*A[i, j]*c*s + A[j, j]*s*s
                        A[j, j] = A[j, j]*c*c - 2.0*A[i, j]*c*s + Aii*s*s
                        A[i, j] = 0.0
                        for k in range(0, n):
                            Vkj = V[k, j]
                            V[k, j] = V[k, j]*c - V[k, i]*s
                            V[k, i] = V[k, i]*c + Vkj*s

        iter = -l
    return iter, e, V

def jacobi_eig_high(A, nums):
    # nums is the number of lowest eigenvalues that we want to calculate
    n = A.shape[0]
    iter = int(0)
    tol = 1.0e-15
    iter_mx = int(100)
    e = np.zeros(n)
    V = np.zeros((n, n))

    for i in range(0, n):
        V[i, i] = 1.0

    for l in range(0, iter_mx):
        s = 0 # sum of off-diagonal elements of A
        for i in range(0, nums):
            s = s + np.sum(np.abs(A[i, (i+1):n]))
        if (s < tol):
            # We have reached the diagonal form of A
            iter = l
            for i in range(0, n):
                e[i] = A[i, i]
            for i in range(nums, n):
                e[i] = 0.0
            break
        else:
            s_av = s/(n*(n-1)/2.0) # average value of off-diagonal elements
            for i in range(0, nums):
                for j in range(i+1, n):
                    if (np.abs(A[i, j]) > s_av):
                        phi = 0.5 * mt.atan2(2.0*A[i, j],(A[i, i] - A[j, j])) # remove pi to get high to low
                        s = np.sin(phi)
                        c = np.cos(phi)
                        for k in range(i+1, j):
                            Aik = A[i, k]
                            A[i, k] = A[i, k]*c + A[k, j]*s
                            A[k, j] = A[k, j]*c - Aik*s
                        for k in range(j+1, n):
                            Aik = A[i, k]
                            A[i, k] = A[i, k]*c + A[j, k]*s
                            A[j, k] = A[j, k]*c - Aik*s
                        for k in range(0, i):
                            Aki = A[k, i]
                            A[k, i] = A[k, i]*c + A[k, j]*s
                            A[k, j] = A[k, j]*c - Aki*s
                        Aii = A[i, i]
                        A[i, i] = A[i, i]*c*c + 2.0*A[i, j]*c*s + A[j, j]*s*s
                        A[j, j] = A[j, j]*c*c - 2.0*A[i, j]*c*s + Aii*s*s
                        A[i, j] = 0.0
                        for k in range(0, n):
                            Vkj = V[k, j]
                            V[k, j] = V[k, j]*c - V[k, i]*s
                            V[k, i] = V[k, i]*c + Vkj*s

        iter = -l
    return iter, e, V