
"""
def test(a, b):
    return len(a) == len(b) and all(t in b for t in a)


st = sorted(set([input().lower() for _ in range(int(input()))]))
bad = []
for i in range(len(st)):
    s = [st[i]]
    for j in range(i + 1, len(st)):
        if st[j] not in bad and test(st[i], st[j]):
            s.append(st[j])
            bad.append(st[j])
        elif st[j] in bad:
            del(bad[bad.index(st[j])])
    if len(s) > 1:
        print(*s)
11
окорок
петлей
Плетей
рококо
теплей
Тишь
ТОМНО
тонко
тонок
тоном
шить
"""

"""
d = dict()
for _ in range(int(input())):
    inp = input().lower()
    s = "".join(sorted(inp))
    if s in d and inp not in d[s]:
        d[s].append(inp)
    else:
        d[s] = [inp]
for x in d:
    print(*d[x])
"""

d = dict()
for _ in range(int(input())):
    inp = input().lower()
    s = "".join(sorted(inp))
    if s in d and inp not in d[s]:
        d[s].append(inp)
    elif s in d and inp in d[s]:
        pass
    else:
        d[s] = [inp]

v = list(d.items())
v.sort(key=lambda x: x[1])
for y in v:
    print(*y[1])
