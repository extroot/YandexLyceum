city1 = input()
city2 = input()

if (city1 == 'Тула' or city2 == 'Пенза') and\
        city1 != city2 and not (city1 == 'Тула' and city2 == 'Пенза'):
    print('ДА')
else:
    print('НЕТ')
