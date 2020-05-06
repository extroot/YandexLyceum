import sys
import pymorphy2

data = list(map(str.strip, sys.stdin))

morph = pymorphy2.MorphAnalyzer()
out = morph.parse('Живая')[0]
out2 = morph.parse('Не живая')[0]

for word in data:
    res = morph.parse(word)[0]
    if res.tag.POS != "NOUN":
        print("Не существительное")
    elif res.tag.animacy == "anim":
        if res.tag.number == "plur":
            print(out.inflect({"plur"}).word.capitalize())
        else:
            print(out.inflect({res.tag.gender}).word.capitalize())
    else:
        if res.tag.number == "plur":
            print(out2.inflect({"plur"}).word.capitalize())
        elif res.tag.gender == "femn":
            print(out2.word.capitalize())
        else:
            print(out2.inflect({res.tag.gender}).word.capitalize())