st = [0] * 30000
now = 0
for x in input():
    if x == '>':
        now += 1
        if now == 30000:
            now = 0
    elif x == '<':
        now -= 1
        if now == -1:
            now = 29999
    elif x == '+':
        st[now] = st[now] + 1 if st[now] != 255 else 0
    elif x == '-':
        st[now] = st[now] - 1 if st[now] != 0 else 255
    else:
        print(st[now])
