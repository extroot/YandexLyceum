def palindrome(s):
    s = s.replace(' ', '')
    return "Палиндром" if s.lower()[len(s) // 2 if len(s) % 2 == 0
                                    else len(s) // 2 + 1:][::-1] == s.lower()[:len(s) // 2]\
        else "Не палиндром"


if __name__ == "__main__":
    print(palindrome(input()))
