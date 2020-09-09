import sys

count = 0
for line in sys.stdin:
    line = line.rstrip('\n')
    if 'далек' in line.lower():
        count += 1
print(count)
