lst = []

for _ in range(int(input())):
    lst.append(tuple(map(int, input().split())))

for n in input().split():
    n = int(n) - 1
    isk = lst.pop(n)
    # (0, 0, 0)
    max_y = (isk[0], isk[1], 0)
    max_x = (isk[0], isk[1], 0)
    for x, y in lst:
        if x == isk[0]:
            r = abs(y - isk[1])  # max(y, isk[1]) - min(y, isk[1])
            if r > max_y[2]:
                max_y = (x, y, r)
            elif r == max_y[2]:
                if y < max_y[1]:
                    max_y = (x, y, r)
        elif y == isk[1]:
            r = abs(x - isk[0])  # r = max(x, isk[0]) - min(x, isk[0])
            if r > max_x[2]:
                max_x = (x, y, r)
            elif r == max_x[2]:
                if x < max_x[0]:
                    max_x = (x, y, r)

    if max_x[2] > max_y[2] or max_x[2] == max_y[2]:
        if isk[0] > max_x[0]:
            lst.insert(n, (isk[0] - 2 * max_x[2], isk[1]))
        else:
            lst.insert(n, (isk[0] + 2 * max_x[2], isk[1]))
    else:
        if isk[1] > max_y[1]:
            lst.insert(n, (isk[0], isk[1] - 2 * max_y[2]))
        else:
            lst.insert(n, (isk[0], isk[1] + 2 * max_y[2]))

inp = input().split()
t1, t2 = lst[int(inp[0]) - 1], lst[int(inp[1]) - 1]
print((max(t1[0], t2[0]) - min(t1[0], t2[0])) * (max(t1[1], t2[1]) - min(t1[1], t2[1])))
