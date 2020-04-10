st = {}
for _ in range(int(input())):
    inp = input().split()
    if inp[1] not in st:
        st[inp[1]] = [inp[0]]
    else:
        st[inp[1]].append(inp[0])

for _ in range(int(input())):
    inp = input()
    if inp in st:
        print(*st[inp])
    else:
        print('Нет в телефонной книге')
