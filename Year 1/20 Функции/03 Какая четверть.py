def quarter(x, y):
    if x < 0 < y:
        print("II четверть")
    elif x > 0 and y > 0:
        print("I четверть")
    elif x < 0 and y < 0:
        print("III четверть")
    else:
        print("IV четверть")


if __name__ == "__main__":
    quarter(float(input()), float(input()))
