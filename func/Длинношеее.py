def print_long_words(text):
    for x in text:
        if not x.isalpha():
            text = text.replace(x, ' ')
    for word in text.split():
        s = 0
        for x in "аоэиуыеёюяaeiouy":
            s += word.count(x)
        if s >= 4:
            print(word.lower())


if __name__ == "__main__":
    print_long_words('Как и в прочих заданиях этого урока,'
                     ' в вашем решении функция должна быть определена, но не должна вызываться.')
