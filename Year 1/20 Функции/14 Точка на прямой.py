def line(s, t):
    s, t = s.split("x"), t.split(";")
    k, b = float(s[0]), float(s[1])
    x, y = float(t[0]), float(t[1])
    print(k * x + b == y)


if __name__ == "__main__":
    line(input(), input())
