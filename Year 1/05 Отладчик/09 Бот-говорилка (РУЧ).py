a = 1
f = True

while f:
    if a == 1:
        answer = input('Какое у вас настроение? ')
        if 'пока' in answer or 'до свидания' in answer:
            print('Пока пока.')
            f = False
        elif 'не' in answer or '?' in answer:
            print('Ничего, скоро всё наладится.')
        elif 'хорош' in answer or 'прекрасн' in answer or 'отличн' in answer:
            print('Отлично, у меня тоже всё хорошо :)')
        elif 'плох' in answer or 'ужасн' in answer or 'отврат' in answer:
            print('Ничего, скоро всё наладится.')
        else:
            print("Я вас не понимаю...")
    elif a == 2:
        answer = input('Как учеба? ')
        if 'пока' in answer or 'до свидания' in answer:
            print('Пока пока.')
            f = False
        elif 'не' in answer or '?' in answer:
            print('Ничего, оценки не главное.')
        elif 'хорош' in answer or 'прекрасн' in answer or 'отличн' in answer:
            print('Отлично, у меня тоже всё хорошо :)')
        elif 'плох' in answer or 'ужасн' in answer or 'отврат' in answer:
            print('Ничего, оценки не главное.')
        else:
            print("Я вас не понимаю...")
    elif a == 3:
        answer = input('Нравится в Яндекс Лицее? ')
        if 'пока' in answer or 'до свидания' in answer:
            print('Пока пока.')
            f = False
        elif 'да' in answer or 'очень' in answer:
            print('Мне тоже')
        elif 'нет' in answer or 'ни капельк' in answer:
            print('Не надо так 。゜゜(´Ｏ) ゜゜。')
        else:
            print("Я вас не понимаю...")
    elif a == 4:
        answer = input('Python или C++? ')
        if 'пока' in answer or 'до свидания' in answer:
            print('Пока пока.')
            f = False
        elif 'c++' in answer or 'с++' in answer or '++' in answer:
            print('.', '_' * 100, '.')
        elif 'python' in answer:
            print('И мне')
        else:
            print("Я вас не понимаю...")

    a += 1
    if a > 5:
        a = 1
