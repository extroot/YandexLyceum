from random import shuffle


def make_bingo():
    s = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]

    for i in range(5):
        x = s[i]
        shuffle(x)
        s[i] = x

    shuffle(s)
    s[2][2] = 0
    return tuple(map(tuple, s))
