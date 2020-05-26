WHITE = 1
BLACK = 2


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        # Пешка белого цвета в клетке E2.

    def current_player_color(self):
        return self.color

    def is_under_attack(self, row, col, color):
        for r in self.field:
            for piece in r:
                if piece is None:
                    continue
                if piece.color != color:
                    continue
                if piece.can_move(row, col):
                    return True
        return False

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True


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


class Bishop(Figure):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, 'B')

    def can_move(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8 and abs(self.col - col) == abs(self.row - row):
            return True
        if 0 <= row < 8 and 0 <= col < 8 and abs(col - self.col) == abs(row - self.row):
            return True
        return False


class Pawn:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if self.col != col:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if self.row + direction == row:
            return True

        # ход на 2 клетки из начального положения
        if self.row == start_row and self.row + 2 * direction == row:
            return True
        return False


class Rook:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'R'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if self.row != row and self.col != col:
            return False
        return True
