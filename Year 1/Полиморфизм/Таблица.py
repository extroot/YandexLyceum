class Table:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def get_value(self, row, col):
        return self.table[row][col] if 0 <= row < self.rows and 0 <= col < self.cols else None

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols
