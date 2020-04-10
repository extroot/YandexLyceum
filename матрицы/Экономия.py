d = {}
n = int(input())
for i in range(1, n):
    st = input().split()
    for j in range(len(st)):
        d[str(i) + str(j)] = st[j]
        d[str(j) + str(i)] = st[j]
a, b = map(str, input().split())

minn = int(d[a + b])
sat = a
for i in range(n):
    if a + str(i) in d and b + str(i) in d:
        s = int(d[a + str(i)]) + int(d[b + str(i)])
        if s < minn:
            minn = s
            sat = i
print(sat)
