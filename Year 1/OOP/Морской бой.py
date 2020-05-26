class SeaMap:
    def __init__(self):
        self.st = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.st[row][col] = '*'
        elif result == 'hit':
            self.st[row][col] = 'x'
        elif result == 'sink':
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        if self.st[i][j] == '.':
                            self.st[i][j] = '*'
            self.st[row][col] = 'x'
            for j in range(len(self.st)):
                if self.st[row][j] == 'x':
                    col = j
                    for i in range(row - 1, row + 2):
                        for k in range(col - 1, col + 2):
                            if 0 <= i < 10 and 0 <= k < 10:
                                if self.st[i][k] == '.':
                                    self.st[i][k] = '*'
            for i in range(len(self.st)):
                if self.st[i][col] == 'x':
                    row = i
                    for j in range(row - 1, row + 2):
                        for k in range(col - 1, col + 2):
                            if 0 <= j < 10 and 0 <= k < 10:
                                if self.st[j][k] == '.':
                                    self.st[j][k] = '*'

    def cell(self, row, col):
        return self.st[row][col]


sm = SeaMap()
sm.shoot(0, 0, 'sink')
sm.shoot(0, 9, 'sink')
sm.shoot(9, 0, 'sink')
sm.shoot(9, 9, 'sink')
sm.shoot(5, 4, 'hit')
sm.shoot(5, 5, 'sink')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()