s = 0
i = 0
while True:
    inp = int(input())
    if inp == 0:
        break
    s += inp
    i += 1
    if s == 10:
        print(i)
        break
