d = {}
inp = input()
st = ''

for word in inp.split():
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
    st += str(d[word]) + ' '

print(st[:-1])
