class Balance:
    def __init__(self):
        self.r = 0
        self.le = 0

    def add_right(self, n):
        self.r += n

    def add_left(self, n):
        self.le += n

    def result(self):
        return '=' if self.le == self.r else 'R' if self.r > self.le else "L"
