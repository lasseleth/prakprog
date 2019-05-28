import numpy as np

for i in range(200):
    print('%g %g %g' % (i*np.pi/100.0, np.sin(i*np.pi/100.0), np.cos(i*np.pi/100.0)))