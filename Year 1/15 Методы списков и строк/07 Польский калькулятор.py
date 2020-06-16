stack = []
for x in input().split():
    if x == '+':
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(a + b)
    elif x == '-':
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(b - a)
    elif x == '*':
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(b * a)
    else:
        stack.append(int(x))
print(stack[0])
