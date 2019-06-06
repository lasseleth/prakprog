import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10, 10)
y = np.linspace(0,10, 10)

def func(x,y): return x*y**2 #just some function


F = np.zeros([len(x), len(y)])
for i in range(len(x)): 
    for j in range(len(y)):
        F[i,j] = func(x[i],y[j]) #Fill in the matrix with values of the function

#print(F)
p = [10, 10]


bilinear(x, y, F, p)

def bilinear(x, y, F, p):
    px = p[0]
    py = p[1]    
    x1 = int(np.floor(px)) 
    x2 = int(np.floor(px+1))
    
    y1 = int(np.floor(py))
    y2 = int(np.floor(py+1))
    
    F11 = F[x1, y1]
    F12 = F[x1, y2]
    F21 = F[x2, y1]
    F22 = F[x2, y2]
    
    x_mat = np.array([x2-px, px-x1])
    
    fq_mat = np.array([[F11, F12],
                       [F21, F22]])
    y_mat = np.array([[y2-py],
                      [py-y1]])
    
    arrays = (np.dot(np.dot(x_mat, fq_mat), y_mat))
        
    q = 1/((x2-x1)*(y2-y1))*arrays[0]

    print(q)
    print(F[x1,y1], F[x2,y2])
    return q


