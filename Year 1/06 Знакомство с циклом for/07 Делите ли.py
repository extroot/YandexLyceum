n = int(input())
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        c += 1
        print(i, end=" ")

if c == 2:
    print("\nПРОСТОЕ")
else:
    print("\nНЕТ")
