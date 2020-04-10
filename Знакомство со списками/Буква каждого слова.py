lst = [input() for _ in range(int(input()))]
inp = int(input()) - 1
for i in lst:
    if len(i) > inp:
        print(i[inp], end="")
