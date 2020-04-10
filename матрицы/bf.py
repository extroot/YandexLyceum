st = [0] * 30000
now = 0
zk = []
inp = input()
i = 0
while i < len(inp):
    x = inp[i]
    if x == '[':
        if st[now] == 0:
            check = 0
            while check != 1:
                i += 1
                if inp[i] == ']':
                    check += 1
                elif inp[i] == '[':
                    check -= 1
        else:
            zk.append(i)
    elif x == ']':
        i = zk.pop() - 1
    elif x == '>':
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
    i += 1
