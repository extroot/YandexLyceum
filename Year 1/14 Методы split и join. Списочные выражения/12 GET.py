lst = [(i.split('=')[0], i.split('=')[1]) for i in input().split('?')[1].split('&')]
inp = input()
for a, b in lst:
    if a == inp:
        print(b)
