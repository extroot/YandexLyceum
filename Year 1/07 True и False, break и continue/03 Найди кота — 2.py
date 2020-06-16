s = -1
i = 1
while True:
    inp = input().lower()
    if inp == "стоп":
        print(s)
        break
    if 'кот' in inp and s < 0:
        s = i
    i += 1
