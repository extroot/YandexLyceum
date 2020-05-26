from PIL import Image

im = Image.open("../lib4 morph/image.jpg")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения
print(sum([pixels[i, j][0] for j in range(y) for i in range(x)])
      // (x * y), sum([pixels[i, j][1] for j in range(y) for i in range(x)])
      // (x * y), sum([pixels[i, j][2] for j in range(y) for i in range(x)]) // (x * y))
