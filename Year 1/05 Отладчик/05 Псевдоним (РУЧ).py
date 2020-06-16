n = int(input("Введите количество камней в куче: "))
while n > 0:
    xn = n
    if n % 4 == 0:
        x = 2
    else:
        x = n % 4
    n -= x
    print("ИИ взял: ", x)
    print("Камней в куче: ", n)
    if n == 0:
        print("Вы проиграли")
    else:
        x = int(input("Ваш ход: "))
        while x > 3 or x < 1 or x > n:
            x = int(input("Неверное число, попробуйте еще раз: "))
        n -= x
        print("Камней в куче: ", n)
        if n == 0:
            print("Вы выиграли")
