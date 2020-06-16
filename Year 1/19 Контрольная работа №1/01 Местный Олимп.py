g1, g2 = int(input()), int(input())
r1, r2 = int(input()), int(input())
m, o = int(input()), int(input())
p1 = r1 - g2
p2 = m - r2
if p1 >= o or p2 >= o:
    print("Влезет")
else:
    print("Не влезет")
