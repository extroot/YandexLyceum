import sys

d = dict()

for line in sys.stdin:
    inp = line.rstrip('\n').split(" - ")
    if inp[1] in d:
        if inp[0] not in d[inp[1]]:
            d[inp[1]].append(inp[0])
    else:
        d[inp[1]] = [inp[0]]

for name in d.keys():
    print(f"{name}: {'; '.join(d[name])}")

# 1: 2:55
