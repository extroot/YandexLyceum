import sys

d = dict()

i = 0
for line in sys.stdin:
    line = line.rstrip('\n')
    i += 1
    if i == 1:
        continue
    if line == '':
        i = 0
        continue
    sp = line.split()
    day = int(sp[-1])
    name = " ".join(sp[:-1])

    if day in d and name not in d[day]:
        d[day].append(name)
    elif day not in d:
        d[day] = [name]
for x, y in sorted(list(d.items()), key=lambda x: int(x[0])):
    print(f"{x}: {', '.join(y)}")
