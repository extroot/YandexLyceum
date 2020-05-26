a = input()
b = input()

if a[-1] == b[0] or (a[-1] == 'ь' and a[-2] == b[0]):
    print("ВЕРНО")
else:
    print("НЕВЕРНО")
