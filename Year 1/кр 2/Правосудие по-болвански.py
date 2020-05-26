def justice(data, *args, **kwargs):
    for fun, i in args:
        if fun in kwargs:
            data[i] = list(filter(kwargs[fun], data[i]))
    return data

print(*justice(
    [
        [2, 6, -13, 48],
        [1, 1, 2, 3, 5, 8, 13, 21],
        [-12, 5, -3, -2, 7, -7, -3, 8, 15, -17]
    ],
    ('negative', 2),
    ('odd_digits', 1),
    ('first_up', 0),
    ('large', 2),
    large=lambda x: abs(x) > 3,
    negative=lambda x: x < 0,
    odd_digits=lambda x: x % 2
), sep='\n')