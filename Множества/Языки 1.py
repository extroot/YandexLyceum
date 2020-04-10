n = int(input()) + int(input())
n1 = n
se = set()

for _ in range(n):
    el = input()
    if el in se:
        n1 -= 2
    se.add(el)
if n1 <= 0:
    print('NO')
else:
    print(n1)
