import datetime as dt

date = dt.datetime.now()
dn = dt.timedelta(days=int(input()))
print((date + dn).day, (date + dn).month)
