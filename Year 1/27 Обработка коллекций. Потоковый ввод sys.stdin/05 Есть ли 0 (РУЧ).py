import sys
print(any(['0' in x for x in list(map(str.split, sys.stdin))]))
