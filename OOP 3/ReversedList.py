class ReversedList:
    def __init__(self, lst):
        self.__lst = lst[::-1]

    def __getitem__(self, key):
        return self.__lst[key]

    def __len__(self):
        return len(self.__lst)
