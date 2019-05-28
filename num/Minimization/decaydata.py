import numpy as np
#Decay data
x_fit = np.array([0.23, 1.29, 2.35, 3.41, 4.47, 5.53, 6.59, 7.65, 8.71, 9.77])
y_fit = np.array([4.64, 3.38, 3.01, 2.55, 2.29, 1.67, 1.59, 1.69, 1.38, 1.46])
error = np.array([0.42, 0.37, 0.34, 0.31, 0.29, 0.27, 0.26, 0.25, 0.24, 0.24])

for i in range(len(error)):
    print(x_fit[i], y_fit[i], error[i])
print('\n')