from random import random as rd

a = 100
limit_Nmax = 1e7
limit_a = 1e6
i = 0
n_in_circ = 0
Nmax = a
while a < limit_a:
    Nmax = a
    while Nmax <= limit_Nmax:
        n_in_circ = 0
        i = 0
        while i < Nmax:
            x = (rd() % (a * 1000)) / 1000
            y = (rd() % (a * 1000)) / 1000
            if y * y <= (a / 2) * (a / 2) - x * x:
                n_in_circ += 1
            i += 1
        Pi = (n_in_circ / Nmax) * 4
        Nmax *= 2
        print(a, Nmax, Pi)
    a *= 2
