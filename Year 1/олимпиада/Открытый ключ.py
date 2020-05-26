n = int(input())
nums = [int(i) for i in input().split()]
word = ""
f = False
for i in range(n):
    string = input()
    st = ""
    num = []
    for x in string:
        if x in st:
            continue
        count = string.count(x)
        if count in num and count == nums[i]:
            print('NO')
            f = True
            break
        num.append(count)
        st += x
    if f:
        break
    if nums[i] not in num:
        print('NO')
        break
    word += st[num.index(nums[i])]
print(word)
