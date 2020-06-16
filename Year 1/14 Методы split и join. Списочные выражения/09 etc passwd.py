passwd = []

while True:
    inp = input()
    if inp == "":
        break
    passwd.append(inp.split(':'))

bad_pass = [i for i in input().split(';')]

for x in passwd:
    if x[1] in bad_pass:
        print("To:", x[0])
        print(x[4].split(',')[0], ', ваш пароль слишком простой, смените его.', sep='')
