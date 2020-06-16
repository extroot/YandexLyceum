def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def get_op_val(op, x):
    if is_digit(op):
        return int(op)
    elif op == 'x':
        return x
    elif op == 'sqrt_fun':
        return x ** 0.5
    return funcs[op].calc(x)


class Function:
    def __init__(self, name, op1, op2, operation):
        self.name = name
        self.op1, self.op2 = op1, op2
        self.operation = operation

    def calc(self, val):
        op = self.operation
        lhs, rhs = get_op_val(self.op1, int(val)), get_op_val(self.op2, int(val))
        if '+' in op:
            return lhs + rhs
        if '-' in op:
            return lhs - rhs
        if '*' in op:
            return lhs * rhs
        if '/' in op:
            return lhs / rhs


funcs = dict()

funcs['x'] = Function('x', 'x', '0', '+')
funcs['sqrt_fun'] = Function('sqrt_fun', 'sqrt_fun', '0', '+')

for i in range(int(input())):
    command = input().split()

    if 'define' in command[0]:
        funcs[command[1]] = Function(command[2],
                                     command[2],
                                     command[4],
                                     command[3])
    elif 'calculate' in command[0]:
        print(' '.join(str(funcs[command[1]].calc(j)) for j in command[2:]))
