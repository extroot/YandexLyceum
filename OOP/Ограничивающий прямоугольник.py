
class BoundingRectangle:
    def __init__(self):
        self.x = []
        self.y = []

    def add_point(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def bottom_y(self):
        return min(self.y) if len(self.y) else 0

    def top_y(self):
        return max(self.y) if len(self.y) else 0

    def left_x(self):
        return min(self.x) if len(self.x) else 0

    def right_x(self):
        return max(self.x) if len(self.x) else 0

    def width(self):
        return abs(self.left_x() - self.right_x())

    def height(self):
        return abs(self.bottom_y() - self.top_y())
