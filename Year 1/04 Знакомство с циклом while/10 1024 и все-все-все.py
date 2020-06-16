inp = int(input())
s = 0

while inp > 1:
    if inp % 2 == 0:
        inp /= 2
        s += 1
    else:
        print('НЕТ')
        break
else:
    print(s)
