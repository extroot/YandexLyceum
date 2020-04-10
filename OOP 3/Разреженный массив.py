class SparseArray:
    def __init__(self):
        self.d = {}

    def __setitem__(self, key, value):
        self.d[key] = value

    def __getitem__(self, item):
        return self.d.get(item, 0)
