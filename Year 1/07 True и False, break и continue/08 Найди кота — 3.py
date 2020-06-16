s = -1
c = 0
i = 1
while True:
    inp = input()
    if inp == "СТОП":
        print(c, s)
        break
    if 'кот' in inp or 'Кот' in inp:
        c += 1
        if s < 0:
            s = i
    i += 1
