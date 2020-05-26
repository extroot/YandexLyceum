class Queue(list):
    def __init__(self, *lst):
        super().__init__(map(str, lst))

    def __str__(self):
        return f"[{' -> '.join(super().copy())}]"

    def __rshift__(self, other):
        return Queue(*super().copy()[other:])

    def __next__(self):
        return Queue(*super().copy()[1:])

    def __add__(self, other):
        return Queue(*(super().copy() + other.lst()))

    def extend(self, q):
        super().__init__(super().copy() + q.lst())

    def lst(self):
        return super().copy()

    def pop(self):
        if len(super().copy()):
            return super().pop(0)

    def append(self, *el):
        lst = super().copy()
        for x in el:
            lst.append(str(x))
        super().__init__(lst)

    def next(self):
        return Queue(*super().copy()[1:])

    def copy(self):
        return Queue(*super().copy())


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)