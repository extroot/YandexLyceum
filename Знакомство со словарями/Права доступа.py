st = [input() for _ in range(int(input()))]

for _ in range(int(input())):
    inp = input()
    if inp in st:
        print('YES')
        continue
    inp2 = inp.split('/')[1:]
    x = '/' + inp2[0]
    i = 1
    while x != inp:
        if x in st:
            print('YES')
            break
        x += '/' + inp2[i]
        i += 1
    else:
        print('NO')
