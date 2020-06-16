def score(*args):
    global scoring
    if args[0] in "ЯблочкоЗеленое_кольцо":
        return scoring[args[0]]
    else:
        return scoring[args[0]][args[1]]
