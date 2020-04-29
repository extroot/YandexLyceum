from PIL import Image


def image_filter(pixels, i, j):
    """Осветляет цвет исходного пикселя"""
    r, g, b = pixels[i, j]
    return r + 20 if r + 20 <= 255 else 255, g + 20 if g + 20 <= 255\
        else 255, b + 20 if b + 20 <= 255 else 255


im = Image.open("image.jpg")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения
for i in range(x):
    for j in range(y):
        pixels[i, j] = image_filter(pixels, i, j)
im.save("out.jpg")
