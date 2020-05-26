n = int(input())
st = [[]]

for i in range(1, n):
    st += [input().split()]

for i in range(n):
    x = ''
    for k in range(n):
        if k < i:
            x += st[i][k]
        elif k == i:
            x += '0'
        else:
            x += st[k][i]
        x += ' '
    print(x[:-1])
