friends = {}


def add_friends(name, friend):
    global friends
    if name in friends:
        for fr in friend:
            friends[name].append(fr)
    else:
        friends[name] = friend


def are_friends(n1, n2):
    return n2 in friends[n1]


def print_friends(name):
    print(*sorted(friends[name]))
