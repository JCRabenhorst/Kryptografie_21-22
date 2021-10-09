import matplotlib.pyplot as plt
import numpy as np

# y^2 = x^3 + ax + b
a = -1
b = 0

# setting up the grid and curve
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
plt.grid()
plt.show()
