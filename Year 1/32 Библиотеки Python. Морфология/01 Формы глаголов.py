import pymorphy2
import sys

morph = pymorphy2.MorphAnalyzer()
text = " ".join(list(map(str.strip, sys.stdin)))
for x in ",./;'\":-=\\|_+?!@#$%^&*()":
    text = text.replace(x, " ")
text = text.split()
count = 0

for word in text:
    res = morph.parse(word)
    for x in res:
        if ("VERB" in x.tag or "INFN" in x.tag) and x.normal_form in \
                ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть']:
            count += 1

print(count)
