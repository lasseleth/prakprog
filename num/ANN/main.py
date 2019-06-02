import ANN
import numpy as np

def f1(x, y=None):
    if y is None:
        return x*np.exp(-x**2)
    else:
        return x*y*np.exp(-y**2)

def f2(x, y=None):
    if y is None:
        return np.cos(5*x)*np.exp(-x**2)
    else:
        return np.cos(5*x)*np.exp(-x**2)*np.exp(-y**2)
#print("Initiating 1D ANN")
N = 30 # number of hidden nodes
tal = 100
#In 1D
x1 = np.linspace(-2, 2, tal)
labels1 = f2(x1)

res = ANN.ANN1D(N, f1)
res.ANN_train(x1, labels1)
y = res.ANN_f_forward(x1)
#print("\n1D ANN done, now onto 2D:")

#In 2D
y2 = np.linspace(-2.5, 2.5, tal)
labels2 = f2(x1, y2)

res2 = ANN.ANN2D(N, f2)
res2.ANN_train([x1, y2], labels2)
z = res2.ANN_f_forward([x1, y2])
#print("2D is done, printing answers:\n")
for i in range(tal):
    print('%g %g %g %g %g %g' % (x1[i], y2[i], y[i], z[i], f2(x1[i]), f2(x1[i], y2[i])))
