def golden_ratio(i):
    lst = [1, 1]
    for _ in range(i - 1):
        lst.append(lst[-1] + lst[-2])
    print(lst[i] / lst[i - 1])


if __name__ == "__main__":
    golden_ratio(int(input()))
