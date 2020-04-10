a, b = int(input()), int(input())
home = set()
for _ in range(a):
    home.add(input())

for _ in range(b):
    if input() in home:
        print("YES")
    else:
        print("NO")
