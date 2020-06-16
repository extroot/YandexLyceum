n = input()
while n[0] != '1':
    n = str(int(n) * int(n[0]))
    if int(n) > 1000000000:
        break
print(n)
