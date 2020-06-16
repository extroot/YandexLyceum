stack = []
for _ in range(int(input())):
    inp = input()
    if 'последний' in inp:
        stack.append(inp.split('-')[-1][1:-1])
    elif 'Следующий' in inp:
        if len(stack) > 0:
            print(f"Заходит {stack.pop(0)}!")
        else:
            print('В очереди никого нет.')
    else:
        stack.insert(0, inp.split()[-1][:-1])
