n, m = int(input()), int(input())
lst = [[input() for _ in range(m)] for _ in range(n)]
print("\t".join(lst[0]))

for x in lst[1:-1]:
    print("\t".join(sorted(x)))

if len(lst) > 1:
    print("\t".join(lst[-1]))
