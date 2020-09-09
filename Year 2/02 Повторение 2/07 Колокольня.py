class LittleBell:
    def sound(self):
        print("ding")


class BigBell:
    def __init__(self):
        self.f = False

    def sound(self):
        if self.f:
            print("dong")
        else:
            print("ding")
        self.f = not self.f


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def sound(self):
        for bell in self.bells:
            bell.sound()
        print('...')

    def append(self, bell):
        self.bells.append(bell)


if __name__ == "__main__":
    bell_tower = BellTower()
    bell_tower.sound()
    bell_tower.append(BigBell())
    bell_tower.sound()
    bell_tower.append(BigBell())
    bell_tower.sound()
