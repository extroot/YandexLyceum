d = {}

for _ in range(int(input())):
    inp = input().split()
    if inp[2] not in d:
        d[inp[2]] = [inp[0]]
    else:
        d[inp[2]] += [inp[0]]

for _ in range(int(input())):
    inp = input()
    if inp in d:
        print(*sorted(d[inp]))
    else:
        print()
