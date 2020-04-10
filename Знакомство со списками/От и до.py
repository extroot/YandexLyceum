lst = [int(input()) for _ in range(int(input()))]
lst = lst[int(input()) - 1:int(input())]

s = 0
for i in lst:
    s += i

print(s)
