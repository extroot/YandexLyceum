inp = input()
n = int(inp[:4].replace(" ", ""))
s = int(inp[4:].replace(" ", ""))

lst = [input() for _ in range(int(n))]
bad = []
ns = 0
n = 1
for i in lst:
    cost = int(i[:7].replace(" ", ""))
    count = int(i[8:12].replace(" ", ""))
    ss = int(i[13:].replace(" ", ""))
    ns += cost * count
    if cost * count != ss:
        bad.append(n)
    n += 1

print(s - ns)
for i in bad:
    print(i, end=" ")
