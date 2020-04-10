def password_level(password):
    level = 0
    check = [True, True, True]  # Цифры, нижний регистр, верхний регистр
    if len(password) < 6:
        return "Недопустимый пароль"
    for x in password:
        if x.isdigit() and check[0]:
            check[0] = False
            level += 1
        elif x.islower() and check[1]:
            check[1] = False
            level += 1
        elif x.isupper() and check[2]:
            check[2] = False
            level += 1
    return "Ненадежный пароль" if level == 1 else "Слабый пароль" if level == 2 \
        else "Надежный пароль"
