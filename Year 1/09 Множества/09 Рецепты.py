ings = set()
for _ in range(int(input())):
    ings.add(input())

for _ in range(int(input())):
    i = 0
    name = input()
    inp = int(input())
    for _ in range(inp):
        if input() in ings:
            i += 1
    if i == inp:
        print(name)
