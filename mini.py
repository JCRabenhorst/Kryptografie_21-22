import numpy as np

prime = 13
m = 4
n = (m**(prime-2)) % prime
v = (n * m) % prime
print(n, m, v)
