a = [input() for _ in range(int(input()))]

for _ in range(int(input())):
    b = []
    for _ in range(int(input())):
        b.append(a[int(input()) - 1])
    a = b

for x in a:
    print(x)
