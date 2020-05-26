
def to_int(st):
    return "1ABCDEFGH".index(st[0].upper()), int(st[1])


def to_str(st):
    return "1ABCDEFGH"[st[0]] + str(st[1])


def possible_turns(cell):
    out = []
    st = [(-1, 2),
          (1, 2),
          (-1, -2),
          (1, -2),
          (-2, 1),
          (-2, -1),
          (2, 1),
          (2, -1)]
    x0, y0 = to_int(cell)
    for x, y in st:
        if 0 < y0 + y < 9 and 0 < x0 + x < 9:
            out.append(to_str((x0 + x, y0 + y)))
    return sorted(out)


if __name__ == "__main__":
    print(possible_turns(input()))
