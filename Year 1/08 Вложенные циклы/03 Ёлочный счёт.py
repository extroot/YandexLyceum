n = int(input())

c = 1
i = 1
while i <= n:
    for _ in range(c):
        print(i, end=" ")
        i += 1
        if i > n:
            break
    c += 1
    print()
