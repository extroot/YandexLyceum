inp = input()
last = ''
c = 0

for i in inp:
    if i != last:
        if c != 0:
            print(c, last)
        last = i
        c = 0
    c += 1

print(c, last)
