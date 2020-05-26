a = int(input())
b = int(input())

angl = set()
nem = set()

for _ in range(a):
    angl.add(input())
for _ in range(b):
    nem.add(input())

ors = angl ^ nem
if len(ors) == 0:
    print("NO")
else:
    print(len(ors))
