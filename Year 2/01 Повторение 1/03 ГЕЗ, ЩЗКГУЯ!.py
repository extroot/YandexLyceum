lst = input()
offset = int(input()) % len(lst)

print(lst[offset:] + lst[:offset])
print(lst)
print(lst[-offset:] + lst[:-offset])
