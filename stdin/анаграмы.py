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
