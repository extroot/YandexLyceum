n = int(input())
count = int(input())
for bull in range(1, min(count, n // 20) + 1):
    for cow in range(0, min(count, n // 10) + 1):
        for calf in range(0, min(count, n // 5) + 1):
            if bull * 20 + cow * 10 + calf * 5 == n and bull + cow + calf == count:
                print(bull, cow, calf)
