symb = "abcdefghijklmnopqrstuvwxyz1234567890_"
inp = input()

for i in range(len(inp)):
    if inp[i] not in symb:
        print("Неверный символ:", inp[i])
        break
else:
    print("OK")
