import sys
data = list(map(str, sys.stdin.read().split('\n')))
st = [(data.index(x) + 1, x.replace('#', '').lstrip()) for x in data if '#' in x]
for i in range(len(st)):
    print(f"Line {st[i][0]}: {st[i][1]}")
