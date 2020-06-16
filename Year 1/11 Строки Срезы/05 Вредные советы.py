for i in range(int(input())):
    inp = input()
    if inp[:3] in "Не не ":
        inp = inp[3:]
    print(inp)
