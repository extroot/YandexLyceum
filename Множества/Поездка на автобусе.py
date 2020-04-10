a = set()
b = set()
f = 0
while True:
    inp = input()
    if inp == "":
        f += 1
        if f == 2:
            isk = a.intersection(b)
            for el in isk:
                print(el)
            if len(isk) == 0:
                print("EMPTY")
            break
        continue
    if f == 0:
        a.add(int(inp))
    if f == 1:
        b.add(int(inp))
