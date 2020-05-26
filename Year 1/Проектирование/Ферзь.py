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


class Queen(Figure):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, 'Q')

    def can_move(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8 and (abs(self.col - col) == abs(self.row - row)
                                              or self.row == row or self.col == col):
            return True
        if 0 <= row < 8 and 0 <= col < 8 and (abs(col - self.col) == abs(row - self.row)
                                              or self.row == row or self.col == col):
            return True
        return False
