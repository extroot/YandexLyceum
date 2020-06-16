f = True
for i in input():
    if f:
        f = False
        print(ord(i), end="")
        continue
    print(',', ord(i), end="")
