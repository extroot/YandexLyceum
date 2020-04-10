class MinMaxWordFinder:
    def __init__(self):
        self.d = {}

    def add_sentence(self, s):
        for x in s.split():
            if len(x) in self.d:
                self.d[len(x)].append(x)
            else:
                self.d[len(x)] = [x]

    def shortest_words(self):
        return sorted(self.d[min(self.d.keys())] if len(self.d.keys()) else [])

    def longest_words(self):
        return sorted(set(self.d[max(self.d.keys())]) if len(self.d.keys()) else [])
