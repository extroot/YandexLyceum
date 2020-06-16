st = [int(input()) for _ in range(int(input()))]
a, b = int(input()), int(input())
for x in st:
    if a <= x <= b:
        print(x)
