n1 = int(input())
n2 = int(input())

while n1 > 0 or n2 > 0:
    if int(input()) == 1:
        n1 -= int(input())
    else:
        n2 -= int(input())
    print(n1, n2)
