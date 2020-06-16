out_neut = 'Я вас не понимаю :('
out_bad = 'Ничего, скоро всё наладится.'
out_good = 'Отлично, у меня тоже всё хорошо :)'

answer = input('Какое у вас настроение? ')
if 'не' in answer or '?' in answer:
    print(out_bad)
elif 'хорош' in answer or 'прекрасн' in answer or 'отличн' in answer:
    # Без окончаний, чтобы срабатывало в любой форме слова
    print(out_good)
elif 'плох' in answer or 'ужасн' in answer or 'отврат' in answer:
    print(out_bad)
else:
    print(out_neut)
