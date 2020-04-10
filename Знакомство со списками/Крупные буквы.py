a = [" * ",
     "* *",
     "***",
     "* *",
     "* *"]

b = ["** ",
     "* *",
     "** ",
     "* *",
     "** "]

c = [" * ",
     "* *",
     "*  ",
     "* *",
     " * "]

inp = input()
for n in range(5):
    for i in inp:
        if i == 'A':
            print(a[n], end="  ")
        elif i == 'B':
            print(b[n], end="  ")
        else:
            print(c[n], end="  ")
    print()
