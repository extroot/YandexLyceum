n = int(input())
x = -1 + 2 * n  # Ширина основания вершины
s = -1
for i in range(n):
    s += 2
    print(" " * int((x - s) // 2), "*" * s, " " * int((x - s) // 2), sep="")
