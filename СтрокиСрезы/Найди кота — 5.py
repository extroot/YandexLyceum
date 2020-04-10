for n in range(int(input())):
    inp = input()
    for i in range(len(inp)):
        if inp[i:i + 3] == 'кот':
            print(n + 1, i + 1)
            break
