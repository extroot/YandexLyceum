inp = float(input())
summ = 0

while inp > 0:
    summ += inp * 0.95 if inp > 1000 else inp
    inp = float(input())

print(summ)
