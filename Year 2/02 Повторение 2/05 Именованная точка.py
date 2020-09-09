class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.coords = x, y

    def get_x(self):
        return self.coords[0]

    def get_y(self):
        return self.coords[1]

    def get_coords(self):
        return self.coords

    def __str__(self):
        return self.name + str(self.coords)

    def __invert__(self):
        return Point(self.name, self.coords[1], self.coords[0])


if __name__ == "__main__":
    point_A = Point('A', 3, -4)
    print(point_A)
    point_B = ~point_A
    print(point_B)
    print(~Point('O', 0, 0))
