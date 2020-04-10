n, m = int(input()), int(input())

f = True

for _ in range(n):
    inp = input()
    if f:
        print(inp[::2])
    f = not f
