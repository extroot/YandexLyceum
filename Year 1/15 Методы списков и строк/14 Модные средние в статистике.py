lst = sorted([float(i) for i in input().split()])

maxx = 0
maxxc = ''
for x in lst:
    if lst.count(x) > maxx:
        maxx = lst.count(x)
        maxxc = x

if len(lst) % 2 == 1:
    print(int(lst[len(lst) // 2]), int(maxxc))
else:
    print(int((lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2), int(maxxc))
