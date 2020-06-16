n1 = int(input())
n2 = int(input())
n3 = int(input())

while n1 > 0 or n2 > 0 or n3 > 0:
    inp = int(input())
    if inp == 1:
        n1 -= int(input())
    elif inp == 2:
        n2 -= int(input())
    else:
        n3 -= int(input())
    print(n1, n2, n3)
