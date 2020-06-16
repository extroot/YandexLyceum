def make_shades(alley, k):
    d = len(alley)
    shades = [False] * d
    for i in range(d):
        height = alley[i]
        if height > 0:
            if k >= 0:
                start = i
                finish = min(i + k * height, d - 1)
            else:
                start = max(i + k * height, 0)
                finish = i
            for j in range(start, finish + 1):
                shades[j] = True
    return shades


def calculate_sunny_length(shades):
    sum_ = 0
    for i in shades:
        sum_ += 1 if i else 0

    return len(shades) - sum_


def main():
    k = int(input())
    alley = [int(height) for height in input().split()]
    shades = make_shades(alley, k)
    print('Обгорел' if calculate_sunny_length(shades) >= 10 else 'Тени достаточно')
