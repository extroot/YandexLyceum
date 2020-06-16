st = []
s = ''
for _ in range(int(input())):
    inp = input()
    while inp != '*':
        s += " " + inp
        inp = input()
    st.append('-'.join(s.split()))
    s = ''

print(', '.join(st[::-1]))
