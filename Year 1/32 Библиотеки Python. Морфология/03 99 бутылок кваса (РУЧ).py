import pymorphy2

morph = pymorphy2.MorphAnalyzer()
comment = morph.parse('бутылка')[0]
num = [1, 21, 31, 41, 51, 61, 71, 81, 91]
for i in range(99, 0, -1):
    print(f"В холодильнике {i} {comment.make_agree_with_number(i).word} кваса.")
    print(f"Возьмём одну и выпьем.")
    print(f"{'Осталось' if (i - 1) not in num else 'Осталась'} "
          f"{i - 1 if i - 1 > 0 else 0} {comment.make_agree_with_number(i - 1).word}"
          f" кваса.")
