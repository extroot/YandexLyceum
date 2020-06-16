n = int(input())
h = 0

for i in range(n):
    b = int(input())
    h_1 = h

    h = b % 256
    b //= 256
    r = b % 256
    b //= 256
    m = b

    if h != (37 * (m + r + h_1) % 256) or h >= 100:
        print(i)
        break
else:
    print('-1')
