s = []


def parrot(phrase):
    if phrase in s:
        print(phrase)
    else:
        s.append(phrase)
