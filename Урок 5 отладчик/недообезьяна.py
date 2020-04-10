n = int(input())
count = 0
while n != 1:
    if n % 2 == 0:
        n /= 2
    elif n % 2 == 1:
        n -= 1
    count += 1
print(count)
