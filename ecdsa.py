import random
import hashlib
from collections import namedtuple


Point = namedtuple("Point", "x y")

#######################################################################################################################
#   Verschlüsseln
#######################################################################################################################

with open('Worte') as f:
    a = f.readlines()

# initialize a string
str1 = ''.join(a)
# encode the string
encoded_str = str1.encode()
# create sha3-256 hash objects
obj_sha3_256 = hashlib.sha3_256(encoded_str)
M = obj_sha3_256.hexdigest()
# print in hexadecimal
print("\nSHA3-256 Hash: ", M)
m = int(M, 16)
print(m)
'''
M = our hashed message
dA = A’s private key
(p,a,b,G,n,h) => domain parameter from elliptic curve
G = Punkt(12, 15)
'''
dA = 4711
G = Point(12, 15)
n = 15
a = 1
b = 5
prime = 19
r = G.x % n


def dsa():
    k = random.randint(1, n - 1)   # bis 14 weil gruppengröße 15 bei uns?
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

mes_list = mes.split(",")
print(mes_list)

if 1 < int(mes_list[1]) and int(mes_list[2]) < (n - 1):
    print("yay")
    sinv = (int(mes_list[2]) ** (n - 2)) % n
    u1 = (sinv * int(mes_list[0])) % n
    u2 = (sinv * int(mes_list[1])) % n
    print("u1", u1, "u2", u2)


else:
    print("Werte nicht im Rahmen")
