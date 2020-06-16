class OddEvenSeparator:
    def __init__(self):
        self.od = []
        self.ev = []

    def add_number(self, n):
        if n % 2 == 0:
            self.ev.append(n)
        else:
            self.od.append(n)

    def even(self):
        return self.ev

    def odd(self):
        return self.od
