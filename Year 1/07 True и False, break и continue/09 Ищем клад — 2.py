out = 0
steps = 0
x1 = 0
y1 = 0


x = int(input())
y = int(input())

while True:
    if x1 == x and y1 == y:
        print(steps)
        break
    else:
        inp = input()
        steps += 1
        moves = int(input())
        if inp == "север":
            y1 += moves
        elif inp == "юг":
            y1 -= moves
        elif inp == "запад":
            x1 -= moves
        else:
            x1 += moves