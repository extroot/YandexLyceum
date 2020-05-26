t1, t2 = tuple([int(x) for x in input().split()])
p, v, a = tuple([int(x) for x in input().split()])


if v * t1 > p:
    print("Pass")
else:
    t0 = v / a
    s = v * t0 - (a * t0 ** 2) / 2
    print(s, t2 - 1)