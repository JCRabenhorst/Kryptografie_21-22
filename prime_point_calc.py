import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Create a Point to represent the points.
from collections import namedtuple
from numpy import *

Point = namedtuple("Point", "x y")
matplotlib.use('TkAgg')
result = Point

'''
###############################
# Made by Julia C. Rabenhorst #
###############################
                                * with help from StackOverflow :P
                                
scatterplot shows the prime shifted points
normal, unshifted elliptic curve as curve

TODO: table of the point additions
'''

a = 4
b = 7
prime = 13
squares = []
xlist = []
ylist = []
x3list = []
yclist = []
point_list = []
added_point_list = []

# y^2 = x^3 + ax + b

for x in range(1, prime):
    x2 = (x**2) % 13
    print(x, " | ", x2)
    squares.append(x2)


if (((b ** 2) / 4) + ((a ** 3) / 27)) % prime != 0:
    for x in range(1, prime):
        y = ((x**3) + (a*x) + b) % prime
        print(y, "y")
        if y in squares:
            print(x, "x")
            indices = [i for i, m in enumerate(squares) if m == y]
            print("ind", indices)
            for w in range(indices.__len__()):
                point_list.append(Point(x, indices[w] + 1))

            xlist.append(x)
            ylist.append(squares.index(y)+1)

    print("aaa", squares)
    print("pos 3", squares[3-1], "| item 4", squares.index(4)+1)
    print("bbb", xlist, " | ", ylist)

# setting up the grid
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.grid()

# scatterplot
for v in range(point_list.__len__()):
    e = point_list[v].x
    f = point_list[v].y
    plt.scatter(e, f, label="stars", color="green",
                marker="*", s=30)

print("scatterplot points (primed points): ", point_list)


def two_points():
    # adding two points
    for u in range(xlist.__len__() - 1):
        for z in range(ylist.__len__() - 1):
            dxdy = (ylist[z+1] - ylist[z]) / (xlist[u+1] - xlist[u])
            print("m = ", dxdy)
            x3 = ((dxdy**2) - xlist[u] - xlist[u+1]) % prime
            yc = -((dxdy * (x3 - xlist[u]) + ylist[z])) % prime
            plt.scatter(x3, yc, label="stars", color="orange",
                        marker="*", s=30)
            print("x3 ", x3, " | yc ", yc)
            x3 = int(x3)
            yc = int(yc)
            print("u", u)

            for i in range(point_list.__len__()):
                if point_list[i].x == x3:
                    if point_list[i].y == yc:
                        print("here", x3, yc)
                        plt.scatter(x3, yc, label="stars", color="cyan",
                                    marker="*", s=30)
                        added_point_list.append(Point(x3, yc))


two_points()
print("added points", added_point_list)

'''
        x und y ausrechnen
        scatterplot machen
        verschiedene punkte addieren (tabelle machen)
        '''

plt.show()
