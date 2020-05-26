text = ' '.join([input().lower() for _ in range(int(input()))])
for x in ",.?!;:":
    text = text.replace(x, '')

d = {}
for x in text.split():
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(i[0].capitalize())
