print(*[str(int(i) ** 2) for i in input().split() if str(int(i) % 10) in "159"])
