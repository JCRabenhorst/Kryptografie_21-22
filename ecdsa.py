import random
import hashlib
import matplotlib.pyplot as plt
from collections import namedtuple
Point = namedtuple("Point", "x y")

#######################################################################################################################
#   Verschlüsseln
#######################################################################################################################

with open('C:/Users/Julia/Documents/Zimtschnecken.txt') as f:
    a = f.readlines()

# initialize a string
str1 = ''.join(a)
# encode the string
encoded_str = str1.encode()
# create sha3-256 hash objects
obj_sha3_256 = hashlib.sha3_256(encoded_str)
M = obj_sha3_256.hexdigest()
# print in hexadecimal
print("\nSHA3-256 Hash in hexa: ", M)
m = int(M, 16)
print("Hash als int: ", m)
'''
M = our hashed message
(prime,a,b,G,n,h) => domain parameter from elliptic curve
G = Punkt(12, 15) Startpunkt von der Gruppe mit Größe n
'''
dA = 4711           # private key
prime = 19          # prime
a = 1               # a from curve
b = 5               # b from curve
G = Point(12, 15)   # basepoint from group size n
n = 15              # size of group
# h = ?
r = G.x % n


def dif_points(x1, x2, y1, y2):
    nenner = ((x2 - x1) ** (prime - 2)) % prime
    M = ((y2 - y1) * nenner) % prime
    M2 = (M * M) % prime
    x3 = (M2 - x1 - x2) % prime
    y3 = (M * (x1 - x3) - y1) % prime
    plt.scatter(x3, y3, label="stars", color="red", marker="*", s=30)
    return Point(x3, y3)


def same_points(x1, y1):
    nenner2 = ((2 * y1) ** (prime - 2)) % prime
    M3 = ((3 * (x1 ** 2) + a) * nenner2) % prime
    M4 = (M3 * M3) % prime
    x3 = (M4 - (2 * x1)) % prime
    y3 = (M3 * (x1 - x3) - y1) % prime
    plt.scatter(x3, y3, label="stars", color="blue", marker="x", s=60)
    return Point(x3, y3)


def dsa():
    k = random.randint(1, n - 1)   # bis 14 weil gruppengröße 15 bei uns
    kinv = (k**(n - 2)) % n
    s = (kinv * (r * dA + m)) % n
    if s != 0:
        return s
    else:
        return dsa()


s = dsa()
print("r =", r, "s =", s)

mes = str(m) + "," + str(r) + "," + str(s)
print(mes)

#######################################################################################################################
#   Verifikation
#######################################################################################################################
pA = 1111           # public key
print("\nVerifikation")
mes_list = mes.split(",")
print(mes_list)
r1 = int(mes_list[1])
s1 = int(mes_list[2])
mes1 = int(mes_list[0])

if 1 < (r1 and s1) < (n - 1):
    sinv = (int(mes_list[2]) ** (n - 2)) % n
    u1 = (sinv * mes1) % n
    u2 = (sinv * r1) % n
    print("u1", u1, "u2", u2)
else:
    print("Werte nicht im Rahmen")


def chaos(G, n):
    result = Point(-1, -1)
    while n != 0:
        if n & 1:
            result = dif_points(G.x, result.x, G.y, result.y)
        n = n // 2
        G = same_points(G.x, G.y)
    print(G)
    return G


Q = chaos(G, u1)            # + (u2 * pA) wie addier ich das das sind 2 zahlen help
if Q == 0:
    print("Q ist null, also falsch")
v = Q.x % n
if v == r:
    print("Alles richtig, v =", v, "r =", r )
else:
    print("Nicht richtig, v =", v, "r =", r)
