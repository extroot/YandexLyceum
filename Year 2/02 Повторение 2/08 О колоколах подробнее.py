class Bell:
    def __init__(self, *args, **kwargs):
        self.args = list(args)
        self.kwargs = kwargs

    def print_info(self):
        if not len(self.args) and not len(self.kwargs):
            print('-', end="")
        if len(self.kwargs):
            print(", ".join([f"{x}: {y}" for x, y in sorted(self.kwargs.items())]), end='')
        if len(self.kwargs) and len(self.args):
            print("; ", end='')
        if len(self.args):
            print(", ".join(self.args), end='')
        print()


class LittleBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sound(self):
        print("ding")


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f = False

    def sound(self):
        if self.f:
            print("dong")
        else:
            print("ding")
        self.f = not self.f


if __name__ == "__main__":
    Bell("бронзовый").print_info()
    LittleBell("медный", нота="ля").print_info()
    BigBell(название="Корноухий", вес="1275 пудов").print_info()
    BigBell("крупнейший в мире действующий колокол", название="Bell of Good Luck",
            высота="810,8 см", диаметр="511,8 см", вес="116 тонн").print_info()
    LittleBell().print_info()
