class Point:
    def __init__(self, x, y):
        self.p = (x, y)

    def __eq__(self, other):
        return self.p == other.p
