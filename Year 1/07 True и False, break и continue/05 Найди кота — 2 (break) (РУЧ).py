i = 1
while True:
    inp = input()
    if inp == "СТОП":
        print(-1)
        break
    if 'кот' in inp or 'Кот' in inp:
        print(i)
        break
    i += 1
