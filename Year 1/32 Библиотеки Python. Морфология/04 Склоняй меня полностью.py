import pymorphy2

d = {"nomn": "именительный",
     "gent": "родительный",
     "datv": "дательный",
     "accs": "винительный",
     "ablt": "творительный",
     "loct": "предложный"}

morph = pymorphy2.MorphAnalyzer()
inp = input()
word = morph.parse(inp)[0]
if morph.parse(inp)[0].tag.POS != "NOUN":
    print("Не существительное")
else:
    print("Единственное число:")
    for pad, name in d.items():
        print(name.capitalize(), "падеж:", word.inflect({pad}).word)
    print("Множественное число:")
    for pad, name in d.items():
        print(name.capitalize(), "падеж:", word.inflect({pad, "plur"}).word)
