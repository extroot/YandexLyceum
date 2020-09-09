lst = input().split(" -> ")
for _ in range(int(input())):
    ind = lst.index(input())
    print(" -> ".join(lst[ind - 1 if ind - 1 > 0 else 0:ind + 2]))
