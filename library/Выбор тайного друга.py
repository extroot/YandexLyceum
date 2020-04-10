import sys
from random import shuffle

data = list(map(str.strip, sys.stdin))
shuffle(data)
for i in range(len(data) - 1):
    print(data[i], '-', data[i + 1])
print(data[-1], '-', data[0])
