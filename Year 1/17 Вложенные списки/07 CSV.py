st = [input().split(',') for _ in range(int(input()))]

for _ in range(int(input())):
    inp = input().split(',')
    print(st[int(inp[0])][int(inp[1])] if len(st[int(inp[0])]) > int(inp[1]) else "")
