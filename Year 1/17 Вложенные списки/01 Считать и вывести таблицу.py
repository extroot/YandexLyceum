a, b = int(input()), int(input())
st = [[input() for _ in range(b)] for _ in range(a)]

for s in st:
    print("\t".join(s))
