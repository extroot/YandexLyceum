out = set()
x = 0
se = set()
for _ in range(int(input())):
    inp = input()
    if inp in se:
        x += 1
    elif inp in out:
        x += 2
        se.add(inp)
    else:
        out.add(inp)

print(x)
