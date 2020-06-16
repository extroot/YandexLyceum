for i in range(2, int(input())):
    d = 2
    while i % d != 0:
        d += 1
    if i == d:
        print(i)
