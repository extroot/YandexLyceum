import math
r, pi = 1, 7  # 2pi ->
x0, y0 = 0.75, 0
print(min([(abs(r * math.cos(t) ** 3 - x0) ** 2 + abs(r * math.sin(t) ** 3 - y0) ** 2)
           ** 0.5 for t in range(0, pi)]))

# for t in range(0, pi):
#     x, y = r * math.cos(t) ** 3, r * math.sin(t) ** 3
#     ls = (abs(x - x0) ** 2 + abs(y - y0) ** 2) ** 0.5
#     print(ls)
