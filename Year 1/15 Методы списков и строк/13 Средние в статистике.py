lst = sorted([float(i) for i in input().split()])

summ, count = 0.0, 0.0
for x in lst:
    summ += x
    count += 1
sr = summ / count

if len(lst) % 2 == 1:
    print(sr, lst[len(lst) // 2])
else:
    print(sr, (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2)

