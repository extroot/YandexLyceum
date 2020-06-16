maxx = 0
inp = input().lower()
for x in inp:
    if inp.count(x) > maxx:
        maxx = inp.count(x)
print(maxx)
