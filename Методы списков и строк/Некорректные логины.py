inp = input().split(',')
out = []
maxx = 0
chars = "йцукенгшщзхъфывапролджэёячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮqwert" \
        "yuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_"
for x in inp:
    for char in x:
        if char not in chars:
            maxx = len(x) if len(x) > maxx else maxx
            out.append(x)
            break

out.sort()
for x in out:
    print(x.rjust(maxx, ' '))
