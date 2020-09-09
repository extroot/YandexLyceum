class Note:
    def __init__(self, h):
        self.h = h

    def play(self):
        print(self.h)


if __name__ == "__main__":
    do = Note("до")
    sol = Note("соль")
    sol.play()
    do.play()
