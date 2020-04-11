class Triangle:
    def __init__(self, a, b, c):
        self.p = a + b + c

    def perimeter(self):
        return self.p


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)
