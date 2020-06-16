a, b = int(input()), int(input())
c = input()
for i in range(a):
    print(c, c * (b - 2) * (i == 0 or i == (a - 1)), " " * (b - 2)
          * (i != 0 and i != (a - 1)), c, sep="")
