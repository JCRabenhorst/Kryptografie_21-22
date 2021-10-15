import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Create a Point to represent the points.
from collections import namedtuple
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

# setting up the grid and curve
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.contour(x.ravel(), y.ravel(), (y**2) - (x**3) - x * a - b, [0])
plt.grid()

# scatterplot
for v in range(point_list.__len__()):
    e = point_list[v].x
    f = point_list[v].y
    plt.scatter(e, f, label="stars", color="green",
                marker="*", s=30)

print("scatterplot points (primed points): ", point_list)

plt.show()

# adding two points
for x in range(xlist.__len__() - 1):
    for y in range(ylist.__len__() - 1):
        dxdy = (ylist[y+1] - ylist[y]) / (xlist[x+1] - xlist[x])
        print("m = ", dxdy)
        x3 = ((dxdy**2) - xlist[x] - xlist[x+1]) % prime
        yc = -((dxdy * (x3 - xlist[x]) + ylist[y])) % prime
        print("x3 ", x3, " | yc ", yc)

        '''
        x und y ausrechnen
        scatterplot machen
        verschiedene punkte addieren (tabelle machen)
        '''
