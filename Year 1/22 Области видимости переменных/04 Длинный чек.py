stack = []
s, c, n = 0, 0, 1


def add_item(a, b):
    global stack, s, c
    stack.append(f"{a} - {b}")
    s += b
    c += 1


def print_receipt():
    global stack, s, c, n
    if c != 0:
        print(f"Чек {n}. Всего предметов: {c}")
        for x in stack:
            print(x)
        print(f"Итого: {s}")
        print('-----')
    else:
        n -= 1
    stack = []
    s, c, = 0, 0
    n += 1
