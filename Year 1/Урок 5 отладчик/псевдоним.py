n = int(input("Введите количество камней в куче: "))
while n > 0:
    if n % 4 == 0:
        n -= 3
    else:
        n -= n % 4
    print("Камней в куче: ", n)
    if n == 0:
        print("Вы проиграли")
    else:
        x = int(input("Ваш ход: "))
        while x > 3 or x < 1:
            x = int(input("Неверное число, попробуйте еще раз: "))
        n -= x
        print("Камней в куче: ", n)
        if n == 0:
            print("Вы выиграли")
