def remove_inappropriate(spells):
    del_spells = []
    for word in spells:
        for x in word:
            if x.isupper():
                break
        else:
            del_spells.append(word)
    for x in del_spells:
        spells.pop(spells.index(x))
