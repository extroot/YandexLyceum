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
