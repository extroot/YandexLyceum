out = set()

for i in range(int(input())):
    if i == 0:
        for _ in range(int(input())):
            out.add(input())
    else:
        xe = set()
        for _ in range(int(input())):
            inp = input()
            if inp in out:
                xe.add(inp)
        out = xe

for i in out:
    print(i)
