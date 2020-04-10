n = int(input("Введите количество камней в куче: "))
while n > 0:
    i = 0
    if n == 1:
        i = 1
        n -= i
    elif (n - 1) % 4 == 0:
        i = 3
        n -= i
    else:
        i = (n - 1) % 4
        n -= i
    print("Ход ИИ: ", i)
    print("Камней в куче: ", n)
    if n == 0:
        print("Вы выиграли")
    else:
        x = int(input("Ваш ход: "))
        while x > 3 or x < 1 or x > n:
            x = int(input("Неверное число, попробуйте еще раз: "))
        n -= x
        print("Камней в куче: ", n)
        if n == 0:
            print("Вы проиграли")
