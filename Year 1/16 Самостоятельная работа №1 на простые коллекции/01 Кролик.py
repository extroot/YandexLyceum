st = input().lower().split('@')
check = 'magic'
count = 0
for word in st:
    n = 0
    for x in check:
        if x in word:
            n += 1
    if n == 1:
        count += 1

print(count)
