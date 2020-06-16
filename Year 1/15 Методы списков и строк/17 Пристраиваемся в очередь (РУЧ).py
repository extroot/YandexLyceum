stack = []
for _ in range(int(input())):
    inp = input()
    if 'в очередь' in inp:
        stack.append(inp.split(' встал')[0])
    elif 'Привет, ' in inp:
        stack.insert(stack.index(inp.split('!')[0][8:]) + 1, inp.split('! ')[1].split(' будет')[0])
    elif 'хватит' in inp:
        stack.pop(stack.index(inp.split(', хватит')[0]))

print('\n'.join(stack))
