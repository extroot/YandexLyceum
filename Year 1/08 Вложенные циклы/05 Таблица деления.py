column = int(input())
for i in range(1, int(input()) + 1):
    for j in range(1, column + 1):
        print(j / i, end=" ")
    print()
