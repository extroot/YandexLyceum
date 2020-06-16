import sys
data = list(map(int, sys.stdin))
print(sum(data) / len(data) if len(data) > 0 else -1)
