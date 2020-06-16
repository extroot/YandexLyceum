out = 0
steps = 0
x1 = 0
y1 = 0
f = True

x = int(input())
y = int(input())

while f:
    if x1 == x and y1 == y:
        f = False
        print(steps)
        if out == 0:
            print('север')
        elif out == 1:
            print('восток')
        elif out == 2:
            print('юг')
        elif out == 3:
            print('запад')
    else:
        inp = input()
        steps += 1
        if inp == 'разворот':
            out += 2
            out = 0 if out == 4 else out
            out = 1 if out == 5 else out

        elif inp == 'налево':
            out -= 1
            if out < 0:
                out = 3
        elif inp == 'направо':
            out += 1
            if out > 3:
                out = 0
        elif inp == 'вперёд':
            move = int(input())
            if out == 0:
                y1 += move
            elif out == 1:
                x1 += move
            elif out == 2:
                y1 -= move
            elif out == 3:
                x1 -= move
