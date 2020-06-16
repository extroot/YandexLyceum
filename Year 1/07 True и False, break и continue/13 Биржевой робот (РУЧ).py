last = 0
now = 0

buy = 0
sell = 0

while True:
    now = int(input())
    if now == 0:
        break
    if last < now and buy == 0 and last != 0:
        buy = now
    elif buy != 0 and sell == 0:
        if now < last:
            sell = now

    last = now

print(buy, sell, sell - buy)
