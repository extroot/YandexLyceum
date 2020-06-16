a = [input() for _ in range(int(input()))]
k = int(input())

for _ in range(int(input())):
    n = 0
    s = 0
    for i in range(0, len(a)):
        n += 1
        if n == k:
            n = 0
            del(a[i - s])
            s += 1
for x in a:
    print(x)
