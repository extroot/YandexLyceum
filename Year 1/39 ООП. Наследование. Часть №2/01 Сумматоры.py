class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        return sum([self.transform(i) for i in range(1, n + 1)])


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3

