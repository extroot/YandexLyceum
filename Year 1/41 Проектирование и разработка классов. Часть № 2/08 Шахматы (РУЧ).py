WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def print_board(board):
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(8, 0, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row - 1, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(chr(col + 65), end='    ')
    print()


def main():
    board = Board()
    while True:
        print_board(board)
        print('Команды:')
        print('    exit                     -- выход')
        print('    E2-E4                    -- ход из клетки E2 в E4')
        print('    0-0-0                    -- рокировка в длинную сторону')
        print('    0-0                      -- рокировка в короткую сторону')

        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход чёрных:')
        command = input()
        if command == 'exit':
            break
        if command == '0-0-0':
            board.castling0()
        elif command == '0-0':
            board.castling7()
        else:
            c = list(command.lower())
            if (c[0] >= 'a' and c[0] <= 'h' and c[1] >= '1' and c[1] <= '8' and
                    c[3] >= 'a' and c[3] <= 'h' and c[4] >= '1' and c[4] <= '8'):
                row, col, row1, col1 = ord(c[1]) - 49, ord(c[0]) - 97, ord(c[4]) - 49, ord(c[3]) - 97
                if board.move_piece(row, col, row1, col1):
                    print('Ход успешен')
                else:
                    print('Координаты некорректы! Попробуйте другой ход!')
            else:
                print('Недопустимая команда! Попробуйте еще раз!')


def correct_coords(row, col):
    '''Функция проверяет, что координаты (row, col) лежат
    внутри доски'''
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)

        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(self, row, col, row1, col1):
            return False

        self.field[row][col] = None
        self.field[row1][col1] = piece

        piece.set_moved()
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if self.field[i][j]:
                    if self.field[i][j].get_color() == color and self.field[i][j].can_move(row, col):
                        return True
        return False

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if not isinstance(self.field[row][col], Pawn):
            return False
        if self.field[row1][col1] is not None:
            if not self.field[row][col].can_attack(self, row, col, row1, col1):
                return False
        else:
            if not self.field[row][col].can_move(self, row, col, row1, col1):
                return False
        piece = self.field[row][col]
        self.field[row][col] = None
        if (char == 'Q'):
            self.field[row1][col1] = Queen(piece.get_color())
        elif (char == 'R'):
            self.field[row1][col1] = Rook(piece.get_color())
        elif (char == 'B'):
            self.field[row1][col1] = Bishop(piece.get_color())
        elif (char == 'N'):
            self.field[row1][col1] = Knight(piece.get_color())
        self.field[row1][col1].set_moved()
        self.color = opponent(self.color)
        return True

    def castling0(self):
        if self.color == WHITE:
            row = 0
        else:
            row = 7
        if not isinstance(self.field[row][0], Rook):
            return False
        if not isinstance(self.field[row][4], King):
            return False
        if self.field[row][0].is_moved():
            return False
        if self.field[row][4].is_moved():
            return False
        if (self.field[row][1] is not None or self.field[row][2] is not None or
                self.field[row][3] is not None):
            return False

        self.field[row][3] = self.field[row][0]
        self.field[row][2] = self.field[row][4]
        self.field[row][0] = None
        self.field[row][4] = None
        self.field[row][2].set_moved()
        self.field[row][3].set_moved()
        self.color = opponent(self.color)
        return True

    def castling7(self):
        if self.color == WHITE:
            row = 0
        else:
            row = 7
        if not isinstance(self.field[row][7], Rook):
            return False
        if not isinstance(self.field[row][4], King):
            return False
        if self.field[row][7].is_moved():
            return False
        if self.field[row][4].is_moved():
            return False
        if self.field[row][5] is not None or self.field[row][6] is not None:
            return False

        self.field[row][5] = self.field[row][7]
        self.field[row][6] = self.field[row][4]
        self.field[row][7] = None
        self.field[row][4] = None
        self.field[row][5].set_moved()
        self.field[row][6].set_moved()
        self.color = opponent(self.color)
        return True


class Piece:
    def __init__(self, color):
        self.color = color
        self.moved = False

    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        if board.cell(row1, col1)[1] != ' ':
            if board.get_piece(row1, col1).get_color() == self.color:
                return False
        return True

    def get_color(self):
        return self.color

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def set_moved(self):
        self.moved = True

    def is_moved(self):
        return self.moved


class Pawn(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if col != col1:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if row + direction == row1:
            return True
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False

    def char(self):
        return 'P'

    def can_attack(self, board, row, col, row1, col1):
        if board.cell(row1, col1)[1] == ' ':
            return False
        if board.get_piece(row1, col1).get_color() == self.color:
            return False
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Rook(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if row != row1 and col != col1:
            return False
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False
        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def char(self):
        return 'R'


class Knight(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if not ((abs(row1 - row) == 2 and abs(col1 - col) == 1) or
                (abs(row1 - row) == 1 and abs(col1 - col) == 2)):
            return False
        return True

    def char(self):
        return 'N'


class Bishop(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if not abs(row1 - row) == abs(col1 - col):
            return False
        stepx = 1 if (col1 >= col) else -1
        stepy = 1 if (row1 >= row) else -1
        for i in range(1, abs(row1 - row)):
            if not (board.get_piece(row + i * stepy, col + i * stepx) is None):
                return False
        return True

    def char(self):
        return 'B'


class Queen(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if abs(row1 - row) == abs(col1 - col):
            stepx = 1 if (col1 >= col) else -1
            stepy = 1 if (row1 >= row) else -1
            for i in range(1, abs(row1 - row)):
                if not (board.get_piece(row + i * stepy, col + i * stepx) is None):
                    return False
            return True
        if row == row1 or col == col1:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                if not (board.get_piece(r, col) is None):
                    return False
            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                if not (board.get_piece(row, c) is None):
                    return False
            return True
        return False

    def char(self):
        return 'Q'


class King(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if abs(row - row1) > 1 or abs(col - col1) > 1:
            return False
        return True

    def char(self):
        return 'K'
