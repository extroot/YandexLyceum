import pymorphy2
morph = pymorphy2.MorphAnalyzer()
inp = input()
word = morph.parse(inp)[0]
st1 = [{"past", "masc"}, {"past", "femn"}, {"past", "neut"}, {"past", "plur"}]
st2 = [{"pres", "1per", "sing"}, {"pres", "1per", "plur"}, {"pres", "2per", "sing"},
       {"pres", "2per", "plur"}, {"pres", "3per", "sing"}, {"pres", "3per", "plur"}]
if morph.parse(inp)[0].tag.POS not in "VERB INFN":
    print("Не глагол")
else:
    print("Прошедшее время:")  # past
    for x in st1:
        print(word.inflect(x).word)
    print("Настоящее время:")  # pres
    for x in st2:
        print(word.inflect(x).word)
