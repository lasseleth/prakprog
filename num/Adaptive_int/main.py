from Integration import integrator, inf_integrator, ra_integrator, Clenshaw_Curtis
import numpy as np
import sys
sys.setrecursionlimit(100000)

#Functions to integrate
def sqrt(x):
    global callnum1
    callnum1 = callnum1 +1
    return x**0.5

def invsqrt(x):
    global callnum2
    callnum2 = callnum2 + 1
    return 1.0/x**0.5

def logsqrt(x):
    global callnum3
    callnum3 = callnum3 + 1
    return np.log(x)/x**0.5

def testfunc(x):
    global callnum4
    callnum4 = callnum4 + 1
    return 4.0*(1-(1-x)**2)**0.5

def gaussian(x):
    global callnum5
    callnum5 = callnum5 + 1
    return np.exp(-x**2)


print("Integrating function with Recursive Adaptive Integrator (RAI)")
a = 0.0 #lower bound 
b = 1.0 #upper bound
acc = 1e-8 #accuracy
eps = 1e-8 #relative accuracy


#_____________________________________________________________
#sqrt integ
callnum1 = 0
error1 = 0
print("\n------ Intergrating sqrt from 0 to 1 ------")
result_sqrt = integrator(sqrt, a, b, acc, eps, error1)

print("\nNumerical solution: ", result_sqrt)
print("Analytical solution: ", 2.0/3.0)
print("There were %i calls to the function." % (callnum1) )
print("The error is estimated to be: ", acc + np.fabs(result_sqrt)*eps) #prints the calculated error
print("The actual error is: ", np.fabs(result_sqrt- 2.0/3.0))
print("\n")

#_____________________________________________________________
#inverse sqrt integ
callnum2 = 0
error2 = 0
print("\n------ Intergrating inverse sqrt from 0 to 1 ------")
result_invsqrt = integrator(invsqrt, a, b, acc, eps, error2)

print("\nNumerical solution: ", result_invsqrt)
print("Analytical solution: ", 2.0)
print("There were %i calls to the function." % (callnum2) )
print("The error is estimated to be: ", acc + np.fabs(result_invsqrt)*eps) #prints the calculated error
print("The actual error is: ", np.fabs(result_invsqrt- 2.0))
print("\n")

#_____________________________________________________________
#log sqrt integ
callnum3 = 0
error3 = 0
print("\n------ Intergrating ln/sqrt from 0 to 1 ------")
result_lnsqrt = integrator(logsqrt, a, b, acc, eps, error3)

print("\nNumerical solution: ", result_lnsqrt)
print("Analytical solution: ", -4.0)
print("There were %i calls to the function." % (callnum3) )
print("The error is estimated to be: ", acc + np.fabs(result_lnsqrt)*eps) #prints the calculated error
print("The actual error is: ", np.fabs(result_lnsqrt+ 4.0))
print("\n")

#_____________________________________________________________
#testfunc integ
callnum4 = 0
error4 = 0
print("\n------ Intergrating test function from 0 to 1 ------")
print("Test function is: 4*sqrt(1-(1-x)^2)")
result_testfunc = integrator(testfunc, a, b, acc, eps, error4)

print("\nNumerical solution: ", result_testfunc)
print("Analytical solution: ", np.pi)
print("There were %i calls to the function." % (callnum4) )
print("The error is estimated to be: ", acc + np.fabs(result_testfunc)*eps) #prints the calculated error
print("The actual error is: ", np.fabs(result_testfunc - np.pi))
print("\n")


print("###################################")
#### Now integrating with the Clenshaw-Curtis variable transformation ###
print("\nNow integrating with the Clenshaw-Curtis variable transformation")


callnum2 = 0
error2 = 0
print("\n---- Intergrating inverse sqrt from 0 to 1, using the Clenshaw-Curtis method ----")
cc_invsqrt = Clenshaw_Curtis(invsqrt, a, b, acc, eps, error2)

print("\nNumerical solution: ", cc_invsqrt)
print("Analytical solution: ", 2.0)
print("There were %i calls to the function." % (callnum2) )
print("The error is estimated to be: ", acc + np.fabs(cc_invsqrt)*eps) #prints the calculated error
print("The actual error is: ", np.fabs(cc_invsqrt- 2.0))
print("\n")

#_____________________________________________________________
#testfunc integ
callnum4 = 0
error4 = 0
print("\n---- Intergrating test function from 0 to 1, using the Clenshaw-Curtis method ----")
print("Test function is: 4*sqrt(1-(1-x)^2)")
cc_testfunc = integrator(testfunc, a, b, acc, eps, error4)

print("\nNumerical solution: ", cc_testfunc)
print("Analytical solution: ", np.pi)
print("There were %i calls to the function." % (callnum4) )
print("The error is estimated to be: ", acc + np.fabs(result_testfunc)*eps) #prints the calculated error
print("The actual error is: ", np.fabs(cc_testfunc - np.pi))
print("\n")


#############################################################
print("Now onto \"Infinite limits\" ")
inf = np.inf

callnum5 = 0
error5 = 0
print("Integrating Gaussian function from 0 to infinity...")
zeroinf = inf_integrator(gaussian, 0, inf, acc, eps, error5)

print("\nNumerical solution: ", zeroinf)
print("Analytical solution: ", np.pi**0.5/2.0)
print("There were %i calls to the function." % (callnum5) )
print("The error is estimated to be: ", acc + np.fabs(zeroinf)*eps) 
print("The actual error is: ", np.fabs(zeroinf - np.pi**0.5/2.0))
print("\n")

#_________________________________________________________
callnum5 = 0
error5 = 0
print("Integrating Gaussian function from -infinity to 0...")
infzero = inf_integrator(gaussian, -inf, 0, acc, eps, error5)

print("\nNumerical solution: ", infzero)
print("Analytical solution: ", np.pi**0.5/2.0)
print("There were %i calls to the function." % (callnum5) )
print("The error is estimated to be: ", acc + np.fabs(infzero)*eps) 
print("The actual error is: ", np.fabs(infzero - np.pi**0.5/2.0))
print("\n")

#_________________________________________________________
callnum5 = 0
error5 = 0
print("Integrating Gaussian function from -infinity to infinity...")
infinf = inf_integrator(gaussian, -inf, inf, acc, eps, error5)

print("\nNumerical solution: ", infinf)
print("Analytical solution: ", np.pi**0.5)
print("There were %i calls to the function." % (callnum5) )
print("The error is estimated to be: ", acc + np.fabs(infinf)*eps) 
print("The actual error is: ", np.fabs(infinf - np.pi**0.5))
print("\n")

