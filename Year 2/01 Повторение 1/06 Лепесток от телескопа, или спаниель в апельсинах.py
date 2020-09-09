import sys

lst = []
source = input()
for line in sys.stdin:
    line = line.rstrip('\n')
    for x in line:
        if x not in source or line.count(x) > source.count(x):
            break
    else:
        lst.append(line)
print(len(lst))
for x in lst:
    print(x)
