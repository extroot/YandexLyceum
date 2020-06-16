inp = int(input())
st = [[i for i in input()] for _ in range(inp)]
f = True
for x in st:
    s = '000'
    for y in x:
        s = s[1:] + y
        if s == 'ooo':
            print('o')
            f = False
            break
        elif s == 'xxx':
            print('x')
            f = False
            break
    if not f:
        break
else:
    f = True
    for i in range(inp):
        s = '000'
        for x in st:
            s = s[1:] + x[i]
            if s == 'ooo':
                print('o')
                f = False
                break
            elif s == 'xxx':
                print('x')
                f = False
                break
        if not f:
            break
    else:
        print('-')
