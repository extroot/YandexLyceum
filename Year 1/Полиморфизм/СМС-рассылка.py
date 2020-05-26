class Person:
    def __init__(self, first_name, middle_name, last_name, phones):
        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.wphone = phones["work"] if "work" in phones else None
        self. pphone = phones["private"] if "private" in phones else None

    def get_phone(self):
        return self.pphone

    def get_name(self):
        return f"{self.lname} {self.fname} {self.mname}"

    def get_work_phone(self):
        return self.wphone

    def get_sms_text(self):
        return f"Уважаемый {self.fname} {self.mname}!" \
               f" Примите участие в нашем беспроигрышном конкурсе для физических лиц"


class Company:
    def __init__(self, name, ctype, phones, *persons):
        self.name = name
        self.ctype = ctype
        if "contact" in phones:
            self.phone = phones["contact"]
        else:
            for person in persons:
                if person.get_work_phone():
                    self.phone = person.get_work_phone()
                    break
            else:
                self.phone = None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f"Для компании {self.name} есть супер предложение!" \
               f" Примите участие в нашем беспроигрышном конкурсе для {self.ctype}"

    def get_phone(self):
        return self.phone


def send_sms(*args):
    for x in args:
        if x.get_phone():
            print(f"Отправлено СМС на номер {x.get_phone()} с текстом: {x.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {x.get_name()}")


person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)