class Selector:
    def __init__(self, nums):
        self.nums = nums
        self.odd = list(filter(lambda x: x % 2 != 0, nums))
        self.even = list(filter(lambda x: x % 2 == 0, nums))

    def get_odds(self):
        return self.odd

    def get_evens(self):
        return self.even
