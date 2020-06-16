n = int(input())
st = [[int(input()) for _ in range(n)] for _ in range(n)]

for _ in range(int(input())):
    x, y = int(input()), int(input())
    st[y][x] = st[y][x] - 8 if st[y][x] - 8 > 0 else 0
    if x > 0:
        st[y][x - 1] = st[y][x - 1] - 4 if st[y][x - 1] - 4 > 0 else 0
    if x < len(st[y]) - 1:
        st[y][x + 1] = st[y][x + 1] - 4 if st[y][x + 1] - 4 > 0 else 0
    if y > 0:
        st[y - 1][x] = st[y - 1][x] - 4 if st[y - 1][x] - 4 > 0 else 0
        if x > 0:
            st[y - 1][x - 1] = st[y - 1][x - 1] - 4 if st[y - 1][x - 1] - 4 > 0 else 0
        if x < len(st[y - 1]) - 1:
            st[y - 1][x + 1] = st[y - 1][x + 1] - 4 if st[y - 1][x + 1] - 4 > 0 else 0
    if y < len(st) - 1:
        st[y + 1][x] = st[y + 1][x] - 4 if st[y + 1][x] - 4 > 0 else 0
        if x > 0:
            st[y + 1][x - 1] = st[y + 1][x - 1] - 4 if st[y + 1][x - 1] - 4 > 0 else 0
        if x < len(st[y + 1]) - 1:
            st[y + 1][x + 1] = st[y + 1][x + 1] - 4 if st[y + 1][x + 1] - 4 > 0 else 0
for x in st:
    print(*x)
