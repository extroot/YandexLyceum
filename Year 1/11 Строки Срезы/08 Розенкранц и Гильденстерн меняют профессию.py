max_o = 0
x = 0
f = False
for i in input():
    if i == 'о':
        f = True
        x += 1
    elif i == 'р':
        f = False
        max_o = x if x > max_o else max_o
        x = 0

if f:
    max_o = x if x > max_o else max_o
print(max_o)
