class Polynomial:
    def __init__(self, k):
        self.k = k

    def __call__(self, x):
        s = 0
        for i in range(len(self.k)):
            s += (x ** i) * self.k[i]
        return s

    def __add__(self, other):
        x = self.k[:]
        y = other.k[:]
        x, y = (y, x) if len(y) > len(x) else (x, y)
        for i in range(len(y)):
            x[i] += y[i]
        return Polynomial(x)


poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))