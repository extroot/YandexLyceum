num = float(input())
if num == 0:
    print(1000000.0)
elif abs(num) < 0.000001:
    print(1000000.0)
else:
    print(1 / num)
