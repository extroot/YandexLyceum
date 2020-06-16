lst = [int(input()) for _ in range(int(input()))]

for i in range(len(lst) - 1):
    print(lst[i] + lst[i + 1])