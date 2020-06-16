st = [input() for _ in range(int(input()))]
for i in range(len(st)):
    if 'кот' in st[i]:
        print(i + 1, st[i].index('кот') + 1)
