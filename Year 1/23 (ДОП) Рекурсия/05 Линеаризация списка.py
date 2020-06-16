def linear(lst, i=0):
    if i < 5:
        return linear(lst, i + 1)
    for x in lst:
        if type(x) == list:
            j = 0
            for y in linear(x):
                lst.insert(lst.index(x) + 1 + j, y)
                j += 1
            del lst[lst.index(x)]
    return lst
