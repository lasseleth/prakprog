import math as mt
import numpy as np
#Ignore the errors, the script works ;)
def ra_integrator(f, a, b, acc, eps, f2, f3, error_int): #Recursive adaptive integrator. Depends on a function, start and end points, accuracy etc. 
    f1 = f(a + (b -a)/6)
    f4 = f(a + 5*(b - a)/6)
    q = (2*(f1 + f4) + f2 + f3)*(b - a)/6
    Q = (f1 + f2 + f3 + f4)*(b - a)/4

    tol = acc + eps*mt.fabs(Q)
    error = mt.fabs(Q - q)
    if (error < tol):
        error_int = error
        return Q 

    else:
        error1 = 0.0
        error2 = 0.0

        Q1 = ra_integrator(f, a, (a + b)/2, acc/2.0**0.5, eps, f1, f2, error1)
        Q2 = ra_integrator(f, (a + b)/2, b, acc/2.0**0.5, eps, f3, f4, error2)
    return (Q1 + Q2) #Result of integration


def integrator(f, a, b, acc, eps, error_int): 
    f2 = f(a + 2*(b - a)/6)
    f3 = f(a + 4*(b - a)/6)

    Q = ra_integrator(f, a, b, acc, eps, f2, f3, error_int)
    return Q


def inf_integrator(f, a, b, acc, eps, error_int):
    A = np.isinf(a)
    B = np.isinf(b)

    if (A == False and B == False):
        # No infinites
        Q = integrator(f, a, b, acc, eps, error_int) #No inifinities, works normally

    elif (A == True and B == True): # Both limits are infinite
        def both_inf(t):
            return (f(t/(1 - t**2))*(1 + t**2)/(1 - t**2)**2)
        Q = integrator(both_inf, -1, 1, acc, eps, error_int)

    elif (A == False and B  == True): #Upper bound B is infinite
        def Up_inf(t):
            return (f(a + (1 - t)/t)/t**2)
        Q = integrator(Up_inf, 0, 1, acc, eps, error_int)

    elif (A == True and B == False): #Lower bound A is infinite
        def Lo_inf(t):
            return (f(b - (1 - t)/t)/t**2)
        Q = integrator(Lo_inf, 0, 1, acc, eps, error_int)

    else: #For errors
        print('ERROR')
        Q = float('Infinity')

    return Q

def Clenshaw_Curtis(f, a, b, acc, eps, error_int): 
    def F(t):
        return (f((a + b)/2.0 + (a - b)*np.cos(t)/2.0)*np.sin(t)*(b - a)/2.0) #func

    return (integrator(F, 0, mt.pi, acc, eps, error_int)) #integrating...