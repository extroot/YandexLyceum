x, y = map(int, input().split())
names = dict()
f = True
for _ in range(x):
    inp = input()
    if inp.lower() in names:
        names[inp.lower()].append(inp)
    else:
        names[inp.lower()] = [inp]

for _ in range(y):
    inp = input().lower()
    s = 0
    for x in inp:
        if x.isdigit():
            s = s * 10 + int(x)

    name = ""
    for i in range(s - 1, len(inp), s):
        name += inp[i]
    if name.lower() in names:
        print(names[name.lower()].pop(0))
        f = False
if f:
    print('NO')
