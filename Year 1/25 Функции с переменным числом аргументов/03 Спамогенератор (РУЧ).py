def spam(name, time, email, place="Москве"):
    return f"""To: {email}
Здравствуйте, {name}!
Были бы рады видеть вас на встрече начинающих программистов в {place}, которая пройдет {time}.
"""


# print(spam(name="Инопланетянин", time="32 января в 24:30", email="i_dont_khow_his_email@yandex.ru"))
# print(spam(name="Инопришеленец", time="32 января в 24:30", email="i_dont_khow_his_email_to@yandex.ru"))
