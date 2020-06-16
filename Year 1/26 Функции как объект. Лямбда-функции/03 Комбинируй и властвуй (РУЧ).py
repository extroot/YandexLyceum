num = sum(map(lambda x: x**2, list(filter(lambda x: x % 9 == 0, range(10, 100)))))
print(num)  # 585
