n, m = int(input()), int(input())
st = [[input() for _ in range(m)] for _ in range(n)]

for s in st:
    print("\t".join(s))
