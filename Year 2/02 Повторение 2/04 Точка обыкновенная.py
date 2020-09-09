class Point:
    def __init__(self, x, y):
        self.coords = x, y

    def get_x(self):
        return self.coords[0]

    def get_y(self):
        return self.coords[1]

    def get_coords(self):
        return self.coords


if __name__ == "__main__":
    point = Point(3, -4)
    print(point.get_x())
    print(point.get_y())
    print(point.get_coords())
