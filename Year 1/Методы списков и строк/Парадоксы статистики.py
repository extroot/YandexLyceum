def med(a):
    if len(a) % 2 == 1:
        return a[len(a) // 2]
    else:
        return (a[len(a) // 2] + a[len(a) // 2 - 1]) / 2


def mod(a):
    maxx = 0
    maxxc = 0
    for x in a:
        if a.count(x) > maxx:
            maxx = a.count(x)
            maxxc = x
    return maxxc


lst = [sorted([int(i) for i in input().split()]) for _ in range(int(input()))]
a_med = []
a_mod = []
for x in lst:
    a_med.append(med(x))
    a_mod.append(mod(x))
print(*a_med)
print(*a_mod)
a_med.sort()
print(med(a_med))
print(mod(a_mod))
full = []
for x in lst:
    for j in x:
        full.append(j)
full.sort()
print(med(full))
print(mod(full))
