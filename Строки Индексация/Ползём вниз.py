spaces = 0
inp = input()
char = inp[0]
st = char

for i in inp[1:]:
    if i == '>':
        st += char
        spaces += 1
    if i == '<':
        st = st[1:] + char
        spaces -= 1
    if i == 'V':
        print(st)
        st = " " * spaces + char

print(st)