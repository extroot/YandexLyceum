st = []
inp = input()
while inp != '':
    st.append([int(i) % 2 == 0 for i in inp.split()])
    inp = input()
for _ in range(int(input())):
    st2 = []
    stf = []
    inp = input()
    while inp != '':
        st2.append([(int(i) % 2 == 1) for i in inp.split()])
        stf.append(i for i in inp.split())
        inp = input()
    if st2 == st:
        for x in stf:
            print(*x)
        break
else:
    print("Таких лабиринтов нет")
