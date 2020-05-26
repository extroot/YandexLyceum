d = {}
for _ in range(int(input())):
    inp = input().split()
    m = inp[2]
    name = inp[0]
    day = int(inp[1])
    if inp[2] in d:
        if day not in d[m]:
            d[m][day] = [name]
        else:
            d[m][day].append(name)
            d[m][day].sort()
    else:
        d[m] = {day: [name]}
for _ in range(int(input())):
    inp = input()
    if inp in d:
        a = list(d[inp].items())
        a.sort()
        s = ''
        for x, y in a:
            for j in y:
                s += str(j) + ' ' + str(x) + ' '
        print(s[:-1])
    else:
        print()
