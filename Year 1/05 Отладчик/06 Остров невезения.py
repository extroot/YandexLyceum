d = int(input())
m = int(input())
e = int(input())

if m == 1 or m == 2:
    e -= 1

c = e // 100
m = m - 2 if m > 2 else 10 + m
y = e % 100
print((d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7)
