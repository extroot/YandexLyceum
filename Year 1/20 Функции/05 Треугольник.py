def triangle(l1, l2, l3):
    if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
        print("Это треугольник")
    else:
        print("Это не треугольник")


if __name__ == "__main__":
    triangle(int(input()), int(input()), int(input()))
