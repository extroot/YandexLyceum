pi = 3.14159


def circle_length(r):
    return 2 * r * pi


def circle_area(r):
    return pi * r * r


def main():
    r = float(input())
    print(circle_length(r), circle_area(r))


if __name__ == "__main__":
    main()
