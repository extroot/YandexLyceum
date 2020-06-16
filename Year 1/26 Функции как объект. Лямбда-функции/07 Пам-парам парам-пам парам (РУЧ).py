st = [sum([i.count(x) for x in "уеыаоэяию"]) for i in input().split()]
print("Парам пам-пам" if sum(st) / st[0] == len(st) else "Пам парам")
