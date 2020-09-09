d = dict()

for _ in range(int(input())):
    name = input()[:-12]
    if name[-1].isdigit():
        name = name[:-1]
    d[name] = d.get(name, 0) + 1

for _ in range(int(input())):
    inp = input()
    d[inp] = d.get(inp, 0) + 1
    print(f"{inp}{d[inp] - 1 if d[inp] - 1 != 0 else ''}@untitled.py")
