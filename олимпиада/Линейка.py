n, m, k = map(int, input().split())
op = [int(i) for i in input().split()]
st = []
for i in range(n):
    for j in range(m - op[i]):
        st.append([i + 1, False])

for i in range(1, n + 1):
    for j in range(i - 1, i * op[i - 1], i):
        st.insert(j, [i, True])

c = []
for i in range(0, len(st), k):
    if st[i][1]:
        c.append(st[i][0])
d = []
for i in range(1, n + 1):
    d.append(str(c.count(i)))
print(" ".join(d))
