pl = [0, 0, 0, 0]

for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    if x == 0 or y == 0:
        print(f"({x}, {y})")
    else:
        if x > 0 and y > 0:
            pl[0] += 1
        elif x < 0 < y:
            pl[1] += 1
        elif x < 0 and y < 0:
            pl[2] += 1
        else:
            pl[3] += 1
print(f"I: {pl[0]}, II: {pl[1]}, III: {pl[2]}, IV: {pl[3]}.")
