stack = [int(input())]

f = input() == "Петя"
for _ in range(int(input())):
    num = stack[-1]
    if f:
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        num += 11
    else:
        num = num * 3 - 2
    f = not f
    stack.append(num)
stack = sorted(stack[1:])
if len(stack) % 2 == 1:
    print(stack[len(stack) // 2])
else:
    print((stack[len(stack) // 2] + stack[len(stack) // 2 - 1]) / 2)
