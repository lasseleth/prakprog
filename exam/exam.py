import numpy as np
import matplotlib.pyplot as plt


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
    
    F = np.array([F11, F12, F21, F22])
    
    x_mat = np.array([x2-px, px-x1])
    
    fq_mat = np.array([[F11, F12],
                       [F21, F22]])
    y_mat = np.array([[y2-py],
                      [py-y1]])
    
    arrays = (np.dot(np.dot(x_mat, fq_mat), y_mat))
        
    q = 1/((x2-x1)*(y2-y1))*arrays[0]
    return q, F
