from swift import words as source
from random import sample

words = list(filter(lambda x: all(list(map(
    lambda i: i in [chr(i) for i in range(ord('а'), ord('я'))], x))), source))


def create_sentences(count_sentences: int = 5, count_words: int = 7):
    return [' '.join(sample(words, count_words)).capitalize() + '.' for _ in range(count_sentences)]


print(*create_sentences(), sep='\n')
