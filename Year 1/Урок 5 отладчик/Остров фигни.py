ch = 0
z = 0
flag = False
for i in range(int(input())):
    chis = int(input())
    znam = int(input())
    if flag:
        ch = ch * znam + chis * z
        z = z * znam
    else:
        ch = chis
        z = znam
        flag = True
a = ch
b = z
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(int(ch / a), '/', int(z / a), sep='')
