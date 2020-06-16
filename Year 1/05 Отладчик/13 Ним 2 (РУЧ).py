heap1 = int(input("Камней в 1 куче: "))
while heap1 <= 0:
    heap1 = int(input("Неверное значение, попробуйте еще раз: "))
heap2 = int(input("Камней в 2 куче: "))
while heap2 <= 0:
    heap2 = int(input("Неверное значение, попробуйте еще раз: "))

if heap1 > heap2:
    print("ИИ взял", heap1 - heap2)
    heap1 = heap1 - (heap1 - heap2)
    print("Осталось:", heap1, heap2)
elif heap1 < heap2:
    print("ИИ взял", heap2 - heap1)
    heap2 = heap2 - (heap2 - heap1)
    print("Осталось:", heap1, heap2)
else:
    print("ИИ взял 1")
    heap1 -= 1
    print("Осталось:", heap1, heap2)

while heap1 + heap2 != 0:
    selected = int(input("Из какой кучки вы заберёте камни, 1 или 2: "))
    while selected != 2 and selected != 1 or (selected == 2 and heap2 == 0) \
            or (selected == 1 and heap1 == 0):
        selected = int(input("Неверное значение, попробуйте еще раз: "))
    take = int(input("Сколько камней вы возьмёте: "))
    if selected == 2:
        while take > heap2 or take < 1:
            take = int(input("Неверное значение, попробуйте еще раз: "))
        heap2 = heap2 - take
        print(heap1, heap2)
        print("Вы взяли", take, ", осталось:", heap1, heap2)
    elif selected == 1:
        while take > heap1 or take < 1:
            take = int(input("Неверное значение, попробуйте еще раз: "))
        heap1 = heap1 - take
        print(heap1, heap2)
        print("Вы взяли", take, ", осталось:", heap1, heap2)
    if heap1 == heap2 == 0:
        print("Вы победили")
    else:
        if heap1 > heap2:
            print("ИИ взял:", heap1 - heap2)
            heap1 = heap2
            print(heap1, heap2)
        elif heap1 < heap2:
            print("ИИ взял:", heap2 - heap1)
            heap2 = heap1
            print(heap1, heap2)
        else:
            print("ИИ взял 1")
            heap1 -= 1
            print("Осталось:", heap1, heap2)
        if heap1 == heap2 == 0:
            print("Вы проиграли")
