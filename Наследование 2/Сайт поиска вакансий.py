class Profile:
    def __init__(self, name):
        self.name = name
        self.inf = ""

    def info(self):
        return self.inf

    def describe(self):
        print(self.name, self.info())


class Vacancy(Profile):
    def __init__(self, name, inf):
        super().__init__(name)
        self.inf = inf

    def info(self):
        return f"Предлагаемая зарплата: {self.inf}"


class Resume(Profile):
    def __init__(self, name, inf):
        super().__init__(name)
        self.inf = inf

    def info(self):
        return f"Стаж работы: {self.inf}"

