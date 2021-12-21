import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import namedtuple
from termcolor import colored

# Create a Point to represent the points.
Point = namedtuple("Point", "x y")
matplotlib.use('TkAgg')
result = Point

'''
using y^2 = x^3 + ax + b
primes: 
19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 
113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 
241, 251, 257, 263, 269, 271, 277, 281, ...

'''

#################
a = 1           #
b = 5           # box of things to set
prime = 19      #
#################

squares = []
xlist = []
ylist = []
point_list = []
added_point_list = []
added_same_point_list = []
added_dif_point_list = []
menge_list = []
count_list = []

# making the list of squares
for x in range(1, prime):
    x2 = (x ** 2) % prime
    squares.append(x2)

# checking if x result has square counterpart
if (((b ** 2) / 4) + ((a ** 3) / 27)) % prime != 0:
    for x in range(0, prime):
        y = ((x ** 3) + (a * x) + b) % prime
        if y in squares:
            pd4 = int((prime + 1)/4)
            ytest = (y ** pd4) % prime
            y1 = ytest
            y2 = prime - y1
            xlist.append(x)
            ylist.append(y1)
            point_list.append(Point(x, y1))
            if y2 != y1:
                xlist.append(x)
                ylist.append(y2)
                point_list.append(Point(x, y2))


# setting up the grid
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.grid()

# add the scatterplot points
for v in range(point_list.__len__()):
    e = point_list[v].x
    f = point_list[v].y
    plt.scatter(e, f, label="stars", color="green", marker="o", s=70)
print(colored("scatterplot points (green circles): ", "green"), point_list, "\n", len(point_list), "points in total")


def dif_points(x1, x2, y1, y2):
    nenner = ((x2 - x1) ** (prime - 2)) % prime
    M = ((y2 - y1) * nenner) % prime
    M2 = (M * M) % prime
    x3 = (M2 - x1 - x2) % prime
    y3 = (M * (x1 - x3) - y1) % prime
    plt.scatter(x3, y3, label="stars", color="red", marker="*", s=30)
    added_point_list.append(Point(x3, y3))
    added_dif_point_list.append(Point(x3, y3))
    return Point(x3, y3)


def same_points(x1, y1):
    nenner2 = ((2 * y1) ** (prime - 2)) % prime
    M3 = ((3 * (x1 ** 2) + a) * nenner2) % prime
    M4 = (M3 * M3) % prime
    x3 = (M4 - (2 * x1)) % prime
    y3 = (M3 * (x1 - x3) - y1) % prime
    plt.scatter(x3, y3, label="stars", color="blue", marker="x", s=60)
    added_point_list.append(Point(x3, y3))
    added_same_point_list.append(Point(x3, y3))
    return Point(x3, y3)


def two_points():
    for i in range(len(point_list)):
        x1 = point_list[i].x
        y1 = point_list[i].y
        for j in range(i + 1, len(point_list)):
            x2 = point_list[j].x
            y2 = point_list[j].y
            if x1 == -1:
                added_point_list.append(Point(x2, y2))
            if x2 == -1:
                added_point_list.append(Point(x1, y1))
            if x1 == x2 and (y1 + y2) % prime == 0:
                added_point_list.append(Point(-1, -1))
            if x1 != 0:
                if x1 != x2:
                    dif_points(x1, x2, y1, y2)
        same_points(x1, y1)
    print("------------------------------------------------------------------------------------")
    print(colored("ALL added points: \n", "yellow"),
          ', '.join(str(item) for item in added_point_list), "\n", len(added_point_list), "points in total")
    print("------------------------------------------------------------------------------------")
    print(colored("Square added points (blue crosses): \n", "blue"),
          ', '.join(str(item) for item in added_same_point_list), "\n", len(added_same_point_list), "points in total")
    print("------------------------------------------------------------------------------------")
    print(colored("Different added points (red stars): \n", "red"),
          ', '.join(str(item) for item in added_dif_point_list), "\n", len(added_dif_point_list), "points in total")
    print("------------------------------------------------------------------------------------")


two_points()


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    print("Primzahlzerlegung: ", primfac)


def mengen():
    for i in range(len(point_list)):
        x1 = point_list[i].x
        y1 = point_list[i].y
        x2 = x1
        y2 = y1
        k = 1
        print((x1, y1), end='')
        x3 = 4711
        y3 = 4711
        while True:
            if x1 == -1:
                x3 = x2
                y3 = y2
            elif x2 == -1:
                x3 = x1
                y3 = y1
            elif x1 == x2 and (y1 + y2) % prime == 0:
                x3 = -1
                y3 = -1
            elif x1 != x2:
                nenner = ((x2 - x1) ** (prime - 2)) % prime
                M = ((y2 - y1) * nenner) % prime
                M2 = (M * M) % prime
                x3 = (M2 - x1 - x2) % prime
                y3 = (M * (x1 - x3) - y1) % prime
            else:
                nenner = ((2 * y1) ** (prime - 2)) % prime
                M3 = ((3 * (x1 ** 2) + a) * nenner) % prime
                M4 = (M3 * M3) % prime
                x3 = (M4 - (2 * x1)) % prime
                y3 = (M3 * (x1 - x3) - y1) % prime
            print((x3, y3), end='')
            x2 = x3
            y2 = y3
            k += 1
            if x3 == -1:
                print(" gruppengröße:", k, end='')
                count_list.append(k)
                break
            if k > 75:
                break
        print()


mengen()
print("countliste: ", count_list)
kgv = np.lcm.reduce(count_list)
print("kgv von countliste: ", kgv)


def hasse(kgv):
    minimum = prime + 1 - (2 * np.sqrt(prime))
    maximum = prime + 1 + (2 * np.sqrt(prime))
    print("Hasse-Intervall von: ", minimum, " ------------ ", prime, " ------------ ", maximum)
    if minimum < kgv < maximum:
        print("KGV ist im Hasse-Intervall")


hasse(kgv)
# plt.show()


def chaos():
    G = Point(12, 15)
    n = 3
    result = Point(-1, -1)
    while n != 0:
        if n & 1:
            result = dif_points(G.x, result.x, G.y, result.y)
        n = n // 2
        G = same_points(G.x, G.y)
    print(G)


chaos()
''' TODO:
    - testmenge machen
    - in testmenge reinschieben
    - verschieben (2l + 1 zur seite springen (schablone verschieben))
    - id bzw #1 finden
'''
