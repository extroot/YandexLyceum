st = [[input().split()[1] for _ in range(int(input()))] for _ in range(int(input()))]
print("ДА" if all([any(i == '5' for i in x) for x in st]) else "НЕТ")