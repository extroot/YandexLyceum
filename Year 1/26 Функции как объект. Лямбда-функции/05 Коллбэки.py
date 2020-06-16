def ask_password(login, password, success, failure):
    login2, password2 = login.lower(), password.lower()
    err = "Wrong number of vowels" if sum([password2.count(x) for x in "aeiouy"]) != 3 else ""
    login2, password2 = list(filter(lambda x: x not in "aeiouy", login2)), list(
        filter(lambda x: x not in "aeiouy", password2))
    for i in range(len(login2)):
        if login2[i] != password2[i] or len(login2) != len(password2):
            err = "Wrong consonants" if not err else "Everything is wrong"
            break
    if err:
        failure(login, err)
    else:
        success(login)


def main(login, password):
    ask_password(login, password, lambda lg: print(f"Привет, {lg}!"),
                 lambda lg, err: print(f"Кто-то пытался притвориться пользователем {lg.lower()},"
                                       f" но в пароле допустил ошибку: {err.upper()}."))
