maxx = - 1
c = -1

for i in range(int(input())):
    min_f = -1
    for j in range(int(input())):
        z = int(input())
        if min_f == -1:
            min_f = z
        elif z < min_f:
            min_f = z
    if maxx == -1:
        maxx = min_f
        c = i + 1
    elif min_f > maxx:
        maxx = min_f
        c = i + 1
print(c, maxx, sep="\n")
