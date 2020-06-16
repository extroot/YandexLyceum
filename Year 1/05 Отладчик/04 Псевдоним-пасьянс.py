n = int(input())
while n > 0:
    inp = int(input())
    if 3 >= inp >= 1 and inp <= n:
        n -= inp
    print(n)
