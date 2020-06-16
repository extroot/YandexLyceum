inp = float(input())
summ = 0
count = 0

while inp > - 300:
    count += 1
    summ += inp
    inp = float(input())

print(summ / count)
