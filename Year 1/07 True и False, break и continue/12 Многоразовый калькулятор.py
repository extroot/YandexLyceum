while True:
    a = int(input())
    do = input()
    if do == 'x':
        print(a)
        break
    if do == '!':
        if a < 0:
            continue
        s = 1
        for i in range(1, a + 1):
            s *= i
        print(s)
        continue
    b = int(input())
    if do == '+':
        print(a + b)
    elif do == "-":
        print(a - b)
    elif do == '*':
        print(a * b)
    elif do == '/':
        if b == 0:
            continue
        print(a // b)
    elif do == '%':
        if b == 0:
            continue
        print(a % b)
