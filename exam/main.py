import numpy as np
import matplotlib.pyplot as plt
from exam import bilinear

x = np.linspace(-10,10, 100)
y = np.linspace(-10,10, 100)

def func(x,y): return np.cos(x)*np.sin(y) #just some function


F = np.zeros([len(x), len(y)])
for i in range(len(x)): 
    for j in range(len(y)):
        F[i,j] = func(x[i],y[j]) #Fill in the matrix with values of the function


n = 100
i_st = np.array([])
j_st = np.array([])
Q = np.zeros( ( n, n) ) 

for i in range(n):
    q_st = np.array([])
    for j in range(n):
        p = [i, j]
        q,_ = bilinear(x, y, F, p)
        q_st = np.append(q_st, q)
        j_st = np.append(j_st, j)
    i_st = np.append(i_st, i)
    
    Q[int(i),:] = q_st   

p = np.random.rand(2)*10
q, F = bilinear(x,y,F,p)
print("Interpolated value of point p (%g, %g) is:" % (p[0], p[1]), q) 
print("While the nearby values are: %0.2g, %0.2g, %0.2g and %0.2g " % (F[0], F[1], F[2], F[3]))   

X, Y = np.meshgrid(i_st, j_st[0:n])
plt.figure()
plt.contourf(i_st, j_st[0:n], Q, 100)
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("cos(x)*sin(x)")