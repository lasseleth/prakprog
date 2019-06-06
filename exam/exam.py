import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10, 10)
y = np.linspace(0,10, 10)

def func(x,y): return x*y**2
F = np.zeros([len(x), len(y)])
for i in range(len(x)): 
    for j in range(len(y)):
        F[i,j] = func(x[i],y[j])



#def bilinear(x, y, F, px, py)
#px = 1
#py = 2
#
#x1=1
#x2=2
#y1=1
#y2=2
#x_vec = np.array([x1, x1, x2, x2])
#y_vec = np.array([y1, y2, y1, y2])
#
#xy_vec = np.array([x1*y1, x1*y2, x2*y1, x2*y2])
#
#mat_A = np.array([[1, 1, 1, 1], x_vec, y_vec, xy_vec])
#mat_A=np.transpose(mat_A)
#
#b = np.dot(np.transpose(np.linalg.inv(mat_A)), np.array([[1],[px],[py],[px*py]]))
#
#f = b[0]*func(x1,y1)+b[1]*func(x1,y2)+b[2]*func(x2,y1)+b[3]*func(x2,y2)





