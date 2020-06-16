s = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчш" \
    "щъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя"


def encrypt_caesar(message, shift=3):
    out = ""
    for x in message:
        if x not in s:
            out += x
            continue
        out += s[s.index(x) + shift]
    return out


def decrypt_caesar(message, shift=3):
    out = ""
    for x in message:
        if x not in s:
            out += x
            continue
        out += s[s.index(x) + 32 - shift]
    return out
