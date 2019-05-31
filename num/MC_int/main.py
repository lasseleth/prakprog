from MonteCarlo import mc
import numpy as np


def f1D(x): #1 dimension
    return np.sqrt(x)

def f2D(x): #2 dimensions
    return np.exp(-x[0, 0]**2 - x[0, 1]**2)

def f3D(x): #3 dimensions
    return 1/((1-np.cos(x[0, 0])*np.sin(x[0, 1])*np.cos(x[0, 2]))*np.pi**3)
print("\n\n#################################################")
print("\n--- Monte Carlo for 1D test function ---")
D1 = 1
N1 = int(1e5)
a1 = np.array([0])
b1 = np.array([1])

S1, err1 = mc(D1, a1, b1, f1D, N1)
expec1 = 2/3
print("\nMonte Carlo result in 1D: %g" % (S1) )
print("with calculated error: %g" %  (err1) )
print("Analytcal result: %g" % (expec1) ) 
print("with the real error: %g" % (np.fabs(expec1-S1)) )
print("\n#################################################")

print("\n--- Monte Carlo for 2D test function ---")
D2 = 2
N2 = int(1e5)
a2 = np. array([-10, -10])
b2 = np.array([10, 10])

S2, err2 = mc(D2, a2, b2, f2D, N2)
expec2 = np.pi
print("\nMonte Carlo result in 2D: %g" % (S2) )
print("with calculated error: %g" %  (err2) )
print("\nAnalytcal result: %g" % (expec2) ) 
print("with the real error: %g" % (np.fabs(expec2-S2)) )
print("\n#################################################")

print("\n--- Monte Carlo for 3D test function ---")
D3 = 3
N3 = int(1e5)
a3 = np.array([0, 0, 0])
b3 = np.array([np.pi, np.pi, np.pi])

S3, err3 = mc(D3, a3, b3, f3D, N3)
expec3 = 1.393203929685
print("\nMonte Carlo result in 3D: %g" % (S3) )
print("with calculated error: %g" %  (err3) )
print("\nAnalytcal result: %g" % (expec3) ) 
print("with the real error: %g" % (np.fabs(expec3-S3)) )
print("\n#################################################")