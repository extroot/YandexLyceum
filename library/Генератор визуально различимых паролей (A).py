from random import sample
st = "qwertyuipasdfghjkzxcvbnm23456789QWERTYUPASDFGHJKLZXCVBNM"


def generate_password(m):
    return "".join(sample(st, k=m))


def main(n, m):
    s = []
    while len(s) < n:
        passwd = generate_password(m)
        if passwd not in s:
            s.append(passwd)
    return s
