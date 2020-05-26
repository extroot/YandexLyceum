def diet(lst):
    global food
    lst = lst.split(', ')
    c = 0
    for x in lst:
        if x in food["диетическое"]:
            c += 1
    return "Не ешь столько, По!" if c > len(lst) / 2 else "Так держать, Воин Дракона!"


def diet(lst):
    lst = lst.split(', ')
    c = 0
    for x in lst:
        if x not in food['диетическое']:
            c += 1
    return "Не ешь столько, По!" if float(c) > len(lst) / 2 else "Так держать, Воин Дракона!"
