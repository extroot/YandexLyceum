a = [input() for _ in range(int(input()))]
for i in a:
    print(i)
print()
for i in a:
    if i[-1] in '45':
        print(i)
