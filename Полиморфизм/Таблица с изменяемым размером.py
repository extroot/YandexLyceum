class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.lst = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self.lst[row][col]

    def set_value(self, row, col, value):
        self.lst[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def rotate(self):
        lst2 = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                lst2[j][i] = self.lst[i][j]
        print(lst2)
        for i in range(5):
            for j in range(3):
                print(lst2[i][j], end=" ")
            print()


tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)

for i in range(3):
    for j in range(5):
        print(tab.get_value(i, j), end=" ")
    print()
tab.rotate()