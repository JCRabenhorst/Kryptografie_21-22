import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

matplotlib.use('TkAgg')

# Create a simple Point class to represent the affine points.
from collections import namedtuple
Point = namedtuple("Point", "x y")

# The point at infinity (origin for the group law).
O = 'Origin'

# Choose a particular curve and prime.  We assume that p > 3.
p = 15733
a = 1
b = 1

P = Point(0, 1)
Q = Point(8, 1267)
R = Point(2, 3103)

result = Point


def valid(q):
    global P
    x = int(P.x)
    y = int(P.y)
    """
    Determine whether we have a valid representation of a point
    on our curve.  We assume that the x and y coordinates
    are always reduced modulo p, so that we can compare
    two points for equality with a simple ==.
    """
    if q == O:
        return True
    else:
        return (
            (y**2 - (x**3 + a*x + b)) % p == 0 and
            0 <= x < p and 0 <= y < p)


def inv_mod_p(x):
    """
    Compute an inverse for x modulo p, assuming that x
    is not divisible by p.
    """
    if x % p == 0:
        raise ZeroDivisionError("Impossible inverse")
    return pow(x, p - 2, p)


def ec_inv(q):
    global P
    """
    Inverse of the point P on the elliptic curve y^2 = x^3 + ax + b.
    """
    if q == O:
        return q
    return Point(P.x, (-P.y) % p)


def ec_add(s, t):
    global result
    global P
    global Q
    """
    Sum of the points P and Q on the elliptic curve y^2 = x^3 + ax + b.
    """
    if not (valid(s) and valid(t)):
        raise ValueError("Invalid inputs")

    # Deal with the special cases where either P, Q, or P + Q is
    # the origin.
    if s == O:
        result = t
    elif t == O:
        result = s
    elif t == ec_inv(s):
        result = O
    else:
        # Cases not involving the origin.
        print(s, " | ", t)
        if s == t:
            print("hi")
            dydx = (3 * P.x**2 + a) * inv_mod_p(2 * P.y)
            result = dydx
        else:
            dydx = (Q.y - P.y) * inv_mod_p(Q.x - P.x)
            x = (dydx ** 2 - P.x - Q.x) % p
            y = (dydx * (P.x - x) - P.y) % p
            result = Point(x, y)

            # The above computations *should* have given us another point
            # on the curve.
        assert valid(result)
        return result



s = type(P.x)
print(P.x, " aaaa ", P.y, s)
TwoP = ec_add(P, P)
ThreeP = ec_add(TwoP, P)
# Compute 4P two different ways.
# assert ec_add(P, ThreeP) == ec_add(TwoP, TwoP)
# Check the associative law.
# assert ec_add(P, ec_add(Q, R)) == ec_add(ec_add(P, Q), R)

print("Twp P ", TwoP, " | Three Points ", ThreeP)
'''''
# setting the x - coordinates
x = np.arange(0, 2, 0.1)
# setting the corresponding y - coordinates
y = np.sqrt(x**3 + a*x + b)
'''
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
plt.grid()
'''''
# poltting the points
plt.plot(x, y)
'''
# function to show the plot
plt.show()

'''import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')
print("hi")

import numpy as np
import pylab as pl

Y, X = np.mgrid[-10:10:100j, -10:10:100j]
#a = -1
#b = 1


def f(x):
    return x**3 -3*x + 5


# blauer punkt spiegel C
px = -2.0
py = -np.sqrt(f(px))

# orangener punkt C
qx = 0.5
qy = np.sqrt(f(qx))

k = (qy - py)/(qx - px)
b = -px*k + py
wert = ((qy - py)/(qx - px))**2 + qx + px
poly = np.poly1d([-1, k**2, 2*k*b+3, b**2-5])

x = np.roots(poly)
y = np.sqrt(f(x))

pl.contour(X, Y, Y**2 - f(X), levels=[0])
pl.plot(x, y, "o")
pl.plot(x, -y, "o")

x = np.linspace(-5, 5)
pl.plot(x, k*x+b)

########
#a = -1  # standard value -1
#b = 1   # standard value 1

#y, x = np.ogrid[-5:5:100j, -5:5:100j]
#plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
#plt.grid()
plt.show()
print("k ", k, " px ", px, " py ", py, " qx ", qx, " qy ", qy, " x3 ", wert)

# setting the x - coordinates
#x = np.arange(0, 1, 0.1)
# setting the corresponding y - coordinates
#y = np.sin(x)

# plotting the points
#plt.plot(x, y)

# function to show the plot
#plt.show()'''

