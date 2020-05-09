class Queue:
    def __init__(self, *lst):
        self.lst = list(map(str, lst))

    def append(self, *el):
        for x in el:
            self.lst.append(str(x))

    def copy(self):
        return Queue(self.lst)

    def next(self):
        return Queue(self.lst[1:])

    def pop(self):
        return self.lst.pop(0) if len(self.lst) else None

    def extend(self, q):
        self.lst += q.lst

    def __add__(self, other):
        return Queue(self.lst + other.lst)

    def __iadd__(self, other):
        self.lst += other.lst

    def __eq__(self, other):
        return self.lst == other.lst

    def __str__(self):
        return f"[{' -> '.join(self.lst)}]"

    def __rshift__(self, other):
        return Queue(self.lst[other:])


def next(qq):
    return qq.copy().next()


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