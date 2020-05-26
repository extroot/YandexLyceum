# import timeit


def foo(n):
    lst = set()
    for i in range(2, n):
        for j in range(2, 1 + int(i ** 0.5)):
            if not i % j:
                break
        else:
            lst.add(i)
    return lst


def main():
    sample = foo(b)
    out = []
    rang = set([x for x in range(a, b + 1)]).difference(sample).difference({0, 1})
    for x in rang:
        for j in sample:
            if j / 2 > x:
                out.append(str(x))
                break
            if x % j == 0 and (x // j) % j == 0:
                break
        else:
            out.append(str(x))

    if len(out) == 0:
        print('NO')
    else:
        print(*out)


a, b = tuple(sorted([int(x) for x in input().split()]))
# print(timeit.timeit("main()", setup="from __main__ import main", number=1))
main()
