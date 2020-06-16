lst = []
for _ in range(int(input())):
    inp = input()
    if 'лук' not in inp:
        lst.append(inp)
print(', '.join(lst))
