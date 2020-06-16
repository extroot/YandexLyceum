for _ in range(int(input())):
    inp = input()
    if inp[:4] == '####':
        pass
    elif inp[:2] == '%%':
        print(inp[2:])
    else:
        print(inp)
