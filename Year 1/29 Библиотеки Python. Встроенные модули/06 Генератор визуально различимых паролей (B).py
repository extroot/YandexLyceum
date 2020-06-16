from random import choices
st = "qwertyuipasdfghjkzxcvbnm23456789QWERTYUPASDFGHJKLZXCVBNM"


def test(word):
    dj, lw, up = 0, 0, 0
    for j in word:
        up += 1 if j.isalpha() and j.isupper() else 0
        lw += 1 if j.isalpha() and j.islower() else 0
        dj += 1 if j.isdigit() else 0
    return dj and lw and up


def generate_password(m):
    s = "".join(choices(st, k=m))
    while not test(s):
        s = "".join(choices(st, k=m))
    return s


def main(n, m):
    s = []
    while len(s) < n:
        passwd = generate_password(m)
        if passwd not in s:
            s.append(passwd)
    return s


print("\n".join(main(100, 10)))
