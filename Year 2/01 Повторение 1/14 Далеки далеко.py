import sys

words = ["далек", "далека", "далеку", "далеки", "далеков", "далекам", "далеком", "далеками",
         "далеке", "далеках"]
count = 0
for line in sys.stdin:
    line = line.rstrip('\n')
    for x in words:
        if f" {x} " in line.lower() or line.lower()[:len(x)] == x or line.lower()[-len(x):] == x:
            count += 1
            break
print(count)
