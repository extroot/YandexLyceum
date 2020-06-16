f = 1

while f:
    pass1 = input()
    pass2 = input()
    if len(pass1) < 8:
        print('Короткий!')
    elif '123' not in pass1:
        if pass1 == pass2:
            print('OK')
            f = 0
        else:
            print('Различаются.')
    else:
        print('Простой!')
