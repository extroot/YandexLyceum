class User:
    def __init__(self, name):
        self.name = name
        self.d = ""

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return self.d

    def describe(self):
        print(self.info())


class Person(User):
    def __init__(self, name, d):
        self.name = name
        self.d = d

    def info(self):
        return f"Дата рождения: {self.d}"

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, d):
        self.name = name
        self.d = d

    def info(self):
        return f"Описание: {self.d}"
