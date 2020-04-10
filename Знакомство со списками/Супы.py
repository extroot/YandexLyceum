lst = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
n = int(input())
i = 0
while i < n:
    for x in lst:
        i += 1
        print(x)
        if i >= n:
            break
