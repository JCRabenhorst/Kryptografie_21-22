import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Create a Point to represent the points.
from collections import namedtuple
Point = namedtuple("Point", "x y")
matplotlib.use('TkAgg')

# The point at infinity (origin for the group law)
Ori = 'Origin'
result = Point

'''
###############################
# Made by Julia C. Rabenhorst #
###############################
                                * with help from StackOverflow :P

Points are not pictured perfectly, because floats.
If you choose new a and b values, you HAVE TO set new A and B points.

Tested Points:
a = 1, b = 1, A = (-0.6, 0.428952...), B = (0, 1)
a = 0, b = 0, A = (1, 1), B = (2, 2.828427...)
'''

# Choose a and b (z is to make point calculations easier, insert the according value)
a = 1
b = 1
z = np.sqrt(((-0.6)**3)+((-0.6)*a)+b)

# Change A and B to match the a and b results
A = Point(-0.6, z)
B = Point(0, 1)


def ec_inv(w):
    global A
    """
    Inverse of the point P on the elliptic curve y^2 = x^3 + ax + b.
    """
    if w == Ori:
        return w
    return Point(A.x, (-A.y))


def ec_add(s, t):
    global result
    global A
    global B
    """
    Sum of the points P and Q on the elliptic curve y^2 = x^3 + ax + b
    """
    # Deal with the special cases where either A, B, or A + B is the origin
    if s.x and s.y == Ori:
        result = t
    elif t.x and t.y == Ori:
        result = s
    elif t == ec_inv(s):
        result = Ori
    else:
        # Cases not involving the origin.
        if float(s.x) == t:
            dydx = (3 * A.x**2 + a) / (2 * A.y)
            result = dydx
        else:
            dydx = (B.y - A.y) / (B.x - A.x)
            x = (dydx ** 2 - A.x - B.x)
            y = -(dydx * (x - A.x) + A.y)
            result = Point(x, y)
            # The above computations SHOULD have given us another point on the curve
        return result


def draw_curve():
    # setting up the grid and curve
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
    plt.grid()


def draw_points():
    # plotting the points
    plt.plot(A.x, A.y, marker='o', markerfacecolor='blue', markersize=5, label="A")
    plt.plot(B.x, B.y, marker='o', markerfacecolor='red', markersize=5)
    plt.plot(TwoA.x, -TwoA.y, marker='o', markerfacecolor='yellow', markersize=5)
    plt.plot(TwoA.x, TwoA.y, marker='o', markerfacecolor='purple', markersize=5)
    # plt.plot(AandB.x, -AandB.y, marker='o', markerfacecolor='yellow', markersize=5)
    # plt.plot(AandB.x, AandB.y, marker='o', markerfacecolor='purple', markersize=5)

    # labeling the points
    plt.text(A.x, A.y, 'A', horizontalalignment='right')
    plt.text(B.x, B.y, 'B', horizontalalignment='right')
    plt.text(TwoA.x, -TwoA.y, 'x3', horizontalalignment='right')
    plt.text(TwoA.x, TwoA.y, 'C', horizontalalignment='left')
    # plt.text(AandB.x, -AandB.y, 'x3', horizontalalignment='right')
    # plt.text(AandB.x, AandB.y, 'C', horizontalalignment='left')

    # setting the line points
    x1 = [A.x, B.x, TwoA.x]
    y1 = [A.y, B.y, -TwoA.y]
    x2 = [TwoA.x, TwoA.x]
    y2 = [-TwoA.y, TwoA.y]
    # x2 = [AandB.x, AandB.x]
    # y2 = [-AandB.y, AandB.y]

    # plotting the lines
    plt.plot(x1, y1, color='orange')
    plt.plot(x2, y2, color='green')

    # function to show the plot
    plt.show()


def extra_stuff():
    # (A + B) + C
    v = (A.x + B.x) + AandB.x
    c = (A.y + B.y) + AandB.y
    print("(A + B) + C = (", v, "|", c, ")")

    # A + (B + C)
    n = A.x + B.x + AandB.x
    m = A.y + B.y + AandB.y
    print("A + B + C = (", n, "|", m, ")")


# calling the calculations
TwoA = ec_add(A, A)
AandB = ec_add(A, B)
print("Two A's ", TwoA)
print("A and B ", AandB)

extra_stuff()
draw_curve()
draw_points()
