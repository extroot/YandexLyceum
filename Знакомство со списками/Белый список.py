lst = [input() for _ in range(int(input()))]
lst2 = [input() for _ in range(int(input()))]

for i in lst2:
    if i in lst:
        print(i)
