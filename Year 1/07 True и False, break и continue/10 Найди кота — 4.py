s = 'НЕТ'
ns = 'МЯУ'
for i in range(int(input())):
    inp = input()
    if 'кот' in inp or 'Кот' in inp:
        if s == 'НЕТ':
            s, ns = ns, s
    if ('пёс' in inp or 'Пёс' in inp) and s == 'МЯУ':
        s, ns = ns, s
print(s)
