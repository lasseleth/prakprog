import numpy as np
import scipy.optimize as opt

class ANN1D:
    def __init__(self, nn, function):
        self.n = nn
        self.dat = np. random.rand(self.n, 3)
        self.f = function
    def ANN_f_forward(self, input):
        x = input
        out = 0
        for i in range(self.n):
            a = self.dat[i][0]
            b = self.dat[i][1]
            c = self.dat[i][2]

            out = out + self.f((x-a)/b)*c
        return out

    def ANN_train(self, inidata, l):
        assert inidata.size == l.size

        def cst(q):
            self.dat = np.reshape(q, (self.n, 3))
            y = self.ANN_f_forward(inidata)
            cst = np.sum((y-l)**2)

            return cst

        opt.minimize(cst, np.random.rand(3*self.n), method = 'BFGS', tol=1e-6)
######################
class ANN2D:
    def __init__(self, nn, function):
        self.n = nn
        self.dat = np. random.rand(self.n, 5)
        self.f = function
    def ANN_f_forward(self, input):
        x = input[0]
        y = input[1]
        out = 0
        for i in range(self.n):
            a = self.dat[i][0]
            b = self.dat[i][1]
            c = self.dat[i][2]
            d = self.dat[i][3]
            e = self.dat[i][4]

            out = out + self.f((x-a)/b, (x-c)/d)*e
        return out

    def ANN_train(self, inidata, l):

        def cst(q):
            self.dat = np.reshape(q, (self.n, 5))
            y = self.ANN_f_forward(inidata)
            cst = np.sum((y-l)**2)

            return cst

        opt.minimize(cst, np.random.rand(5*self.n), method = 'BFGS', tol=1e-6)
