count = int(input())
s = 0.0
n = 0.0

for i in range(count):
    x = float(input())
    s += x
    n += 1
    if x == s / n:
        print(0)
    elif x > s / n:
        print(">")
    else:
        print("<")
