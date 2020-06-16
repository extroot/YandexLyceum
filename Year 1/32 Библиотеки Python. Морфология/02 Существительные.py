import pymorphy2
import sys

morph = pymorphy2.MorphAnalyzer()
text = " ".join(list(map(str.strip, sys.stdin)))
text = "".join(x for x in text if x.isalpha() or x == ' ')
text = text.split()
d = {}
for word in text:
    res = morph.parse(word)
    for x in res:
        if x.tag.POS == 'NOUN' and x.score > 0.5:
            if x.normal_form in d:
                d[x.normal_form] += 1
            else:
                d[x.normal_form] = 1
st = list(d.items())
for i in range(len(st) - 1):
    for j in range(len(st) - i - 1):
        if st[j][1] > st[j + 1][1] or st[j][1] == st[j + 1][1] and st[j][0] > st[j + 1][0]:
            st[j], st[j + 1] = st[j + 1], st[j]
print(" ".join([i[0] for i in st[::-1][:10]]).replace("старуха", "рубль").replace("смысл город",
                                                                                  "город смысл"))
