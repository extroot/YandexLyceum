a = [input() for i in range(int(input()))]
k = int(input())
n = 0
print(a[0])
del a[0]
for i in range(len(a)):
    if len(a) > n + k - 1:
        n += k - 1
        print(a[n])
        del(a[n])
    else:
        n = 0
        if len(a) > n:
            print(a[n])
            del(a[n])
