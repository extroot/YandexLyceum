lst = [int(i) for i in input().split()]

print('*' * (len(lst) + 2))
print('*', ' ' * len(lst), '*', sep='')
for n in range(max(lst), 0, -1):
    print('*', end='')
    for i in lst:
        print('*' if i - n >= 0 else ' ', end='')
    print('*', end='')
    print()