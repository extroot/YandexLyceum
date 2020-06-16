import random as rand
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
cash = []


def is_bull(val, lhs, rhs):
    lhs, rhs = list(lhs), list(rhs)
    for i in range(len(rhs)):
        if rhs[i] == lhs[i] == val:
            return True
    return False


def is_cow(val, lhs, rhs):
    return val in lhs and val in rhs and not is_bull(val, rhs, lhs)


def counts(num, trying):
    num, trying = list(num), list(trying)
    cow, bull = 0, 0
    for i in range(len(num)):
        if num[i] == trying[i]:
            bull += 1
            continue
        if num[i] in trying:
            cow += 1
    return cow, bull


def get_num():
    ret = set()
    while len(ret) < 4:
        ret = ret.union(rand.sample(range(1, 10), 4))
    return ''.join(map(lambda x: str(x), ret))


def change_num(_num, trying):
    trying = list(trying)
    num = _num[:]
    count = 0

    while num in cash or count < 10:
        count += 1
        if counts(_num, trying) == (0, 0):
            num = get_num()
            cash.append((num, *counts(num, trying)))
            break

        ret = [i for i in num if not is_bull(i, _num, trying) and not is_cow(i, _num, trying)]
        change = set()

        while len(change) < len(ret):
            change = set(filter(lambda x: x not in list(_num) and x not in ret
                                and x not in list(trying), rand.sample(range(1, 10), len(ret))))

        change = list(change)

        for i in range(len(ret)):
            num = num.replace(ret[i], str(change[i]))

        ret = [i for i in num if is_cow(i, _num, trying)]

        num = list(num)
        if len(ret) == 4:
            rand.shuffle(num)
        else:
            # tmp = {}
            # for i in num:
            #    if is_bull(i, num, trying):
            #       tmp[i] = num.index(i)

            if len(ret) == 2:
                num[num.index(ret[0])], num[num.index(ret[1])] \
                    = num[num.index(ret[1])], num[num.index(ret[0])]
        num = ''.join(num)

    cash.append((num, *counts(num, trying)))

    return num


num = get_num()
cash.append(num)
print("Компьютер загадал число. Отгадайте его:")
cow, bull = morph.parse('корова')[0], morph.parse('бык')[0]
trying = ''

while num != trying:
    trying = input()
    while len(trying) < 4 or list(sorted(list(set(trying)))) != list(sorted(trying)):
        print("Неправильный ввод, попробуйте еще.")
        trying = input()
    ct = counts(num, trying)

    pc = cow.make_agree_with_number(ct[0]).word
    pb = bull.make_agree_with_number(ct[1]).word

    print(f"Не угадали, но у вас {ct[0]} {pc} и {ct[1]} {pb}")
    num = change_num(num, trying)
    trying = ''
    print(f"Дальше!")
