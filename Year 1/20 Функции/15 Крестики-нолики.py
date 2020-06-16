def tic_tac_toe(field):
    for x in field:
        if x == list('xxx'):
            return print("x win")
        elif x == list('000'):
            return print("0 win")
    for i in range(3):
        s = ""
        for x in field:
            s += x[i]
        if s == 'xxx':
            return print("x win")
        elif s == '000':
            return print("0 win")
    s = field[0][0] + field[1][1] + field[2][2]
    if s == 'xxx':
        return print("x win")
    elif s == '000':
        return print("0 win")
    s = field[0][2] + field[1][1] + field[2][0]
    if s == 'xxx':
        return print("x win")
    elif s == '000':
        return print("0 win")
    print("draw")
