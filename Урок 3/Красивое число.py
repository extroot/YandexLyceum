num = input()
a1 = int(num[0])
a2 = int(num[1])
a3 = int(num[2])

if ((min(a1, a2, a3) + max(a1, a2, a3)) / 2) == (a1 + a2 + a3 - max(a1, a2, a3) - min(a1, a2, a3)):
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')
