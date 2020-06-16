m, n, k = int(input()), int(input()), int(input())
x = m + n + k
okf = set()
se = set()

for _ in range(x):
    inp = input()
    if inp in se:
        if inp not in okf:
            okf.add(inp)
        else:
            okf.remove(inp)
            se.remove(inp)
    else:
        se.add(inp)

if len(okf) == 0:
    print("NO")
else:
    print(len(okf))
