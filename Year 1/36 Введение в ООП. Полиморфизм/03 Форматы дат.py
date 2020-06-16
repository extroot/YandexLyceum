class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def set_year(self, n):
        self.y = n

    def set_month(self, n):
        self.m = n

    def set_day(self, n):
        self.d = n

    def get_year(self):
        return self.y

    def get_month(self):
        return self.m

    def get_day(self):
        return self.d


class AmericanDate(Date):
    def format(self):
        return ".".join([str(self.m).rjust(2, '0'), str(self.d).rjust(2, '0'), str(self.y)])


class EuropeanDate(Date):
    def format(self):
        return ".".join([str(self.d).rjust(2, '0'), str(self.m).rjust(2, '0'), str(self.y)])
