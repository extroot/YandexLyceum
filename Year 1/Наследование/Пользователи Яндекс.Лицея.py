class User:
    def solve(self, n):
        pass


class Student(User):
    pass


class Teacher(User):
    def check_solution(self, user, n):
        pass


class Admin(User):
    def edit(self, n):
        pass


class SuperAdmin(Admin):
    def grant(self, user):
        pass
