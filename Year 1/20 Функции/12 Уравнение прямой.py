def equation(a, b):
    a, b = a.split(';'), b.split(';')
    x1, y1 = float(a[0]), float(a[1])
    x2, y2 = float(b[0]), float(b[1])

    if x1 - x2 != 0:
        k = (y1 - y2) / (x1 - x2)
        c = y2 - k * x2
        if k == 0:
            print(c)
        else:
            print(k, c)
    else:
        print(0.0)


if __name__ == "__main__":
    equation(input(), input())
