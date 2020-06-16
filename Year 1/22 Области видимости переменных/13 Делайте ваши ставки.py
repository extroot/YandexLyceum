stack = []


def do_bet(num, bet):
    if num in stack or bet == 0 or num > 10 or num < 1:
        print("Что-то пошло не так, попробуйте еще раз")
    else:
        stack.append(num)
        print(f"Ваша ставка в размере {bet} на лошадь {num} принята")
