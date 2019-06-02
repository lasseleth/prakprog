import search
from lspline import linterp, integ_linterp
from qspline import qspline, integ_qspline, deriv_qspline, eval_qspline
from cspline import cspline, integ_cspline, deriv_cspline, eval_cspline

x = [0, 2, 4, 6, 8, 10]
y = [0, 4, 16, 36, 64, 100]

N = len(x)

for i in range(100):
    z = i/10
    print("%.1f %0.1f %0.2f %0.1f %0.3f %0.1f %0.3f %0.3f %0.3f" % (z, linterp(N, x, y, z), integ_linterp(N, x, y, z), eval_qspline(x, y, z)+10, integ_qspline(x, y, z), deriv_qspline(x, y, z), eval_cspline(x, y, z)+20, integ_cspline(x, y, z), deriv_cspline(x, y, z)))