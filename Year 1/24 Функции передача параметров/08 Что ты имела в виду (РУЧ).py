numbers = [2, 5, 7, 7, 8, 4, 1, 6]
"""
odd = []
even = odd
print(odd is even)  # True
В исходном коде создавалась ссылка на список, а не второй пустой список.
"""
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
