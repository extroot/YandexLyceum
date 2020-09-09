from PIL import Image

im = Image.open("image.png")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения
cords = [x, y, 0, 0]  # Верх, лево, низ, право
background = pixels[0, 0]

for i in range(x):
    for j in range(y):
        if pixels[i, j] != background:
            if i < cords[0]:
                cords[0] = i
            if i > cords[2]:
                cords[2] = i
            if j < cords[1]:
                cords[1] = j
            if j > cords[3]:
                cords[3] = j + 1
cropped = im.crop(cords)
cropped.save("res.png")
