profile = ('', '')


def setup_profile(name, vacation_dates):
    global profile
    profile = (name, vacation_dates)


def print_application_for_leave():
    print(f"Заявление на отпуск в период {profile[1]}. {profile[0]}")


def print_holiday_money_claim(st):
    print(f"Прошу выплатить {st} отпускных денег. {profile[0]}")


def print_attorney_letter(st):
    print(f"На время отпуска в период {profile[1]} моим заместителем назначается {st}. {profile[0]}")
