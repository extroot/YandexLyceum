class Figure:
    def __init__(self, row, col, color, char):
        self.row = row
        self.col = col
        self.color = color
        self.charr = char

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return self.charr

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        return False


class Knight(Figure):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, 'N')

    def can_move(self, row, col):
        if (self.row + 1 == row or self.row - 1 == row) and\
                (self.col + 2 == col or self.col - 2 == col) and 0 <= row < 8 and 0 <= col < 8:
            return True
        if (self.row + 2 == row or self.row - 2 == row) and\
                (self.col + 1 == col or self.col - 1 == col) and 0 <= row < 8 and 0 <= col < 8:
            return True
        return False
