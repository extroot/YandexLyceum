class Cl:
    def __init__(self):
        self.n = []

    def add_number(self, x):
        self.n.append(x)


class MinStat(Cl):
    def result(self):
        return min(self.n) if len(self.n) else None


class MaxStat(Cl):
    def result(self):
        return max(self.n) if len(self.n) else None


class AverageStat(Cl):
    def result(self):
        return sum(self.n) / len(self.n) if len(self.n) else None
