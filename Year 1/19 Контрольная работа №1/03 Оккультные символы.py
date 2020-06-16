st = input().split('//&')
st2 = input().split('*?*')
for check in st:
    word = []
    chars = set(check)
    for entity in st2:
        chars1 = set(entity)
        if len(chars & chars1) <= 1:
            word.append(entity)
    if len(word) > 0:
        print(f"{check}: {', '.join(word)}")
    else:
        print(f"{check}: не сложилось")
