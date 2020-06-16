num = input()
a1 = num[0]
a2 = num[1]
a3 = num[2]

if a1 == a2 and a1 == a3:
    print('В числе все цифры одинаковые')
elif (a1 == a2 and a1 != a3) or (a1 == a3 and a1 != a2) or (a2 == a3 and a2 != a1):
    print('В числе две одинаковые цифры')
else:
    print('ОК')
