inp = input()
n = int(input())

if 1 <= n <= len(inp):
    print(inp[n - 1])
else:
    print('ОШИБКА')
