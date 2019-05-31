import numpy as np

def randompoints(a, b):
    x = a + np.random.rand(1, len(a))*(b-a)
    return x

def mc(dimen, a, b, f, N): #depends on dimension, ..., a function f, and the number of points N.
    #res = 0
    #err = 0
    V = 1.0
    for i in range(dimen):
        V = V*(b[i] - a[i])
    
    sum = 0
    sumq = 0

    for i in range(N):
        x = randompoints(a, b)
        fval = f(x)
        sum = sum + fval
        sumq = sumq + fval**2
    
    avg = sum/N             #average
    var = sumq/N - avg**2   #variance

    res = avg*V
    err = V*(var/N)**0.5

    return res, err