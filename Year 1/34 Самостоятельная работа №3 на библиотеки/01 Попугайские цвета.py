from PIL import Image


def direction(image, color):
    pixels = image.load()  # список с пикселями
    x, y = image.size  # ширина (x) и высота (y) изображения
    x0 = []
    y0 = []
    for i in range(x):
        for j in range(y):
            if color == pixels[i, j]:
                x0.append(i)
                y0.append(j)
    sx = sum(x0) // len(x0) if len(x0) else 0
    sy = sum(y0) // len(y0) if len(y0) else 0
    return abs(sx - x // 2), abs(sy - y // 2)
