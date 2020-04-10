d = {}


def get_transactions(t):
    if t == "print_it":
        for x in d.items():
            print(len(d[x[0]]), x[0], sum(d[x[0]]))
        return
    type, mon = t.split('-')[1].split(':')
    if type in d:
        d[type].append(int(mon))
    else:
        d[type] = [int(mon)]
    