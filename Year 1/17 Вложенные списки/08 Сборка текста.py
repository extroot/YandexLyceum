num = [int(i) for i in input().split()]
words = input().lower().split()
word = ''
for x in num:
    word += words[x - 1] + " "
print(word[:-1].capitalize())
