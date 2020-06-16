def eratosthenes(n):
    stack = [x for x in range(2, n + 1)]
    i = 2
    s = ""
    while i != stack[-1]:
        for x in stack:
            if x % i == 0 and x != i:
                s += str(x) + " "
                stack.pop(stack.index(x))
        i = stack[stack.index(i) + 1]
    print(s[:-1])


if __name__ == "__main__":
    eratosthenes(int(input()))
