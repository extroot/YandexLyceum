def late1(now, classes, bus):
    h1, m1 = [int(x) for x in now.split(':')]
    h2, m2 = [int(x) for x in classes.split(':')]

    d = h2 * 60 + m2 - h1 * 60 - m1
    bus = bus[::-1]
    if len(bus) == 1:
        bus.append(0)
    for i in range(len(bus)):
        if d - 20 - bus[i] < 0:
            return f"Выйти через {bus[i - 1] + 5} минут"


def late1(now,classes,bus):
    now = now.split(':')
    now[0],now[-1] = int(now[0]),int(now[-1])
    _now = now[0] * 60 + now[-1]
    classes = classes.split(':')
    classes[0],classes[-1] = int(classes[0]),int(classes[-1])
    _classes = (classes[0] * 60 + classes[-1]) - _now
    _answ = []
    for time in bus:
        if time >= 5 and time <= _classes - 15:
            _answ.append(time)
    if _answ == []:
        return 'Опоздание';
    else:
        return 'Выйти через '+str(max(_answ) - 5)+' минут(ы)';


 