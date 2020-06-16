for _ in range(int(input())):
    lst = [int(i) for i in input().split()]
    x = []
    last = -1
    while len(lst) > 1:
        if lst[0] >= lst[1] and lst[0] >= lst[-1] and (lst[0] <= last or last == -1):
            last = lst[0]
            x.append(lst.pop(0))
        elif (lst[-1] >= lst[-2] or lst[-1] >= lst[0]) and (lst[-1] <= last or last == -1):
            last = lst[-1]
            x.append(lst.pop(-1))
        else:
            x.clear()
            break
    if len(lst) == 1:
        x.append(lst.pop(0))
    if len(x) > 0:
        print(*x)
    else:
        print('НЕТ')
