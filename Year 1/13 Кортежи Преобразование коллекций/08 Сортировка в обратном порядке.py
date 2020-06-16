a = [int(input()) for _ in range(int(input()))]
for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

for x in a[-1::-1]:
    print(x)
