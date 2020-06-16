lst = [[input(), int(input())] for _ in range(int(input()))]
for i in range(len(lst) - 1, -1, -1):
    print(lst[i][0], lst[i][1])
