class Pigeon:
    def __init__(self, name, lg, m):
        self.name = name
        self.lg = lg
        self.m = m
        self.z = 0
        self.flap = -1

    def __str__(self):
        return f"Pigeon {self.name}, {self.m}"

    def flap_wings(self):
        self.flap *= -1
        return "up" if self.flap == 1 else "down"

    def eat(self, food):
        self.m += food // 10
        self.z += food % 10
        if self.z >= 10:
            self.m += self.z // 10
            self.z = self.z % 10

    def carry(self, load, ran):
        return load <= self.m and ran <= self.lg

    def __lt__(self, other):  # x < y
        return (self.m, self.lg, len(self.name), self.name)\
               < (other.m, other.lg, len(other.name), other.name)

    def __le__(self, other):  # x <= y
        return (self.m, self.lg, len(self.name), self.name)\
               <= (other.m, other.lg, len(other.name), other.name)

    def __eq__(self, other):  # x == y
        return (self.m, self.lg, len(self.name), self.name)\
               == (other.m, other.lg, len(other.name), other.name)

    def __ne__(self, other):  # x != y
        return (self.m, self.lg, len(self.name), self.name)\
               != (other.m, other.lg, len(other.name), other.name)

    def __gt__(self, other):  # x > y
        return (self.m, self.lg, len(self.name), self.name)\
               > (other.m, other.lg, len(other.name), other.name)

    def __ge__(self, other):  # x >= y
        return (self.m, self.lg, len(self.name), self.name)\
               >= (other.m, other.lg, len(other.name), other.name)


# 1: 2:16

p1 = Pigeon('Johnas', 100, 10)
p2 = Pigeon('Calman', 100, 10)
print(p1, p2, sep='\n')
print(p1 > p2)
p2.eat(13)
print(p1 >= p2)
p1.eat(42)
p2.eat(7)
print(p1, p2, sep='\n')
print(p1.carry(90, 15))
