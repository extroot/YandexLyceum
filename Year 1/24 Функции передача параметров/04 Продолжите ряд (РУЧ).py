def continue_fibonacci_sequence(sequence, n):
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element)
        # Исходная ф-я меняла саму переменную внутри себя
        # Исправленная меняет внутренние элементы переменной.
