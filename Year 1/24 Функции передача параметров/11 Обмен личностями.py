def swap(a, b):
    c = a[:]
    a.clear()
    for x in b:
        a.append(x)
    b.clear()
    for x in c:
        b.append(x)
