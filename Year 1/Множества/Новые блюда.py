start = set()
for _ in range(int(input())):
    start.add(input())

for _ in range(int(input())):
    for _ in range(int(input())):
        inp = input()
        if inp in start:
            start.remove(inp)

for i in start:
    print(i)
