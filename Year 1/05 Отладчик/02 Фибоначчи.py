last, now = 1, 1
n = int(input())
while last <= n:
    print(last)
    last, now = now, last + now
