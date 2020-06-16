def check_pin(pin):
    a, b, c = pin.split('-')
    return "Корректен" if prime(int(a)) and palindrome(b) and check2(int(c)) else "Некорректен"


def palindrome(s):
    s = s.replace(' ', '')
    return s.lower()[len(s) // 2 if len(s) % 2 == 0 else
                     len(s) // 2 + 1:][::-1] == s.lower()[:len(s) // 2]


def prime(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def check2(n):
    return not bool(n & (n - 1))
