class TicTacToeBoard:
    def __init__(self):
        self.st = [['-' for _ in range(3)] for _ in range(3)]
        self.x = 1
        self.game = True

    def get_field(self):
        return self.st

    def check_field(self):
        for i in range(3):
            if "".join(self.st[i]) == 'XXX':
                return 'X'
        for i in range(3):
            if "".join(self.st[i]) == '000':
                return '0'
        for i in range(3):
            if self.st[0][i] + self.st[1][i] + self.st[2][i] == 'XXX':
                return 'X'
        for i in range(3):
            if self.st[0][i] + self.st[1][i] + self.st[2][i] == '000':
                return '0'
        if self.st[0][0] + self.st[1][1] + self.st[2][2] == '000':
            return '0'
        if self.st[0][0] + self.st[1][1] + self.st[2][2] == 'XXX':
            return 'X'
        if self.st[0][2] + self.st[1][1] + self.st[2][0] == '000':
            return '0'
        if self.st[0][2] + self.st[1][1] + self.st[2][0] == 'XXX':
            return 'X'

    def new_game(self):
        self.st = [['-' for _ in range(3)] for _ in range(3)]
        self.x = 1
        self.game = True

    def make_move(self, row, col):
        if self.game:
            row, col = row - 1, col - 1
            if self.st[row][col] == '-':
                self.st[row][col] = 'X' if self.x == 1 else '0'
                self.x *= -1
                if self.check_field():
                    self.game = False
                    return f"Победил игрок {self.check_field()}"
                else:
                    return "Продолжаем играть"
            else:
                return f"Клетка {row + 1}, {col + 1} уже занята"
        else:
            return "Игра уже завершена"
