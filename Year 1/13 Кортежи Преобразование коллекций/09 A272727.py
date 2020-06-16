a = [0, 1, 0, 3, 0, 3, 0]
inp = int(input())

for _ in range(inp - 7):
    s = 0
    for i in range(len(a)):
        if a[i] == a[-1::-1][i]:
            s += 1
    a.append(s)

for i in range(inp):
    print(a[i])
