answer1 = input('Какой ОС вы пользуетесь? ')
if answer1 != 'linux' and answer1 != 'windows' and answer1 != 'macos':
    print('Ответ не предусмотрен')
else:
    answer2 = input('Python 2.x или 3.x? ')
    if answer2 != '2' and answer2 != '3':
        print('Ответ не предусмотрен')
    else:
        out = answer1 + answer2
        if out == 'linux2':
            print('Вы не приверженец новых технологий.')
        elif out == 'linux3':
            print('Вы хотите казаться умным.')
        elif out == 'windows2':
            print('Вы обладаете незаурядным умом.')
        elif out == 'windows3':
            print('Вы среднестатистический ученик Яндекс лицея.')
        elif out == 'macos2':
            print('Вы модник который не любит новые технологии.')
        elif out == 'macos3':
            print('Вы следуете моде.')
