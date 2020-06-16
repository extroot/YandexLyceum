pass1 = input()

if len(pass1) < 8:
    print('Короткий!')
elif '123' not in pass1:
    if pass1 == input():
        print('OK')
    else:
        print('Различаются.')
else:
    print('Простой!')
