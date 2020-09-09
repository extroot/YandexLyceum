menu = dict()
out = []

for _ in range(int(input())):
    inp = input().split('\t')
    menu[inp[0]] = int(inp[1])
input()
inp = input()
z = 0
while inp != '.':
    if inp == '':
        if z != 0:
            out.append(z)
        z = 0
    else:
        inp = inp.split('\t')
        z += menu[inp[0]] * int(inp[1])
    inp = input()
if z != 0:
    out.append(z)
for i in range(len(out)):
    print(f"{i + 1}) {out[i]}")
print(f"Итого: {sum(out)}")
