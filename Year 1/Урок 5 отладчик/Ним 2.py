c1 = int(input("Камней в 1 куче: "))
c2 = int(input("Камней в 2 куче: "))
if c1 > c2:
    print("ИИ взял", c1 - c2)
    c1 = c1 - (c1 - c2)
    print("Осталось:", c1, c2)
elif c1 < c2:
    print("ИИ взял", c2 - c1)
    c2 = c2 - (c2 - c1)
    print("Осталось:", c1, c2)
else:
    print("ИИ взял 1")
    c1 -= 1
    print("Осталось:", c1, c2)
while c1 + c2 != 0:
    c3 = int(input("Из какой кучки вы заберёте камни, 1 или 2: "))
    while c3 != 2 and c3 != 1:
        c3 = int(input("Неверное значение, попробуйте еще раз: "))
    c4 = int(input("Сколько камней вы возьмёте: "))
    if c3 == 2:
        while c4 > c2:
            c4 = int(input("Неверное значение, попробуйте еще раз: "))
        c2 = c2 - c4
        print(c1, c2)
        print("Вы взяли", c4, ", осталось:", c1, c2)
    elif c3 == 1:
        while c4 > c1:
            c1 = int(input("Неверное значение, попробуйте еще раз: "))
        c1 = c1 - c4
        print(c1, c2)
        print("Вы взяли", c4, ", осталось:", c1, c2)
    if c1 == c2 == 0:
        print("Вы победили")
    if c1 > c2:
        print("ИИ взял:", c1 - c2)
        c1 = c2
        print(c1, c2)
    elif c1 < c2:
        print("ИИ взял:", c2 - c1)
        c2 = c1
        print(c1, c2)
    else:
        print("ИИ взял 1")
        c1 -= 1
        print("Осталось:", c1, c2)
    if c1 == c2 == 0:
        print("Вы проиграли")