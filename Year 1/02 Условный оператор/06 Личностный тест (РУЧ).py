answer1 = input('Вы любите Python? ')
if answer1 != 'да' and answer1 != 'нет':
    print('Input error')
else:
    answer2 = input('Вы любите Java? ')
    if answer2 != 'да' and answer2 != 'нет':
        print('Input error')
    else:
        if answer1 == 'да' and answer2 == 'да':
            print('Вы двуликий человек!')
        elif answer1 == 'нет' and answer2 == 'да':
            print('Вы обладаете незаурядным умом.')
        elif answer1 == 'да' and answer2 == 'нет':
            print('Вы следуете моде!')
        else:
            print('Вы не программист!')
