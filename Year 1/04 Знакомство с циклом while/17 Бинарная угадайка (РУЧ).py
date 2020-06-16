up = 1000
do = 1
count = 0
f = 1

while f:
    inp = input(str((up - do) // 2 + do) + '? ')
    if inp == '<':
        up = (up - do) // 2 + do
    if inp == '>':
        do = (up - do) // 2 + do
    if inp == '=':
        f = 0
    count += 1
    if count > 10:
        print('Game over')
        f = 0
