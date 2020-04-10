width = 4
lst = [[x for x in input()] for _ in range(width)]  # Создание матрицы - поля для морского боя.

"""
Example:
xxx.
....
x.xx
x...
"""


def lst_print(st):
    for x in st:
        print(*x)
    print()


def vert(st):
    return [x for x in st[::-1]]


def hor(st):
    return [[y for y in x[::-1]] for x in st]


def tr(st):
    return [[st[j][i] for j in range(width)] for i in range(width)]


lst_print(lst)  # исходное поле
lst_print(vert(lst))  # вертикальное отражение
lst_print(hor(lst))  # горизонтальное отражение
lst_print(tr(lst))  # транспонирование
lst_print(vert(hor(lst)))  # отражение вдоль горизонтали и вертикали одновременно
lst_print(tr(vert(lst)))  # вертикальное отражение, затем транспонирование
lst_print(vert(hor(tr(lst))))  # транспонирование, затем два отражения
