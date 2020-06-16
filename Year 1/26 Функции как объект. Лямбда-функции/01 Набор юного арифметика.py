def arithmetic_operation(ch):
    if ch == '+':
        return lambda a, b: a + b
    if ch == '-':
        return lambda a, b: a - b
    if ch == '/':
        return lambda a, b: a / b
    return lambda a, b: a * b
