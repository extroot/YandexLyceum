d = {}
for _ in range(int(input())):
    inp = input()
    d[inp.split()[0]] = inp[inp.index(" ") + 1:]

for _ in range(int(input())):
    print(d.get(input(), 'Нет в словаре'))
