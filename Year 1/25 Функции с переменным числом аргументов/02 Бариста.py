items = {
    "Эспрессо": [1, 0, 0],
    "Капучино": [1, 3, 0],
    "Маккиато": [2, 1, 0],
    "Кофе по-венски": [1, 0, 2],
    "Латте Маккиато": [1, 2, 1],
    "Кон Панна": [1, 0, 1],
}


def choose_coffee(*args):
    global ingredients
    for x in args:
        need = items[x]
        if ingredients[0] - need[0] >= 0 and ingredients[1] - need[1] >= 0 and ingredients[2] - need[2] >= 0:
            ingredients[0] -= need[0]
            ingredients[1] -= need[1]
            ingredients[2] -= need[2]
            return x
    else:
        return "К сожалению, не можем предложить Вам напиток"
