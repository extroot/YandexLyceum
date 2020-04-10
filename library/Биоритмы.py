import datetime as dt
from math import sin, pi

b_date = [int(i) for i in input().split('.')]
b_date = dt.date(b_date[2], b_date[1], b_date[0])

now_date = [int(i) for i in input().split('.')]
now_date = dt.date(now_date[2], now_date[1], now_date[0])

diff = (now_date - b_date).days
fis = sin((2 * pi * diff) / 23) * 100
em = sin((2 * pi * diff) / 28) * 100
intel = sin((2 * pi * diff) / 33) * 100

print(fis, em, intel, sep='\n')
