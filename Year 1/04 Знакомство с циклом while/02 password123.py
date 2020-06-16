pass1 = input()

if len(pass1) < 8:
    print('Короткий!')
elif pass1 == input():
    print('OK')
else:
    print('Различаются.')
