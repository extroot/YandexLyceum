inp = input()
maxx = ""
minn = ""
while inp != "стоп":
    if len(inp) > len(maxx):
        maxx = inp
    if len(inp) < len(minn) or minn == "":
        minn = inp
    inp = input()

for i in minn:
    if i not in maxx:
        print("НЕТ")
        break
else:
    print("ДА")
