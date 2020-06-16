text = []
# '\,' - просто запята; ',' - разделитель
for _ in range(int(input())):
    inp = input()
    st = []
    s = ""
    for i in range(len(inp)):
        if inp[i] == ',' and (i == 0 or inp[i - 1] != '\\'):
            st.append(s)
            s = ""
        elif inp[i] == '\\' and i != len(inp) - 1 and inp[i + 1] == ',':  # Заменить '\,' на ','
            pass
        else:
            s += inp[i]
    st.append(s)
    text.append(st)
for _ in range(int(input())):
    inp = input().split(',')
    x, y = int(inp[0]), int(inp[1])
    for el in text[x][y].split('\\n'):
        print(el)
