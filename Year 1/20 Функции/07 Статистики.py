def print_statistics(lst):
    print(len(lst))
    print(sum(lst) / len(lst) if len(lst) > 0 else 0)
    print(min(lst) if len(lst) > 0 else 0)
    print(max(lst) if len(lst) > 0 else 0)
    if len(lst) > 0:
        lst.sort()
        if len(lst) % 2 == 1:
            print(lst[len(lst) // 2])
        else:
            print((lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2)
    else:
        print(0)


if __name__ == "__main__":
    print_statistics([int(i) for i in input().split()])
