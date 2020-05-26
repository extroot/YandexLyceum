max_len = int(input())
for i in range(int(input())):
    inp = input()
    if len(inp) > max_len:
        inp = inp[:max_len - 3] + "..."
    print(inp)
