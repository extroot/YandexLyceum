import math


def solve(args):
    if len(args) > 3 or len(args) < 1:
        return []

    if len(args) == 1:
        if args[0] == 0:
            return ["all"]
        else:
            return []

    if len(args) == 2:
        b, c = args
        if b == 0 and c == 0:
            return ["all"]
        if c != 0 and b == 0:
            return []
        return [-c / b]

    a, b, c = args
    if a == b == 0:
        if c == 0:
            return ["all"]
        else:
            return []
    if a == 0:
        if b == 0 and c == 0:
            return ["all"]
        if c != 0 and b == 0:
            return []
        return [-c / b]
    d = b ** 2 - (4 * a * c)
    if d < 0:
        return []
    if d == 0:
        return [-b / (2 * a)]
    if d > 0:
        return [int(f"{(-b + math.sqrt(d)) / (2 * a):g}"), int(f"{(-b - math.sqrt(d)) / (2 * a):g}")]


print(*sorted(solve([int(x) for x in input().split()])))
