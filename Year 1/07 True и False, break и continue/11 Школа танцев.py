stop = int(input())
s = 0
c = 0
while True:
    if s >= stop:
        print('На сегодня хватит.')
        break
    if input() != "раз":
        print('Правильных отсчётов было ', c, ', но теперь вы ошиблись.', sep="")
        s += 1
        c = 0
        continue
    c += 1
    if input() != "два":
        print('Правильных отсчётов было ', c, ', но теперь вы ошиблись.', sep="")
        s += 1
        c = 0
        continue
    c += 1
    if input() != "три":
        print('Правильных отсчётов было ', c, ', но теперь вы ошиблись.', sep="")
        s += 1
        c = 0
        continue
    c += 1
    if input() != "четыре":
        print('Правильных отсчётов было ', c, ', но теперь вы ошиблись.', sep="")
        s += 1
        c = 0
        continue
    c += 1
