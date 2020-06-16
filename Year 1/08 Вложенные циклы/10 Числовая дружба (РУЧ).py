last = -1
for i in range(10000):
    summ = 0
    for j in range(1, i):
        if i % j == 0:
            summ += j

    summ2 = 0

    for j in range(1, summ):
        if summ % j == 0:
            summ2 += j

    if summ2 == i and last != i and i != summ:
        print(i, summ)
        last = summ
