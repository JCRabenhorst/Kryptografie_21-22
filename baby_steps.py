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
using y^2 = x^3 + ax + b
i only make the positive points
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
x3list = []
yclist = []
point_list = []
added_point_list = []
added_same_point_list = []
added_dif_point_list = []
menge_list = []
count_list = []
new_count_list = []


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
    plt.scatter(e, f, label="stars", color="green",
               marker="o", s=70)
print("scatterplot points (green circles): ", point_list, "\n", len(point_list), "points in total \n")


def two_points():
    for i in range(len(xlist)):
        x1 = xlist[i]
        y1 = ylist[i]
        for j in range(i + 1, len(xlist)):
            # different points
            x2 = xlist[j]
            y2 = ylist[j]
            if x1 != x2:
                nenner = ((x2 - x1) ** (prime - 2)) % prime
                M = ((y2 - y1) * nenner) % prime
                M2 = (M*M) % prime
                x3 = (M2 - x1 - x2) % prime
                y3 = (M * (x1 - x3) - y1) % prime
                # print("aaaaaa", x1, y1, x2, y2, x3, y3)
                plt.scatter(x3, y3, label="stars", color="red", marker="*", s=30)
                added_point_list.append(Point(x3, y3))
                added_dif_point_list.append(Point(x3, y3))
        # same points
        nenner2 = ((2 * y1)**(prime - 2)) % prime
        M3 = ((3 * (x1**2) + a) * nenner2) % prime
        M4 = (M3*M3) % prime
        xx3 = (M4 - (2 * x1)) % prime
        yy3 = (M3 * (x1 - xx3) - y1) % prime
        # print("bbbbb", x1, y1, xx3, yy3)

        plt.scatter(xx3, yy3, label="stars", color="blue", marker="x", s=60)
        added_point_list.append(Point(xx3, yy3))
        added_same_point_list.append(Point(xx3, yy3))

    print("ALL added points: \n", ', '.join(str(item) for item in added_point_list), "\n", len(added_point_list),
          "points in total")
    print("------------------------------------------------------------------------------------")
    print("Square added points (blue crosses): \n",
          ', '.join(str(item) for item in added_same_point_list), "\n", len(added_same_point_list), "points in total")
    print("------------------------------------------------------------------------------------")
    print("Different added points (red stars): \n",
          ', '.join(str(item) for item in added_dif_point_list), "\n", len(added_dif_point_list), "points in total")
    print("------------------------------------------------------------------------------------")


# end of two point calc
two_points()


# punkt als menge (x,y); ((x,y)+(x,y)); ((x,y)+(x,y)+(x,y)) .... bis y-y = 0 (zyklisch)
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


def mengen(n):
    count = 1
    menge_list.clear()
    menge_list.append(Point(added_same_point_list[n].x, added_same_point_list[n].y))
    mathex = (added_same_point_list[n].x + added_same_point_list[n].x) % prime
    mathey = (added_same_point_list[n].y + added_same_point_list[n].y) % prime
    menge_list.append(Point(mathex, mathey))
    for i in range(1, 500):
        if menge_list[-1].y == menge_list[0].y:
            break
        else:
            mathex = (menge_list[i].x + menge_list[0].x) % prime
            mathey = (menge_list[i].y + menge_list[0].y) % prime
            menge_list.append(Point(mathex, mathey))
            count += 1
    # remove last item because double
    menge_list.pop()
    print("menge", menge_list)
    print("counter", count)
    count_list.append(count)
    # primes(count)   # primfaktorzerlegung; macht nix, wenn count ne prime ist


for i in range(added_same_point_list.__len__()):
    mengen(i)
print("countliste: ", count_list)

kgv = np.lcm.reduce(count_list)
print("kgv von countliste: ", kgv)


def hasse():
    minimum = prime + 1 - (2 * np.sqrt(prime))
    maximum = prime + 1 + (2 * np.sqrt(prime))
    print("Hasse-Intervall von: ", minimum, " ------------ ", prime, " ------------ ", maximum)


hasse()

for i in range(len(xlist)):
    x1 = xlist[i]
    y1 = ylist[i]
    x2 = x1
    y2 = y1
    k = 0
    print((x1, y1), end='')
    x3 = 4711
    y3 = 4711
    while True:
        if x1 != x2:
            nenner = ((x2 - x1) ** (prime - 2)) % prime
            M = ((y2 - y1) * nenner) % prime
            M2 = (M * M) % prime
            x3 = (M2 - x1 - x2) % prime
            y3 = -(M * (x3 - x1) + y1) % prime
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
        if x3 == x1:
            break
        # print(x3 == x1)
        if k > 75:
            break
    print()


# plt.show()

''' TODO:
    - kgv = gruppengröße
    - gruppengröße im bereich hasse intervall
    - testmenge machen
    - in testmenge reinschieben
    - verschieben (2l + 1 zur seite springen (schablone verschieben)
    - id bzw #1 finden
'''
