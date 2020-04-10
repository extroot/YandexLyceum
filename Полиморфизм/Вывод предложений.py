class LeftParagraph:
    def __init__(self, length):
        self.length = length
        self.text = []

    def add_word(self, word):
        if len(self.text) > 0 and len(word) + len(self.text[-1]) + 1 <= self.length:
            self.text[-1] = self.text[-1] + ' ' + word
        else:
            self.text.append(word)

    def end(self):
        for x in self.text:
            print(x.ljust(self.length, ' '))
        self.text = []


class RightParagraph:
    def __init__(self, length):
        self.length = length
        self.text = []

    def add_word(self, word):
        if len(self.text) > 0 and len(word) + len(self.text[-1]) + 1 <= self.length:
            self.text[-1] = self.text[-1] + ' ' + word
        else:
            self.text.append(word)

    def end(self):
        for x in self.text:
            print(x.rjust(self.length, ' '))
        self.text = []
