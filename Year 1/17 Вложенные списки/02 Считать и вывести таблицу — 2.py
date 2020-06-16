n, m = int(input()), int(input())
st = [[input() for _ in range(m)] for _ in range(n)]
for x in st:
    print("\t".join(x))
print()
for k in range(m):
    for x in st:
        print(x[k], end="\t")
    print()
