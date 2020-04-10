lst = [input() for _ in range(int(input()))]
lst2 = [input() for _ in range(int(input()))]

for i in lst:
    for n in lst2:
        if n not in i:
            break
    else:
        print(i)
