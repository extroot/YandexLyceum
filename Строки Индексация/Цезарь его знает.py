n = int(input())
s = ""
for i in input():
    f = False
    if ord(i) < ord('A') or ord(i) > ord('я'):
        s += i
        continue
    if ord('А') <= ord(i) <= ord('Я'):
        f = True
    i = i.lower()
    if ord(i) + n > ord('я'):
        up = chr(ord('а') + (ord(i) + n) - ord('я') - 1)
    else:
        up = chr(ord(i) + n)
    if f:
        s += up.upper()
    else:
        s += up
print(s)