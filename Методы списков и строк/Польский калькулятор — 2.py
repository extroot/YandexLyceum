import math
stack = []
for x in input().split():
    if x == '+':
        a, b = stack.pop(-1), stack.pop(-1)
        stack.append(a + b)
    elif x == '-':
        a, b = stack.pop(-1), stack.pop(-1)
        stack.append(b - a)
    elif x == '*':
        a, b = stack.pop(-1), stack.pop(-1)
        stack.append(a * b)
    elif x == '/':
        a, b = stack.pop(-1), stack.pop(-1)
        stack.append(b // a)
    elif x == '~':
        stack.append(stack.pop(-1) * -1)
    elif x == '#':
        a = stack.pop(-1)
        stack.append(a)
        stack.append(a)
    elif x == '@':
        a, b, c = stack.pop(-1), stack.pop(-1), stack.pop(-1)
        stack.append(b)
        stack.append(a)
        stack.append(c)
    elif x == '!':
        stack.append(math.factorial(stack.pop(-1)))
    else:
        stack.append(int(x))

print(stack[0])
