s, f = 0, 1
for i in range(int(input())):
    s += f * int(input())
    f *= -1
print(s)
