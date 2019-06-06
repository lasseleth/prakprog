import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10, 100)
y = np.linspace(-10,10, 100)

def func(x,y): return np.cos(x)*np.sin(y) #just some function


F = np.zeros([len(x), len(y)])
for i in range(len(x)): 
    for j in range(len(y)):
        F[i,j] = func(x[i],y[j]) #Fill in the matrix with values of the function

#print(F)

def bilinear(x, y, F, p):
    px = p[0]
    py = p[1]    
    if px >= len(x)-2:
        x1 = len(x)-2
        x2 = len(x)-1
    else:
        x1 = int(np.floor(px)) 
        x2 = int(np.floor(px+1))
    
    if py >= len(y)-2:
        y1 = len(y)-2
        y2 = len(y)-1
    else:
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

#    print(q)
#    print(F[x1,y1], F[x2,y2])
    return q


n = 100
#k = np.linspace(0,3,1)
i_st = np.array([])
j_st = np.array([])
Q = np.zeros( ( n, n) ) 

for i in range(n):
    q_st = np.array([])
    for j in range(n):
        p = [i, j]
        q = bilinear(x, y, F, p)
#        print(q)
        q_st = np.append(q_st, q)
        j_st = np.append(j_st, j)
#    print(q_st)
    i_st = np.append(i_st, i)
    
    Q[int(i),:] = q_st
print(Q)
#Q = np.array(q_st[1:3]) 
#for i in range(len(k)):
#    Q = np.column_stack((Q, q_st[(1+3*i):(10+3*i)]))
    
    

X, Y = np.meshgrid(i_st, j_st[0:n])
plt.contourf(i_st, j_st[0:n], Q, 100)

plt.colorbar()