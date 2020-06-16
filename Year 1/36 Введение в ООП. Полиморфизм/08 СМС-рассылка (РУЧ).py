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
