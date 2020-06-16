class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def isect(self, a0, a1, b0, b1):
        if a1 <= b0 or b1 <= a0:
            return None
        elif a0 <= b0 <= b1 <= a1:
            return (b0, b1)
        elif b0 <= a0 <= a1 <= b1:
            return (a0, a1)
        elif a0 <= b0 <= a1:
            return (b0, a1)
        elif b0 <= a0 <= b1:
            return (a0, b1)
        else:
            return 0

    def intersection(self, other):
        x_interval = self.isect(self.x, self.x + self.w, other.x, other.x + other.w)
        y_interval = self.isect(self.y, self.y + self.h, other.y, other.y + other.h)
        if x_interval is None or y_interval is None:
            return None
        x0, x1 = x_interval
        y0, y1 = y_interval

        return Rectangle(x0, y0, x1 - x0, y1 - y0)
