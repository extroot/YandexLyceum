n = int(input())
f1, f2, f3 = 1, 1, 1
print(f1, end=" ")
for _ in range(n - 1):
    print(f2, end=" ")
    f1, f2, f3 = f2, f3, f1 + f2 + f3
