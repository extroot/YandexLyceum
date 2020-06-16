import datetime as dt


def before_the_concert(first, second):
    first = list(map(int, first.split('-')))
    second = list(map(int, second.split('-')))
    if dt.date(*first).weekday() in [0, 2]:
        first[2] += 1
    if dt.date(*second).weekday() in [0, 2]:
        second[2] += 1
    return (dt.date(*first) - dt.datetime.now().date()).days, (dt.date(*second) - dt.datetime.now().date()).days
