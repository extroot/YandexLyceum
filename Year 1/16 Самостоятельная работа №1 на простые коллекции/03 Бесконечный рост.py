for _ in range(int(input())):
    fst = [int(i) for i in input().split()]
    minn, maxx = min(fst), max(fst)
    print(minn, maxx)
    gr = (minn + maxx) / 3
    x = []
    for num in input().split():
        if int(num) >= gr:
            x.append(int(num))
    print(*x)
