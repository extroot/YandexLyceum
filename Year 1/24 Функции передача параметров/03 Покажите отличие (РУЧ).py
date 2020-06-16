lst = [1, 2, 3, 4, 5]

print(sorted(lst))  # [1, 2, 3, 4, 5] - Возвращает список
print(lst.sort())  # None - Не возвращает ничего

print(sorted.__init__)  # Sorted имеет атрибуты
print(sorted.__call__(lst))

print(lst.sort)  # <built-in method sort of list object at 0x010145D0> - Метод списка
print(sorted)  # <built-in function sorted> - Функция

print(id(lst))
print(id(lst), id(sorted(lst)))  # id исходного списка сохраняется, sorted же создает новый список
