st = [input() for i in range(int(input()[1:]))]

for i in range(len(st)):
    out = ''
    for x in st[i]:
        if x == '#':
            break
        out += x
    print(out.rstrip())
