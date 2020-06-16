def ask_password():
    for _ in range(3):
        if input() == "password":
            print("Пароль принят")
            break
    else:
        print("В доступе отказано")
