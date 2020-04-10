с1 = int(input("Камней в 1 куче: "))
с2 = int(input("Камней во 2 куче: "))
с3 = int(input("Камней в 3 куче: "))

nim = с1 ^ с2 ^ с3

if nim > 0:
    if с1 ^ nim < с1:
        dif = с1 - (с1 ^ nim)
        с1 -= dif
        get = с1
        num = 1
    elif с2 ^ nim < с2:
        dif = с2 - (с2 ^ nim)
        с2 -= dif
        get = с2
        num = 2
    else:
        dif = с3 - (с3 ^ nim)
        с3 -= dif
        get = с3
        num = 3
else:
    с1 -= 1
    dif = 1
    num = 1
    get = с1
print("ИИ взял " + str(dif) + " камней из " + str(num) + " кучи, осталось " + str(get) + " камней")
step = 0
while с1 + с2 + с3 > 0:
    step = 2
    num = 0
    while num < 1 or num > 3:
        num = int(input("Из какой кучки вы заберёте камни, 1 или 2 или 3: "))
        if num == 1 and с1 == 0 or num == 2 and с2 == 0 or num == 3 and с3 == 0:
            print("Здесь уже нет камней!")
            num = 0
    con = True
    while con:
        if num == 1:
            get = с1
        elif num == 2:
            get = с2
        else:
            get = с3
        dif = int(input("Сколько камней вы возьмёте: "))
        if 0 < dif <= get:
            if num == 1:
                с1 -= dif
                get = с1
            elif num == 2:
                с2 -= dif
                get = с2
            else:
                с3 -= dif
                get = с3
            print("Вы взяли ", dif, " камней из", num, " кучи, осталось", get, "камней")
            con = False
    if с1 + с2 + с3 > 0:
        step = 1
        nim = с1 ^ с2 ^ с3
        if nim > 0:
            if с1 ^ nim < с1:
                dif = с1 - (с1 ^ nim)
                с1 -= dif
                get = с1
                num = 1
            elif с2 ^ nim < с2:
                dif = с2 - (с2 ^ nim)
                с2 -= dif
                get = с2
                num = 2
            else:
                dif = с3 - (с3 ^ nim)
                с3 -= dif
                get = с3
                num = 3
        else:
            if с1 > 0:
                с1 -= 1
                num = 1
                get = с1
            elif с2 > 0:
                с2 -= 1
                num = 2
                get = с2
            else:
                с3 -= 1
                num = 3
                get = с3
            dif = 1
        print("ИИ взял ", dif, " камней из ", num, " кучи, осталось", get, "камней")
if step == 1:
    print("ИИ победил")
else:
    print("Вы победили")
