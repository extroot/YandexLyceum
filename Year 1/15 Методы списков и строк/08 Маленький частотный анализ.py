inp = input().lower().replace(' ', '')
maxx = 0
maxxc = ''
for x in inp:
    if inp.count(x) > maxx:
        maxx = inp.count(x)
        maxxc = x
    elif inp.count(x) == maxx:
        maxxc = x if maxxc > x else maxxc
print(maxxc)
