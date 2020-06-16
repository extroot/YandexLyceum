def squared():
    for x in range(10, 100, 10):
        for y in range(1, 10):
            if y == 9:
                print((x + y) ** 2)
            else:
                print(str((x + y) ** 2).ljust(4), end=" ")


if __name__ == "__main__":
    squared()
