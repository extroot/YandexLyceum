class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.range = range
        self.damage = damage

    def __str__(self):
        return self.name

    def hit(self, actor, target):
        if target.is_alive():
            x = abs(actor.x - target.x)
            y = abs(actor.y - target.y)
            if self.range >= (x ** 2 + y ** 2) ** 0.5:
                print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
                target.get_damage(self.damage)
            else:
                print(f"Враг слишком далеко для оружия {self.name}")
        else:
            print("Враг уже повержен")


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.x, self.y = pos_x, pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return self.x, self.y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print("Могу ударить только Главного героя")

    def __str__(self):
        return f"Враг на позиции ({self.x}, {self.y}) с оружием {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []

    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapons.append(weapon)
            print(f"Подобрал {weapon}")
        else:
            print("Это не оружие")

    def next_weapon(self):
        if len(self.weapons) > 1:
            self.weapons.append(self.weapons.pop(0))
            print(f"Сменил оружие на {self.weapons[0]}")
        elif len(self.weapons) == 1:
            print("У меня только одно оружие")
        else:
            print("Я безоружен")

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f"Полечился, теперь здоровья {self.hp}")

    def hit(self, target):
        if isinstance(target, BaseEnemy):
            if len(self.weapons) == 0:
                print("Я безоружен")
            else:
                self.weapons[0].hit(self, target)
        else:
            print("Могу ударить только Врага")


weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)