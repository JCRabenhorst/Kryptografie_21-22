import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple
from colorama import Fore

# Create a Point to represent the points.
Point = namedtuple("Point", "x y")
matplotlib.use('TkAgg')
result = Point

'''
###############################
# Made by Julia C. Rabenhorst #
###############################
                                * with help from StackOverflow :P
                                
scatterplot shows the prime shifted points

prime examples: 
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 
113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 
241, 251, 257, 263, 269, 271, 277, 281, ...

i ONLY make the positive points, NO NEGATIVE POINTS, so some points are MISSING
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
added_point_equal_existing_point_list = []

# y^2 = x^3 + ax + b

# making the list of squares
for x in range(1, prime):
    x2 = (x**2) % 13
    squares.append(x2)

# checking if x result has square counterpart
if (((b ** 2) / 4) + ((a ** 3) / 27)) % prime != 0:
    for x in range(1, prime):
        y = ((x**3) + (a*x) + b) % prime
        if y in squares:
            indices = [i for i, m in enumerate(squares) if m == y]
            for w in range(indices.__len__()):
                point_list.append(Point(x, indices[w] + 1))

            xlist.append(x)
            ylist.append(squares.index(y)+1)

# setting up the grid
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.grid()

#  add the scatterplot points
for v in range(point_list.__len__()):
    e = point_list[v].x
    f = point_list[v].y
    plt.scatter(e, f, label="stars", color="green",
                marker="*", s=30)
print("scatterplot points (primed points): ", point_list, "\n", len(point_list), "points in total \n")


def two_points():
    # adding two points
    for u in range(xlist.__len__() - 1):
        for z in range(ylist.__len__() - 1):
            dxdy = (ylist[z+1] - ylist[z]) / (xlist[u+1] - xlist[u])
            x3 = ((dxdy**2) - xlist[u] - xlist[u+1]) % prime
            yc = -(dxdy * (x3 - xlist[u]) + ylist[z]) % prime
            plt.scatter(x3, yc, label="stars", color="orange",
                        marker="*", s=30)
            added_point_list.append(Point(x3, yc))

            # check if added point equals existing scatterplot point
            for i in range(point_list.__len__()):
                if point_list[i].x == x3:
                    if point_list[i].y == yc:
                        plt.scatter(x3, yc, label="stars", color="cyan",
                                    marker="*", s=30)
                        added_point_equal_existing_point_list.append(Point(x3, yc))

    # print("added points", added_point_list)
    # print("added points that equal existing point", added_point_equal_existing_point_list)
    for i in range(len(added_point_list)):
        for j in range(len(added_point_equal_existing_point_list)):
            if added_point_list[i] == added_point_equal_existing_point_list[j]:
                added_point_list[i] = Fore.RED + str(added_point_list[i]) + Fore.RESET

    print("added points, red are the ones where they coincide with existing points: \n",
          ', '.join(str(item) for item in added_point_list), "\n", len(added_point_list), "points in total, with",
          len(added_point_equal_existing_point_list), "points equal to scatterplot points")


two_points()    # if you want the added points, leave active. if you only want scatterplot, comment out
plt.show()
