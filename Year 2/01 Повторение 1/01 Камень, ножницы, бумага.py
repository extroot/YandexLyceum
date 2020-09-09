s = ["ножницы", "камень", "бумага"]
first = s.index(input())
second = s.index(input())
if second == first:
    print("ничья")
elif first == 0 and second == 2 or first == 1 and second == 0 or first == 2 and second == 1:
    print("первый")
else:
    print("второй")
