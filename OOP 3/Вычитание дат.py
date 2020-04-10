import datetime


class Date:
    def __init__(self, m, d):
        self.days = (datetime.date(2019, m, d) - datetime.date(2019, 1, 1)).days + 1

    def __sub__(self, other):
        return self.days - other.days
