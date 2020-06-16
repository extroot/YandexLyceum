def print_average(lst):
    print(sum(lst) / len(lst) if len(lst) > 0 else 0)


if __name__ == "__main__":
    print_average([int(i) for i in input().split()])
