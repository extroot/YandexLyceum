"""

     1
   / | \
  П  X   2
        / \
        X  П
Х - хорошая концовка
П - плохая концовка

"""

f = True

while f:
    answer1 = input("""\nВы находись в комнате из которой ведут 3 тоннеля.
Вам нужно выбрать один, в который вы пойдете.
Напишите номер тоннеля в который вы хотите пойти (1-3): """)

    if answer1 == '1':
        print('Вы долго шли по тоннелю, но вдруг, вы случайно наступили'
              ' в кем-то сотавленную ловушку - яму на полу, разбившись об шипы.')
        f = False
    elif answer1 == '2':
        print('Пройдя совсем немного по тоннелю, вы увидели свет и вышли на улицу.')
        f = False
    elif answer1 == '3':
        answer2 = input("""\nВы пришли в комнату из которой ведут 2 тоннеля.
Вам нужно выбрать один, в который вы пойдете, или вернуться назад
Напишите номер тоннеля в который вы хотите пойти (1-2, или 0 - назад): """)
        if answer2 == '1':
            print('Пройдя 50 метров по узкому тоннелю, вы встретели подземную жабу,'
                  ' которая съела вас целиком.')
            f = False
        elif answer2 == '2':
            print('Только вступив в темноту тонеля, вы провалились в'
                  ' небольшою подземную речку, которая вынесла вас на поляну.')
            f = False
        elif answer2 == '0':
            print("\nВы верулись по черному тоннелю в первую комнату.")
        else:
            print('Ответ не предусмотрен')
    else:
        print('Ответ не предусмотрен')