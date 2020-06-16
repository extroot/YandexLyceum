st = [int(i) for i in input().split()]
s = 0
st2 = [int(i) for i in input().split()]
for x in st[st2[0]:st2[1] + 1]:
    s += x
print(s)
