class BigBell:
    def __init__(self):
        self.flag = True

    def sound(self):
        if self.flag:
            print("ding")
        else:
            print("dong")
        self.flag = not self.flag
