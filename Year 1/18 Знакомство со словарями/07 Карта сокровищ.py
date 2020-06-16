st = [[i for i in input().split()] for _ in range(int(input()))]
d = {}
for x in st:
    a, b = x[0][:-1], x[0][:-1]
    if f'{a} {b}' not in d:
        d[f'{a} {b}'] = 1
    else:
        d[f'{a} {b}'] += 1
print(sorted(list(d.items()), key=lambda x: x[1])[-1][1])
