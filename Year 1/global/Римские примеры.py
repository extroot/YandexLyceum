def checkio(n):
    result = ''
    for arabic, romain in [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                           (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'),
                           (4, 'IV'), (1, 'I')]:
        result += n // arabic * romain
        n %= arabic
    return result


def roman():
    global one, two, three
    three = one + two
    print(checkio(one), '+', checkio(two), '=', checkio(one + two))
