from PIL import Image


def makeanagliph(filename, delta):
    im = Image.open(filename)
    im2 = im.copy()
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    pixels2 = im2.load()  # список с пикселями

    for i in range(x):
        for j in range(y):
            r, g, b = pixels2[i, j]
            if i > delta:
                r1, g1, b1 = pixels[i - delta, j]
                pixels2[i, j] = r1, g, b
            else:
                pixels2[i, j] = 0, g, b
    im2.save("res.jpg")
