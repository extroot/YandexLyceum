d = {}
n = int(input())
for i in range(1, n):
    st = input().split()
    for j in range(len(st)):
        d[str(i) + str(j)] = st[j]
        d[str(j) + str(i)] = st[j]

stack = []
for i in range(n):
    for j in range(i + 1, n):
        minn = int(d[str(i) + str(j)])
        for x in range(n):
            if x != i and x != j:
                s = int(d[str(i) + str(x)]) + int(d[str(x) + str(j)])
                if s < minn:
                    stack.append([i, j])
                    break

for i in range(len(stack) - 1):
    for j in range(len(stack) - i - 1):
        if stack[j][0] > stack[j + 1][0] or (stack[j][0] == stack[j + 1][0]
                                             and stack[j][1] > stack[j + 1][1]):
            stack[j], stack[j + 1] = stack[j + 1], stack[j]
for x in stack:
    print(*x)
