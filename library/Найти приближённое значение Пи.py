from random import random as rd
n = 100000
k = 0.0
for i in range(n):
    x = rd()
    y = rd()
    k += x ** 2 + y ** 2 < 1.0

print(4 * k / n)
