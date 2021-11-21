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
primes: 
13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 
113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 
241, 251, 257, 263, 269, 271, 277, 281, ...
i ONLY make the positive points, NO NEGATIVE POINTS, so some points are missing

------------------------------------------------------------------------------------------------------------------------

Graphic point help:
- normal points = green
- square added points = black
- square added points equal normal point = yellow
- different added points = orange
- different added points equal normal points = cyan

------------------------------------------------------------------------------------------------------------------------

At prime 127 (took 2 minutes):
- scatterplot points (primed points): 126 points in total 
- All added points: 7688 points in total, with 64 points equal to scatterplot points
- Square added points: 3844 points in total, with 0 points equal to scatterplot points
- different added points: 3844 points in total, with 64 points equal to scatterplot points
- counter für menge, stelle 9: counter 3843
- primzahlzerlegung: [3, 3, 7, 61]
'''

#################
a = 4           #
b = 7           # box of things to set
prime = 13      #
#################

squares = []
xlist = []
ylist = []
x3list = []
yclist = []
point_list = []
added_point_list = []
col_added_point_list = []
added_same_point_list = []
added_dif_point_list = []
added_point_equal_existing_point_list = []
menge_list = []
count_list = []
new_count_list = []


# making the list of squares
for x in range(1, prime):
    x2 = (x ** 2) % prime
    squares.append(x2)

# checking if x result has square counterpart
if (((b ** 2) / 4) + ((a ** 3) / 27)) % prime != 0:
    for x in range(1, prime):
        y = ((x ** 3) + (a * x) + b) % prime
        if y in squares:
            indices = [i for i, m in enumerate(squares) if m == y]
            for w in range(indices.__len__()):
                point_list.append(Point(x, indices[w] + 1))

            xlist.append(x)
            ylist.append(squares.index(y) + 1)

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
            dxdx = ((3 * (xlist[u]) + a) / (2 * (ylist[z]))) % prime
            xx3 = ((dxdx ** 2) - (2 * (xlist[u]))) % prime
            yyc = -(dxdx * (xx3 - xlist[u]) + ylist[z]) % prime
            plt.scatter(xx3, yyc, label="stars", color="black",
                        marker="*", s=30)
            added_point_list.append(Point(xx3, yyc))
            added_same_point_list.append(Point(xx3, yyc))

            # check if added point equals existing scatterplot point
            for i in range(point_list.__len__()):
                if point_list[i].x == xx3:
                    if point_list[i].y == yyc:
                        plt.scatter(xx3, yyc, label="stars", color="yellow",
                                    marker="*", s=30)
                        added_point_equal_existing_point_list.append(Point(xx3, yyc))

            dxdy = (ylist[z + 1] - ylist[z]) / (xlist[u + 1] - xlist[u])
            x3 = ((dxdy ** 2) - xlist[u] - xlist[u + 1]) % prime
            yc = -(dxdy * (x3 - xlist[u]) + ylist[z]) % prime
            plt.scatter(x3, yc, label="stars", color="orange",
                        marker="*", s=30)
            added_point_list.append(Point(x3, yc))
            added_dif_point_list.append(Point(x3, yc))
            # check if added point equals existing scatterplot point
            for i in range(point_list.__len__()):
                if point_list[i].x == x3:
                    if point_list[i].y == yc:
                        plt.scatter(x3, yc, label="stars", color="cyan",
                                    marker="*", s=30)
                        added_point_equal_existing_point_list.append(Point(x3, yc))

    # square_added = 0
    # dif_added = 0
    # making my lists look pretty
    '''
    for i in range(len(added_point_list)):
        for j in range(len(added_point_equal_existing_point_list)):
            if added_point_list[i] == added_point_equal_existing_point_list[j]:
                added_point_list[i] = Fore.RED + str(added_point_list[i]) + Fore.RESET
    
    for i in range(len(added_same_point_list)):
        for j in range(len(added_point_equal_existing_point_list)):
            if added_same_point_list[i] == added_point_equal_existing_point_list[j]:
                added_same_point_list[i] = Fore.RED + str(added_same_point_list[i]) + Fore.RESET
                square_added += 1

    for i in range(len(added_dif_point_list)):
        for j in range(len(added_point_equal_existing_point_list)):
            if added_dif_point_list[i] == added_point_equal_existing_point_list[j]:
                added_dif_point_list[i] = Fore.RED + str(added_dif_point_list[i]) + Fore.RESET
                dif_added += 1
    '''

    print("ALL added points, red are the ones where they coincide with existing points: \n",
          ', '.join(str(item) for item in added_point_list), "\n", len(added_point_list), "points in total, with",
          len(added_point_equal_existing_point_list), "points equal to scatterplot points")
    print("------------------------------------------------------------------------------------")
    print("Square added points, red are the ones where they coincide with existing points: \n",
          ', '.join(str(item) for item in added_same_point_list), "\n", len(added_same_point_list), "points in total")
    print("------------------------------------------------------------------------------------")
    print("Different added points, red are the ones where they coincide with existing points: \n",
          ', '.join(str(item) for item in added_dif_point_list), "\n", len(added_dif_point_list), "points in total")
    print("------------------------------------------------------------------------------------")


# end of two point calc
two_points()  # if you want the added points, leave active. if you only want scatterplot, comment out


# punkt als menge (x,y); ((x,y)+(x,y)); ((x,y)+(x,y)+(x,y)) .... bis y-y = 0 (zyklisch)
# added point stelle 9 (x = 8, y = 8)

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
    menge_list.append(Point(added_point_list[n].x, added_point_list[n].y))
    mathex = (added_point_list[n].x + added_point_list[n].x) % prime
    mathey = (added_point_list[n].y + added_point_list[n].y) % prime
    menge_list.append(Point(mathex, mathey))
    for i in range(1, 100):
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


for i in range(1, added_point_list.__len__()):
    mengen(i)
    # tut nicht wie ich will weil floats
print("countliste: ", count_list)

# 100er entfernen
for i in range(count_list.__len__()):
    if count_list[i] != 100:
        new_count_list.append(count_list[i])
print("neue countliste: ", new_count_list)

# kgv ohne die 100er
kgv = np.lcm.reduce(new_count_list)
print("kgv von neuer countliste: ", kgv)


def hasse():
    minimum = prime + 1 - (2 * np.sqrt(prime))
    maximum = prime + 1 + (2 * np.sqrt(prime))
    print("Hasse-Intervall von: ", minimum, " ------------ ", prime, " ------------ ", maximum)


hasse()
plt.show()

''' TODO:
    - kgv = gruppengröße
    - gruppengröße im bereich hasse intervall
    - testmenge machen
    - in testmenge reinschieben
    - verschieben (2l + 1 zur seite springen (schablone verschieben)
    - id bzw #1 finden
'''
