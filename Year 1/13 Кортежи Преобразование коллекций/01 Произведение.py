a = [int(input()) for _ in range(int(input()))]
inp = int(input())
f = True
if len(set(a)) < 2:
    print("НЕТ")
else:
    for i in range(len(a)):
        for n in range(i + 1, len(a)):
            if a[n] * a[i] == inp:
                print("ДА")
                f = False
                break
        if not f:
            break
    else:
        print("НЕТ")
