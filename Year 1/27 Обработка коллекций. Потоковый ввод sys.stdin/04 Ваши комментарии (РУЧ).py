import sys
data = list(map(str.lstrip, sys.stdin))
print(sum(x[0] == '#' if len(x) > 0 else False for x in data))
