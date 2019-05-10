#Main
import random
import numpy as np
import matplotlib.pyplot as plt
import interpolation 



def main():
    random.seed(42)
    N=10
    x = [0.3+i + 0.5*np.sin(i) for i in range(N)]
    y = [i + np.cos(i*i) for i in range(N)]
    
    for i in range(len(x)): print(x[i]," ", y[i])
    
    print("\n\n")
    
    z = x[0]
    z_vec = np.zeros(0)
    ls_vec = np.zeros(0)
    inte_vec = np.zeros(0)
    
    while z <= x[-1]:
        ls = interpolation.linterp(N,x,y,z)
        z_vec = np.append(z_vec, z)
        ls_vec = np.append(ls_vec, ls)
        inte = interpolation.linterp_integ(N, x, y, z)
        inte_vec = np.append(inte_vec, inte)
        print(z," ", ls, " ")
        z = z+0.1
        
#    print(inte_vec, inte_vec.shape, z_vec.shape)
    plt.figure(1)
    plt.subplot(2,1,1)    
    plt.plot(x,y, '*', label="Points")
    plt.plot(z_vec,ls_vec, 'r-', label="linear spline")
#    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    
    plt.subplot(2,1,2)
    plt.plot(z_vec,np.cumsum(inte_vec), label="Integrated value")
    plt.ylabel("sum")
    plt.xlabel("x")
    plt.legend()
    plt.savefig("plot.svg")


main()