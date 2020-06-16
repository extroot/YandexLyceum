last = input()
new = input()
while new[0] == last[-1]:
    last = new
    new = input()
print(new)
