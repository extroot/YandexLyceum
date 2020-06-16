inp = input()
minn = 200
maxx = 0
summ = 0

while inp != '!':
    if 150 <= int(inp) <= 190:
        summ += 1
        minn = int(inp) if int(inp) < minn else minn
        maxx = int(inp) if int(inp) > maxx else maxx
    inp = input()

print(summ)
print(minn, maxx)
