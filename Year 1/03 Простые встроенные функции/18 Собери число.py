number = str(input())  # Задача сделанная еще в прошлом году :0

a = int(number[0]) + int(number[1])
b = int(number[1]) + int(number[2])

number2 = int(str(max(a, b)) + str(min(a, b)))
print(number2)
