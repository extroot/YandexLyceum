def hello(name):
    global query
    if None in query:
        a = query.index(None)
        query[a] = name
        print(f'Здравствуйте, {name}! Подойдите к окошку номер {a + 1}')
    else:
        print(f'Простите, {name}. Все окна заняты')


def search_card(name):
    if name in query:
        if name in base:
            print(f'Ваша карта с номером {base.index(name) + 1} найдена')
        else:
            print('Ваша карта не найдена')
    else:
        print(f'Простите, {name}, дождитесь своей очереди')


def good_bye(name):
    global query
    print(f'До свидания, не болейте, {name}')
    query[query.index(name)] = None
