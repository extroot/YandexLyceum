st = ['1', '1']
for n in range(int(input())):
    if not n:
        print(1)
        continue
    print(" ".join(st))
    s = []
    for i in range(len(st)):
        if not i:
            s.append('1')
            continue
        s.append(str(int(st[i - 1]) + int(st[i])))
    s.append('1')
    st = s
