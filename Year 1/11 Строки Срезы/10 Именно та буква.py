inp = input()
n = int(input()) - 1
char = input()

if len(char) > 1 or n > len(inp) - 1 or n < 0:
    print("ОШИБКА")
elif inp[n] == char:
    print("ДА")
else:
    print("НЕТ")
