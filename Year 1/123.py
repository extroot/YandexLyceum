# В первом примере мы создаём списки numbers и numbers_add, затем выводим на экран id этого списка.
# После мы прибовляем к списку numbers список numbers_add используя "=", и снова выводим на экран id
# списка, мы можем заметить что выведенные id отличаются друг от друга, значит при использовании
# "=" создаётся новый объект в который записывается результат сложения.


# Во втором примере мы будем присоединять numbers_add к value используя "+=", и также до и после выведем
# id списка numbers. В отличии от первого примера, можно заметить что id не изменился, значит используя
# "+=" новый объект не создаётся, и меняется только значение.

"""
При операции x += y
 id не меняется => новый объект не создается

При операции x = x + y
 id изменился => создается новый объект
"""
x = [1, 2, 3]
y = [5, 6, 7]
print(id(x))
x += y
print(id(x))
print()

x = [1, 2, 3]
y = [5, 6, 7]
print(id(x))
x = x + y
print(id(x))